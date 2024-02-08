import typer
from typing_extensions import Annotated

from modules import auth, user

from modules.utils import DataFile, USERDATA_PATH

import spotipy
from spotipy import CacheFileHandler

from halo import Halo

app = typer.Typer(add_completion=False)
app.add_typer(auth.auth_app, name="auth")

def main():
    userdata = DataFile(USERDATA_PATH)
    if not userdata.get("access_token"):
        typer.echo("You are not logged in")
        auth.login()

    app()

@app.command(short_help="returns info about the current user")
def whoami():
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=auth.sp_oauth)

    # Call the whoami function from the user module
    user.whoami(sp)    

@app.command(short_help="search for a song")
def search(query: Annotated[str, typer.Argument()], limit: int = typer.Option(5, help="number of results")):
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=auth.sp_oauth)

    # Call the search function from the user module
    user.search(sp=sp, query=query, limit=limit)

@app.command(short_help="show my devices")
def devices():
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=auth.sp_oauth)

    # Call the search function from the user module
    user.devices(sp=sp)

if __name__ == '__main__':
    main()
