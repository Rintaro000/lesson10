import streamlit as st
import math

st.title("自動通分アプリ")

num1 = st.number_input("一つ目の分数の分子を入力", value=0)
num2 = st.number_input("一つ目の分数の分母を入力", value=1)
num3 = st.number_input("二つ目の分数の分子を入力", value=0)
num4 = st.number_input("二つ目の分数の分母を入力", value=1)

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

if num2 == num4:
    st.write("分母が等しいため通分の必要はありません")
else:
    common_denominator = lcm(int(num2), int(num4))

    new_num1 = int(num1) * (common_denominator // int(num2))
    new_num3 = int(num3) * (common_denominator // int(num4))
    
    st.write(f"{num1}/{num2} , {num3}/{num4} = {new_num1}/{common_denominator} , {new_num3}/{common_denominator}")