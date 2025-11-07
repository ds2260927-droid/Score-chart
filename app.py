import streamlit as st
import pandas as pd
import os

# ======== CONFIG ========
DATA_FILE = "C:/Users/ds226/OneDrive/Desktop/india_cricket_runs.csv"

# ======== LOAD DATA ========
@st.cache_data
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        st.error("Data file not found! Please add 'india_cricket_runs.csv' in the same folder.")
        return pd.DataFrame(columns=["Year", "Player", "Runs"])

df = load_data()

# ======== STREAMLIT UI ========
st.set_page_config(page_title="🏏 Indian Cricket Runs Chart", page_icon="🏏", layout="centered")
st.title("🏏 Indian Men's Cricket Team – Runs by Year")

st.markdown("Enter a **year** to view runs scored by all Indian players in that year.")

# ======== USER INPUT ========
year = st.number_input("Enter Year (e.g., 2023):", min_value=2000, max_value=2100, step=1)

if st.button("Show Runs"):
    if df.empty:
        st.warning("No data available.")
    else:
        # Filter data for entered year
        year_data = df[df["Year"] == year]

        if year_data.empty:
            st.warning(f"No records found for {year}.")
        else:
            st.success(f"Showing runs scored by Indian players in {year}")
            st.dataframe(year_data)

            # ======== CHART ========
            st.subheader("📊 Runs Chart")
            st.bar_chart(data=year_data, x="Player", y="Runs", use_container_width=True)

            # ======== STATS ========
            st.subheader("📈 Statistics")
            total_runs = year_data["Runs"].sum()
            avg_runs = year_data["Runs"].mean()
            top_scorer = year_data.loc[year_data["Runs"].idxmax()]

            st.metric("Total Runs (Team)", total_runs)
            st.metric("Average Runs per Player", round(avg_runs, 2))
            st.metric("Top Scorer", f"{top_scorer['Player']} ({top_scorer['Runs']} runs)")



