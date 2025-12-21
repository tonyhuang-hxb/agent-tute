import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash"
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print("Prompt:", prompt)
    
    response = client.models.generate_content(
        model=model, contents=prompt
    )
    print("Response:\n" + response.text)



if __name__ == "__main__":
    main()
