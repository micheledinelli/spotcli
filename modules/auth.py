import spoty_client
from spotipy import util
import spotipy

import sys

def is_auth(sp_oauth):
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
        # If no cached token is found ask to login
        print("Please login first")
        exit(0)

def login():
    '''
    Authenticate with Spotify and retrieve an access token.

    Parameters:
    - spoty_client: An instance of your Spotipy client containing client_id, client_secret, redirect_uri, and scope.

    Returns:
    - token: The access token if authentication is successful.
    '''
    token = util.prompt_for_user_token(client_id=spoty_client.client_id,
                                       client_secret=spoty_client.client_secret,
                                       redirect_uri=spoty_client.redirect_uri,
                                       scope=spoty_client.scope)
    if token:
        print("Succesfully logged in")
        return token
    else:
        print("Can't get a valid access token")
        sys.exit(1)

def refresh_token(sp_oauth):
    '''
    Refresh the Spotify access token using the provided Spotipy OAuth instance.

    Parameters:
    - sp_oauth: An instance of SpotipyOAuth containing client_id, client_secret, redirect_uri, and other necessary information.

    Returns:
    - token: The refreshed access token.
    '''
    # Check if a cached token exists
    if sp_oauth.get_cached_token():
        # If a cached token exists, retrieve it
        cached_token = sp_oauth.get_cached_token()

        # Use the refresh token to obtain a new access token
        token = sp_oauth.refresh_access_token(cached_token["refresh_token"])
    else:
        # If no cached token is found, print an error message and exit
        print("No token found")
        sys.exit(1)

def grant_access(sp_oauth):
    '''
    Grant access to Spotify API by obtaining and returning a Spotify object with a valid access token.

    Parameters:
    - sp_oauth: An instance of SpotipyOAuth containing client_id, client_secret, redirect_uri, and other necessary information.

    Returns:
    - sp: A Spotify object with a valid access token.
    '''
    # Check if the user is authenticated and get the access token
    token = is_auth(sp_oauth)

    # Create a Spotify object with the obtained access token
    sp = spotipy.Spotify(auth=token)

    # Return the Spotify object with a valid access token
    return sp
