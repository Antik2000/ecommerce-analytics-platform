from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_response(question: str, dataframe) -> str:
    """
    Convert query results into a business-friendly response.
    """

    prompt = f"""
    You are a business analytics assistant.

    User Question:
    {question}

    Query Result:
    {dataframe.to_string(index=False)}

    Provide a concise business-friendly answer.
    Do not mention SQL.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text.strip()