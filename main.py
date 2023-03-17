import requests
from send_email import message

topic = "tesla"

key = "8075fc4c97ae4378b5f182388340517f"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-02-17&sortBy= \
        publishedAt&apiKey={key}&language=en"

request = requests.get(url)

content = request.json()

body = ""
for articles in content['articles'][:20]:
    subject = "News from Tesla"
    body = body + articles['title'] + "\n" \
           + articles['description'] + "\n" \
           + articles['url'] + 2*"\n"

message(subject, body)
