import requests
from bs4 import BeautifulSoup

req = requests.get("https://twitter.com/i/status/1687488206017638400")
soup = BeautifulSoup(req.content, "html.parser")
res= soup.title

print(soup.prettify())

# import requests
# from bs4 import BeautifulSoup

# def scrape_twitter_video(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     video_elements = soup.select('div.js-tweet-text-container video')

#     if video_elements:
#         video_url = video_elements[0]['src']
#         return video_url

#     return None

# def download_video(url, save_as):
#     response = requests.get(url, stream=True)
#     if response.status_code == 200:
#         with open(save_as, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     file.write(chunk)
#         print("Video downloaded successfully!")
#     else:
#         print("Failed to download video.")

# # Provide the Twitter video link here
# twitter_link = "https://twitter.com/i/status/1687488206017638400"

# video_url = scrape_twitter_video(twitter_link)

# if video_url:
#     print("Video URL:", video_url)
#     # Use the video URL to download the video
#     file_name = "video.mp4" # Specify the desired file name
#     download_video(video_url, file_name)
# else:
#     print("No video found at the provided link.")

