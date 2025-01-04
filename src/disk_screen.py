# src/disk_screen.py
from typing import Type

import psutil
from textual.widget import Widget
from textual.widgets import Static, ProgressBar

class DiskScreen(Widget):
    def __init__(self):
        super().__init__()
        self.disk_usage_text = Static()
        self.disk_usage_bar = ProgressBar(total=100, show_percentage=True)

    def compose(self):
        yield self.disk_usage_text
        yield self.disk_usage_bar

    async def on_mount(self):
        self.set_interval(1, self.update_disk_usage)

    async def update_disk_usage(self):
        disk_usage = psutil.disk_usage('/')
        disk_percent = disk_usage.percent
        self.disk_usage_text.update(f"Disk Usage: {disk_percent}%")
        self.disk_usage_bar.progress = disk_percent