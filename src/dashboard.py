"""Create an empty dashboard in textualize"""
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class Dashboard(App):
    BINDINGS = [("q", "quit", "Quit")]
    STYLES = {"background": "white", "text": "black"}

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()