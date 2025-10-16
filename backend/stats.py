import gc
import sys
import psutil
import threading
import tracemalloc
import multiprocessing
from datetime import datetime

from logger import get_logger


logger = get_logger()

# Tracing our memory allocation
tracemalloc.start()


def log_stats():
    cpu_count = multiprocessing.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=0) # Not a good metric, it needs data
    thread_count = threading.active_count()
    thread_switch_interval = sys.getswitchinterval()
    gc_count = gc.get_count()

    current, peak = tracemalloc.get_traced_memory()
    current_mb = current / (1024 * 1024)
    peak_mb = peak / (1024 * 1024)

    logger.info(f"CPU Count: {cpu_count}, CPU Usage (%): {cpu_percent}, Thread Count: {thread_count}, Thread Switch Interval: {thread_switch_interval} secs, GC Count: {gc_count}, Current Memory (MB): {current_mb:.2f}, Peak Memory (MB): {peak_mb:.2f}")


def log_mem_diff(before, after):
    diff = after.compare_to(before, 'lineno')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("_mem_diff.txt", "a") as f:
        f.write(f"\n--- Mem Diff at {timestamp} ---\n")
        for stat in diff[:5]: # Top 5 lines because it is too heavy
            f.write(str(stat) + "\n")
