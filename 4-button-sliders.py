import streamlit as st
import time

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')


st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
"Select your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")


st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')


st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))


st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])


st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label="Download Image",
data=open("C:/Users/Solit/Documents/SEMESTER7/visdat/praktikum01/assets/harimau.jpg", "rb"),
file_name="harimau.jpg",
mime="image/jpg"
)



st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')



st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')