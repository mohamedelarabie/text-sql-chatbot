import yaml
from pathlib import Path
import argparse

def load_config():
    """Load database configuration from YAML file."""
    config_path = Path("config/general_config.yaml")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config



def parse_args():

    parser = argparse.ArgumentParser(
        description="Text-to-SQL Chatbot (Gemini + MySQL)"
    )

    parser.add_argument("--question",type=str,help="Ask a question directly")
    parser.add_argument("--database_name",type=str,default=load_config()['database']['name'],help="Name of the database to connect to")
    parser.add_argument("--database_user",type=str,default=load_config()['database']['user'],help="Database username")
    parser.add_argument("--database_password",type=str,default=load_config()['database']['password'],help="Database password")
    parser.add_argument("--provider_name",type=str,default=load_config()['provider']['name'],help="LLM provider name (e.g., 'gemini')")
    parser.add_argument("--model_name",type=str,default=load_config()['provider']['model_name'],help="LLM model name (e.g., 'gemini-2b')")
    parser.add_argument("--provider_api_key",type=str,default=load_config()['provider']['api_key'],help="API key for the LLM provider")

    args = parser.parse_args()

    # validation
    if not args.question:
        parser.error("Please provide a question using --question")
    return args
