import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(layout="wide", page_title="Chicken Win - Final Light")

st.title("🎯 Gold to win - Sniper Dashboard")

# ลองดึงข้อมูลแบบเจาะจงแท่งวัน เพื่อลดภาระเซิร์ฟเวอร์
try:
    data = yf.download("GC=F", period="5d", interval="1h")
    
    if not data.empty:
        curr = data['Close'].iloc[-1]
        st.metric("GOLD PRICE (REALTIME)", f"{curr:,.2f}")
        
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                        open=data['Open'], high=data['High'],
                        low=data['Low'], close=data['Close'])])
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("ตลาดอาจจะปิดหรือเซิร์ฟเวอร์หน่วง กรุณารอ 1 นาทีแล้วรีเฟรช")
except:
    st.error("เครื่องยนต์ขัดข้องชั่วคราว กำลังพยายามเชื่อมต่อใหม่...")
