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
# Spotify Mood Playlist 2025: Project Architecture

Here is the professional structure of the repository:

```mermaid
graph TD
    A[README.md] --> B(Project Overview & Roadmap);
    A --> P[Configuration: requirements.txt, .gitignore];
    
    subgraph Data Flow & Processing
        D[data/ <br> (Raw & Processed Datasets)]
        S[sql/ <br> (Schema & Queries)]
        E((src/etl/ <br> (Extract, Transform, Load)));
        
        D -- Read Raw Data --> E;
        E -- Write Cleaned Data --> D;
        E -- Prepare Aggregates --> S;
    end
    
    subgraph Analysis & Modeling
        N[notebooks/ <br> (EDA & Prototypes)];
        M((src/models/ <br> (Production Models)));
        U((src/utils/ <br> (API Clients, Helpers)));
        
        D -- Feeds Features --> N;
        N -- Prototypes Logic --> M;
        M -- Deploys Model Classes --> C;
        E -- Utilizes --> U;
        M -- Utilizes --> U;
    end
    
    subgraph Output & Reporting
        C[Core Recommendation Engine]
        R[reports/ <br> (Documentation & Results)];
        H[dashboard/ <br> (Power BI Files)]
        
        C -- Generates Metrics --> R;
        C -- Powers Visualization --> H;
        N -- Summarizes Findings --> R;
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ddd,stroke:#333
    style P fill:#ddd,stroke:#333
    style D fill:#c7e0f4,stroke:#333
    style N fill:#fff3b0,stroke:#333
    style E fill:#a8dadc,stroke:#333
    style M fill:#b8e0b7,stroke:#333
    style U fill:#d3f2d2,stroke:#333
    style S fill:#ffadad,stroke:#333
    style C fill:#8dcbff,stroke:#333
    style R fill:#ffe6cc,stroke:#333
    style H fill:#e6ccff,stroke:#333
