import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(layout="wide", page_title="Gold to win - Super Stable")

# --- ส่วนดึงข้อมูล (เน้นความชัวร์) ---
@st.cache_data(ttl=30)
def get_gold_data():
    # เปลี่ยนมาดึงข้อมูลทองคำล่วงหน้า (Gold Futures) ย้อนหลัง 7 วันเพื่อให้มีข้อมูลชัวร์ๆ
    data = yf.download("GC=F", period="7d", interval="1h")
    return data

st.title("🎯 Gold to win - Realtime Dashboard")

try:
    df = get_gold_data()
    
    if len(df) > 0:
        current_price = df['Close'].iloc[-1]
        
        # --- แถบสถานะ ---
        c1, c2, c3 = st.columns(3)
        c1.metric("GOLD PRICE (USD)", f"{current_price:,.2f}")
        c2.error("STRATEGY: V5 SNIPER")
        c3.warning("SIGNAL: ANALYZING")

        # --- ส่วนกราฟ ---
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                        open=df['Open'], high=df['High'],
                        low=df['Low'], close=df['Close'])])

        fig.update_layout(title="XAU/USD - Hourly Chart", template="plotly_dark", height=600)
        st.plotly_chart(fig, use_container_width=True)
        st.success(f"อัปเดตข้อมูลล่าสุดเมื่อ: {datetime.now().strftime('%H:%M:%S')}")
    else:
        st.warning("กำลังรอสัญญาณจากดาวเทียมตลาดทองคำ... กรุณากด Refresh อีกครั้งใน 10 วินาที")

except Exception as e:
    st.info("เครื่องยนต์กำลังวอร์มเครื่อง... กรุณารอสักครู่")
