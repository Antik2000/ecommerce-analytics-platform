from openai import OpenAI

from config import OPENAI_API_KEY
from schema import SCHEMA_CONTEXT

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_sql(user_question: str) -> str:
    """
    Convert natural language question to BigQuery SQL.
    """

    prompt = f"""
    {SCHEMA_CONTEXT}

    User Question:
    {user_question}

    Generate valid BigQuery SQL.
    Return ONLY SQL.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text.strip()