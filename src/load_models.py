from pathlib import Path
import joblib
import pandas as pd
from scipy import sparse

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"


class ModelManager:
    def __init__(self):

        print("Loading models...")

        self.tfidf = joblib.load(MODELS_DIR / "tfidf.pkl")
        self.svd = joblib.load(MODELS_DIR / "svd.pkl")
        self.kmeans = joblib.load(MODELS_DIR / "kmeans.pkl")

        self.data = pd.read_csv(DATA_DIR / "netflix_processed.csv")

        self.indices = joblib.load(MODELS_DIR / "title_indices.pkl")

        self.X = sparse.load_npz(MODELS_DIR / "X_tfidf.npz")

        print("Models loaded successfully!")


model_manager = ModelManager()