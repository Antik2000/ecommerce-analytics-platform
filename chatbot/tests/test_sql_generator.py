from chatbot.sql_generator import generate_sql

question = "Which store generated the highest revenue?"

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)