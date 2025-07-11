import requests
import csv

# Step 1: Get top anime from Jikan
url = "https://api.jikan.moe/v4/top/anime"
response = requests.get(url)
data = response.json()

# Step 2: Extract title and score
anime_list = []
for item in data["data"]:
    title = item["title"]
    score = item["score"]
    anime_list.append([title, score])

# Step 3: Write to CSV
with open("top_anime.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Score"])
    writer.writerows(anime_list)

print("Top anime saved to top_anime.csv")
