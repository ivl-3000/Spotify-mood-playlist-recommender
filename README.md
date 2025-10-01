# 🎵 Spotify – Mood & Context-Aware Playlist Recommender (2025 Project)  

## 📌 Project Overview  
This project aims to build a **mood & context-aware music recommender system** using **Spotify playlists, lyrics, and social sentiment data**. By combining **NLP (mood detection)** with **recommender system techniques (collaborative + content-based + hybrid)**, the goal is to recommend playlists not only based on user preferences but also on **mood and emotional context**.  

---

## 🎯 Project Scope  

✅ **In Scope**  
- Collecting Spotify playlist metadata (songs, artists, albums, genres).  
- Collecting & preprocessing lyrics data.  
- Collecting social sentiment data (Twitter/Reddit or dataset).  
- Storing all data in SQL for structured access.  
- NLP pipeline for mood/emotion detection from lyrics & posts.  
- Building a hybrid recommender (collaborative + content-based + mood-aware).  
- Power BI dashboard for mood trends & recommendations.  
- Documentation & showcase (GitHub + LinkedIn).  

❌ **Out of Scope**  
- Real-time Spotify app integration.  
- Production-level deployment.  
- Multilingual lyric support (focus: English only).  
- Advanced deep reinforcement learning recommenders.  

---

## 🎯 Project Objectives  

1. **Data Collection & Storage**  
   - Gather Spotify playlists, lyrics, and sentiment data.  
   - Store datasets in SQL with a clean schema.  

2. **Mood Detection with NLP/LLMs**  
   - Preprocess text data (tokenization, lemmatization, stopwords).  
   - Fine-tune BERT/LLaMA models for emotion classification.  
   - Categorize moods: *happy, sad, energetic, calm*.  

3. **Recommender System Development**  
   - Implement collaborative filtering (user–item).  
   - Implement content-based filtering (lyrics/genre similarity).  
   - Add mood-aware filtering layer.  
   - Combine into hybrid recommender & evaluate with metrics (Precision@K, Recall@K, NDCG).  

4. **Dashboard & Showcase**  
   - Build Power BI dashboard (mood trends, recommendations).  
   - Write technical report.  
   - Publish GitHub repo & LinkedIn showcase posts.  

---

## 📌 Project Roadmap  

### Phase 1: Setup & Data Collection (Oct 1 – Oct 15)  
- Repo setup, dataset research, SQL schema design, raw data storage.  

### Phase 2: Mood Detection with NLP/LLMs (Oct 16 – Oct 31)  
- NLP preprocessing, model fine-tuning, mood classification.  

### Phase 3: Recommender System Development (Nov 1 – Nov 30)  
- Baseline recommenders, hybrid model, evaluation, visualization.  

### Phase 4: Dashboard & Final Deliverables (Dec 1 – Dec 30)  
- Power BI dashboard, report writing, GitHub polish, LinkedIn showcase.  

---

## 📂 Repository Structure (planned)  
graph TD
    A[Spotify Mood Playlist 2025] --> B(README.md);

    subgraph Project Structure
        B --> C[data/];
        B --> D[notebooks/];
        B --> E[src/];
        B --> F[sql/];
        B --> G[dashboard/];
        B --> H[reports/];
    end

    subgraph data/
        C --> C1(raw_data/);
        C --> C2(processed_data/);
    end

    subgraph notebooks/
        D --> D1(EDA.ipynb);
        D --> D2(Model_Prototyping.ipynb);
    end

    subgraph src/
        E --> E1(etl/);
        E --> E2(models/);
        E --> E3(utils/);
    end

    subgraph etl/
        E1 --> E1_1(extract.py);
        E1 --> E1_2(transform.py);
        E1 --> E1_3(load.py);
    end

    subgraph models/
        E2 --> E2_1(mood_classifier.py);
        E2 --> E2_2(recommender.py);
    end

    subgraph utils/
        E3 --> E3_1(spotify_api_client.py);
        E3 --> E3_2(config.py);
    end

    subgraph sql/
        F --> F1(schema.sql);
        F --> F2(queries.sql);
    end

    subgraph dashboard/
        G --> G1(Spotify_Mood_Dashboard.pbix);
        G --> G2(Dashboard_Specs.pdf);
    end

    subgraph reports/
        H --> H1(Technical_Report.pdf);
        H --> H2(Presentation.pptx);
    end

    style A fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
    style B fill:#2196F3,stroke:#1976D2,stroke-width:1px,color:#fff
    style C fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px
    style D fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px
    style E fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px
    style F fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px
    style G fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px
    style H fill:#FFEB3B,stroke:#FBC02D,stroke-width:1px

    style C1 fill:#f9f9f9,stroke:#ccc
    style C2 fill:#f9f9f9,stroke:#ccc
    style D1 fill:#f9f9f9,stroke:#ccc
    style D2 fill:#f9f9f9,stroke:#ccc
    style E1 fill:#f9f9f9,stroke:#ccc
    style E2 fill:#f9f9f9,stroke:#ccc
    style E3 fill:#f9f9f9,stroke:#ccc
    style E1_1 fill:#f9f9f9,stroke:#ccc
    style E1_2 fill:#f9f9f9,stroke:#ccc
    style E1_3 fill:#f9f9f9,stroke:#ccc
    style E2_1 fill:#f9f9f9,stroke:#ccc
    style E2_2 fill:#f9f9f9,stroke:#ccc
    style E3_1 fill:#f9f9f9,stroke:#ccc
    style E3_2 fill:#f9f9f9,stroke:#ccc
    style F1 fill:#f9f9f9,stroke:#ccc
    style F2 fill:#f9f9f9,stroke:#ccc
    style G1 fill:#f9f9f9,stroke:#ccc
    style G2 fill:#f9f9f9,stroke:#ccc
    style H1 fill:#f9f9f9,stroke:#ccc
    style H2 fill:#f9f9f9,stroke:#ccc
