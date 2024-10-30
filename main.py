import openai
import os
import tweepy
import schedule
import time
import random

from dotenv import load_dotenv

# Load environment variables from keys.env file
load_dotenv("keys.env")

# Twitter API credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Twitter API client for v2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# List of hardcoded prompts
prompts = [
    "Write a motivational tweet about starting fresh.",
    "Tweet a fun fact related to nature.",
    "Create a tweet that asks an engaging question about daily life.",
    "Post a tech-related tweet.",
    "Write something humorous about daily routines.",
    "Share a quote about personal growth.",
    "Tweet about the importance of self-care and how it can impact our lives.",
    "Write a tweet sharing a unique fact about space that will surprise readers.",
    "Create a tweet that challenges followers to share their favorite book recommendations.",
    "Compose a tweet expressing excitement for an upcoming movie release and why it’s anticipated.",
    "Tweet a fun, light-hearted joke that can bring a smile to your followers' faces.",
    "Write a tweet that encourages followers to reflect on their goals for the month.",
    "Create a tweet about a memorable childhood experience that shaped who you are today.",
    "Compose a tweet highlighting an inspiring woman in history and her contributions.",
    "Tweet a thought-provoking question about the future of technology and its impact on society.",
    "Write a tweet about the joys of cooking and share a simple recipe that followers can try.",
    "Create a tweet that invites followers to share their favorite travel destinations and why they love them.",
    "Tweet about a recent hobby or activity you started and encourage others to try something new.",
    "Compose a tweet sharing tips for maintaining a positive mindset during challenging times.",
    "Write a tweet about the beauty of art and how it influences our lives.",
    "Tweet a fun historical fact that many people might not know about.",
    "Tweet any unpopular opinion.",
]

# Randomly select a prompt for each tweet
def generate_random_prompt():
    return random.choice(prompts)

# Function to generate a response from ChatGPT using the new API
def generate_response(prompt, attempts=3):
    for attempt in range(attempts):
        try:
            full_prompt = (
                f"{prompt}\n\n"
                "Create a tweet that is engaging, concise, and no longer than 50 characters. "
                "Focus on the main idea without adding extra details."
            )
            
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=150
            )
            tweet_content = response.choices[0].message['content'].strip()
            return tweet_content

        except Exception as e:
            print(f"Error generating response: {e}")
            return None
    
    # Return None if maximum attempts are reached without a valid response
    return None

# Function to schedule tweets
def scheduled_tweet():
    print("Scheduling a new tweet...")  # Debug statement
    prompt = generate_random_prompt()
    chatgpt_response = generate_response(prompt)
    
    if chatgpt_response:
        try:
            # Try to send the tweet
            tweet_text(chatgpt_response)
        except Exception as e:
            print(f"Failed to send tweet: {e}")
    else:
        print("No response generated.")

# Function to tweet the response
def tweet_text(text):
    try:
        response = client.create_tweet(text=text)
        # Print a confirmation message without showing the tweet text
        print("Tweet sent successfully.")
    except tweepy.TweepyException as e:
        print(f"An error occurred while tweeting: {e}")

# Send an initial tweet before starting the scheduler
scheduled_tweet()

# Scheduling tweets every 2 minutes
schedule.every(1).minutes.do(scheduled_tweet)

print("Tweet scheduler is running...")

# Infinite loop to keep the script running and checking for scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute between each check
