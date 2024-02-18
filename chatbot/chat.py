import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

#Patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am good, thanks for asking.']),
    (r'what is your name', ['I am a simple chatbot.', 'You can call me ChatBot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'(.*)', ['I am not sure how to respond to that.', 'Could you please rephrase your question?'])
]

#chatbot
chatbot = Chat(patterns, reflections)

def simple_chat():
    print("Hello! I'm a simple chatbot. Ask me anything or just say hello.")
    print("You can type 'bye' to exit the conversation.")

    #Loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

if __name__ == "__main__":
    simple_chat()
