import streamlit as st

st.title("Columns Chart")
st.write("Kelompok: 22")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col2.write("Ini adalah kolom kedua")

col1.image("../images/animal1.jpg")
col2.image("../images/animal1.jpg")

