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

console = Console()
app = typer.Typer()
sp_oauth = spotipy.SpotifyOAuth(client_id=spoty_client.client_id,
                            client_secret=spoty_client.client_secret,
                            redirect_uri=spoty_client.redirect_uri,
                            scope=spoty_client.scope)

def isAuth():
    cached_token = sp_oauth.get_cached_token()
    if cached_token:
        if not sp_oauth.is_token_expired(cached_token):
            # refresh_token()
            return cached_token["access_token"]
    else:
        login()

@app.command(short_help="login")
def login(verbose: bool = typer.Option(False, help="print the token retrieved")):
    token = util.prompt_for_user_token(client_id=spoty_client.client_id,
                                        client_secret=spoty_client.client_secret,
                                        redirect_uri=spoty_client.redirect_uri,
                                        scope=spoty_client.scope)
    if token:
        print("Succesfully logged in")
        if verbose: 
            print(token)
        return token
    else:
        print("Can't get a valid access token")

@app.command(short_help="refresh the access token")
def refresh_token(verbose: bool = typer.Option(False, help="print the refreshed token")):
    if sp_oauth.get_cached_token():
        cached_token = sp_oauth.get_cached_token()
        token = sp_oauth.refresh_access_token(cached_token["refresh_token"])
        if verbose:
            print(token["access_token"]) 
    else:
        print("No token found")              

@app.command(short_help="return recent tracks of the user")
def recent_tracks(howmany: Optional[int] = typer.Argument(10)):
    token = isAuth()
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
    token = isAuth()
    sp = spotipy.Spotify(auth=token)
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("username", min_width=25)
    table.add_column("followers", min_width=20, justify="center")
    table.add_column("url", min_width=20)
    results = sp.current_user()
    table.add_row(results['display_name'], str(results['followers']['total']), results['href'])
    console.print(table)

@app.command(short_help="clear the cached token")
def clear_cache():
    for f in os.listdir('./'):
        if re.search('^\.cache', f):
            os.remove(f)     

@app.command(short_help="available devices")
def devices(show: bool = typer.Option(False, help="show the available devices")):
    token = isAuth()
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

def queue(device_id, uri):
    token = isAuth()
    sp = spotipy.Spotify(auth=token)
    sp.add_to_queue(uri, device_id=None)

@app.command()
def search(q: str = typer.Argument("", help="query"), limit: int = typer.Option(5, help="number of results")):
    token = isAuth()
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
    for idx, device in enumerate(device_list):
        if device["is_active"]:
            active_id = device_list[0]['id']   
            break
    if active_id is None:
        print("No active device found")

    uri = name_uri_dict[track_name]
    queue(device_id=active_id, uri=uri) 
    sp.next_track(device_id=active_id)

@app.command(short_help="stick to the queue")
def stick():
    token = isAuth()
    sp = spotipy.Spotify(auth=token)
    console.clear()
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("name", min_width=30, justify="center")
    table.add_column("artist", min_width=30, justify="center")
    table.add_column("album", min_width=30, justify="center")
    current_track = sp.current_user_playing_track()
    table.add_row(current_track["item"]["name"], current_track["item"]["artists"][0]["name"], current_track["item"]["album"]["name"], )
    console.print(table)    
    while True:
        poll_track = sp.current_user_playing_track()
        if current_track["item"]["id"] != poll_track["item"]["id"]:
            stick()
        time.sleep(3)

if __name__ == "__main__":
    app()