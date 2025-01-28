import streamlit as st

st.title("Generate Your Absurdly Excused")

# Daftar awal untuk pekerjaan dan kategori
default_jobs = ["Data Scientist", "Software Engineer", "Product Manager", "Policeman", "Teacher"]
default_cat = ["Animal", "Family", "Vehicle"]

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

