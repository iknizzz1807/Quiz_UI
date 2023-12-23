import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
# This is the API URL to the question data.
response.raise_for_status()
data = response.json()
question_data = data["results"]