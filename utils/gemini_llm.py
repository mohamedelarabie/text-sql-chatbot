import os
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.parser import parse_args

args = parse_args()
os.environ["GOOGLE_API_KEY"] = args.provider_api_key

def get_llm():
    return ChatGoogleGenerativeAI(
        model=args.model_name,
        temperature=0
    )