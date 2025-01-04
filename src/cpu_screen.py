from typing import Type

import psutil
from textual._path import CSSPathType
from textual.app import App, ComposeResult
from textual.driver import Driver
from textual.widgets import Static

class CPUScreen(App):
    def __init__(
            self,
            driver_class: Type[Driver] | None = None,
            css_path: CSSPathType | None = None,
            watch_css: bool = False,
    ):
        super().__init__(driver_class, css_path, watch_css)
        self.cpu_usage = None

    def compose(self) -> ComposeResult:
        self.cpu_usage = Static()
        yield self.cpu_usage

    async def on_mount(self) -> None:
        self.set_interval(1, self.update_cpu_usage)

    async def update_cpu_usage(self) -> None:
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_usage.update(f"CPU Usage: {cpu_percent}%")