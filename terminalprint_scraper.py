import requests

# Step 1: Get top anime from Jikan API
url = "https://api.jikan.moe/v4/top/anime"
response = requests.get(url)
data = response.json()

# Step 2: Extract and print title + score
print("📺 Top 25 Anime on MyAnimeList:")
print("-" * 40)

for rank, item in enumerate(data["data"], start=1):
    title = item["title"]
    score = item["score"]
    print(f"#{rank}. {title} — Score: {score}")
