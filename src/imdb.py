import urllib.parse

def get_imdb_search_url(title: str):
    return f"https://www.imdb.com/find/?q={urllib.parse.quote(title)}"