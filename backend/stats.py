import gc
import sys
import psutil
import threading
import multiprocessing

from logger import get_logger


logger = get_logger()


def log_stats():
    cpu_count = multiprocessing.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=0) # Not a good metric, it needs data
    thread_count = threading.active_count()
    thread_switch_interval = sys.getswitchinterval()
    gc_count = gc.get_count()
    logger.info(f"CPU Count: {cpu_count}, CPU Usage (%): {cpu_percent}, Thread Count: {thread_count}, Thread Switch Interval: {thread_switch_interval} secs, GC Count: {gc_count}")
