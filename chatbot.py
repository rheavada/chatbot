from difflib import get_close_matches
from typing import Optional, Dict, List

def get_best_match(user_question: str, questions: Dict[str, str]) -> Optional[str]:
    """Compares the user message similarity to the ones in the dictionary."""
    
    question_list: List[str] = list(questions.keys())
    matches: List[str] = get_close_matches(user_question.lower(), question_list, n=1, cutoff=0.6)

    # Return the first best match, else return None
    return matches[0] if matches else None

def chatbot(knowledge: Dict[str, str]):
    """Chatbot loop that interacts with the user."""
    
    print("Chatbot is ready! Type 'exit' to end the conversation.")
    
    while True:
        user_input: str = input('You: ').strip()

        # Check for exit command
        if user_input.lower() in ('exit', 'quit'):
            print('Bot: Goodbye!')
            break

        # Find the best match, otherwise return None
        best_match: Optional[str] = get_best_match(user_input, knowledge)

        # Get the response from the knowledge base or provide a default message
        if best_match and (answer := knowledge.get(best_match)):
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand... Could you try rephrasing that?')

if __name__ == "__main__":
    brain: Dict[str, str] = {
        "hello": "Hey there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "how are you?": "I'm a chatbot, but I'm here to help you!",
        "what is Spirit Airlines?": "Spirit Airlines is an American ultra-low-cost carrier headquartered in Miramar, Florida.",
        "how can I book a flight?": "You can book a flight by visiting our website or using our mobile app.",
        "what is your baggage policy?": "Spirit Airlines has a carry-on baggage policy that allows one personal item for free. Additional fees apply for carry-on and checked bags
