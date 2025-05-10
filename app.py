import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model yang sudah dilatih
model = joblib.load("model/random_forest_model.joblib")

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

st.markdown("""
Masukkan data pendaftar di bawah ini untuk memprediksi apakah mahasiswa berisiko dropout atau tidak. 
Semua input yang diminta harus sesuai dengan kategori yang ditentukan dalam penjelasan.
""")

# Input fitur yang diketahui saat pendaftaran

# Status Perkawinan
marital_status = st.selectbox("Status Perkawinan", [1, 2], help="Pilih 1 untuk 'Single' (Belum Menikah) atau 2 untuk 'Married' (Menikah).")

# Mode Aplikasi
application_mode = st.selectbox("Mode Aplikasi", [1, 2, 3, 4, 5], help="Pilih mode aplikasi (1 - Online, 2 - Offline, dst.).")

# Urutan Aplikasi
application_order = st.slider("Urutan Aplikasi", min_value=1, max_value=10, value=1, help="Urutan aplikasi mahasiswa (1-10).")

# Course (kode kursus yang diambil)
course = st.selectbox("Course", [33, 171, 8014, 9003, 9119], help="Pilih kode kursus dari daftar yang ada.")

# Daytime/Evening Attendance
attendance = st.selectbox("Daytime/Evening Attendance", [1, 0], help="1 untuk 'Daytime' (Pagi), 0 untuk 'Evening' (Sore).")

# Pendidikan Sebelumnya
previous_qualification = st.selectbox("Kualifikasi Sebelumnya", [1, 2, 3, 4, 5], help="Pilih tingkat kualifikasi pendidikan sebelumnya (1 - Dasar, 2 - Menengah, 3 - Tinggi, dst.).")

# Nilai grade pada kualifikasi sebelumnya
prev_grade = st.number_input("Grade Kualifikasi Sebelumnya", 0.0, 200.0, 100.0, help="Masukkan nilai grade dari kualifikasi pendidikan sebelumnya.")

# Kebangsaan
nationality = st.selectbox("Kebangsaan", [1, 2], help="Pilih 1 untuk 'Portuguese' (Portugal), 2 untuk 'Other' (Negara Lain).")

# Pendidikan Ibu
mother_qual = st.selectbox("Pendidikan Ibu", [1, 2, 3, 4, 5], help="Pilih tingkat pendidikan ibu (1 - Dasar, 2 - Menengah, dst.).")

# Pendidikan Ayah
father_qual = st.selectbox("Pendidikan Ayah", [1, 2, 3, 4, 5], help="Pilih tingkat pendidikan ayah (1 - Dasar, 2 - Menengah, dst.).")

# Pekerjaan Ibu
mother_job = st.selectbox("Pekerjaan Ibu", [1, 2, 3], help="Pilih kategori pekerjaan ibu (1 - Rumah Tangga, 2 - Pekerjaan Tetap, dst.).")

# Pekerjaan Ayah
father_job = st.selectbox("Pekerjaan Ayah", [1, 2, 3], help="Pilih kategori pekerjaan ayah (1 - Rumah Tangga, 2 - Pekerjaan Tetap, dst.).")

# Nilai grade pada saat pendaftaran
admission_grade = st.number_input("Grade Pendaftaran", 0.0, 200.0, 150.0, help="Masukkan nilai grade pada saat pendaftaran.")

# Apakah mahasiswa adalah mahasiswa pindahan
displaced = st.selectbox("Mahasiswa Pindahan", [0, 1], help="Pilih 1 jika mahasiswa adalah mahasiswa pindahan, 0 jika bukan.")

# Apakah mahasiswa memiliki kebutuhan khusus
special_needs = st.selectbox("Berkebutuhan Khusus", [0, 1], help="Pilih 1 jika mahasiswa memiliki kebutuhan khusus, 0 jika tidak.")

# Apakah mahasiswa memiliki tunggakan
debtor = st.selectbox("Apakah memiliki tunggakan?", [0, 1], help="Pilih 1 jika mahasiswa memiliki tunggakan, 0 jika tidak.")

# Apakah biaya pendidikan up to date
tuition_up_to_date = st.selectbox("Biaya Pendidikan Up to Date?", [0, 1], help="Pilih 1 jika biaya pendidikan up to date, 0 jika tidak.")

