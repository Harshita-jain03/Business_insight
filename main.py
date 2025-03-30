import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize Model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def get_business_insight(query):
    """Generate AI-powered business insights."""
    try:
        response = model.generate_content(query)  
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# CLI-based Interface
def main():
    print("\nAI Business Insights Assistant\n")
    while True:
        user_query = input("Ask a business-related question (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_business_insight(user_query)
        print("\nAI Response:", response, "\n")

if __name__ == "__main__":
    main()
