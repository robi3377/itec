import openai
from dotenv import load_dotenv
from os import getenv
load_dotenv()

# Set up the OpenAI API client
openai.api_key = getenv('GPT_KEY')

# Define a function to generate poetry
def generate_poem(prompt):
    # Define the parameters for the GPT-3 API request
    model_engine = "text-davinci-002"
    temperature = 1
    max_tokens = 100

    # Make the GPT-3 API request to generate the poem
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n = 2,
        stop=None,
        frequency_penalty=1,
        presence_penalty=0
    )

    # Extract the generated poem from the API response
    poem = response.choices[0].text.strip()
    # poem = poem.split('\n')[0]

    # Return the generated poem
    return poem
