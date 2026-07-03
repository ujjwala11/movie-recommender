from src.load_models import model_manager


def cluster_of(title):

    idx = model_manager.indices.get(title)

    if idx is None:

        return None

    return {

        "title": title,

        "cluster": int(

            model_manager.data.iloc[idx]["cluster"]

        )

    }