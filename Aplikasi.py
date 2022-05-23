import streamlit as st

st.title('Kumpulan Aplikasi Sederhana')
st.caption(''' Kelompok 10
1. Rahayu Puspita Dewi (7211421001)
2. Diajeng Ayuning Ati (7211421021)
3. Ayesha Reisla Hanifa (7211421120)
4. Via Alfu Khasanah (7211421132)
5. I Gusti Bagus Surya Wedanta (7211421250)''' )




def Konverter_Jarak():
    st.header('Konverter jarak')
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
    st.header('Konverter Suhu')
    st.caption('Aplikasi ini akan mengubah suhu celcius menjadi fahrenheit')
    # Menginput Suhu dalam Derajat Celcius
    celcius = st.number_input("Tuliskan Suhu dalam Celcius: ")

    # Menghitung Suhu dalam Derajat Fahrenheit
    fahrenheit = (celcius * 1.8) + 32

    # Menampilkan Hasil Konversi Jarak
    st.write('%0.2f Derajat Celcius sama dengan %0.2f Derajat Fahrenheit' % (celcius, fahrenheit))


def blank():
    st.write ('Silahkan Pilih Sistem')

def Menghitung_Kubus():
    st.header('Menghitung Volume Kubus')
    st.caption('aplikasi ini akan menghitung volume kubus')
    # Menginput Sisi Kubus
    sisi = st.number_input('Tulis Sisi Kubus: ',0,)

    # Hitung Volume Kubus
    volume = sisi ** 3

    # Menampilkan Hasil Perhitungan
    st.write('Volume Kubus adalah %0.2f' % volume)

def Menghitung_Segitiga() :
    st.header('Menghitung Luas Segitiga')
    st.caption('Aplikasi ini akan menghitung Luas Segitiga')
    # Menginput Alas dan Tinggi Segitiga
    alas = st.number_input('Tulis Alas Segitiga: ')
    tinggi = st.number_input('Tulis Tinggi Segitiga: ')

    # Hitung Luas Segitiga
    luas = (alas * tinggi) / 2

    # Menampilkan Hasil Perhitungan
    st.write('Luas Segitiga adalah %0.2f' % luas)

def kiw () :
    st.header('sudah dibilang jangan dibuka')
    st.image("https://i.pinimg.com/originals/66/0d/5a/660d5af194cc62242ed2bc6a5d88f50e.jpg")

def diskon () :

    diskon = st.number_input('tuliskan jumlah diskon',0,100)
    harga  = st.number_input('masukan jumlah uang',0,)

    total = (diskon/100) * harga

    st.write('Jumlah yang harus anda bayar adalah =','Rp', (float(total)))


pages = {
    '': blank,
    'konverter jarak' : Konverter_Jarak,
    'konverter suhu'  : Konverter_Suhu,
    'Menghitung Volume Kubus' : Menghitung_Kubus,
    'Menghitung Luas Segitiga' : Menghitung_Segitiga,
    'Menghitung Diskon' : diskon,
    'JANGAN BUKA YANG INI! ' : kiw

}
selected_page = st.selectbox(
    'pilih alat',
    pages.keys()
)
pages[selected_page]()
