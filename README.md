Markdown

# Twitter Bot with OpenAI

This project demonstrates a simple Twitter bot that uses OpenAI's GPT model to generate and post tweets automatically.

## Features

* **Automated Tweeting:**  The bot uses a scheduler to tweet at regular intervals.
* **Diverse Content:** The bot selects from a variety of prompts to generate different types of tweets, including motivational quotes, fun facts, questions, and humorous observations.
* **OpenAI Integration:** Leverages the OpenAI API to generate creative and engaging tweet content.
* **Tweepy Library:** Uses the Tweepy library to interact with the Twitter API.
* **.env for API Keys:**  Securely stores API keys in a `.env` file.

## Getting Started

### Prerequisites

* **Python 3.7 or higher**
* **OpenAI Account:**  [Sign up for OpenAI](https://platform.openai.com/signup) and obtain an API key.
* **Twitter Developer Account:**  Apply for a Twitter developer account and create an app to get your API credentials.
* **Required Python packages:**
    ```bash
    pip install tweepy python-dotenv openai
    ```

### Setup

1. **Clone the repository:**
   ```bash
   git clone [invalid URL removed]
Create a .env file:
In the project's root directory, create a .env file and add your API keys:

OPENAI_API_KEY=your_openai_api_key
API_KEY=your_twitter_api_key
API_SECRET=your_twitter_api_secret
BEARER_TOKEN=your_twitter_bearer_token
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret 
Run the script:

Bash

python main.py 
Customization
Tweet Frequency: Modify the schedule.every(10).minutes.do(scheduled_tweet) line in main.py to adjust the tweeting interval.
Prompts: Add or modify the prompts in the prompts list to customize the types of tweets generated.
OpenAI Model: Experiment with different OpenAI models (e.g., gpt-3.5-turbo) by changing the model parameter in the generate_response function.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License

github.com
