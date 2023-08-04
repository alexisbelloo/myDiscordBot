# This file handles the responses the bot returns when responding to a command
import random

phrases = ["It\'s either one day, or day one!", "Energy flows where your mind goes.", "Just one small positive thought in the morning can change your whole day.", "Never back down, never give up!", "It is never too late to be what you might have been.", "Success is a journey not a destination.", "Change your thoughts, and you change your world.", "It\'s always you vs you.", "If opportunity doesn't knock, build a door.", "If you can dream it, you can do it.", "Everyone thinks of changing the world, but no one thinks of changing himself."]

def response_hand(message) -> str:
    mes = message.lower()
    if mes == "hello":
        return "Hey there! Get up and grind today!"
    if mes == "motivate me!":
        return random.choice(phrases)
    
    # If bot does not recognize command
    return "The world is yours, go get it!"