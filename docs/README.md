## 📌 Day 3 – Research on Spotify Recommendation Systems

As part of my 6-month Spotify Data Science Project Simulation, today I studied how **Spotify builds recommender systems** using academic papers and engineering blog posts.

### 🔑 Key Learnings
- Spotify uses a **hybrid recommender** combining collaborative filtering, content-based filtering, and NLP on audio/lyrics.
- **Collaborative Filtering (ALS, Matrix Factorization):** Learns from user–item interactions.
- **Content-Based Filtering:** Uses audio features (tempo, key, loudness) and lyrics embeddings.
- **NLP & Embeddings:** Word2Vec, BERT, and Annoy are used for playlist/track similarity.
- **Context-Aware Signals:** Time of day, device, and user activity influence recommendations.
- **Bandits & Exploration:** Spotify balances exploration of new songs with exploitation of known preferences.

### 📄 Document
I compiled my notes into a Word document for reference:  
👉 [Spotify_Recommender_Notes_Day3.docx](Spotify_Recommender_Notes_Day3.docx)

### 📚 References
- [Spotify Engineering Blog](https://engineering.atspotify.com)  
- [MIT Tech Review – How Discover Weekly Works](https://www.technologyreview.com/2015/09/30/165944/how-spotify-discover-weekly-works/)  
- Hu, Koren, Volinsky (2008) – *Collaborative Filtering for Implicit Feedback Datasets*  
- Spotify Open Source Library – [Annoy](https://github.com/spotify/annoy)  

