import streamlit as st
import base64
import os

# --- Fungsi untuk menambahkan gambar sebagai background ---
def add_local_background_image(image_path):
    if not os.path.exists(image_path):
        st.error(f"❌ File tidak ditemukan: {image_path}")
        return

    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Panggil fungsi untuk menambahkan background (sama dengan animal1.jpg) ---
add_local_background_image("images/bg1.jpg")

# --- Menampilkan satu gambar ---
st.write("Ini Display Kucing Lucu")
st.image("images/animal1.jpg")
st.write("Image Courtesy: Unsplash")

# --- Menampilkan beberapa gambar sekaligus ---
st.write("Displaying Multiple Images")
animal_images = [
    "images/animal1.jpg",
    "images/animal2.jpg",
    "images/animal3.jpg",
    "images/animal4.jpg",
]
st.image(animal_images, width=150)
st.write("Image Courtesy: Unsplash")

import streamlit as st
from PIL import Image

# Membuka gambar dari lokal
original_image = Image.open("images/animal1.jpg")

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))

# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)