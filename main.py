from database.create_database import create_database
from database.create_tables import create_tables
from database.seed_data import insert_data
from utils.chatbot_chain import build_chatbot
from utils.help import ask
from utils.parser import parse_args,load_config
import json
from pathlib import Path

def main():
    args = parse_args()
    config = load_config()
    if config['database']['name'] == "inventory_db":
        create_database()
        create_tables()
        insert_data()
        
    full_chain, sql_chain = build_chatbot()
    response = ask(args.question, sql_chain, full_chain)
    output_path = config['output']['path']
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'response2.json'

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({'response': response}, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()