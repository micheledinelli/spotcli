import spoty_client
from spotipy import util

import sys

def is_auth(sp_oauth):
    cached_token = sp_oauth.get_cached_token()
    if cached_token:
        if not sp_oauth.is_token_expired(cached_token):
            # refresh_token()
            return cached_token["access_token"]
    else:
        print("Please login first")

def login(verbose):
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
        sys.exit(1)

def refresh_token(sp_oauth, verbose):
    if sp_oauth.get_cached_token():
        cached_token = sp_oauth.get_cached_token()
        token = sp_oauth.refresh_access_token(cached_token["refresh_token"])
        if verbose:
            print(token["access_token"]) 
    else:
        print("No token found")
        sys.exit(1)