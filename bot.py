import discord 
import openai 
import os
import time
import json
import configparser
from os import path

# set up cfg
parser = configparser.ConfigParser()
parser.read('conf.ini')

openai.api_key = parser.get('DEFAULT', 'OPENAI_API_KEY')
# set up discord client
client = discord.Client()

# Création de la requête et récupération de la réponse
# Faites varier les paramètres pour des résultats différents
async def OpenAI_Completion(subject,length):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=subject,
        temperature=0.70,
        max_tokens=int(length),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = json.loads(str(response))
    responsetext = result['choices'][0]['text']
    return responsetext

async def createLog(subject,response):
    if (path.exists("logs.txt") == False) :
        f = open("logs.txt","w+")
        f.close()

    f = open("logs.txt","a+")
    f.write(subject + " : " + response + "\n")

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):

    # Commande help
    if message.content.startswith('!help'):
        await message.channel.send("!generate [subject] [length]")

    # Commande generate
    if message.content.startswith("!generate"):

        subject = ""
        args = message.content.split(" ")
        length = 0
        if len(args) > 2:
            for i in range(1,len(args)):
                if(args[i] == '"'):
                    continue 
                else:
                    if(i != len(args)-1):
                        subject += args[i] + " "
                    else: 
                        length = args[i]

            response = await OpenAI_Completion(subject,length)
            await message.channel.send(response)
            await createLog(subject,response)

client.run(str(parser.get('DEFAULT', 'DISCORD_TOKEN')))
