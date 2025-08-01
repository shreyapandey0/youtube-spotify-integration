📁 Project Title: YouTube & Spotify Integrated Music Analysis

📄 Description:
This project extracts the top 50 trending music videos from YouTube using the YouTube Data API, and then cross-references them with Spotify using the Spotify API. The final result is a single Excel sheet containing detailed metadata for each song from both platforms.

🎯 Objective:
- Fetch the top 50 trending music videos from YouTube (Music Category).
- Extract video metadata: title, views, likes, comments, upload date, duration, channel name, and video URL.
- Use the title as a keyword to search for the same song on Spotify.
- Extract Spotify metadata: title, artist, album, release date, popularity, duration, and Spotify link.
- Generate a combined Excel file with a one-to-one mapping of YouTube and Spotify data.

🧰 Tech Stack:
- Language: Python 3.11+
- APIs: 
  - YouTube Data API v3
  - Spotify Web API
- Libraries/Packages:
  - `spotipy`
  - `google-api-python-client`
  - `pandas`
  - `xlsxwriter`
  - `tqdm`
  - `re`
  - `time`

📁 Folder/File Structure:
YouTube and Spotify Integrated Analysis/
│
├── main.py # Main driver script that ties everything together
├── yt_scraper.py # Fetches trending music videos using YouTube Data API
├── spotify_fetcher.py # Matches YouTube titles with Spotify tracks
├── yt_spotify_trending_combined.xlsx # Final Excel output (generated after running)
├── requirements.txt # List of required Python packages (optional)
└── README.txt # You're reading this file


📌 How It Works:
1. `main.py` calls `get_trending()` from `yt_scraper.py` to fetch 50 trending music videos across IN, US, and GB.
2. Each video title is cleaned and passed to Spotify API via `search_spotify_track()` from `spotify_fetcher.py`.
3. Matched data is combined using `pandas` and exported into an Excel file with 3 sheets:
   - `Combined Data`
   - `YouTube Data`
   - `Spotify Data`

📂 Output File:
- **yt_spotify_trending_combined.xlsx**  
Contains full merged data, one row per song, including:
  - YouTube stats: Title, Channel, Views, Likes, Comments, Upload Time, Duration, URL
  - Spotify stats: Title, Artist, Album, Release Date, Popularity, Duration, URL

🔐 Credentials:
- Replace `API_KEY` in `main.py` and `yt_scraper.py` with your YouTube Data API key.
- Replace `client_id` and `client_secret` in `spotify_fetcher.py` with your Spotify developer credentials.

📦 How to Run:
1. Make sure you have Python 3.11+ installed.
2. Install the required packages:
   ```bash
   pip install spotipy google-api-python-client pandas xlsxwriter tqdm
3.Run the main script:
python main.py
4.Check the output file: yt_spotify_trending_combined.xlsx.