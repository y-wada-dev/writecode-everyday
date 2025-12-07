import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("japan_temp_by_year_scaled.csv")

def main():
    st.title("日本の年別・都道府県別 気温ダッシュボード")

    df = load_data()

    st.write("このダッシュボードでは、日本の各都道府県の年別気温データを表示します。")
    st.dataframe(df.head())

    df_year = df.groupby("year")["temp_c"].mean().reset_index()

    st.subheader("年別平均気温の推移")
    st.line_chart(df_year.set_index("year"))

if __name__ == "__main__":
    main()