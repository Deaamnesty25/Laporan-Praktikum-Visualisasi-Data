import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok: 22")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)

