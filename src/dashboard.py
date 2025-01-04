# src/dashboard.py
from typing import Type

from textual._path import CSSPathType
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.driver import Driver
from textual.widgets import Header, Footer, Placeholder
from src.cpu_screen import CPUScreen
from src.disk_screen import DiskScreen
from src.memory_screen import MemoryScreen

class Dashboard(App):
    BINDINGS = [("q", "quit", "Quit"), ("c", "copy", "Copy"), ("d", "toggle_dark_mode", "Toggle Dark Mode")]
    STYLES = {"background": "white", "text": "black"}
    CSS_PATH = "styles.tcss"

    def __init__(
            self,
            driver_class: Type[Driver] | None = None,
            css_path: CSSPathType | None = None,
            watch_css: bool = False,
    ):
        super().__init__(driver_class, css_path, watch_css)
        self.clipboard = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                CPUScreen(),  # Replaced "Screen 1" placeholder with CPUScreen
                DiskScreen(),  # Replaced "Screen 2" placeholder with DiskScreen
                MemoryScreen()  # Replaced "Screen 3" placeholder with MemoryScreen
            , id="vertical-layout"),
            Container(
                Placeholder("Screen 4"),
                Placeholder("Screen 5"),
                Placeholder("Screen 6"),
                id="right-container"
            )
        )
        yield Footer()

    async def quit(self):
         self.exit()

    async def copy(self):
        await self.clipboard.copy("Hello, World!")

    async def toggle_dark_mode(self):
        self.dark = not self.dark