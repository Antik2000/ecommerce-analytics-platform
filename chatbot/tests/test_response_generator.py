from chatbot.sql_generator import generate_sql
from chatbot.bigquery_service import execute_query
from chatbot.response_generator import generate_response


question = "Which store generated the highest revenue?"

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

df = execute_query(sql)

print("\nQuery Results:\n")
print(df)

answer = generate_response(question, df)

print("\nBusiness Answer:\n")
print(answer)