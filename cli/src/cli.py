import requests
from argparse import ArgumentParser, Namespace
from enum import Enum


# # Enum to be implemented at a future date
# class Action(Enum):
#     NEWGAME = 1
#     GAMEACTION = 2
#     QUIT = 3
# print(list(Action))


parser = ArgumentParser()
parser.add_argument('server_url', help='The URL of the server')
args = parser.parse_args()
server_url = args.server_url

print(f"Server URL: {server_url}")

CURRENT_SERVER = "http://192.168.0.199:80"

r = requests.get(f"{server_url}")
print(r.text)

action = ''

def cli():
    while True:
        action = input('type "newgame", "action" or "quit": ')

        if action == "newgame":
            r = requests.get(f"{server_url}/newGame")
            print(r.text)

        elif action == "action":
            r = requests.get(f"{server_url}/action")
            r = requests.get(f"{server_url}/gameState")
            print(r.text)

        elif action == "quit":
            exit()


cli()