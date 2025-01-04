# src/memory_screen.py
import psutil
from textual.widget import Widget
from textual.widgets import Static, ProgressBar

class MemoryScreen(Widget):
    def __init__(self):
        super().__init__()
        self.memory_usage_text = Static()
        self.memory_usage_bar = ProgressBar(total=100, show_percentage=True)

    def compose(self):
        yield self.memory_usage_text
        yield self.memory_usage_bar

    async def on_mount(self):
        self.set_interval(1, self.update_memory_usage)

    async def update_memory_usage(self):
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        self.memory_usage_text.update(f"Memory Usage: {memory_percent}%")
        self.memory_usage_bar.progress = memory_percent