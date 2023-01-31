from typing import Optional
import typer
from rich.console import Console
from rich.table import Table
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util
import os, re
import spoty_client

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
    table.add_row(results['id'], str(results['followers']['total']), results['href'])
    console.print(table)

@app.command(short_help="clear the cached token")
def clear_cache():
    for f in os.listdir('./'):
        if re.search('^\.cache', f):
            os.remove(f)      

if __name__ == "__main__":
    app()