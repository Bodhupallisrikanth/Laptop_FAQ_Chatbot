import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Data
faq_data = {
    "hi": "Hello! Welcome to Laptop Store. How can I help you today?",
    "hello": "Hello! Welcome to Laptop Store. How can I help you today?",
    "hey": "Hello! Welcome to Laptop Store. How can I help you today?",
    "thanks": "You're welcome! Happy to help.",
    "thank you": "You're welcome! Happy to help.",
    "bye": "Thank you for visiting Laptop Store. Have a great day!",

    "Do you provide warranty?": "Yes, all laptops include a 1-year manufacturer warranty.",
    "Do you provide EMI?": "Yes, EMI is available on selected credit cards.",
    "How long does delivery take?": "Delivery usually takes 3 to 7 business days.",
    "Which laptop is good for students?": "Dell Inspiron and Lenovo IdeaPad are popular student choices.",
    "Do you have gaming laptops?": "Yes, we offer gaming laptops from ASUS, Acer and Lenovo.",
    "What brands are available?": "We sell Dell, HP, Lenovo, ASUS and Acer laptops.",
    "Can I return my laptop?": "Yes, returns are accepted within 7 days.",
    "What is the price of Dell Inspiron?": "The Dell Inspiron starts at ₹55,000.",
    "Do you sell accessories?": "We sell keyboards, mice, bags and headphones.",
    "Do you offer student discounts?": "Student discounts are available on selected models.",
    "What RAM options are available?": "We offer 8GB, 16GB and 32GB RAM options.",
    "Do you support Linux?": "Some laptops support Linux installations.",
    "Do you have SSD laptops?": "SSD storage options range from 256GB to 1TB.",
    "What processors are available?": "We offer Intel Core i3, i5, i7 and AMD Ryzen processors.",
    "Do you have HP laptops?": "HP laptops are available in multiple configurations.",
    "Do you have Dell laptops?": "Dell laptops are known for reliability and performance.",
    "Do you have Lenovo laptops?": "Lenovo offers excellent laptops for students and professionals.",
    "Do you have ASUS laptops?": "ASUS is popular for gaming and creator laptops.",
    "Do you have Acer laptops?": "Acer provides budget-friendly and gaming laptops.",
    "What battery backup do laptops provide?": "Most laptops provide 6 to 10 hours of battery backup.",
    "Do you provide exchange offers?": "Laptop exchange offers are available during promotions.",
    "Do laptops have backlit keyboards?": "Many models feature backlit keyboards.",
    "Do you have touchscreen laptops?": "Selected premium models include touchscreen displays.",
    "What screen sizes are available?": "Available screen sizes range from 14 to 17 inches.",
    "How can I contact support?": "Contact support at support@laptopstore.com."
}

questions = list(faq_data.keys())

# Text Preprocessing
def preprocess(text):
    return text.lower().strip()

processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot Response
def get_bot_response(user_input):

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform([processed_input])

    similarities = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    if best_score > 0.2:
        return faq_data[questions[best_match_index]]
    else:
        return "Sorry, I couldn't find a matching answer."

# Send Message
def send_message():

    user_message = entry.get().strip()

    if not user_message:
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, f"You: {user_message}\n", "user")

    response = get_bot_response(user_message)

    chat_area.insert(tk.END, f"Bot: {response}\n\n", "bot")

    chat_area.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

    chat_area.yview(tk.END)

# Clear Chat
def clear_chat():

    chat_area.config(state=tk.NORMAL)

    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Welcome to Laptop Store FAQ Chatbot!\n\n",
        "bot"
    )

    chat_area.config(state=tk.DISABLED)

# Enter Key
def enter_key(event):
    send_message()

# GUI Window
root = tk.Tk()
root.title("Laptop Store FAQ Chatbot")
root.geometry("800x650")

title = tk.Label(
    root,
    text="Laptop Store FAQ Chatbot",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    width=90,
    height=25,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

chat_area.insert(
    tk.END,
    "Bot: Welcome to Laptop Store FAQ Chatbot!\n\n",
    "bot"
)

chat_area.config(state=tk.DISABLED)

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(
    frame,
    width=50,
    font=("Arial", 12)
)

entry.pack(side=tk.LEFT, padx=5)

entry.bind("<Return>", enter_key)

send_btn = tk.Button(
    frame,
    text="Send",
    font=("Arial", 12, "bold"),
    command=send_message
)

send_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(
    frame,
    text="Clear Chat",
    font=("Arial", 12),
    command=clear_chat
)

clear_btn.pack(side=tk.LEFT)

root.mainloop()