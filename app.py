import streamlit as st
import math

st.title("自動約分アプリ")

num1 = st.number_input("分子を入力", value = 0)
num2 = st.number_input("分母を入力", value = 0)
if num1 == 0:
    st.write("分子が0なので、結果は0です。")
else:
    gcd = math.gcd(int(num1), int(num2))
    
    reduced_num1 = int(num1 / gcd)
    reduced_num2 = int(num2 / gcd)
    st.write(f"約分された分数: {reduced_num1}/{reduced_num2}")