def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif 'hi' in user_input or 'hello' in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but thank you for asking! How about you?")
        elif 'what is your name' in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")
        elif 'help' in user_input:
            print("Chatbot: Sure! What do you need help with?")
        else:
            print("Chatbot: I'm sorry, I don't understand that.")
chatbot()