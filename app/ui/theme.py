import streamlit as st

def load_theme():

    st.markdown("""
    <style>

    /* ---------- Background Gradient Animation ---------- */

    .stApp {
        background: linear-gradient(-45deg,#1a2a6c,#16222a,#3a6073,#2c3e50);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position:0% 50%;}
        50% {background-position:100% 50%;}
        100% {background-position:0% 50%;}
    }

    /* ---------- Titles ---------- */

    .title {
        font-size:50px;
        font-weight:800;
        text-align:center;
        color:white;
        margin-bottom:10px;
    }

    .subtitle {
        font-size:20px;
        text-align:center;
        color:#dcdcdc;
        margin-bottom:40px;
    }

    /* ---------- Sections ---------- */

    .section {
        font-size:28px;
        font-weight:700;
        margin-top:40px;
        margin-bottom:15px;
    }

    /* ---------- Cards ---------- */

    .card {
        background:rgba(255,255,255,0.08);
        padding:25px;
        border-radius:15px;
        backdrop-filter: blur(12px);
        box-shadow:0 8px 30px rgba(0,0,0,0.3);
        margin-bottom:20px;
    }

    /* ---------- Feature Boxes ---------- */

    .feature {
        background:rgba(255,255,255,0.1);
        padding:20px;
        border-radius:12px;
        text-align:center;
        font-size:18px;
        font-weight:600;
        transition:0.3s;
    }

    .feature:hover {
        transform:translateY(-5px);
        background:rgba(255,255,255,0.2);
    }

    /* ---------- Fix disappearing text ---------- */

    h1,h2,h3,h4,h5,p,span,label {
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)