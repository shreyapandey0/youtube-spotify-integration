# main.py

import os
from yt_scraper import get_trending
from spotify_fetcher import search_spotify_track
import pandas as pd
from tqdm import tqdm

# It's safer to use environment variables for API keys
API_KEY = os.getenv("YOUTUBE_API_KEY", "AIzaSyC7h61TBD4_5AkmA4MaRaC4_bUg60o9cg8")  # Replace with your real API key or set env variable

def main():
    print("Hey! Starting the YouTube trending music videos scraping...")
    yt_df = get_trending(API_KEY, count=50)

    if yt_df.empty:
        print("Oops! YouTube data was not scraped properly. Exiting the program.")
        return

    print("\nHere's a quick peek at the YouTube data we got:")
    print(yt_df.head())
    print(f"\nTotal videos scraped: {len(yt_df)}")

    print("\nNow, let's match these titles with Spotify tracks. This might take a moment...")
    spotify_data = []

    for title in tqdm(yt_df["YouTube Title"], desc="Matching with Spotify"):
        spotify_info = search_spotify_track(title)
        spotify_data.append(spotify_info)

    spotify_df = pd.DataFrame(spotify_data)
    combined_df = pd.concat([yt_df, spotify_df], axis=1)

    with pd.ExcelWriter("yt_spotify_trending_combined.xlsx", engine='xlsxwriter') as writer:
        combined_df.to_excel(writer, sheet_name='Combined Data', index=False)
        yt_df.to_excel(writer, sheet_name='YouTube Data', index=False)
        spotify_df.to_excel(writer, sheet_name='Spotify Data', index=False)

    print("\nAll done! Data has been successfully written to 'yt_spotify_trending_combined.xlsx'.")
    print(f"Total Spotify matches found: {len(spotify_df[spotify_df['Spotify Title'] != 'Not Found'])} out of {len(yt_df)}")

if __name__ == "__main__":
    main()
