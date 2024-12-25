import psutil

def get_disk_usage_percent():
    """
    Returns the current system-wide disk usage as a percentage.
    """
    return psutil.disk_usage("/").percent