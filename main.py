import typer
from rich.console import Console
import spotipy
import spoty_client

from halo import Halo

# custom modules
import modules.auth as auth
import modules.utils as utils
import modules.player as player
import modules.nerd_commands as nerd_commands

import modules.playback_commands as playback

console = Console()

app = typer.Typer(add_completion=False)

sp_oauth = spotipy.SpotifyOAuth(client_id=spoty_client.client_id,
                                client_secret=spoty_client.client_secret,
                                redirect_uri=spoty_client.redirect_uri,
                                scope=spoty_client.scope)

@app.command(short_help="login")
def login():
    return auth.login()

@app.command(short_help="refresh the access token")
def refresh_token():
    auth.refresh_token(sp_oauth)     

# Utils stuff
@app.command(short_help="clear the cached token")
def clear_cache():
    utils.clear_cache() 

@app.command(short_help="returns info about the current user")
def whoami():
    '''
    Command to retrieve and display information about the current Spotify user.

    This command uses the is_auth function to check if the user is authenticated,
    retrieves the user's information, and displays it in a tabular format using Rich library.

    Parameters:
    - None

    Returns:
    - None
    '''
    # Create a Spotify object with the access information from oauth
    sp = auth.grant_access(sp_oauth)

    # Retrieve current user information from Spotify API
    with Halo(text='Fetching devices', spinner='dots'):
        user_info = sp.current_user()

    # Display the formatted JSON using Rich library
    console.print(f'[bold purple]Info about:[/bold purple] [green]{user_info["id"]}[/green]')
    utils.pretty_print_json(user_info)

# # Client operation  

# @app.command(short_help="return recent tracks of the user")
# def recent_tracks(howmany: Optional[int] = typer.Argument(10)):
#     token = auth.is_auth(sp_oauth)
#     sp = spotipy.Spotify(auth=token)
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("#", style="dim", width=5)
#     table.add_column("Artist", min_width=20)
#     table.add_column("Track", min_width=30)
#     results = sp.current_user_saved_tracks(limit=howmany)
#     for idx, item in enumerate(results['items']):
#         track = item['track']
#         artist_name = track['artists'][0]['name']
#         table.add_row(str(idx), artist_name, track['name'])
#     console.print(table)


@app.command(short_help="available devices")
def devices(show: bool = typer.Option(False, help="show the available devices")):
    # Create a Spotify object with the access information from oauth
    sp = auth.grant_access(sp_oauth)

    nerd_commands.get_devices(sp, show=show)

# def queue(uri, device_id=None):
#     token = auth.is_auth(sp_oauth)
#     sp = spotipy.Spotify(auth=token)
#     sp.add_to_queue(uri, device_id=device_id)

@app.command()
def search(q: str = typer.Argument("", help="query"), limit: int = typer.Option(5, help="number of results")):
    # Create a Spotify object with the access information from oauth
    sp = auth.grant_access(sp_oauth)
    playback.search(sp, q)

# @app.command(short_help="transfer playback on selected device")
# def transfer():
#     token = auth.is_auth(sp_oauth)
#     sp = spotipy.Spotify(auth=token)
#     device_list = devices(show=False)
#     names_id_dict = {}
#     for idx, item in enumerate(device_list):
#         names_id_dict[item["name"]] = item["id"]
    
#     questions = [
#         inquirer.List(
#             "devices",
#             message="Where do you want to transfer the playback?",
#             choices=names_id_dict.keys(),
#         ),
#     ]
#     answwer = inquirer.prompt(questions)
#     device_name = answwer["devices"]
#     sp.transfer_playback(names_id_dict[device_name], True)

# def transfer_on_wb(uri):
#     time.sleep(5)
#     token = auth.is_auth(sp_oauth)
#     sp = spotipy.Spotify(auth=token)
#     device_list = devices(show=False)
#     print(device_list)
#     device_id = device_list[0]["id"]
#     sp.transfer_playback(device_id=device_id, force_play=True)
#     queue(uri=uri)
#     sp.next_track(device_id)

# def get_an_active_id(token):
#     sp = spotipy.Spotify(auth=token)
#     device_list = devices(show=False)
#     active_id = None
#     for idx, device in enumerate(device_list):
#         if device["is_active"]:
#             active_id = device_list[0]['id']   
#             break
#     return active_id

if __name__ == "__main__":
    app()