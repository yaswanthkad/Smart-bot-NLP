#               SMART CHATBOT IN PYTHON WITH NLP (NATURAL LANGUAGE PROCESSING)



import random
import nltk #pip install nltk 
from nltk.stem import PorterStemmer
from data import data

#initialize NLTK and download required resources
nltk.download("punkt")
nltk.download("punkt_tab")
stemmer = PorterStemmer()


#Map intenet categories to theri corressponding response categories
INTENT_RESPONSE_MAP = {
    "greetings" : "responses",
    "farewells" : "farewell_responses",
    "questions" : "question_responses",
    "small_talk" : "small_talk_responses",
    "profesinal_talk": "profesinal_talk_response",
    "one":"one_response",
    "project":"project_response",
    "Road_map":"Road_map_response",
    "Tools":"Tools_response",
    "Tasks":"Tasks_response",
    "NLTK":"NLTK_response"
}

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]


def get_response(user_input):
    processed_input = preprocess(user_input)

    #check for all the pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])
            
    #fall back for unknown inputs 
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