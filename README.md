# 🎶 Song Popularity Prediction – End-to-End ML Application

An end-to-end machine learning application designed to analyze structured music streaming data and estimate Spotify stream counts using audio and platform-level signals.

This project goes beyond model training — it focuses on transforming analysis into a deployable, interactive data product.

🔗 **Live App:**  
https://music-streaming-hit-predictor.streamlit.app/

---

## 📌 Project Overview

Streaming performance is influenced by multiple structured signals — including audio characteristics and platform visibility.

This project aims to:

- Perform structured exploratory data analysis (EDA)
- Engineer meaningful predictive features
- Compare multiple regression models
- Improve performance using log transformation
- Extract feature importance for interpretability
- Deploy a production-style multi-page ML app using Streamlit

The final result is an interactive what-if simulator that allows users to explore how changes in inputs affect predicted streaming performance.

---

## 🧠 Problem Framing

Can structured audio traits and platform presence signals help estimate streaming performance?

Using supervised regression modeling, this project builds a predictive framework to estimate Spotify stream counts based on:

- Audio features (danceability, energy, valence, etc.)
- Playlist and platform presence
- Release metadata

While streaming success depends on broader ecosystem factors (artist popularity, marketing, genre dynamics), this application demonstrates how far structured data can go in predictive modeling.

---

## 🛠 Tech Stack

**Language**
- Python

**Core Libraries**
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- joblib
- streamlit

**Deployment**
- Streamlit Cloud

---

## 📊 Exploratory Data Analysis

- Distribution analysis of stream counts
- Correlation heatmaps
- Feature vs. stream trend visualization
- Playlist presence impact analysis
- Seasonality exploration
- Audio trait influence breakdown

All EDA development is contained in:

`notebooks/Song Popularity EDA.ipynb`

---

## 🏗 Modeling Approach

Models evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Enhancements applied:

- Log transformation of target variable for stability
- Cross-validation comparisons
- Baseline vs. improved model comparison

**Best Performing Model**
- Random Forest (log-transformed)
- R² ≈ 0.79

Final saved model:
`models/random_forest_log_model.pkl`

---

## 📈 Feature Importance Insights

Key predictors included:

- Playlist presence (Spotify, Apple)
- Platform visibility metrics
- Audio attributes (energy, danceability)

Feature importance analysis provides interpretability — helping translate model output into business insights.

---

## 🌐 Streamlit Application

The deployed app is structured as a modular multi-page dashboard:

```
components/
│── nav.py                     # Custom navigation & styling
pages/
│── EDA_Insights.py
│── Model Training Information.py
│── Prediction Tool.py
│── Project_Summary.py
Home.py                        # Landing page
```

### App Highlights

- Clean navigation with custom CSS styling
- Modular architecture
- Interactive prediction engine
- State-safe input handling
- Custom UI refinement aligned with modern dashboard aesthetics
- End-to-end deployment ready

---

## 🔮 Interactive Prediction Tool

Users can input:

- Audio features
- Platform metrics
- Release information

The model returns:

- Estimated Spotify stream count
- Interpretable prediction output

Designed as a decision-support simulation rather than a static prediction script.

---

## 💼 Business Implications

This application demonstrates how predictive analytics can support:

- A&R scouting decisions
- Playlist strategy evaluation
- Marketing timing considerations
- Platform visibility analysis
- Audio feature impact interpretation

It bridges analytical modeling with product usability.

---

## 📁 Repository Structure

```
.
├── .streamlit/
│   └── config.toml
├── components/
│   └── nav.py
├── images/
│   ├── EDA visualizations
│   ├── feature importance plots
│   ├── background & banner assets
├── models/
│   └── random_forest_log_model.pkl
├── notebooks/
│   └── Song Popularity EDA.ipynb
├── pages/
│   ├── EDA_Insights.py
│   ├── Model Training Information.py
│   ├── Prediction Tool.py
│   ├── Project_Summary.py
├── Home.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Running Locally

Clone the repository:

```
git clone <your-repo-link>
cd <repo-folder>
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run Home.py
```

---

## 🎯 What This Project Demonstrates

- Structured EDA methodology
- Feature engineering & transformation
- Model comparison and validation
- Interpretability via feature importance
- Transition from notebook → deployed app
- UI/UX refinement without breaking model logic
- End-to-end ML workflow ownership

---

## 👤 Author

Akash Ray  
Data Analytics & Machine Learning Enthusiast  

🔗 LinkedIn: https://www.linkedin.com/in/akashray1/
🔗 Live App: https://music-streaming-hit-predictor.streamlit.app/

--
