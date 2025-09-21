import streamlit as st
import random

st.title("じゃんけんゲーム")

st.write("最初はグー。じゃんけん...")

janken_start = st.button("ポン！")

if janken_start:
    hand = random.randint(1,3)

    if hand == 1:
        st.write("グー")
    
    elif hand == 2:
        st.write("チョキ")

    else:
        st.write("パー")