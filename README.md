# MSCS633 Assignment 3 - ChatterBot Terminal Client

A terminal-based chatbot client built with Django/Python and ChatterBot.

## Dependencies

- Python 3.9+
- Django 4.2
- ChatterBot 1.2
- spaCy (with en_core_web_sm model)

## Setup

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Running the Program

Activate the virtual environment and run the terminal client:

```bash
source venv/bin/activate
python3 chat/terminal_client.py
```

On first run, choose 'yes' to train the chatbot with conversation data.

## Example Usage

```
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

Type `quit` or `exit` to end the conversation.