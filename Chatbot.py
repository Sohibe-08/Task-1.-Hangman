def chatbot():
    print("Welcome to the CodeAlpha Chatbot, Enjoy!")
    while True:
        user = input("User:").lower()
        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I can't understand that")
chatbot()