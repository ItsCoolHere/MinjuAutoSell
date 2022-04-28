import discord
client = discord.Client()

tokens = []

import json

def open_config():
    f2 = open("../data/config.json")
    config = json.load(f2)
    return config

config = open_config()

@client.event
async def on_ready():
    print('[-1]: logged in as {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):
    for embed in message.embeds:
        embed = embed.to_dict()
        author = embed.get("author")
        name = author["name"]
        if name.upper() == f"{config['user']} — MARKETPLACE".upper():
            f = open("../data/tokens.json", "w")
            print("[0]: command executed")
            for field in embed.get("fields"):
                field_value = field["value"].split("\n")
                tokens.append(field_value[0])
            json.dump(tokens, f)
            print(f"[1]: {type(tokens)} dumped in {f.name}")
            print(f"[3]: {f.name} file closed (for correct storing)")
            f.close()

client.run(config["bot_token"])
