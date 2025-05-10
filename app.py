import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model
model = joblib.load("model/random_forest_model.joblib")

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

st.markdown("Masukkan data pendaftar di bawah ini untuk memprediksi apakah mahasiswa berisiko dropout atau tidak.")

# Input fitur yang diketahui saat pendaftaran
marital_status = st.selectbox("Status Perkawinan", [1, 2])  # 1 - Single, 2 - Married
application_mode = st.selectbox("Mode Aplikasi", [1, 2, 3, 4, 5])  # 1 to 5 options
application_order = st.slider("Urutan Aplikasi", min_value=1, max_value=10, value=1)
course = st.selectbox("Course", [33, 171, 8014, 9003, 9119])  # List courses
attendance = st.selectbox("Daytime/Evening Attendance", [1, 0])  # 1 - Daytime, 0 - Evening
previous_qualification = st.selectbox("Kualifikasi Sebelumnya", [1, 2, 3, 4, 5])  # Various levels of previous education
prev_grade = st.number_input("Grade Kualifikasi Sebelumnya", 0.0, 200.0, 100.0)
nationality = st.selectbox("Kebangsaan", [1, 2])  # 1 - Portuguese, 2 - Other countries
mother_qual = st.selectbox("Pendidikan Ibu", [1, 2, 3, 4, 5])  # Basic, Secondary, Higher, None, Other
father_qual = st.selectbox("Pendidikan Ayah", [1, 2, 3, 4, 5])  # Basic, Secondary, Higher, None, Other
mother_job = st.selectbox("Pekerjaan Ibu", [1, 2, 3])  # 1, 2, or 3 for job categories
father_job = st.selectbox("Pekerjaan Ayah", [1, 2, 3])  # 1, 2, or 3 for job categories
admission_grade = st.number_input("Grade Pendaftaran", 0.0, 200.0, 150.0)
displaced = st.selectbox("Mahasiswa Pindahan", [0, 1])  # 0 - No, 1 - Yes
special_needs = st.selectbox("Berkebutuhan Khusus", [0, 1])  # 0 - No, 1 - Yes
debtor = st.selectbox("Apakah memiliki tunggakan?", [0, 1])  # 0 - No, 1 - Yes
tuition_up_to_date = st.selectbox("Biaya Pendidikan Up to Date?", [0, 1])  # 0 - No, 1 - Yes
gender = st.selectbox("Jenis Kelamin", [0, 1])  # 0 - Male, 1 - Female
scholarship = st.selectbox("Penerima Beasiswa?", [0, 1])  # 0 - No, 1 - Yes
age = st.slider("Umur saat Mendaftar", 16, 60, 20)
international = st.selectbox("Mahasiswa Internasional?", [0, 1])  # 0 - No, 1 - Yes

# Semester 1
cu1_credited = st.number_input("CU 1st Sem Credit", 0, 60, 30)
cu1_enrolled = st.number_input("CU 1st Sem Enrolled", 0, 60, 30)
cu1_eval = st.number_input("CU 1st Sem Evaluations", 0, 60, 30)
cu1_approved = st.number_input("CU 1st Sem Approved", 0, 60, 30)
cu1_grade = st.number_input("CU 1st Sem Grade", 0.0, 20.0, 10.0)
cu1_without_eval = st.number_input("CU 1st Sem Without Evaluations", 0, 60, 0)

# Semester 2
cu2_credited = st.number_input("CU 2nd Sem Credit", 0, 60, 30)
cu2_enrolled = st.number_input("CU 2nd Sem Enrolled", 0, 60, 30)
cu2_eval = st.number_input("CU 2nd Sem Evaluations", 0, 60, 30)
cu2_approved = st.number_input("CU 2nd Sem Approved", 0, 60, 30)
cu2_grade = st.number_input("CU 2nd Sem Grade", 0.0, 20.0, 10.0)
cu2_without_eval = st.number_input("CU 2nd Sem Without Evaluations", 0, 60, 0)

