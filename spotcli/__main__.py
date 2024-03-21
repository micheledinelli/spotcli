import spotipy
import argparse
from rich.live import Live

from spotcli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI, USERDATA_PATH
from spotcli.auth import login, logout, is_auth
from spotcli.console import console
from spotcli.components.layout import make_layout

def main():
    """
    Main function for the spotcli application.
    """

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
        is_user_authenticated = is_auth(auth_manager=sp_oauth)
        
        if args.info and is_user_authenticated:
            console.print_json(data=sp_client.me())
            exit(0)
        elif args.info and not is_user_authenticated:
            console.print("You need to login first", style="warning")

        if args.token and is_user_authenticated:
            console.print_json(data=sp_oauth.get_cached_token())
            exit(0)
        elif args.token and not is_user_authenticated:
            console.print("You need to login first", style="warning")
            exit(1)

        login(auth_manager=sp_oauth)
        exit(0)
    
    if not is_auth(auth_manager=sp_oauth):
        login(auth_manager=sp_oauth)

    try:
        layout = make_layout(client=sp_client)
        with Live(layout, refresh_per_second=10, screen=True):
            while True:
                pass
    except KeyboardInterrupt:
        console.print("Goodbye!", style="info")
        exit(0)

if __name__ == "__main__":
    exit(main())