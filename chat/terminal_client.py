"""
Terminal Chat Client using ChatterBot
A simple command-line interface for chatting with a ChatterBot instance.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot():
    """
    Create and configure the ChatBot instance.
    """
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


def train_chatbot(chatbot):
    """
    Train the chatbot using the ChatterBot corpus.
    """
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    # Train on English corpus
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
        "chatterbot.corpus.english.humor",
    )
    print("Training completed!")


def main():
    """
    Main function to run the terminal chat client.
    """
    print("=" * 50)
    print("Welcome to the ChatterBot Terminal Client!")
    print("=" * 50)
    print("\nInitializing chatbot...")
    
    # Create the chatbot
    chatbot = create_chatbot()
    
    # Ask if user wants to train
    train_choice = input("\nDo you want to train the chatbot? (yes/no): ").strip().lower()
    if train_choice in ['yes', 'y']:
        print("\nTraining the chatbot. This may take a moment...")
        train_chatbot(chatbot)
    
    print("\n" + "=" * 50)
    print("Chatbot is ready! Type 'quit' or 'exit' to end the conversation.")
    print("=" * 50 + "\n")
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("user: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("bot: Goodbye! Have a great day!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Get bot response
            response = chatbot.get_response(user_input)
            print(f"bot: {response}")
            
        except KeyboardInterrupt:
            print("\n\nbot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
