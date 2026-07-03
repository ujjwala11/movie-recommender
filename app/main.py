from fastapi import FastAPI
from app.routes import router

app = FastAPI(

title="Netflix Content Intelligence API",

version="1.0",

description="""
Recommendation engine built using

• TF-IDF

• TruncatedSVD

• KMeans++

• Cosine Similarity

• Explainable AI
""",

contact={
"name":"Ujjwala Thakur",
"email":"..."
},

license_info={
"name":"MIT"
}
)
app.include_router(router)