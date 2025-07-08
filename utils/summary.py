import pandas as pd
import streamlit as st

def show_summary(all_results,initial_cash):
    for result in all_results:
        result["return_pct"] = round((result["profit"] / initial_cash) * 100, 2)
    comparison_df = pd.DataFrame(all_results)
    comparison_df = comparison_df[["strategy", "final_cash", "profit", "return_pct","trades"]]
    comparison_df.columns = ["Strategy", "Final Cash (₹)", "Profit (₹)", "Return (%)", "Trades"]

    comparison_df.sort_values(by="Profit (₹)", ascending=False, inplace=True)

    st.subheader("📊 Strategy Comparison")
    st.dataframe(comparison_df, use_container_width=True)

    top_strategy = comparison_df.iloc[0]
    st.markdown(f"""
    ### Best Performing Strategy
    The **{top_strategy['Strategy']}** strategy delivered the highest profit of **₹ {top_strategy['Profit (₹)']}** over the selected period.
    """)