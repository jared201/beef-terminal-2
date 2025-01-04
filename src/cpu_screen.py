from typing import Type

import psutil
from textual._path import CSSPathType
from textual.app import ComposeResult
from textual.driver import Driver
from textual.widget import Widget
from textual.widgets import Static, ProgressBar

class CPUScreen(Widget):
    def __init__(
            self,
            driver_class: Type[Driver] | None = None,
            css_path: CSSPathType | None = None,
            watch_css: bool = False,
    ):
        super().__init__()
        self.cpu_usage_text = Static()
        self.cpu_usage_bar = ProgressBar(total=100, show_percentage=True)

    def compose(self) -> ComposeResult:
        yield self.cpu_usage_text
        yield self.cpu_usage_bar

    async def on_mount(self) -> None:
        self.set_interval(1, self.update_cpu_usage)

    async def update_cpu_usage(self) -> None:
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_usage_text.update(f"CPU Usage: {cpu_percent}%")
        self.cpu_usage_bar.progress = cpu_percent