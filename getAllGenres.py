import json

with open("all_genres2.js") as f:
    allGenres = json.load(f)

for genre in allGenres:
    print(genre['name'])