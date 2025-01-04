import sys
import os
import pytest
from textual.app import App
from textual.widgets import Static

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from cpu_screen import CPUScreen

@pytest.fixture
def app():
    return CPUScreen()

def test_cpu_screen_initialization(app: App):
    assert isinstance(app, CPUScreen)
    assert isinstance(app.cpu_usage, Static)

@pytest.mark.asyncio
async def test_update_cpu_usage(app: App):
    await app.update_cpu_usage()
    assert "CPU Usage:" in app.cpu_usage.text