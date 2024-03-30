import streamlit as st

st.header('aplikasi penjumlahan bilangan numerik', divider='rainbow')

angka_pertama = st.number_input('masukan angka pertama')
st.write('the first number is', angka_pertama)

angka_kedua = st.number_input('masukan angka kedua')
st.write('the second number is', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua 
st.write("angka pertama {angka_pertama} * angka kedua {angka_kedua} = {operasi_matematika}")