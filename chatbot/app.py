import streamlit as st

from sql_generator import generate_sql
from bigquery_service import execute_query
from response_generator import generate_response


st.set_page_config(
    page_title="Ecommerce Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ecommerce Analytics Assistant")

with st.expander(
    "🏗️ View Data Platform Architecture",
    expanded=False
):
    st.markdown(
        """
        ```text
        CSV Source
            ↓
        Raw Layer
            ↓
        Staging Layer
            ↓
        Mart Layer
            ↓
        Data Quality Framework
            ↓
        Validation Framework
            ↓
        AI Analytics Assistant
        ```
        """
    )

st.markdown(
    """
Ask business questions about sales performance, stores, customers, and product categories.

### Example Questions
- Which store generated the highest revenue?
- Which category sold the most products?
- What was the average order value?
- Which store had the most customers?
"""
)

question = st.text_input(
    "Enter your question:"
)

if st.button("Generate Insights"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:

        with st.status(
            "🚀 Executing Analytics Pipeline...",
            expanded=True
        ) as status:

            st.write(
                "✅ Step 1: Business Question Received"
            )

            st.info(question)

            st.write(
                "🟡 Step 2: Generating SQL using GPT-5..."
            )

            sql = generate_sql(question)

            st.write(
                "✅ SQL Generated Successfully"
            )

            st.write(
                "🟡 Step 3: Executing Query on BigQuery..."
            )

            df = execute_query(sql)

            st.write(
                f"✅ Query Executed Successfully ({len(df)} rows returned)"
            )

            st.write(
                "🟡 Step 4: Generating Business Insight..."
            )

            answer = generate_response(
                question,
                df
            )

            st.write(
                "✅ Business Insight Generated"
            )

            status.update(
                label="🎉 Pipeline Execution Completed",
                state="complete"
            )

        if df.empty:

            st.warning(
                "No data found for the requested question."
            )

        else:

            st.success(
                "Analysis completed successfully."
            )

            col1, col2 = st.columns(
                [2, 1]
            )

            with col1:

                st.subheader(
                    "💡 Business Insight"
                )

                st.write(
                    answer
                )

            with col2:

                st.subheader(
                    "📈 Records Returned"
                )

                st.metric(
                    label="Rows",
                    value=len(df)
                )

            with st.expander(
                "📝 Generated SQL",
                expanded=False
            ):
                st.code(
                    sql,
                    language="sql"
                )

            with st.expander(
                "📊 Query Results",
                expanded=False
            ):
                st.dataframe(
                    df,
                    use_container_width=True
                )

    except Exception as e:

        st.error(
            f"An error occurred: {str(e)}"
        )