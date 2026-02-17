import streamlit as st

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(layout="wide", page_title="Gold to win - Chicken Edition")

# --- ส่วนที่ 1: แถบสถานะ (The Signal Bar) ---
st.title("🎯 Gold to win - Commander Dashboard")
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.error("MARKET STATUS: STRONG SELL")
with col_stat2:
    st.warning("DXY STATUS: BULLISH")
with col_stat3:
    st.info("VOLATILITY: HIGH")

st.divider()

# --- ส่วนที่ 2: กราฟและบทวิเคราะห์ (The Dashboard) ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 Clean Sniper Chart")
    st.write("(กราฟ Real-time กำลังถูกเชื่อมต่อในขั้นตอนถัดไป...)")
    # จำลองหน้าจอกราฟที่คลีนที่สุด
    st.image("https://via.placeholder.com/800x400.png?text=Your+Clean+Chart+Will+Appear+Here")

with col_right:
    st.subheader("🛡️ Decision Matrix")
    st.table({
        "ตัวบ่งชี้": ["Trend (1H)", "Momentum", "Volume"],
        "สถานะ": ["⬇️ Down", "🔴 Bearish", "✅ Confirmed"]
    })
    
    st.subheader("📍 Key Levels")
    st.metric("Resistance (SL)", "4,945.00")
    st.metric("Support (TP)", "4,911.00")

# --- ส่วนที่ 3: คำแนะนำจาก AI ---
st.success("AI COMMAND: รักษาวินัย หากราคาไม่ทะลุ SL ให้ถือลุ้นไปที่เป้าหมายกำไร!")
