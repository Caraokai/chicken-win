import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import pandas_ta as ta
from datetime import datetime

st.set_page_config(layout="wide", page_title="Chicken Win - Sniper V5")

# --- โหลดข้อมูล (ดึงเผื่อไว้เยอะๆ เพื่อความเสถียร) ---
@st.cache_data(ttl=30)
def load_data():
    df = yf.download("GC=F", period="5d", interval="1h")
    # ใส่สูตร V5 Sniper
    df['EMA12'] = ta.ema(df['Close'], length=12)
    df['EMA34'] = ta.ema(df['Close'], length=34)
    df['EMA100'] = ta.ema(df['Close'], length=100)
    return df

st.title("🎯 Gold to win - Commander Dashboard")

try:
    df = load_data()
    if not df.empty:
        # ดึงราคาล่าสุด
        curr_price = df['Close'].iloc[-1]
        ema12 = df['EMA12'].iloc[-1]
        ema34 = df['EMA34'].iloc[-1]
        ema100 = df['EMA100'].iloc[-1]
        
        # --- แถบสถานะ ---
        c1, c2, c3 = st.columns(3)
        c1.metric("GOLD PRICE", f"{curr_price:,.2f}")
        
        # ลอจิกตัดสินใจสไตล์ V5
        if ema12 > ema34 and curr_price > ema100:
            c2.success("SIGNAL: BUY")
        elif ema12 < ema34 and curr_price < ema100:
            c2.error("SIGNAL: SELL")
        else:
            c2.warning("SIGNAL: WAIT")
        c3.info(f"Last Update: {datetime.now().strftime('%H:%M:%S')}")

        # --- กราฟ Sniper ---
        fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Price')])
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA12'], line=dict(color='yellow', width=1.5), name='EMA 12'))
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA34'], line=dict(color='purple', width=1.5), name='EMA 34'))
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA100'], line=dict(color='white', width=2), name='EMA 100'))
        
        fig.update_layout(template="plotly_dark", height=600, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("กำลังเชื่อมต่อสัญญาณจากดาวเทียม... กรุณารอ 10 วินาที")
except:
    st.info("กำลังรีสตาร์ทเครื่องยนต์... หากนานเกิน 1 นาที ให้กด Refresh ที่เบราว์เซอร์")
