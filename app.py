import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(layout="wide", page_title="Gold to win - Realtime")

# --- ส่วนดึงข้อมูล Real-time ---
@st.cache_data(ttl=60)
def get_gold_data():
    data = yf.download("GC=F", period="1d", interval="5m")
    return data

df = get_gold_data()
current_price = df['Close'].iloc[-1]

# --- แถบสถานะด้านบน ---
st.title("🎯 Gold to win - Realtime Dashboard")
c1, c2, c3 = st.columns(3)
c1.metric("GOLD PRICE (USD)", f"{current_price:,.2f}")
c2.error("STRATEGY: V5 SNIPER")
c3.warning("SIGNAL: WAITING")

# --- ส่วนกราฟ Plotly (ขยับได้ ซูมได้) ---
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])])

fig.update_layout(title="XAU/USD - 5m Chart", template="plotly_dark", height=500)
st.plotly_chart(fig, use_container_width=True)

st.success(f"อัปเดตล่าสุดเมื่อ: {datetime.now().strftime('%H:%M:%S')}")
