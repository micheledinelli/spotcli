from rich.panel import Panel
from rich.table import Table
from datetime import datetime
import spotipy

class Header():
    def __init__(self, client: spotipy.Spotify):
        self.client = client

    def __rich__(self) -> Panel:
        username = self.client.me()["display_name"]
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            f"Welcome to [link=https://github.com/micheledinelli/spotcli]spotcli[/link], [cyan]{username}!",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid)