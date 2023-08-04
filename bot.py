# This file contains all the functionalities of the bot including sending messages

import discord
import responses

# Method for sending a message
async def sendMessage(message, userMessage,isPrivate):
    # Handles responses and catches any errors if so
    try:
        response = responses.response_hand(userMessage) # return message to user
        # checks to see which channel message is sent to
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)

# Method for actually running the bot
def run_discord_bot():
    token = "CHANGED DUE TO PRIVACY"
    client = discord.Client(intents=discord.Intents.default()) #client for bot

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    # Functionality fro bot to respond to messages
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        if userMessage.strip().lower() == 'bye':
            return  # The bot will not respond if the user says "bye"
        
        # Sends private messages
        if userMessage.strip() and userMessage[0] == '!':
            userMessage = userMessage[1:]
            await sendMessage(message, userMessage, isPrivate=True)
        else:
            await sendMessage(message, userMessage, isPrivate=False)
    
    client.run(token)
