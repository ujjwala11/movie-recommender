from difflib import get_close_matches
from src.load_models import model_manager


def get_titles(search: str | None = None):
    titles = sorted(model_manager.data["title"].dropna().unique())

    if search:
        search = search.lower()
        titles = [t for t in titles if search in t.lower()]

    return titles


def suggest_titles(title: str, n: int = 5):
    titles = model_manager.data["title"].dropna().unique().tolist()

    return get_close_matches(
        title,
        titles,
        n=n,
        cutoff=0.4
    )