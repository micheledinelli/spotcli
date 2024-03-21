from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

console = Console(theme=custom_theme)
error_console = Console(stderr=True, style="bold red")

# Prompt
prompt = Prompt()