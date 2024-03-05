from googleapiclient.discovery import build
from tabulate import tabulate

api_key = 'AIzaSyDwRBHNrHLnoFPHI8cUOUruf_1VmtdER-I'
youtube = build('youtube', 'v3', developerKey=api_key)

trending_videos = youtube.videos().list(
    part='snippet,statistics',
    chart='mostPopular',
    regionCode='IN',
    maxResults=50
).execute()

# Define the column headers
headers = ['Video ID', 'Title', 'Views', 'Likes', 'Comments']

# Create a list to store the video data
video_data = []

for video in trending_videos['items']:
    video_id = video['id']
    title = video['snippet']['title']
    view_count = video['statistics']['viewCount']
    like_count = video['statistics']['likeCount']
    comment_count = video['statistics']['commentCount']

    # Append the video data to the list
    video_data.append([video_id, title, view_count, like_count, comment_count])

# Create a tabular representation of the data
table = tabulate(video_data, headers=headers, tablefmt='fancy_grid')

# Print the table
print(table)


    # api_key = 'AIzaSyC6pFOo5ZqxKMHqsW2u7wKtzH5nhvDXHSI'