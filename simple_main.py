# main.py
from src.cpu_usage import get_cpu_usage_percent
from src.memory_usage import get_memory_usage_percent
from src.disk_usage import get_disk_usage_percent

def main():
    cpu_usage = get_cpu_usage_percent()
    memory_usage = get_memory_usage_percent()
    disk_usage = get_disk_usage_percent()
    print(f"Current CPU Usage: {cpu_usage}%")
    print(f"Current Memory Usage: {memory_usage}%")
    print(f"Current Disk Usage: {disk_usage}%")

if __name__ == "__main__":
    main()