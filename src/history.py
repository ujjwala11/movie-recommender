from collections import deque

# Store the last 20 searches
_history = deque(maxlen=20)


def add_history(title: str):
    _history.appendleft(title)


def get_history():
    return list(_history)


def clear_history():
    _history.clear()