
from langchain_community.utilities import SQLDatabase
from utils.parser import parse_args, load_config


args = parse_args()

def ask(question, sql_chain, full_chain):

    sql_query = sql_chain.invoke({"question": question})
    answer = full_chain.invoke({"question": question})

    return {
        "natural_language_answer": answer,
        "sql_query": sql_query
    }

def get_database():

    uri = (
        f"mysql+mysqlconnector://{args.database_user}:"
        f"{args.database_password}@"
        f"{load_config()['database']['host']}/"
        f"{args.database_name}"
    )   
 

    return SQLDatabase.from_uri(uri)



def get_schema(_):
    db = get_database()
    return db.get_table_info()