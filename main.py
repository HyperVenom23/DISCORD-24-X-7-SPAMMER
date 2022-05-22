from webserver import keep_alive
import requests

channelID = 911481124319010837
headers = {
    "authorization":
    "1653165289232"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
