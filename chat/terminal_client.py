"""
Terminal Chat Client using ChatterBot
A simple command-line interface for chatting with a ChatterBot instance.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot() -> ChatBot:
    """
    Create and configure the ChatBot instance.
    
    Returns:
        ChatBot: A configured ChatterBot instance with SQL storage and BestMatch logic.
    """
    # Initialize chatbot with SQLite storage for persistence
    chatbot = ChatBot(
        'ChatBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )
    return chatbot


def train_chatbot(chatbot: ChatBot) -> None:
    """
    Train the chatbot using the ChatterBot corpus.
    
    Args:
        chatbot: The ChatBot instance to train.
    """
    # Initialize the corpus trainer
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    # Train on English corpus datasets for greetings, conversations, and humor
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
        "chatterbot.corpus.english.humor",
    )
    print("Training completed!")


def main() -> None:
    """
    Main function to run the terminal chat client.
    Handles user input/output loop and graceful exit.
    """
    # Display welcome banner
    print("=" * 50)
    print("Welcome to the ChatterBot Terminal Client!")
    print("=" * 50)
    print("\nInitializing chatbot...")
    
    # Create the chatbot instance
    chatbot = create_chatbot()
    
    # Prompt user for training option
    train_choice = input("\nDo you want to train the chatbot? (yes/no): ").strip().lower()
    if train_choice in ['yes', 'y']:
        print("\nTraining the chatbot. This may take a moment...")
        train_chatbot(chatbot)
    
    # Display ready message with instructions
    print("\n" + "=" * 50)
    print("Chatbot is ready! Type 'quit' or 'exit' to end the conversation.")
    print("=" * 50 + "\n")
    
    # Main conversation loop
    while True:
        try:
            # Get user input and remove leading/trailing whitespace
            user_input = input("user: ").strip()
            
            # Check for exit commands to end the conversation
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("bot: Goodbye! Have a great day!")
                break
            
            # Skip empty inputs and continue the loop
            if not user_input:
                continue
            
            # Get response from chatbot and display it
            response = chatbot.get_response(user_input)
            print(f"bot: {response}")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nbot: Goodbye! Have a great day!")
            break
        except Exception as e:
            # Display any unexpected errors
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
