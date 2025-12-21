import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    client = genai.Client(api_key=api_key)
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("model", type=str, help="Model to use", default="gemini-2.5-flash", nargs='?')
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    response = client.models.generate_content(
        model=args.model, contents=messages
    )
    
    metadata = response.usage_metadata
    
    if metadata is None:
        raise RuntimeError("Usage metadata is missing in the response. API request may have failed")
    
    prompt_token_count = metadata.prompt_token_count
    candidates_token_count = metadata.candidates_token_count
    
    print("="*10)
    print("Prompt:", args.user_prompt)
    print()
    print("Response:\n" + response.text)
    print("="*10)
    print("Metadata:", metadata)
    print("Prompt tokens:", prompt_token_count)
    print("Response tokens:", candidates_token_count)
    

if __name__ == "__main__":
    main()
