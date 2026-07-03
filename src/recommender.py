from sklearn.metrics.pairwise import cosine_similarity
from src.load_models import model_manager
from src.search import suggest_titles
from src.imdb import get_imdb_search_url

def recommend(title: str, top_n: int = 10):

    if title not in model_manager.indices:
        return {
            "error": True,
            "message": f"'{title}' not found.",
            "suggestions": suggest_titles(title)
        }

    idx = model_manager.indices[title]

    cluster = model_manager.data.iloc[idx]["cluster"]

    cluster_idx = (
        model_manager.data[
            model_manager.data["cluster"] == cluster
        ]
        .index
        .tolist()
    )

    # safety check
    if len(cluster_idx) <= 1:
        return []

    movie_vector = model_manager.X[idx].reshape(1, -1)
    cluster_vectors = model_manager.X[cluster_idx]

    similarities = cosine_similarity(
        movie_vector,
        cluster_vectors
    ).flatten()

    scores = list(zip(cluster_idx, similarities))

    scores = [x for x in scores if x[0] != idx]

    scores.sort(key=lambda x: x[1], reverse=True)

    recommendations = []

    for i, score in scores[:top_n]:

        recommendations.append({
            "title": model_manager.data.iloc[i]["title"],
            "type": model_manager.data.iloc[i]["type"],
            "genre": model_manager.data.iloc[i]["listed_in"],
            "rating": model_manager.data.iloc[i]["rating"],
            "similarity": round(float(score), 3),
            "imdb_url": get_imdb_search_url(model_manager.data.iloc[i]["title"])
        })

    return recommendations