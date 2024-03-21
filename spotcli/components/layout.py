from rich.layout import Layout
from spotcli.components.header import Header
import spotipy

def make_layout(client: spotipy.Spotify) -> Layout:
    layout = Layout()
    layout.update(Header(client))
    return layout