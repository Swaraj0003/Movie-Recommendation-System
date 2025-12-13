Movie Recommendation System


A modular, content-based Movie Recommendation System built using Python, Machine Learning, and Streamlit.
The application recommends movies similar to a user-selected title based on textual features such as genres and plot descriptions, and presents results through an interactive web interface.

The system uses a Content-Based Filtering technique:

Text Feature Engineering

Movie genres and plot summaries are combined and vectorized

Similarity Computation

Cosine similarity is computed to measure closeness between movies

Recommendation Logic

Movies with the highest similarity scores are recommended

This approach ensures recommendations are based on movie content, not user history.


Movie_Recommentation_System/

│

├── app.py

│
├── src/

│   ├── data_loader.py        # Data loading utilities

│   ├── recommender.py        # Similarity matrix & recommendation logic

│   ├── ui_components.py      # Streamlit UI components

│
├── data/

│   └── movies_with_posters.csv

│
├── requirements.txt

└── README.md


git clone https://github.com/Swaraj0003/Movie-Recommendation-System.git


cd Movie-Recommendation-System



python -m venv venv


source venv/bin/activate


pip install -r requirements.txt


streamlit run app.py

