from time import sleep

import spotipy
from spotcli.console import console
from spotcli.console import prompt 
from rich import print
from rich.panel import Panel

from rich import print
from rich.table import Table
import time

from rich.live import Live
from rich.table import Table

def prova(client: spotipy.Spotify):
    # console.print("Welcome to [link=https://github.com/micheledinelli/spotcli]spotcli[/link]!")
    # name = prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
    # username = client.me()["display_name"]
    # spotcli_link = "Welcome to [link=https://github.com/micheledinelli/spotcli]spotcli[/link]!"
    # print(Panel(spotcli_link, title=f"Hello, {username}!"))

    # grid = Table.grid(expand=True)
    # grid.add_column()
    # grid.add_column(justify="right")
    # grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")

    # print(grid)

    

    # table = Table(title="Star Wars Movies", expand=True, leading=2, show_lines=True, header_style="bold magenta", border_style="green")

    # table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    # table.add_column("Title", style="magenta")
    # table.add_column("Box Office", justify="right", style="green")

    # table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    # table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    # table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    # table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

    
    # selected_row = None
    # while selected_row is None:
    #     console.print(table)
    #     console.print("Select a row by entering its index (0-3):")
    #     index = prompt.ask("Index:")
    #     try:
    #         selected_row = table.rows[int(index)]
    #     except (ValueError, IndexError):
    #         console.print("Invalid index. Please try again.")
    
    # console.clear()
    # console.print(f"You selected: {selected_row}")
    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(generate_table(), refresh_per_second=4) as live:
        for _ in range(40):
            time.sleep(0.4)
            live.update(generate_table())

import random
import time

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table

