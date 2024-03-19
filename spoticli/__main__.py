import spotipy
import argparse

from spoticli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI, USERDATA_PATH
from spoticli.auth import login, logout, is_auth

def main():

    # Custom cache handler for absolute path
    cache_handler = spotipy.CacheFileHandler(cache_path=USERDATA_PATH)

    sp_oauth = spotipy.SpotifyOAuth(
        cache_handler=cache_handler,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )

    sp_client = spotipy.Spotify(auth_manager=sp_oauth)

    # Setting up some commands
    parser = argparse.ArgumentParser(description="spoticli")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    logout_parser = subparsers.add_parser("logout", help="Logout from spoticli")
    login_parser = subparsers.add_parser("login", help="Login to spoticli")

    args = parser.parse_args()
    if args.subcommand == "logout":
        logout()
        exit(0)
    elif args.subcommand == "login":
        login(auth_manager=sp_oauth)
        exit(0)
    
    if not is_auth(auth_manager=sp_oauth):
        login(auth_manager=sp_oauth)

    # Main Loop

if __name__ == "__main__":
    main()