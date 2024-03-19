from spotipy.oauth2 import SpotifyOAuth
from spotipy import util

import os

from spoticli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI, USERDATA_PATH

def login(auth_manager: SpotifyOAuth):
    """
    Logs in the user using the provided SpotifyOAuth authentication manager.

    If the user is already logged in, it prints "Already logged in" and returns.
    Otherwise, it prompts the user to authenticate and obtain an access token.
    If a valid access token is obtained, it prints "Successfully logged in" and returns.
    If a valid access token cannot be obtained, it prints "Can't get a valid access token" and exits with code 1.

    Args:
        auth_manager (SpotifyOAuth): The SpotifyOAuth authentication manager.

    Returns:
        None
    """
    token = util.prompt_for_user_token(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope=SCOPE,
                                       oauth_manager=auth_manager)
    if token:
        print("Successfully logged in")
        return
    else:
        print("Can't get a valid access token")
        exit(1)

def logout():
    '''
    Clear cached Spotify tokens in the current directory.

    This function searches for files starting with '.cache' in the current directory and removes them.

    Note: Be cautious when using this function, as it permanently deletes cache files.

    Returns:
    - None
    '''
    # Remove USERDATA_PATH file
    if os.path.exists(USERDATA_PATH):
        os.remove(USERDATA_PATH)
        print("Successfully logged out")
    else:
        print("Already logged out")

def is_auth(auth_manager: SpotifyOAuth):
    """
    Checks if the user is authenticated by verifying the token.

    Args:
        auth_manager (SpotifyOAuth): The SpotifyOAuth object used for authentication.

    Returns:
        bool: True if the user is authenticated, False otherwise.
    """
    token = auth_manager.get_cached_token()

    return token and not auth_manager.is_token_expired(auth_manager.get_cached_token())
    