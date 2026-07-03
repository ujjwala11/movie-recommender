from src.load_models import model_manager


def dataset_statistics():

    df = model_manager.data

    return {
        "total_titles": len(df),

        "movies": int((df["type"] == "Movie").sum()),

        "tv_shows": int((df["type"] == "TV Show").sum()),

        "clusters": int(df["cluster"].nunique()),

        "ratings": int(df["rating"].nunique()),

        "genres": int(df["listed_in"].nunique()),

        "oldest_year": int(df["release_year"].min()),

        "newest_year": int(df["release_year"].max())
    }