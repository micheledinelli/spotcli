import typer
import inquirer
from spotipy import Spotify 
from halo import Halo
from modules.utils import pprint

def whoami(sp: Spotify):
    """
    Retrieve and display information about the current user from the Spotify API.

    Parameters:
    - sp: An instance of the Spotify class for making API calls.
    """
    # Retrieve current user information from Spotify API
    with Halo(text='Fetching info', spinner='dots'):
        user_info = sp.current_user()

    # Display the formatted JSON using Rich library
    typer.echo(f'[bold purple]Info about:[/bold purple] [green]{user_info["id"]}[/green]')
    pprint(user_info)

def search(sp: Spotify, query: str, limit: int):
    """
    Search for songs on Spotify and prompt the user to choose a song to play.

    Parameters:
    - sp: An instance of the Spotify class for making API calls.
    - query: The search query for songs.
    - limit: The maximum number of search results to retrieve.
    
    Returns:
    - uri: The Spotify URI of the selected song.
    """
    with Halo(text='Fetching songs', spinner='dots'):
        # Retrieve information about song search
        results = sp.search(q=query, limit=limit)
        
        # Process the JSON
        songs_dict = results['tracks']
        song_items = songs_dict['items']
    
        name_uri_dict = {}
        for i, item in enumerate(song_items): 
            song_name = item['name']               
            artist_name = item["artists"][0]["name"]
            name_uri_dict[song_name + " - " + artist_name] = item['external_urls']['spotify']
    
    questions = [
        inquirer.List(
            "tracks",
            message="Which song do you want to play?",
            choices=name_uri_dict.keys(),
        ),
    ]

    answer = inquirer.prompt(questions)
    track_name = answer['tracks']

    uri = name_uri_dict[track_name]
    return uri

def devices(sp: Spotify, show=True):
    '''
    Command to retrieve and optionally display information about available Spotify devices.

    Parameters:
    - show (bool): A flag to indicate whether to display the available devices in a table format.

    Returns:
    - device_list (list): List of available devices.
    '''
    with Halo(text='Fetching devices', spinner='dots'):
        # Retrieve information about available devices from Spotify API
        devices_dict = sp.devices()

    device_list = devices_dict["devices"]
    if show:
        # Display the JSON
        pprint(device_list)

    # Return the list of available devices
    return device_list