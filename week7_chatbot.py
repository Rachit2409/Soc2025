import random
import nltk
from nltk.stem import PorterStemmer

data = {
    "greetings": ["Hello", "Hi", "hey", "howdy", "hola", "good morning", "good afternoon", "good evening", "what's up", "yo"],
    "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I help you?", "Nice to see you!", "Hi, how are you?", "Hey, what's going on?"],
    "farewells": ["bye", "goodbye", "see you later", "take care", "farewell", "have a good day", "catch you later"],
    "farewell_responses": ["Goodbye!", "See you later!", "Take care!", "Have a great day!", "Bye! Come back soon!", "Farewell!"],
    "questions": ["how are you", "what's your name", "what can you do", "who created you", "what's the weather today"],
    "question_responses": ["I'm just a bot, but I'm doing great!", "I'm your friendly chatbot!", "I can answer questions and chat with you.", "I was created by a developer."],
    "small_talk": ["tell me a joke", "what's new", "how's it going", "what are you up to"],
    "small_talk_responses": ["Why don't scientists trust atoms? Because they make up everything!", "Not much, just here to chat with you!", "It's going well, thanks!"]
}

nltk.download("punkt")
nltk.download("punkt_tab")
stemmer = PorterStemmer()

RESPONSE_MAP = {
    "greetings" : "responses",
    "farewells" : "farewell_responses",
    "questions" : "question_responses",
    "small_talk" : "small_talk_responses"
}

def preprocess(sent):
    tokens = nltk.word_tokenize(sent.lower())
    return [stemmer.stem(token) for token in tokens]


def get_response(input):
    processed_input = preprocess(input)

    for intent_category, response_category in RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])
    return "I'am not sure how to respond to that. Could you rephrase that?"

def chat():
    print("Chatbot : Hello! I'm your friendly chatbot. type 'exit' to end the converstaion.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()