import requests
import json
import pandas as pd
from tqdm import tqdm

# url = "https://api.themoviedb.org/3/tv/popular?language=en-US&page=5"
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTIzMWMzOGIwZjYyZTZhMDE5ZmYyY2I0NDAxNDg3ZCIsInN1YiI6IjY2MWQ1ZGMzMGU1YWJhMDE4NmY1N2ZkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mOA67eZyv8770KPddl7o6b0KOOgEATiC0HKV7Fvs79c"
# }
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     data = json.loads(response.text)
#     results = data["results"]

#     # Extract titles from the results
#     titles = [movie["name"] for movie in results]
#     years = [movie["first_air_date"][:4] for movie in results]
# else:
#     print("Failed to fetch data. Status code:", response.status_code)

df = pd.read_csv("TMDB_tv_dataset_v3.csv")

names = df["name"]

mykey = ''' INSERT YOUR OWN KEY HERE'''

for name in tqdm(names[]):
    showInfo = requests.get(f"http://www.omdbapi.com/?apikey={mykey}&t={name}&plot=full")

    if showInfo.status_code == 200:
        try:
            showInfo = showInfo.json()
            with open('shows.json', 'a') as f:
                json.dump(showInfo, f)
                f.write(',\n')
        except:
            pass
    elif showInfo.status_code == 401:
        print(f"Unauthorized")
        break
    else:
        print(f"Unable to get acess to movie {name}")