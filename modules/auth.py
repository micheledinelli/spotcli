from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy import util
import os
import sys
import re
import typer

auth_app = typer.Typer(add_completion=False)

load_dotenv(find_dotenv())

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SCOPE = os.environ['SPOTIPY_CLIENT_SCOPE']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

sp_oauth = spotipy.SpotifyOAuth(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                scope=SCOPE)

@auth_app.command(short_help="login")
def login():
    '''
    Authenticate with Spotify and retrieve an access token.

    Parameters:
    - spoty_client: An instance of your Spotipy client containing client_id, client_secret, redirect_uri, and scope.

    Returns:
    - token: The access token if authentication is successful.
    '''
    token = util.prompt_for_user_token(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope=SCOPE)
    if token:
        print("Succesfully logged in")
        return token
    else:
        print("Can't get a valid access token")
        sys.exit(1)

@auth_app.command(short_help="logout")
def logout():
    '''
    Clear cached Spotify tokens in the current directory.

    This function searches for files starting with '.cache' in the current directory and removes them.

    Note: Be cautious when using this function, as it permanently deletes cache files.

    Returns:
    - None
    '''
    # Iterate through files in the current directory
    for f in os.listdir('./'):
        # Check if the file name matches the pattern '^\.cache'
        if re.search('^\.cache', f):
            # Remove the cache file
            os.remove(f)

@auth_app.command()
def is_auth():
    '''
    Check if the user is authenticated with Spotify.

    Parameters:
    - sp_oauth: An instance of SpotipyOAuth containing client_id, client_secret, redirect_uri, and other necessary information.

    Returns:
    - access_token: The valid access token if the user is authenticated.
    '''
    # Retrieve the cached token, if available
    cached_token = sp_oauth.get_cached_token()

    # Check if a cached token exists
    if cached_token:
        # Check if the cached token is still valid
        if not sp_oauth.is_token_expired(cached_token):
            # If the token is still valid, return the access token
            return cached_token["access_token"]
    else:
        return False