import streamlit as st
import matplotlib.pyplot as plt 

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout streamlit
st.title("Visualisasi Penjualan Produk ")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
                                                        "Multiple & Customizations",
                                                        "Jenis Garis Untuk Menunjukan Tren",
                                                        "Subplot"))
                                                        
# Identitas kelompok
st.caption("Praktikum 3 Kel 22 - Matplotlib Line Chart")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color="blue", linestyle="--", marker='o')
    ax.set_title('Penjualan Product A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid('True')
    st.pyplot(fig)

# Multiple Line Plot & Cuztomizations
def customizations_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label= 'Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label= 'Product B', color='red', linestyle='-', marker='x')

    ax.set_title('Penjualan Product C per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid('True')
    st.pyplot(fig)


# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
product_C_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_D_sales = [5,10,8,15,18,20,22,30,25,35,40,45]
def tren_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_C_sales, label= 'Product C', color='green', marker='d')
    ax.plot(months, product_D_sales, label= 'Product D', color='purple', marker='s')
    ax.set_title('Penjualan Product C per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid('True')
    st.pyplot(fig)


# Subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))

    # plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Product C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid('True')

# plot pertama untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', color='purple', marker='s')
    axs[1].set_title('Penjualan Product D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid('True')

    plt.tight_layout()
    st.pyplot(fig)



# Logika untuk menampilkan visualiasasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customizations_plot()
elif option == "Jenis Garis Untuk Menunjukan Tren":
    tren_plot()
elif option == "Subplot":
    subplots()
