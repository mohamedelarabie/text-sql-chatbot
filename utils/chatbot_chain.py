"""Refrence: https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/"""

from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from utils.gemini_llm import get_llm
from utils.help import get_database, get_schema


# SQL GENERATION PROMPT

sql_prompt = ChatPromptTemplate.from_template(
    """
    Based on the table schema below, write a MySQL query that answers the user's question.

    Schema:
    {schema}

    Question:
    {question}

    SQL Query (no markdown code blocks):
    """
)


# ANSWER PROMPT
answer_prompt = ChatPromptTemplate.from_template(
    """
    Based on the table schema below, question, sql query, and sql response:
    Schema:  {schema}
    Question: {question}
    SQL Query: {query}
    SQL Response: {response}

    Explain the result in natural language.
    """
)

# BUILD CHATBOT PIPELINE
def build_chatbot():
    db = get_database()
    llm = get_llm()
    execute_query = QuerySQLDataBaseTool(db=db)

    # SQL GENERATION CHAIN
    sql_chain = (
        RunnablePassthrough.assign(schema=get_schema)
        | sql_prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    # FULL PIPELINE: Question -> SQL Query -> Execute -> Answer
    full_chain = (
        RunnablePassthrough.assign(query=sql_chain)
        .assign(response=itemgetter("query") | execute_query)
        .assign(schema=get_schema)
        | answer_prompt
        | llm
        | StrOutputParser()
    )

    return full_chain, sql_chain