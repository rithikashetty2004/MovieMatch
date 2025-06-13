#  CineMatch: Your AI Movie Companion

##  Overview
**CineMatch** is an intelligent movie recommendation system built using **Python** and **Streamlit**.  
It recommends similar movies based on user selection and fetches real-time **posters**, **IMDb ratings**, and **plots** using the **OMDb API**.  
It also includes a **“Trending Movies”** section powered by **TMDb** data.

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/rithikashetty2004/MovieMatch.git
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your OMDb API key**
   Update the `api_key` inside `fetch_poster()` in `app.py`:

```python
api_key = "your_actual_omdb_api_key"
```

4. **Run the app**

```bash
streamlit run app.py
```


