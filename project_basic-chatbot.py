import nltk
import random
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections

nltk.download('wordnet')

pairs = [
    [r"hi|hello|hey", ["Hi there!", "Hey! How can I help you?"]],
    [r"i am good", ["Glad to hear that! How's your day going so far?"]],
    [r"Who created you?", ["I was created by Wahid jamadar for a code alpha internship task"]],
    [r"Who is wahid?", [" I  was created by wahid ,Inshort wahid brought me to life with code and a lot of creativity!"]],
    [r"how are you?", ["I'm a chatbot, but I'm here to help!", "I'm great, thanks for asking!"]],
    [r"what is your name?", ["I'm ChatBot, your friendly assistant."]],
    [r"bye|goodbye", ["Goodbye!", "See you soon!", "It was nice talking to you!"]],
    [r"(.*) help (.*)", ["I'm here to help! What do you need assistance with?", "Sure, I can help with that."]],
     [r"help", ["I'm here to help! What do you need assistance with?", "Sure, I can help with that."]],
    [r"(.*) your favorite (.*)", ["I don't have personal preferences, but I can help you with yours!"]],
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I am a basic chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chat()