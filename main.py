import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hhdehd32d9dh93hf332b3b3",
    "username": "anirbanbasu",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url= pixela_endpoint, json= user_params)
print(response)
print(response.text)
