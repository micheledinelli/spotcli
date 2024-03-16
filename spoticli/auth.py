from spotipy.oauth2 import SpotifyOAuth
from spotipy import util

import os
import re

from spoticli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI, USERDATA_PATH

def login(auth_manager: SpotifyOAuth):
    """
    Logs in the user using the provided SpotifyOAuth authentication manager.

    Args:
        auth_manager (SpotifyOAuth): The authentication manager to use for logging in.

    Returns:
        str: The access token if the login is successful.

    Raises:
        SystemExit: If a valid access token cannot be obtained.
    """
    if is_auth(auth_manager):
        print("Already logged in")
        return

    token = util.prompt_for_user_token(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope=SCOPE)
    if token:
        print("Successfully logged in")
        return token
    else:
        print("Can't get a valid access token")
        exit(1)

def logout(auth_manager: SpotifyOAuth):
    '''
    Clear cached Spotify tokens in the current directory.

    This function searches for files starting with '.cache' in the current directory and removes them.

    Note: Be cautious when using this function, as it permanently deletes cache files.

    Returns:
    - None
    '''
    if not is_auth(auth_manager=auth_manager):
        print("Already logged out")
        return

    # Iterate through files in the current directory
    for f in os.listdir('./'):
        # Check if the file name matches the pattern '^\.cache'
        if re.search('^\.cache', f):
            # Remove the cache file
            os.remove(f)

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
    