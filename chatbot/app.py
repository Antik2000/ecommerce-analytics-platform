import streamlit as st

from sql_generator import generate_sql
from bigquery_service import execute_query
from response_generator import generate_response


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Ecommerce Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("📊 Ecommerce Analytics Assistant")

st.markdown(
    """
Ask business questions about sales performance, stores, customers, and product categories.
"""
)

# =====================================================
# ARCHITECTURE SECTION
# =====================================================

with st.expander(
    "🏗️ View Data Platform Architecture",
    expanded=False
):

    st.subheader(
        "End-to-End Analytics Platform"
    )

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.info("📄 Source")

    with col2:
        st.success("🥉 Raw")

    with col3:
        st.success("🥈 Staging")

    with col4:
        st.success("🥇 Mart")

    with col5:
        st.warning("✅ DQ")

    with col6:
        st.warning("🔍 Validation")

    with col7:
        st.error("🤖 AI")

    st.markdown(
        """
**Pipeline Flow**

Source → Raw → Staging → Mart → Data Quality → Validation → AI Analytics Assistant
"""
    )

    st.divider()

    st.subheader(
        "Pipeline Statistics"
    )

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            label="Raw Records Loaded",
            value=f"{10050:,}"
        )

    with metric2:
        st.metric(
            label="Staging Records",
            value=f"{9851:,}"
        )

    with metric3:
        st.metric(
            label="Mart Aggregates",
            value=f"{965:,}"
        )

    st.divider()

    st.subheader(
        "Technology Stack"
    )

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.info("🐍 Python")

    with tech2:
        st.info("☁️ BigQuery")

    with tech3:
        st.info("🤖 OpenAI GPT-5")

    with tech4:
        st.info("📊 Streamlit")


# =====================================================
# EXAMPLE QUESTIONS
# =====================================================

st.markdown(
    """
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

# =====================================================
# GENERATE INSIGHTS
# =====================================================

if st.button("Generate Insights"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

        st.stop()

    try:

        # =============================================
        # PIPELINE EXECUTION MONITOR
        # =============================================

        with st.status(
            "🚀 Executing Analytics Pipeline",
            expanded=True
        ) as status:

            st.write(
                "✅ Step 1: Business Question Received"
            )

            st.info(question)

            st.write(
                "🟡 Step 2: Generating SQL using GPT-5"
            )

            sql = generate_sql(question)

            st.write(
                "✅ SQL Generated Successfully"
            )

            st.write(
                "🟡 Step 3: Executing Query on BigQuery"
            )

            df = execute_query(sql)

            st.write(
                f"✅ Query Executed Successfully ({len(df)} rows returned)"
            )

            st.write(
                "🟡 Step 4: Generating Business Insight"
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

        # =============================================
        # EMPTY RESULT HANDLING
        # =============================================

        if df.empty:

            st.warning(
                "No data found for the requested question."
            )

        else:

            st.success(
                "Analysis completed successfully."
            )

            # =========================================
            # EXECUTION SUMMARY
            # =========================================

            summary_col1, summary_col2 = st.columns(2)

            with summary_col1:

                st.metric(
                    label="Records Returned",
                    value=len(df)
                )

            with summary_col2:

                st.metric(
                    label="Generated SQL Statements",
                    value="1"
                )

            st.divider()

            # =========================================
            # BUSINESS INSIGHT
            # =========================================

            st.subheader(
                "💡 Business Insight"
            )

            st.write(
                answer
            )

            # =========================================
            # GENERATED SQL
            # =========================================

            with st.expander(
                "📝 Generated SQL",
                expanded=False
            ):

                st.code(
                    sql,
                    language="sql"
                )

            # =========================================
            # QUERY RESULTS
            # =========================================

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