# memory_usage.py
import psutil

def get_memory_usage_percent():
    """
    Returns the current system-wide memory usage as a percentage.
    """
    return psutil.virtual_memory().percent