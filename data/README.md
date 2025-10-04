# 📂 Dataset Overview  
**Project:** Spotify – Mood & Context-Aware Playlist Recommender (2025)  

This folder contains datasets used for building a mood & context-aware playlist recommender system.  

---

## 1️⃣ Spotify Playlists 🎵
- **Source:** [Spotify Web API](https://developer.spotify.com/documentation/web-api/), [Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge), [Spotify Tracks DB (Kaggle)](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)  
- **Features:**  
  - Track ID, artist, genre, popularity  
  - Audio features: `danceability`, `energy`, `valence`, `tempo`, etc.  
  - Playlist context: playlist name, curator tags  
- **Purpose:** Core recommendation signals (song properties + playlist metadata).  

📁 Folder: `data/spotify/`  

---

## 2️⃣ Genius Lyrics 📜
- **Source:** [Genius API](https://docs.genius.com/), [Lyrics Dataset (Kaggle)](https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres)  
- **Features:**  
  - Song lyrics (raw text)  
  - Extracted emotions using NLP (joy, sadness, anger, positivity/negativity)  
- **Purpose:** Mood-aware feature extraction from song lyrics.  

📁 Folder: `data/lyrics/`  

---

## 3️⃣ Twitter / Reddit Sentiment 🐦📢
- **Source:** [Twitter Academic API](https://developer.twitter.com/en/docs/twitter-api), [Pushshift Reddit API](https://pushshift.io/)  
- **Features:**  
  - Post/tweet text  
  - Hashtags & mood indicators (#happy, #sad, #studyvibes)  
  - Sentiment score (positive, negative, neutral)  
- **Purpose:** Context-aware signals for user moods, activities, and listening context.  

📁 Folder: `data/social_media/`  

---

## ✅ Summary Table

| Dataset | Source | Features | Purpose |
|---------|--------|----------|---------|
| Spotify Playlists | Spotify API, Kaggle | Audio features, playlist metadata | Core recommendation signals |
| Genius Lyrics | Genius API, Kaggle | Song lyrics, NLP sentiment/emotion | Mood-aware features |
| Twitter/Reddit | APIs, Pushshift | User mood posts, hashtags, sentiment | Context-aware features |

---

👉 Next Steps:  
- Download sample datasets into respective folders.  
- Preprocess raw data for **ETL pipeline** (to be implemented in later steps).  
