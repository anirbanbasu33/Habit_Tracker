import requests

USERNAME = "anirbanbasu"
TOKEN = "hhdehd32d9dh93hf332b3b3"
GRAPH_ID = "graph1"



pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

# POST - /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Book_Reading_Tracker",
    "unit": "pages",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Kolkata",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

# POST - /v1/users/<username>/graphs/<graphID>
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_creation_config = {
    "date": "20250207",
    "quantity": "10"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)


