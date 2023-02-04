from typing import Optional
import typer
from rich.console import Console
from rich.table import Table
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util
import os, re
import spoty_client
import inquirer
import time
import webbrowser
from tqdm import tqdm
from alive_progress import alive_bar
import threading
import sys

# custom modules
import modules.auth as auth
import modules.utils as utils
import modules.player as player

console = Console()

app = typer.Typer()

sp_oauth = spotipy.SpotifyOAuth(client_id=spoty_client.client_id,
                            client_secret=spoty_client.client_secret,
                            redirect_uri=spoty_client.redirect_uri,
                            scope=spoty_client.scope)

# Auth and token stuff

@app.command(short_help="login")
def login(verbose: bool = typer.Option(False, help="print the token retrieved")):
    return auth.login(verbose)

@app.command(short_help="refresh the access token")
def refresh_token(verbose: bool = typer.Option(False, help="print the refreshed token")):
    auth.refresh_token(sp_oauth, verbose)     

# Utils stuff

@app.command(short_help="clear the cached token")
def clear_cache():
    utils.clear_cache() 

# Client operation  

@app.command(short_help="return recent tracks of the user")
def recent_tracks(howmany: Optional[int] = typer.Argument(10)):
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=5)
    table.add_column("Artist", min_width=20)
    table.add_column("Track", min_width=30)
    results = sp.current_user_saved_tracks(limit=howmany)
    for idx, item in enumerate(results['items']):
        track = item['track']
        artist_name = track['artists'][0]['name']
        table.add_row(str(idx), artist_name, track['name'])
    console.print(table)

@app.command(short_help="returns info about the current user")
def whoami():
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("username", min_width=25)
    table.add_column("followers", min_width=20, justify="center")
    table.add_column("url", min_width=20)
    results = sp.current_user()
    table.add_row(results['display_name'], str(results['followers']['total']), results['href'])
    console.print(table)

@app.command(short_help="available devices")
def devices(show: bool = typer.Option(False, help="show the available devices")):
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    devices_dict = sp.devices()
    device_list = devices_dict["devices"]
    if show:
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("id", min_width=25)
        table.add_column("name", min_width=20, justify="center")
        table.add_column("type", min_width=20)
        table.add_column("is_active", min_width=20)
        for idx, item in enumerate(device_list):
            table.add_row(item["id"], item["name"], item["type"], str(item["is_active"]))
        console.print(table)

    return device_list

def queue(uri, device_id=None):
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    sp.add_to_queue(uri, device_id=device_id)

@app.command()
def search(q: str = typer.Argument("", help="query"), limit: int = typer.Option(5, help="number of results")):
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    results = sp.search(q=q, limit=limit)
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    name_uri_dict = {}
    for idx, item in enumerate(song_items):
        name_uri_dict[item['name']] = item['external_urls']['spotify']

    questions = [
        inquirer.List(
            "tracks",
            message="Which song do you want to play?",
            choices=name_uri_dict.keys(),
        ),
    ]

    answer = inquirer.prompt(questions)
    track_name = answer['tracks']
    device_list = devices(show=False)
    active_id = None
    for idx, device in enumerate(device_list):
        if device["is_active"]:
            active_id = device_list[0]['id']   
            break

    uri = name_uri_dict[track_name]
    if active_id is None:
        print("No active device found")
        webbrowser.open(uri)
        transfer_on_wb(uri)
    else:
        queue(uri=uri, device_id=active_id) 
        player.next(token, active_id)

@app.command(short_help="transfer playback on selected device")
def transfer():
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    device_list = devices(show=False)
    names_id_dict = {}
    for idx, item in enumerate(device_list):
        names_id_dict[item["name"]] = item["id"]
    
    questions = [
        inquirer.List(
            "devices",
            message="Where do you want to transfer the playback?",
            choices=names_id_dict.keys(),
        ),
    ]
    answwer = inquirer.prompt(questions)
    device_name = answwer["devices"]
    sp.transfer_playback(names_id_dict[device_name], True)

def transfer_on_wb(uri):
    time.sleep(5)
    token = auth.is_auth(sp_oauth)
    sp = spotipy.Spotify(auth=token)
    device_list = devices(show=False)
    print(device_list)
    device_id = device_list[0]["id"]
    sp.transfer_playback(device_id=device_id, force_play=True)
    queue(uri=uri)
    sp.next_track(device_id)

def get_an_active_id(token):
    sp = spotipy.Spotify(auth=token)
    device_list = devices(show=False)
    active_id = None
    for idx, device in enumerate(device_list):
        if device["is_active"]:
            active_id = device_list[0]['id']   
            break
    return active_id

if __name__ == "__main__":
    app()