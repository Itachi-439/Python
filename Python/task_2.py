from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

print("Chatbot is ready to chat!")

def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")
