import tkinter as tk
import random

# Define more rules for the chatbot
rules = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a computer program, but I'm doing well. How can I help you?"],
    "what's your name": ["I'm a chatbot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "help": ["I'm here to answer your questions. Just ask anything!"],
    "age": ["I'm ageless, just a few lines of code!", "Age is just a number for me."],
    "weather": ["I'm not sure about the weather, but you can check your favorite weather website for updates."],
    "time": ["I don't have a watch, but your device can tell you the time."],
    "thanks": ["You're welcome!", "No problem, happy to help!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?"]
}


def chatbot_response(user_input):
    user_input = user_input.lower()

    for key, value in rules.items():
        if key in user_input:
            return random.choice(value)

    return random.choice(rules["default"])


def send_message():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    response = chatbot_response(user_input)
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.insert(tk.END, "ChatBot: " + response + "\n")
    chat_box.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Rule-Based ChatBot")

# Create GUI components
chat_box = tk.Text(root, height=20, width=60)
user_entry = tk.Entry(root, width=60)
send_button = tk.Button(root, text="Send", command=send_message)

# Configure GUI components
chat_box.config(state=tk.DISABLED)
chat_box.pack()
user_entry.pack()
send_button.pack()

# Run the main loop
root.mainloop()
