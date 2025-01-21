import requests

url = "https://opentdb.com/api.php?amount=10&category=25&difficulty=easy"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error fetching data:", response.status_code)