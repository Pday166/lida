import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=os.environ["PALM_API_KEY"])

# Initialize the GenerativeModel
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-001")

# Create the prompt message in the correct format
prompt = "Summarize the dataset."
messages = [{"parts": [{"text": prompt}]}]

# Generate the content
response = model.generate_content(messages)

# Print the generated text
print(response.text)