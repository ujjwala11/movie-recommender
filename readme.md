# 🎬 Movie Recommendation System

A content-based movie recommender built with **Python, Scikit-learn, and Streamlit**. It suggests similar movies using **TF-IDF features, K-Means clustering, and cosine similarity**, along with explanations and IMDb search links.

---

## 🚀 Features

- 🎯 Movie recommendations based on similarity
- 🧠 K-Means clustering for grouping movies
- 📊 TF-IDF + cosine similarity ranking
- 💡 Simple explanation for each recommendation
- ⭐ Rating, genre, and similarity score
- 🎬 IMDb search link for each movie
- 🌐 Streamlit web app

---

## 🧠 How It Works

1. Movie metadata is combined (genre, description, cast, etc.)
2. TF-IDF converts text into vectors
3. K-Means groups similar movies
4. Cosine similarity finds closest matches
5. Top results are displayed in UI

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## ▶️ Run Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Improvements

- TMDb API integration (posters + details)
- Hybrid recommendation system
- User personalization
- Better explainability model

---

## 👩‍💻 Author

Ujjwala Thakur
