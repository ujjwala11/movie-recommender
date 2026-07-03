import requests

BASE_URL = "http://127.0.0.1:8000"

def recommend(title, top_n=10):

    response = requests.post(
        f"{BASE_URL}/recommend",
        json={
            "title": title,
            "top_n": top_n
        }
    )

    return response.json()

def titles(search=None):

    params = {}

    if search:
        params["search"] = search

    response = requests.get(
        f"{BASE_URL}/titles",
        params=params
    )

    return response.json()

def stats():

    response = requests.get(f"{BASE_URL}/stats")

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    return response.json()


def history():

    return requests.get(
        f"{BASE_URL}/history"
    ).json()


def explain(title):

    return requests.get(
        f"{BASE_URL}/explain/{title}"
    ).json()

