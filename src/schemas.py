from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    title: str = Field(..., example="Stranger Things")
    top_n: int = Field(default=10, ge=1, le=20)


class Recommendation(BaseModel):
    title: str
    type: str
    genre: str
    rating: str
    similarity: float


class RecommendationResponse(BaseModel):
    query: str
    recommendations: list[Recommendation]

from pydantic import BaseModel


class StatsResponse(BaseModel):

    total_titles: int

    movies: int

    tv_shows: int

    clusters: int

    ratings: int

    genres: int

    oldest_year: int

    newest_year: int