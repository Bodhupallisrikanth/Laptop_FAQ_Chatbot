while True:

    user_question = input("You: ").lower().strip()

    if user_question == "exit":
        print("Bot: Thank you for visiting our Laptop Store. Goodbye!")
        break

    # Keyword-based responses
    if "warranty" in user_question:
        print("Bot: Yes, all laptops include a 1-year manufacturer warranty.\n")
        continue

    if "emi" in user_question:
        print("Bot: Yes, EMI is available on selected credit cards.\n")
        continue

    if "delivery" in user_question:
        print("Bot: Delivery usually takes 3 to 7 business days.\n")
        continue

    if "student" in user_question or "college" in user_question:
        print("Bot: Dell Inspiron and Lenovo IdeaPad are popular student choices.\n")
        continue

    if "gaming" in user_question:
        print("Bot: Yes, we offer gaming laptops from ASUS, Acer and Lenovo.\n")
        continue

    if "brand" in user_question:
        print("Bot: We sell Dell, HP, Lenovo, ASUS and Acer laptops.\n")
        continue

    if "return" in user_question:
        print("Bot: Yes, returns are accepted within 7 days.\n")
        continue

    # TF-IDF fallback
    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    if best_score < 0.20:
        print("Bot: Sorry, I couldn't find a matching answer.\n")
        continue

    matched_question = questions[best_match_index]
    answer = faq_data[matched_question]

    print("Bot:", answer)
    print()