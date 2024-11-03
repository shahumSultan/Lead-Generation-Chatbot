import random

# BOT RESPONSE FOR SIMPLE CUSTOMER QUERY
def bot_response_simple(leadType):
    responses = {
        "loan": [
            "We can help with loan options. What would you like to know? Would you please provide your name, email and phone number for further assistance?",
            "Have questions about loans? We're here to help. Would you please provide your name, email and phone number for further assistance?",
            "Let us know if you need details on loans. Please provide your name, email and phone number for further assistance?"
        ],
        "borrowing": [
            "How much are you looking to borrow? Would you please provide your name, email and phone number for further assistance?",
            "Let's talk about borrowing options. Would you please provide your name, email and phone number for further assistance?",
            "Interested in borrowing? We're here to help. Would you please provide your name, email and phone number for further assistance?",
            "What type of loan are you looking for? Would you please provide your name, email and phone number for further assistance?",
            "How much do you need to borrow? Would you please provide your name, email and phone number for further assistance?",
            "What timeline do you have in mind for the loan? Would you please provide your name, email and phone number for further assistance?"
        ],
        "investment": [
            "Thinking of investing? Let's chat. Would you please provide your name, email and phone number for further assistance?",
            "We can guide you on investment options. Would you please provide your name, email and phone number for further assistance?",
            "Interested in investing? We'd love to help. Would you please provide your name, email and phone number for further assistance?",
            "Interested in real estate private notes? We'd be happy to share details. Would you please provide your name, email and phone number for further assistance?",
            "We offer various investment options. Would you like to learn more? Would you please provide your name, email and phone number for further assistance?",
            "Thinking about investing? We can guide you on real estate private notes. Would you please provide your name, email and phone number for further assistance?"
        ],
        "partnership": [
            "Looking for a partnership? Let's discuss. Would you please provide your name, email and phone number for further assistance?",
            "We'd love to talk about partnering. Would you please provide your name, email and phone number for further assistance?",
            "Interested in a partnership? Let us know. Would you please provide your name, email and phone number for further assistance?",
            "Can you tell us more about your role? Would you please provide your name, email and phone number for further assistance?",
            "We'd love to learn about your interest in collaborating with us. Would you please provide your name, email and phone number for further assistance?",
            "Are you interested in partnering with our business? Let's discuss your goals. Would you please provide your name, email and phone number for further assistance?"
        ]
    }

    bot_response = responses.get(leadType)
    return random.choice(bot_response)

# BOT RESPONSE FOR HIGH CUSTOMER QUERY
def bot_response_high(leadType):
    responses = {
        "loan": [
            "Thank you for your interest in our loan options. How can we assist you further? Please do provide your name, email and phone number for a personalised experience.",
            "We're here to help with your loan inquiries. Do you have any specific questions? Please do provide your name, email and phone number for a personalised experience.",
            "Looking to explore loan options? Let us know the details, and we'll guide you! Please do provide your name, email and phone number for a personalised experience."
        ],
        "borrowing": [
            "We're glad you're considering borrowing with us! How much were you interested in borrowing? Please do provide your name, email and phone number for a personalised experience.",
            "Borrowing is a great option! We're here to discuss terms and help you with the process. Please do provide your name, email and phone number for a personalised experience.",
            "Need more details on borrowing? Let us know your goals, and we'll find a solution for you. Please do provide your name, email and phone number for a personalised experience."
        ],
        "investment": [
            "Excited to discuss investment opportunities! What kind of investment are you considering? Please do provide your name, email and phone number for a personalised experience.",
            "Investment planning is our specialty! Let us know your interests, and we'll help you get started. Please do provide your name, email and phone number for a personalised experience.",
            "Thinking about investing? We'd love to share insights and opportunities with you. Please do provide your name, email and phone number for a personalised experience."
        ],
        "partnership": [
            "We're thrilled to discuss partnership possibilities! Tell us more about your vision. Please do provide your name, email and phone number for a personalised experience.",
            "Partnerships create great potential. What kind of collaboration are you interested in? Please do provide your name, email and phone number for a personalised experience.",
            "Looking to partner with us? Let's talk about how we can work together to achieve mutual goals. Please do provide your name, email and phone number for a personalised experience."
        ]
    }

    bot_response = responses.get(leadType)
    return random.choice(bot_response)