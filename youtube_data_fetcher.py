import googleapiclient.discovery
import os

# This script demonstrates fetching data from the YouTube Data API v3.
# It's a simplified example to illustrate how one might programmatically
# access content, similar to how platforms like Ark STEM leverage YouTube's
# vast educational resources.

# Replace with your actual API key or set it as an environment variable.
# You can obtain an API key from the Google Cloud Console.
API_KEY = os.environ.get('YOUTUBE_API_KEY', 'YOUR_API_KEY_HERE')

if API_KEY == 'YOUR_API_KEY_HERE':
    print("Please set your YOUTUBE_API_KEY environment variable or replace 'YOUR_API_KEY_HERE' with your actual API key.")
    exit()

# Build the YouTube API service object.
# This object allows us to make requests to the YouTube Data API.
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def search_youtube_videos(query, max_results=5):
    """Searches YouTube for videos based on a given query."""
    try:
        # The search.list method is used to find videos, channels, and playlists.
        # We specify 'video' as the type to get video results.
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=max_results
        )
        response = request.execute()

        print(f"--- Top {max_results} YouTube videos for '{query}' ---")
        for item in response.get('items', []):
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            channel_title = item['snippet']['channelTitle']
            print(f"Title: {title}")
            print(f"Channel: {channel_title}")
            print(f"URL: https://www.youtube.com/watch?v={video_id}")
            print("---")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Example: Search for STEM educational videos.
    # This mimics how Ark STEM might discover and curate content.
    search_query = "STEM education"
    search_youtube_videos(search_query, max_results=3)

    search_query_specific = "Python programming tutorial"
    search_youtube_videos(search_query_specific, max_results=2)
