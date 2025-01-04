# cpu_usage.py
import psutil

def get_cpu_usage_percent():
    """
    Returns the current system-wide CPU usage as a percentage.
    """
    return psutil.cpu_percent(interval=1)