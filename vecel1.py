import requests

# Define the URL of the ChatGPT API
API_URL = "https://api.openai.com/v1/engines/davinci/completions"

# Define the headers for the API request
headers = {
    "Authorization": "Bearer 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"
}

# Define a function to prompt the chatbot
def prompt_chatbot(business_data):
    """Prompts the ChatGPT API with the given business data and returns the chatbot's response."""

    # Create the request body
    request_body = {
        "prompt": "Create a chatbot for my business based on the following data:\n\n" + business_data,
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    # Make the API request
    response = requests.post(API_URL, headers=headers, json=request_body)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        raise Exception("Failed to prompt ChatGPT: {}".format(response.status_code))


# Prompt the user for their business data
business_data = input("Enter your business data:\n")

# Prompt the chatbot
chatbot_response = prompt_chatbot(business_data)

# Print the chatbot's response
print("Chatbot response:\n\n" + chatbot_response)
