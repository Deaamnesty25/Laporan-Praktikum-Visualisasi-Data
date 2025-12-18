import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

#Header
st.title("Praktikum 06 VisDat")
st.write("Kel 22")
st.markdown("""
    - Dea Amnesty (0110122209)
    - Dadin Ahmad Jamaludin (0110222111)
""")

#Data Set
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [140, 190, 170]

#data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

#data quarter
q1_male = [150,180,160]
q1_female = [140,200, 180]
q2_male = [170,190,175]
q2_female = [130, 210, 160]

#1 grafik stacked vertical bar chart
st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

#2 grafik stacked vertical bar chart
st.subheader("2. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='green')

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

#3 grafik kustomisasi stacked vertical bar chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

#4 grafik multiple stacked vertical bar chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom= q1_male, label='Q1 Male', color='pink', width=width)

ax.bar(x + width/2, q2_male, label='Q2 Male', color='blue', width=width)
ax.bar(x + width/2, q2_female, bottom= q2_male, label='Q2 Female', color='red', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)