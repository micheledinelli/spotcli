import typer
from typing_extensions import Annotated

from modules.auth import auth_app, sp_oauth
import modules.user as user

import spotipy

from halo import Halo

app = typer.Typer(add_completion=False)

# Loading modules
app.add_typer(auth_app, name="auth")

@app.command(short_help="returns info about the current user")
def whoami():
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    # Call the whoami function from the user module
    user.whoami(sp)    

@app.command(short_help="search for a song")
def search(query: Annotated[str, typer.Argument()], limit: int = typer.Option(5, help="number of results")):
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    # Call the search function from the user module
    user.search(sp=sp, query=query, limit=limit)

@app.command(short_help="show my devices")
def devices():
    # Create a Spotify object with the access information from oauth
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    # Call the search function from the user module
    user.devices(sp=sp)

if __name__ == '__main__':
    app()
