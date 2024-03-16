import blessed
import spotipy
import argparse

from spoticli.utils import CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI
from spoticli.auth import login, logout, is_auth

def main(term):
    # Defining the auth manager and the client
    sp_oauth = spotipy.SpotifyOAuth(client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    redirect_uri=REDIRECT_URI,
                                    scope=SCOPE)

    sp_client = spotipy.Spotify(auth_manager=sp_oauth)

    # Setting up some commands
    parser = argparse.ArgumentParser(description="spoticli")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    logout_parser = subparsers.add_parser("logout", help="Logout from spoticli")
    login_parser = subparsers.add_parser("login", help="Login to spoticli")

    args = parser.parse_args()
    if args.subcommand == "logout":
        logout(auth_manager=sp_oauth)
        exit(0)
    elif args.subcommand == "login":
        login(auth_manager=sp_oauth)
        exit(0)

    # Start the main loop
    
    # with term.cbreak(), term.hidden_cursor(), term.fullscreen():
    #     while True:
    #         input("Press Enter to continue...")

if __name__ == "__main__":
    exit(main(blessed.Terminal()))