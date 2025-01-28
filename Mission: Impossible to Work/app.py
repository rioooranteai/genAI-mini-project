import streamlit as st

st.title("Generate Your Absurdly Excused")

# Daftar awal untuk pekerjaan dan kategori
default_jobs = ["Data Scientist", "Software Engineer", "Product Manager", "Policeman", "Teacher"]
default_cat = ["Animal", "Family", "Vehicle"]
default_media = ['Chat Apps', 'Email']

# Sidebar: Job Picker
st.sidebar.title("Job Picker")
job = st.sidebar.selectbox("Pick A Job", default_jobs)

# Input tambahan untuk pekerjaan
new_job = st.sidebar.text_input("Add a new job if not listed", key="job_input")
if st.sidebar.button("Add Job"):
    if new_job and new_job not in default_jobs:
        default_jobs.append(new_job)
        job = new_job
    elif not new_job:
        st.sidebar.error("Please enter a job to add!")
    else:
        st.sidebar.error("Job already exists!")

# Sidebar: Category Picker
st.sidebar.title("Category Picker")
category = st.sidebar.selectbox("Pick A Category", default_cat)

# Input tambahan untuk kategori
new_category = st.sidebar.text_input("Add a new category if not listed", key="category_input")
if st.sidebar.button("Add Category"):
    if new_category and new_category not in default_cat:
        default_cat.append(new_category)
        category = new_category
    elif not new_category:
        st.sidebar.error("Please enter a category to add!")
    else:
        st.sidebar.error("Category already exists!")

# Sidebar: Media Picker
st.sidebar.title("Media Picker")
media = st.sidebar.selectbox("Pick A Media", default_media)

# Sidebar: OpenAI Temperature
st.sidebar.title("OpenAI Temperature")

slider_helper_text = """
The LLM temperature in OpenAI refers to a parameter that controls the randomness of the model's responses, 
where higher values (e.g., 1.0) make the output more creative and diverse, while lower values (e.g., 0.2) make it more 
focused and deterministic.
"""

nilai = st.sidebar.slider("Set Your OpenAI Temperature", 0, 10, 5,  help=slider_helper_text)

if st.sidebar.button("Tombol Khusus", key="sidebar_button"):
    pass
