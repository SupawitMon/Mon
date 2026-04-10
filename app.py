import streamlit as st
import random
import time

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="วันนี้กินอะไรดี 🍜",
    page_icon="🍜",
    layout="centered"
)

# ---------------- HIDE STREAMLIT ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
padding-top:1rem;
max-width:700px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* ===== Background ===== */
.stApp{
background: linear-gradient(-45deg,#ffd6e7,#ffe8cc,#dff6ff,#ffe3f1);
background-size:400% 400%;
animation:bg 12s ease infinite;
font-family:sans-serif;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* ===== Card ===== */
.card{
background:white;
padding:45px;
border-radius:30px;
box-shadow:0 20px 45px rgba(0,0,0,.15);
text-align:center;
animation:fade .6s ease;
}

@keyframes fade{
from{opacity:0;transform:translateY(20px);}
to{opacity:1;}
}

/* ===== Title ===== */
.title{
font-size:42px;
font-weight:bold;
color:#ff4d88;
margin-bottom:10px;
}

/* ===== Result ===== */
.food{
font-size:40px;
font-weight:bold;
color:#222;
margin-top:25px;
animation:pop .4s ease;
text-shadow:0 0 15px rgba(255,105,180,.3);
}

@keyframes pop{
0%{transform:scale(.7);opacity:0;}
100%{transform:scale(1);}
}

/* ===== BUTTON ===== */
.stButton>button{
background:linear-gradient(90deg,#ff8ecf,#ffb3e6);
color:white;
border:none;
border-radius:35px;
height:60px;
font-size:20px;
font-weight:bold;
transition:.3s;
}

.stButton>button:hover{
transform:scale(1.07);
box-shadow:0 0 25px pink;
}

/* ===== FIX SELECTBOX ===== */
div[data-baseweb="select"] > div{
background:white !important;
color:#333 !important;
border-radius:15px !important;
border:2px solid #ffd1e6 !important;
}

div[data-baseweb="select"] *{
color:#333 !important;
}

ul[role="listbox"]{
background:white !important;
color:#333 !important;
border-radius:15px !important;
}

li[role="option"]:hover{
background:#ffe4f1 !important;
color:#ff4f8b !important;
}

li[aria-selected="true"]{
background:#ffd6ec !important;
color:#ff4f8b !important;
}

/* footer */
.footer{
margin-top:30px;
font-size:14px;
color:#666;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MENU DATA ----------------

thai_food = [
"กะเพราไก่","กะเพราหมูกรอบ","ข้าวผัด","ข้าวหมูแดง","ข้าวมันไก่",
"ข้าวขาหมู","ผัดซีอิ๊ว","ราดหน้า","ผัดไทย",
"ก๋วยเตี๋ยวเรือ","ต้มยำกุ้ง","ลาบหมู","ส้มตำ","หมูปิ้ง"
]

fast_food = [
"เบอร์เกอร์","พิซซ่า","ไก่ทอด","นักเก็ต",
"สปาเกตตี","แซนด์วิช","ชีสเบอร์เกอร์"
]

japanese_food = [
"ซูชิ","ซาชิมิ","ราเมง","อุด้ง",
"ข้าวหน้าเนื้อ","ทงคัตสึ","เทมปุระ"
]

korean_food = [
"บิบิมบับ","คิมบับ","ต๊อกบกกี",
"ไก่ทอดเกาหลี","รามยอน","หมูย่างเกาหลี"
]

dessert = [
"บิงซู","ไอศกรีม","ชีสเค้ก",
"บราวนี่","ฮันนี่โทสต์","โดนัท","ชานมไข่มุก"
]

all_food = thai_food + fast_food + japanese_food + korean_food + dessert

# ---------------- UI ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🍜 วันนี้กินอะไรดี</div>", unsafe_allow_html=True)

category = st.selectbox(
"เลือกหมวดอาหาร",
["สุ่มทั้งหมด","อาหารไทย","ฟาสต์ฟู้ด","ญี่ปุ่น","เกาหลี","ของหวาน"]
)

result_placeholder = st.empty()

# ---------------- RANDOM BUTTON ----------------
if st.button("✨ สุ่มเมนู ✨"):

    if category == "อาหารไทย":
        menu = thai_food
    elif category == "ฟาสต์ฟู้ด":
        menu = fast_food
    elif category == "ญี่ปุ่น":
        menu = japanese_food
    elif category == "เกาหลี":
        menu = korean_food
    elif category == "ของหวาน":
        menu = dessert
    else:
        menu = all_food

    # animation random
    for i in range(18):
        result_placeholder.markdown(
            f"<div class='food'>{random.choice(menu)}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.05 + i*0.01)

    st.session_state.food = random.choice(menu)
    st.balloons()

# ---------------- RESULT ----------------
if "food" in st.session_state:

    result_placeholder.markdown(
        f"<div class='food'>👉 {st.session_state.food}</div>",
        unsafe_allow_html=True
    )

    col1,col2 = st.columns(2)

    with col1:
        if st.button("❌ ไม่เอา"):
            st.session_state.food = random.choice(all_food)

    with col2:
        st.button("❤️ น่ากิน")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
"<center class='footer'>คิดไม่ออกบอกฉัน 🍴</center>",
unsafe_allow_html=True
)