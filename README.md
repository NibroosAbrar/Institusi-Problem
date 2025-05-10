
# 📊 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## 🧠 Business Understanding

**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Institusi ini telah mencetak banyak lulusan berkualitas dengan reputasi yang sangat baik. Namun, dalam perjalanannya, Jaya Jaya Institut menghadapi tantangan serius yaitu **tingginya angka mahasiswa yang mengalami dropout (tidak menyelesaikan pendidikan)**.

Tingginya dropout menjadi ancaman besar bagi reputasi dan kualitas akademik institusi. Oleh karena itu, diperlukan sistem analisis dan prediksi untuk mendeteksi mahasiswa yang berpotensi dropout agar dapat diberikan bimbingan dan perhatian khusus.

### 🎯 Permasalahan Bisnis

- Jumlah mahasiswa yang dropout tergolong tinggi (**1.421 dari total 4.424 mahasiswa**).
- Sulitnya memahami faktor-faktor yang menyebabkan mahasiswa tidak menyelesaikan studinya.
- Tidak tersedianya sistem visualisasi performa mahasiswa secara menyeluruh dan real-time untuk pihak manajemen dan akademik.

### 🔍 Cakupan Proyek

- Melakukan eksplorasi dan analisis data performa mahasiswa.
- Membuat dashboard interaktif menggunakan Metabase untuk memantau status mahasiswa.
- Membangun prototype sistem machine learning untuk prediksi risiko dropout mahasiswa.
- Menyediakan insight dan rekomendasi strategis untuk menurunkan angka dropout.

### ⚙️ Persiapan

**Sumber Data**: Dataset performa mahasiswa yang disediakan oleh Jaya Jaya Institut (format CSV)

**Kolom Penting**:
`Gender`, `Status` (Dropout, Enrolled, Graduate), `Course`, `Nationality`, `UnemploymentRate`, dll.

**Environment Setup**:

```bash
# Menjalankan Metabase menggunakan Docker
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

---

## 📈 Business Dashboard

Dashboard dibangun menggunakan **Metabase** untuk menampilkan informasi utama tentang performa mahasiswa.

📎 **Link Dashboard**: [Metabase Dashboard (Local)](http://localhost:3000/public/dashboard/c668be09-ae85-42f8-93e5-567609842fb0)

### Visualisasi Kunci:

- **Jumlah Mahasiswa**: 4.424
- **Jumlah Dropout**: 1.421
- Sebaran mahasiswa berdasarkan **status**: Dropout, Enrolled, Graduate.
- Perbandingan status berdasarkan **gender**.
- Komposisi **kewarganegaraan** mahasiswa (mayoritas Portuguese).
- Jumlah dropout berdasarkan **bidang studi (course)**.
- Korelasi antara **tingkat pengangguran** dan jumlah dropout.

---

## 🤖 Menjalankan Sistem Machine Learning

Sistem prediksi dibuat menggunakan Python dan Streamlit, bertujuan untuk memprediksi kemungkinan seorang mahasiswa akan dropout berdasarkan fitur-fitur yang tersedia dalam dataset.

📎 **Link Aplikasi Machine Learning**: [Streamlit App](https://nibroos-institusi-problem.streamlit.app/)

```bash
# Menjalankan aplikasi Streamlit secara lokal
streamlit run app.py
```

---

## ✅ Conclusion

- Terdapat **1.421 mahasiswa** yang dropout dari total 4.424.
- Mayoritas mahasiswa berasal dari kewarganegaraan **Portuguese** (97.5%).
- Jumlah mahasiswa perempuan yang dropout sedikit lebih tinggi dibanding laki-laki.
- Program studi seperti **Social Service**, **Nursing**, dan **Management** memiliki tingkat dropout tertinggi.
- Dropout memiliki kecenderungan meningkat pada **wilayah dengan tingkat pengangguran yang tinggi**.

---

## 🚀 Rekomendasi Action Items

- 📚 **Adakan program bimbingan belajar atau konseling akademik** untuk mahasiswa yang terindikasi berisiko dropout.
- 📊 **Gunakan sistem prediksi berbasis machine learning** secara aktif untuk mendeteksi mahasiswa yang membutuhkan intervensi.
- 🤝 **Perkuat dukungan psikososial dan finansial**, terutama di program studi dengan tingkat dropout tinggi.
- 📈 **Integrasikan dashboard performa** ke sistem akademik internal agar dapat dipantau secara berkala oleh pihak manajemen.