# Jenis Kelamin
gender = st.selectbox("Jenis Kelamin", [0, 1], help="Pilih 0 untuk 'Male' (Laki-laki), 1 untuk 'Female' (Perempuan).")

# Apakah mahasiswa menerima beasiswa
scholarship = st.selectbox("Penerima Beasiswa?", [0, 1], help="Pilih 1 jika mahasiswa menerima beasiswa, 0 jika tidak.")

# Umur saat mendaftar
age = st.slider("Umur saat Mendaftar", 16, 60, 20, help="Masukkan umur mahasiswa saat pendaftaran.")

# Apakah mahasiswa adalah mahasiswa internasional
international = st.selectbox("Mahasiswa Internasional?", [0, 1], help="Pilih 1 jika mahasiswa adalah mahasiswa internasional, 0 jika tidak.")

# Semester 1
cu1_credited = st.number_input("CU 1st Sem Credit", 0, 60, 30, help="Masukkan jumlah kredit yang diterima pada semester 1.")
cu1_enrolled = st.number_input("CU 1st Sem Enrolled", 0, 60, 30, help="Masukkan jumlah unit kursus yang diikuti pada semester 1.")
cu1_eval = st.number_input("CU 1st Sem Evaluations", 0, 60, 30, help="Masukkan jumlah evaluasi yang diikuti pada semester 1.")
cu1_approved = st.number_input("CU 1st Sem Approved", 0, 60, 30, help="Masukkan jumlah kursus yang disetujui pada semester 1.")
cu1_grade = st.number_input("CU 1st Sem Grade", 0.0, 20.0, 10.0, help="Masukkan nilai grade pada semester 1.")
cu1_without_eval = st.number_input("CU 1st Sem Without Evaluations", 0, 60, 0, help="Masukkan jumlah kursus pada semester 1 tanpa evaluasi.")

# Semester 2
cu2_credited = st.number_input("CU 2nd Sem Credit", 0, 60, 30, help="Masukkan jumlah kredit yang diterima pada semester 2.")
cu2_enrolled = st.number_input("CU 2nd Sem Enrolled", 0, 60, 30, help="Masukkan jumlah unit kursus yang diikuti pada semester 2.")
cu2_eval = st.number_input("CU 2nd Sem Evaluations", 0, 60, 30, help="Masukkan jumlah evaluasi yang diikuti pada semester 2.")
cu2_approved = st.number_input("CU 2nd Sem Approved", 0, 60, 30, help="Masukkan jumlah kursus yang disetujui pada semester 2.")
cu2_grade = st.number_input("CU 2nd Sem Grade", 0.0, 20.0, 10.0, help="Masukkan nilai grade pada semester 2.")
cu2_without_eval = st.number_input("CU 2nd Sem Without Evaluations", 0, 60, 0, help="Masukkan jumlah kursus pada semester 2 tanpa evaluasi.")

# Ekonomi Makro
unemployment = st.number_input("Tingkat Pengangguran (%)", 0.0, 100.0, 7.0, help="Masukkan tingkat pengangguran (%).")
inflation = st.number_input("Tingkat Inflasi (%)", 0.0, 100.0, 2.5, help="Masukkan tingkat inflasi (%).")
gdp = st.number_input("GDP", 0.0, 1e6, 30000.0, help="Masukkan nilai GDP.")

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
        'Gender': {0: 0, 1: 1},
        'Debtor': {0: 0, 1: 1},
        'Scholarship_holder': {0: 0, 1: 1},
        'Displaced': {0: 0, 1: 1},
        'Educational_special_needs': {0: 0, 1: 1},
        'Tuition_fees_up_to_date': {0: 0, 1: 1},
        'International': {0: 0, 1: 1}
    }
    for column, mapping in mappings.items():
        df[column] = df[column].map(mapping)
    return df

# Prediksi berdasarkan model
encoded_input = encode_features(input_data)
prediction = model.predict(encoded_input)

# Tampilkan hasil prediksi
if prediction == 1:
    st.write("Mahasiswa berisiko tinggi untuk dropout.")
else:
    st.write("Mahasiswa tidak berisiko dropout.")
