from typing import Optional
import typer

from rich.console import Console
from rich.table import Table

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os, re

import spoty_client

console = Console()
sp = None
app = typer.Typer()

@app.command(short_help="return recent tracks of the user")
def recent_tracks(howmany: Optional[int] = typer.Argument(10)):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spoty_client.client_id,
                                                    client_secret=spoty_client.client_secret,
                                                    redirect_uri=spoty_client.redirect_uri,
                                                    scope=spoty_client.scope))
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=5)
    table.add_column("Artist", min_width=20)
    table.add_column("Track", min_width=30)
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        artist_name = track['artists'][0]['name']
        table.add_row(str(idx), artist_name, track['name'])
    console.print(table)

@app.command(short_help="login")
def login():
    whoami()   

@app.command(short_help="returns info about the current user")
def whoami():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a80867c5ce9640d4888f52ac2223df83",
                                                    client_secret="c7f0223ecf524f05b5126eaff343c1db",
                                                    redirect_uri="http://localhost:8081",
                                                    scope="user-library-read"))
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("username", min_width=25)
    table.add_column("followers", min_width=20, justify="center")
    table.add_column("url", min_width=20)
    results = sp.current_user()
    table.add_row(results['id'], str(results['followers']['total']), results['href'])
    console.print(table)

@app.command(short_help="clear the cache")
def clear_cache():
    for f in os.listdir('./'):
        if re.search('^\.', f):
            os.remove(f)

if __name__ == "__main__":
    app()