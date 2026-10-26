import streamlit as raza
import pandas as aqil
raza.write("young, wild and free")
df = aqil.DataFrame(
    {'SKU': ['G2G-803', 'G2G-234', 'G2G-232', 'G2G-07', 'G2G-3103'],
     'QTY': [288, 96, 96, None, 288]})

print(df)
raza.write(df)
raza.header("Widget dasar")

nama = raza.text_input("Nama")
region = raza.selectbox("Region", ["Sulawesi 1", "Sulawesi 2"])
place = raza.selectbox("Tempat", ["Makassar", "Parepare", "Palopo"])
produk = raza.multiselect("Produk", ["Serum", "Sunscreen", "Cleanser"])
target = raza.slider("Target pencapaian (%)", 0, 150, 100)
detail = raza.checkbox("Tampilkan detail")
if raza.button("Hitung"):
    raza.success(f"{nama} - {region} - {place} - target {target}%")
if detail:
    raza.write("Produk dipilih:", produk)

raza.spinner("Loading data...")
raza.balloons()
raza.radio("Pilih warna tema", ["Merah", "Biru", "Hijau"])
raza.warning("Perhatian! Data yang ditampilkan belum diverifikasi.")
raza.color_picker("Pilih warna tema", "#00f900")