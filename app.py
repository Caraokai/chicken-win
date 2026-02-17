import streamlit as st
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Chicken Win - Sniper V5")

@st.cache_data(ttl=60) # พักเครื่องทุก 1 นาที ไม่ให้โดนแบน
def get_gold_data():
    try:
        # ดึงข้อมูล Gold Futures
        df = yf.download("GC=F", period="2d", interval="15m")
        if not df.empty:
            df['EMA12'] = ta.ema(df['Close'], length=12)
            df['EMA34'] = ta.ema(df['Close'], length=34)
            df['EMA100'] = ta.ema(df['Close'], length=100)
            return df
    except:
        return None

st.title("🎯 Gold to win - Sniper Dashboard")

data = get_gold_data()

if data is not None:
    curr = data['Close'].iloc[-1]
    st.metric("GOLD PRICE (REAL-TIME)", f"{curr:,.2f}")
    
    fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
    # ใส่เส้นสไนเปอร์
    fig.add_trace(go.Scatter(x=data.index, y=data['EMA12'], name="EMA12", line=dict(color='yellow')))
    fig.add_trace(go.Scatter(x=data.index, y=data['EMA34'], name="EMA34", line=dict(color='purple')))
    fig.add_trace(go.Scatter(x=data.index, y=data['EMA100'], name="EMA100", line=dict(color='white')))
    
    fig.update_layout(template="plotly_dark", height=500)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("ระบบกำลังรอสัญญาณจากดาวเทียม... กรุณารีเฟรชอีกครั้งใน 1 นาที")
