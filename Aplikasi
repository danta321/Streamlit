import streamlit as st

st.title('Kumpulan Aplikasi Sederhana')
st.caption('Dibuat di phyton kemudian di tampilkan melalui Streamlit')


def Konverter_Jarak():
    st.header('Konverter jarak')
    st.write('Aplikasi konversi kilometer ke mil', anchor='program1')
    st.caption('aplikasi ini akan mengubah angka yang dimasukan dari kilometer menjadi'
               ' mil')

    # Menginput Jarak dalam Satuan Kilometer
    kilometer = st.number_input("Tuliskan Jarak dalam Kilometer: ")

    # Nilai Faktor Konversi
    faktor_konversi = 0.621371

    # Menghitung Jarak dalam Satuan Mil
    mil = kilometer * faktor_konversi

    # Menampilkan Hasil Konversi Jarak
    st.write('%0.2f Kilometer sama dengan %0.2f Mil' % (kilometer, mil))

def Konverter_Suhu() :

    # Menginput Suhu dalam Derajat Celcius
    celcius = st.number_input("Tuliskan Suhu dalam Celcius: ")

    # Menghitung Suhu dalam Derajat Fahrenheit
    fahrenheit = (celcius * 1.8) + 32

    # Menampilkan Hasil Konversi Jarak
    st.write('%0.2f Derajat Celcius sama dengan %0.2f Derajat Fahrenheit' % (celcius, fahrenheit))


def blank():
    st.write ('Silahkan Pilih Sistem')

def Menghitung_Kubus():
    # Menginput Sisi Kubus
    sisi = st.number_input('Tulis Sisi Kubus: ')

    # Hitung Volume Kubus
    volume = sisi ** 3

    # Menampilkan Hasil Perhitungan
    st.write('Volume Kubus adalah %0.2f' % volume)

def Menghitung_Segitiga() :
    # Menginput Alas dan Tinggi Segitiga
    alas = st.number_input('Tulis Alas Segitiga: ')
    tinggi = st.number_input('Tulis Tinggi Segitiga: ')

    # Hitung Luas Segitiga
    luas = (alas * tinggi) / 2

    # Menampilkan Hasil Perhitungan
    st.write('Luas Segitiga adalah %0.2f' % luas)

def kiw () :
    st.image("https://www.meme-arsenal.com/memes/95f8e2a3efbf96affa20603869dd5345.jpg")



pages = {
    '': blank,
    'konverter jarak' : Konverter_Jarak,
    'konverter suhu'  : Konverter_Suhu,
    'Menghitung Volume Kubus' : Menghitung_Kubus,
    'Menghitung Luas Segitiga' : Menghitung_Segitiga,
    'JANGAN BUKA YANG INI! ' : kiw,
}
selected_page = st.selectbox(
    'pilih alat',
    pages.keys()
)
pages[selected_page]()
