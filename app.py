import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(layout="wide")
st.title("📈 A股市场情绪仪表盘")

# 加载数据
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv", parse_dates=["date"])
    return df.sort_values("date")

df = load_data()

# 日期筛选器
start_date = st.sidebar.date_input("开始日期", df["date"].min().date())
end_date = st.sidebar.date_input("结束日期", df["date"].max().date())

filtered_df = df[(df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))]

# 画图
fig = go.Figure()
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["margin_balance"], mode="lines", name="两融余额"))
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["sz_index"], mode="lines", name="深成指"))
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["turnover"], mode="lines", name="成交额"))
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["northbound"], mode="lines", name="北向资金"))
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["up_down_ratio"], mode="lines", name="涨跌停比"))
fig.add_trace(go.Scatter(x=filtered_df["date"], y=filtered_df["etf_flow"], mode="lines", name="ETF净申购"))

fig.update_layout(title="情绪指标走势", height=600, hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)
st.dataframe(filtered_df)
