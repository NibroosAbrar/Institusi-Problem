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
gender = st.selectbox("Jenis Kelamin", ["male", "female"])
age = st.slider("Umur saat mendaftar", min_value=15, max_value=60, value=20)
nationality = st.selectbox("Kebangsaan", ["Portuguese", "Angolan", "Cape Verdean", "Guinean", "Mozambican", "Other"])
previous_qualification = st.selectbox("Kualifikasi Sebelumnya", [
    'Secondary education', 'Higher education', 'Professional course', 'Other'
])
mother_qualification = st.selectbox("Pendidikan Ibu", [
    'Basic', 'Secondary', 'Higher', 'None', 'Other'
])
father_qualification = st.selectbox("Pendidikan Ayah", [
    'Basic', 'Secondary', 'Higher', 'None', 'Other'
])
debtor = st.selectbox("Apakah memiliki tunggakan?", ["yes", "no"])
scholarship = st.selectbox("Penerima beasiswa?", ["yes", "no"])
displaced = st.selectbox("Apakah siswa pindahan/displaced?", ["yes", "no"])
edu_special_needs = st.selectbox("Berkebutuhan khusus?", ["yes", "no"])

# Konversi ke dataframe
input_data = pd.DataFrame({
    'Gender': [gender],
    'Age_at_enrollment': [age],
    'Nacionality': [nationality],
    'Previous_qualification': [previous_qualification],
    'Mothers_qualification': [mother_qualification],
    'Fathers_qualification': [father_qualification],
    'Debtor': [debtor],
    'Scholarship_holder': [scholarship],
    'Displaced': [displaced],
    'Educational_special_needs': [edu_special_needs],
})

# Preprocessing manual jika diperlukan (label encoding sederhana)
def encode_features(df):
    mappings = {
        'Gender': {'male': 0, 'female': 1},
        'Debtor': {'no': 0, 'yes': 1},
        'Scholarship_holder': {'no': 0, 'yes': 1},
        'Displaced': {'no': 0, 'yes': 1},
        'Educational_special_needs': {'no': 0, 'yes': 1},
    }

    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)

    # Label Encoding sisa fitur kategorikal (pastikan urutan sesuai training!)
    label_encoders = {
        'Nacionality': {'Portuguese': 0, 'Angolan': 1, 'Cape Verdean': 2, 'Guinean': 3, 'Mozambican': 4, 'Other': 5},
        'Previous_qualification': {'Secondary education': 0, 'Higher education': 1, 'Professional course': 2, 'Other': 3},
        'Mothers_qualification': {'None': 0, 'Basic': 1, 'Secondary': 2, 'Higher': 3, 'Other': 4},
        'Fathers_qualification': {'None': 0, 'Basic': 1, 'Secondary': 2, 'Higher': 3, 'Other': 4}
    }

    for col, enc in label_encoders.items():
        df[col] = df[col].map(enc)

    return df

input_encoded = encode_features(input_data)

# Tombol prediksi
if st.button("Prediksi Dropout"):
    prediction = model.predict(input_encoded)[0]
    proba = model.predict_proba(input_encoded)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Mahasiswa ini **berisiko dropout** (Probabilitas: {proba:.2f})")
    else:
        st.success(f"✅ Mahasiswa ini **tidak berisiko dropout** (Probabilitas: {proba:.2f})")
