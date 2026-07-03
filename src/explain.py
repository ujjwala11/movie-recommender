from src.load_models import model_manager


def explain(title):

    idx = model_manager.indices.get(title)

    if idx is None:

        return None

    row = model_manager.data.iloc[idx]

    return {

        "title": row["title"],

        "cluster": int(row["cluster"]),

        "genre": row["listed_in"],

        "rating": row["rating"],

        "type": row["type"]

    }