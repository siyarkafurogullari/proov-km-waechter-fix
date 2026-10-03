# log_util.py
# Cleaned up and modernized logger.

import time

LOG_LINES: list = []

def log(message: str) -> None:
    """Log a message with a timestamp to the global buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)

def flush_log(path: str) -> None:
    """Write all logged lines to the specified file and clear the buffer."""
    with open(path, "a", encoding="utf-8") as f:
        for line in LOG_LINES:
            f.write(f"{line}\n")
            
    LOG_LINES.clear()
