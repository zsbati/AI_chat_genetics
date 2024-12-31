import json
import random
import os


class SimpleChatbot:
    def __init__(self):
        self.knowledge = {}
        self.load_knowledge()

    def load_knowledge(self):
        # Try to load existing knowledge from file
        try:
            with open('chatbot_knowledge.json', 'r') as f:
                self.knowledge = json.load(f)
        except FileNotFoundError:
            self.knowledge = {}

    def save_knowledge(self):
        # Save knowledge to file
        with open('chatbot_knowledge.json', 'w') as f:
            json.dump(self.knowledge, f)

    def get_response(self, user_input):
        # Convert input to lowercase for consistency
        user_input = user_input.lower()

        # If we have a response for this input, return it
        if user_input in self.knowledge:
            return random.choice(self.knowledge[user_input])
        else:
            # If we don't know how to respond, ask for help
            new_response = input("I don't know how to respond to that. How should I respond? ")

            # Store the new response
            if user_input not in self.knowledge:
                self.knowledge[user_input] = []
            self.knowledge[user_input].append(new_response)
            self.save_knowledge()

            return "Thanks for teaching me! I'll remember that."


def main():
    print("Simple Chatbot: Hello! Type 'quit' to exit.")
    chatbot = SimpleChatbot()

    while True:
        user_input = input("You: ").lower()

        if user_input == 'quit':
            print("Simple Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Simple Chatbot:", response)


if __name__ == "__main__":
    main()
