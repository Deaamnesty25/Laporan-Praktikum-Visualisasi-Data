# import library
import streamlit as st
import pandas as pd # data dalam bentuk tabel
import numpy as np # data numerik acak
import altair as alt # data chart interaktif 

# Judul
st.title("Paraktikum VisDat Pekan 6")
# Judul utama
st.caption("Bagian 2: Data Elements")

# st.markdown
st.subheader("Kelompok 22:")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

# DataFrame
st.subheader("DataFrame")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)
st.dataframe(df)
st.subheader("Highlight Minimum Value di DataFrame")
st.dataframe(df.style.highlight_min(axis=0))

# Table statis
st.subheader("Tabel Statis")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)
st.table(df)

# Metrics
st.subheader("Metrics")
st.metric(label="Temperature", value= "31 C", delta="1.2 C")
# Definisikan
col1, col2, col3 = st.columns(3)
# Indikator
col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off")

# Menampilkan
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Math calculations with no functions defined ---
st.write("Adding 5 & 4 =", 5 + 4)

# --- Displaying variable 'a' and its value ---
a = 5
st.write("'a' =", a)

# --- Markdown with Magic ---
st.markdown("""
### Magic Feature  
Markdown works even without explicitly defining its function.
""")

# --- DataFrame using magic ---
df = pd.DataFrame({'col': [1, 2]})
st.write("DataFrame:", df)

# --- Magic working on Charts ---
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

# --- Display chart in Streamlit ---
st.pyplot(chart)




