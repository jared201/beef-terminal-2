"""Create an empty dashboard in textualize"""
from typing import Type

from textual._path import CSSPathType
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Container
from textual.driver import Driver
from textual.widgets import Header, Footer, Placeholder


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
        yield Container(
            Placeholder("Screen 1", id="col1"),
            Placeholder("Screen 2", id="col2"),
            Placeholder("Screen 3", id="col3")
        , id="top")
        yield Footer()

    async def quit(self):
         self.exit()

    async def copy(self):
        await self.clipboard.copy("Hello, World!")

    async def toggle_dark_mode(self):
        self.dark = not self.dark

