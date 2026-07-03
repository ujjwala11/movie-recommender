from fastapi import APIRouter, HTTPException, Query

from src.schemas import (
    RecommendRequest,
    RecommendationResponse,
    StatsResponse
)

from src.recommender import recommend
from src.search import get_titles
from src.statistics import dataset_statistics
from src.clusters import cluster_of
from src.explain import explain
from src.history import add_history, get_history
from src.logger import logger

router = APIRouter()

# ======================================================
# General
# ======================================================

@router.get(
    "/",
    tags=["General"],
    summary="Home",
    description="Returns basic information about the API."
)
def home():

    return {
        "project": "Netflix Content Intelligence API",
        "version": "1.0.0",
        "status": "Running"
    }


@router.get(
    "/health",
    tags=["General"],
    summary="Health Check",
    description="Checks whether the API is running."
)
def health():

    return {
        "status": "healthy"
    }


# ======================================================
# Recommendation
# ======================================================

@router.post(
    "/recommend",
    response_model=RecommendationResponse,
    tags=["Recommendation"],
    summary="Recommend similar Netflix content"
)
def get_recommendations(request: RecommendRequest):

    logger.info(
        "Recommendation requested | title=%s | top_n=%d",
        request.title,
        request.top_n
    )

    results = recommend(
        request.title,
        request.top_n
    )

    if isinstance(results, dict) and results.get("error"):

        logger.warning(
            "Title not found | %s",
            request.title
        )

        raise HTTPException(
            status_code=404,
            detail=results
        )

    add_history(request.title)

    return {
        "query": request.title,
        "recommendations": results
    }


# ======================================================
# Search
# ======================================================

@router.get(
    "/titles",
    tags=["Search"],
    summary="Search titles"
)
def titles(
    search: str | None = Query(
        default=None,
        description="Optional title search"
    )
):

    return get_titles(search)


# ======================================================
# Statistics
# ======================================================

@router.get(
    "/stats",
    response_model=StatsResponse,
    tags=["Analytics"],
    summary="Dataset Statistics"
)
def stats():

    logger.info("Statistics requested")

    return dataset_statistics()


# ======================================================
# Cluster
# ======================================================

@router.get(
    "/cluster/{title}",
    tags=["Analytics"],
    summary="Get Cluster of a Title"
)
def get_cluster(title: str):

    logger.info("Cluster requested | %s", title)

    result = cluster_of(title)

    if result is None:

        raise HTTPException(
            status_code=404,
            detail="Title not found."
        )

    return result


# ======================================================
# Explainability
# ======================================================

@router.get(
    "/explain/{title}",
    tags=["Explainability"],
    summary="Explain Recommendation"
)
def explain_title(title: str):

    logger.info("Explanation requested | %s", title)

    result = explain(title)

    if result is None:

        raise HTTPException(
            status_code=404,
            detail="Title not found."
        )

    return result


# ======================================================
# History
# ======================================================

@router.get(
    "/history",
    tags=["Search"],
    summary="Recent Search History"
)
def history():

    logger.info("History requested")

    return {
        "recent_searches": get_history()
    }