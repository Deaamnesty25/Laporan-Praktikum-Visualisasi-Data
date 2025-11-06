# import library yang dibutuhkan
import streamlit as st

# text element
# header - untuk membuat tulisan headder
st.header("ini header") # untuk membuat headder
st.subheader("ini sub header") # untuk membuat subjudul yang lebih kecil
st.text("ini teks biasa tanpa format") # untuk membuat teks polos tanpa format
st.markdown("**ini teks bold** dan *ini teks italic*") # markdown
st.caption("ini caption")

# coba mandiri
st.title("Paraktikum VisDat Pekan 6")
st.subheader("Kelompok 22:")
st.markdown("""
1. DEA AMNESTY - 0110122209
2. DADIN AHMAD JAMALUDIN - 0110222111
3. MUHAMMAD MAULANA - 0110221114
""")

# Bagian 2: Menampilkan rumus LaTex
st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # kuadrat binominal

# Bagian 3: Menmpilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

# Simpan ke variable
code = '''
daf hello():
    print("Hello, Streamlit!)
'''

# st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main (String arg[]) {
            System.out.printIN("Hello World");
        }
    }
    """, language='java')

# Fungsi st.code () bisa digunakan untuk bahasa pemrograman lain sperti java, javascript, C++, HTM,dll.

st.subheader("JavaScript Code")
st.code("""
<script>
try {
    addalert(Welcome guest!); // kesalahan ketik (addalaert)
    sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementaryById("demo").innerHTML = err.massage; // menampilkan pesan error 
    dielemen HTML dengan id 'demo'
}
</script>
""", language= 'javascript')

