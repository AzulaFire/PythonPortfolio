import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)


#http://www.omdbapi.com/?apikey=[yourkey]&
#http://img.omdbapi.com/?apikey=[yourkey]&
#c471e769