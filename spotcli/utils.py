import os

CLIENT_ID="a80867c5ce9640d4888f52ac2223df83"
CLIENT_SECRET="eca83a36fb8c4ebdbbc1ace8d6b7deb2"
SCOPE="user-read-playback-state user-modify-playback-state user-library-read"
REDIRECT_URI="http://localhost:8081"
home_dir = os.path.expanduser("~")
USERDATA_PATH = os.path.abspath(os.path.join(home_dir, ".config", "spoticli", "userdata.json"))
