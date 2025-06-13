# MovieMatch
MovieMatch is an intelligent movie recommendation system built using Python and Streamlit. It recommends similar movies based on user selection and fetches real-time posters, IMDb ratings, and plots using the OMDb API. It also includes a “Trending Movies” section powered by TMDb data.


Setup Instructions
1. Clone the repository

2. Install dependencies
pip install -r requirements.txt

3. Add your OMDb API key
Update the api_key inside fetch_poster() in app.py:
api_key = "your_actual_omdb_api_key"

4. Run the app
streamlit run app.py
