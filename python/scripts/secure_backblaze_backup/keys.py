from pathlib import Path
import sys

from cryptography.fernet import Fernet
from rich.panel import Panel
from rich import print
from rich.console import Console


console = Console()


def create_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()

    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

    print(
        Panel.fit(
            "Copy the [bold cyan]encryption_key.key[/bold cyan] file or it's contents or [underline red]you won't be able to decrypt your data![/underline red]",
            title="Important!",
        )
    )

    return key


def load_key(encryption_key_path):
    """
    Read an encryption key
    """

    if Path(encryption_key_path).is_file():
        return open(encryption_key_path, "rb").read()
    else:
        console.print(f"[red] File does not exist[/red]: {encryption_key_path}")
        sys.exit(1)
