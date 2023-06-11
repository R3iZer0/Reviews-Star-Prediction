from googleapiclient.discovery import build
import csv

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'AIzaSyDqHZeaYUSqXFfF7gLmPGG-4YeXLYqzDwA'

# Replace 'VIDEO_ID' with the ID of the YouTube video you want to download comments from
VIDEO_ID = 'yWYkoZKHLfg'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Retrieve the comments for the specified video
response = youtube.commentThreads().list(
    part='snippet',
    videoId=VIDEO_ID,
    maxResults=100,  # Adjust this value to control the number of comments to retrieve
    order='relevance'  # You can change the order if needed
).execute()

# Create a CSV file to save the comments
csv_file = open('youtube_commentsTOMSCOT.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Comment', 'Author', 'Likes'])

# Iterate over the comments and save them in the CSV file
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    likes = item['snippet']['topLevelComment']['snippet']['likeCount']
    csv_writer.writerow([comment, author, likes])

# Close the CSV file
csv_file.close()