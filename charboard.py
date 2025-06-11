import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

# Intents dictionary
intents = {
    "greeting": ["hello", "hi", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye"],
    "thanks": ["thank you", "thanks", "thx"],
    "name_query": ["what is your name", "who are you"],
    "default": ["I'm sorry, I didn't understand that."]
}

# Responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "name_query": "I'm MediBot, your health assistant!",
    "default": "Sorry, I didn’t quite get that. Can you rephrase?"
}

# Preprocessing
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

# Intent detection
def detect_intent(user_input):
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in user_input.lower():
                return intent
    return "default"

# Response
def get_response(intent):
    return responses.get(intent, responses["default"])

# Chat loop
def chat():
    print("🤖 MediBot: Hi, I’m MediBot. Ask me something!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("🤖 MediBot: Bye! Stay healthy.")
            break
        intent = detect_intent(user_input)
        response = get_response(intent)
        print(f"🤖 MediBot: {response}")

if __name__ == "__main__":
    chat()
