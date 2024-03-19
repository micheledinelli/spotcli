import spotipy
import argparse
from pprint import pprint

from spotcli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI, USERDATA_PATH
from spotcli.auth import login, logout, is_auth

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
    login_parser.add_argument("-i", "--info", help="Shows info about current user", 
                              action="store_true", required=False)
    login_parser.add_argument("-t", "--token", help="Shows token info", 
                            action="store_true", required=False)
    
    args = parser.parse_args()
    if args.subcommand == "logout":
        logout()
        exit(0)
    elif args.subcommand == "login":
        
        if args.info and not is_auth(auth_manager=sp_oauth):
            print("Please login first")
            exit(0)

        if args.info and is_auth(auth_manager=sp_oauth):
            pprint(sp_client.me())
            exit(0)

        if args.token and not is_auth(auth_manager=sp_oauth):
            print("Please login first")
            exit(0)

        if args.token and is_auth(auth_manager=sp_oauth):
            pprint(sp_oauth.get_cached_token())
            exit(0)

        login(auth_manager=sp_oauth)
        exit(0)
    
    if not is_auth(auth_manager=sp_oauth):
        login(auth_manager=sp_oauth)

    # TODO: Main Loop

if __name__ == "__main__":
    main()