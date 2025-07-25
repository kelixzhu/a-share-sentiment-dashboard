import pandas as pd
import datetime as dt

# 模拟数据抓取函数（可替换为东方财富爬虫）
def fetch_latest_data():
    today = dt.date.today()
    return {
        "date": today,
        "margin_balance": 19100,
        "sz_index": 11320,
        "turnover": 11200,
        "northbound": 230,
        "up_down_ratio": 4.5,
        "etf_flow": 52
    }

# 加载已有数据
def load_existing_data(file_path):
    try:
        return pd.read_csv(file_path, parse_dates=["date"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["date", "margin_balance", "sz_index", "turnover", "northbound", "up_down_ratio", "etf_flow"])

# 写入数据
def update_data():
    file_path = "data.csv"
    df = load_existing_data(file_path)
    latest = fetch_latest_data()
    if df.empty or pd.to_datetime(latest["date"]) > df["date"].max():
        df = df._append(latest, ignore_index=True)
        df.to_csv(file_path, index=False)
        print("✅ 数据已更新并保存到 data.csv")
    else:
        print("ℹ️ 数据已是最新，无需更新")

if __name__ == "__main__":
    update_data()
