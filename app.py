import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(layout="wide", page_title="Gold to win - Stable V5")

# --- ส่วนดึงข้อมูล (ปรับปรุงให้เสถียรขึ้น) ---
@st.cache_data(ttl=60)
def get_gold_data():
    # ดึงข้อมูลย้อนหลัง 2 วัน เพื่อป้องกันข้อมูลว่างเปล่า
    data = yf.download("GC=F", period="2d", interval="5m")
    return data

try:
    df = get_gold_data()
    
    if not df.empty:
        # ใช้ข้อมูลล่าสุดที่หาเจอ
        current_price = df['Close'].iloc[-1]
        
        # --- แถบสถานะด้านบน ---
        st.title("🎯 Gold to win - Realtime Dashboard")
        c1, c2, c3 = st.columns(3)
        c1.metric("GOLD PRICE (USD)", f"{current_price:,.2f}")
        c2.error("STRATEGY: V5 SNIPER")
        c3.warning("SIGNAL: WAITING")

        # --- ส่วนกราฟ ---
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                        open=df['Open'], high=df['High'],
                        low=df['Low'], close=df['Close'])])

        fig.update_layout(title="XAU/USD - 5m Real-time Chart", template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
        st.success(f"อัปเดตล่าสุด: {datetime.now().strftime('%H:%M:%S')}")
    else:
        st.error("ระบบกำลังรอข้อมูลจากตลาดทองคำ กรุณารอสักครู่...")

except Exception as e:
    st.info("กำลังสตาร์ทเครื่องยนต์... หากรอนานเกิน 1 นาที ให้กดปุ่ม Refresh ที่หน้าเว็บ")
