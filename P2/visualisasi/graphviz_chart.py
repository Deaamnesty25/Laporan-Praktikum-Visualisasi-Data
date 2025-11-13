import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 22")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

st.graphviz_chart("""
    digraph{
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")