# Ekonomi Makro
unemployment = st.number_input("Tingkat Pengangguran (%)", 0.0, 100.0, 7.0)
inflation = st.number_input("Tingkat Inflasi (%)", 0.0, 100.0, 2.5)
gdp = st.number_input("GDP", 0.0, 1e6, 30000.0)

# Konversi input ke dataframe
input_data = pd.DataFrame({
    'Marital_status': [marital_status],
    'Application_mode': [application_mode],
    'Application_order': [application_order],
    'Course': [course],
    'Daytime_evening_attendance': [attendance],
    'Previous_qualification': [previous_qualification],
    'Previous_qualification_grade': [prev_grade],
    'Nacionality': [nationality],
    'Mothers_qualification': [mother_qual],
    'Fathers_qualification': [father_qual],
    'Mothers_occupation': [mother_job],
    'Fathers_occupation': [father_job],
    'Admission_grade': [admission_grade],
    'Displaced': [displaced],
    'Educational_special_needs': [special_needs],
    'Debtor': [debtor],
    'Tuition_fees_up_to_date': [tuition_up_to_date],
    'Gender': [gender],
    'Scholarship_holder': [scholarship],
    'Age_at_enrollment': [age],
    'International': [international],
    'Curricular_units_1st_sem_credited': [cu1_credited],
    'Curricular_units_1st_sem_enrolled': [cu1_enrolled],
    'Curricular_units_1st_sem_evaluations': [cu1_eval],
    'Curricular_units_1st_sem_approved': [cu1_approved],
    'Curricular_units_1st_sem_grade': [cu1_grade],
    'Curricular_units_1st_sem_without_evaluations': [cu1_without_eval],
    'Curricular_units_2nd_sem_credited': [cu2_credited],
    'Curricular_units_2nd_sem_enrolled': [cu2_enrolled],
    'Curricular_units_2nd_sem_evaluations': [cu2_eval],
    'Curricular_units_2nd_sem_approved': [cu2_approved],
    'Curricular_units_2nd_sem_grade': [cu2_grade],
    'Curricular_units_2nd_sem_without_evaluations': [cu2_without_eval],
    'Unemployment_rate': [unemployment],
    'Inflation_rate': [inflation],
    'GDP': [gdp]
})

# Preprocessing manual jika diperlukan (label encoding sederhana)
def encode_features(df):
    mappings = {
        'Gender': {'male': 0, 'female': 1},
        'Debtor': {0: 0, 1: 1},
        'Scholarship_holder': {0: 0, 1: 1},
        'Displaced': {0: 0, 1: 1},
        'Educational_special_needs': {0: 0, 1: 1},
    }

    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)

    # Label Encoding sisa fitur kategorikal (pastikan urutan sesuai training!)
    label_encoders = {
        'Nacionality': {1: 0, 2: 1},  # Portuguese -> 0, Other -> 1
        'Previous_qualification': {1: 0, 2: 1, 3: 2, 4: 3},  # Secondary -> 0, Higher -> 1, etc.
        'Mothers_qualification': {1: 0, 2: 1, 3: 2, 4: 3, 5: 4},
        'Fathers_qualification': {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    }

    for col, enc in label_encoders.items():
        df[col] = df[col].map(enc)

    return df

input_encoded = encode_features(input_data)

# Tombol prediksi
if st.button("Prediksi Dropout"):
    prediction = model.predict(input_encoded)[0]
    proba = model.predict_proba(input_encoded)[0][1]  # Probabilitas dropout (kelas 1)

    # Menampilkan hasil prediksi
    if prediction == 1:
        st.error(f"⚠️ Mahasiswa ini **berisiko dropout** (Probabilitas: {proba:.2f})")
    else:
        st.success(f"✅ Mahasiswa ini **tidak berisiko dropout** (Probabilitas: {proba:.2f})")
