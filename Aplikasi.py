import streamlit as st

st.title('Kumpulan Perhitungan Sederhana')
st.write(''' Kelompok 10
1. Rahayu Puspita Dewi (7211421001)
2. Diajeng Ayuning Ati (7211421021)
3. Ayesha Reisla Hanifa (7211421120)
4. Via Alfu Khasanah (7211421132)
5. I Gusti Bagus Surya Wedanta (7211421250)''' )


def diet_m():
    st.header('Menghitung berat badan ideal untuk pria')

    tinggi = st.number_input('Masukan Tinggi Badan Anda (cm)', 0)
    total = (tinggi - 100) - (tinggi - 100) * 10 / 100

    st.write('berat badan ideal adalah %0.0f KG' % total)
    st.caption('kurang dari hasil berarti berat badan anda kurang ideal')


def diet_w():
    st.header('Menghitung berat badan ideal untuk wanita')

    tinggi = st.number_input('Masukan Tinggi Badan Anda (cm)', 0)
    total = (tinggi - 100) - (tinggi - 100) * 15 / 100

    st.write('berat badan ideal adalah %0.0f KG' % total)
    st.caption('kurang dari hasil berarti berat badan anda kurang ideal')


def diskon () :

    diskon = st.number_input('tuliskan jumlah diskon',0)
    harga  = st.number_input('masukan jumlah uang',0,)

    total = (diskon/100) * harga

    st.write('total yang harus anda bayar adalah Rp %0.0f' % total)


def mata_uang():
    st.header('konversi mata uang Euro ke Rupiah')
    st.caption('dengan nilai 1 euro = Rp.15.600')
    uang = st.number_input('Masukan Nominal Uang (euro)', 0)
    total = uang * 15600
    st.write('Hasil Konversi Rp %0.0f' % total)


def Menghitung_Segitiga() :
    st.header('Menghitung Luas Segitiga')
    st.caption('Aplikasi ini akan menghitung Luas Segitiga')

    alas = st.number_input('Tulis Alas Segitiga: ',0)
    tinggi = st.number_input('Tulis Tinggi Segitiga: ',0)


    luas = (alas * tinggi) / 2


    st.write('Luas Segitiga adalah %0.0f' % luas)

def Menghitung_Kubus():
    st.header('Menghitung Volume Kubus')
    st.caption('aplikasi ini akan menghitung volume kubus')

    sisi = st.number_input('Tulis Sisi Kubus: ',0,)


    volume = sisi ** 3


    st.write('Volume Kubus adalah %0.2f' % volume)

def Konverter_Jarak():
    st.header('Konverter jarak')
    st.caption('aplikasi ini akan mengubah angka yang dimasukan dari kilometer menjadi'
               ' mil')

    kilometer = st.number_input("Tuliskan Jarak dalam Kilometer: ",0)

    faktor_konversi = 0.621371


    mil = kilometer * faktor_konversi


    st.write('%0.2f Kilometer sama dengan %0.2f Mil' % (kilometer, mil))

def Konverter_Suhu() :
    st.header('Konverter Suhu')
    st.caption('Aplikasi ini akan mengubah suhu celcius menjadi fahrenheit')

    celcius = st.number_input("Tuliskan Suhu dalam Celcius: ",0)


    fahrenheit = (celcius * 1.8) + 32


    st.write('%0.2f Derajat Celcius sama dengan %0.2f Derajat Fahrenheit' % (celcius, fahrenheit))


def jam():
    st.header('Konversi Jam ke Menit')
    jam = st.number_input('masukan jam', 0)
    ayam = 60 * jam
    st.write('Hasil Konversi %0.0f menit' % ayam)


def yard():
    yard = st.number_input('masukan ukuran yard', 0)
    total = 0.914 * yard
    st.write('Hasil Konversi Meter', total, 'meter')


def blank():
    st.write ('Silahkan Pilih Sistem')



def kiw () :
    st.header('hampter')
    st.write('hampter')
    st.image('https://memezila.com/wp-content/Hampter-meme-8263.png')






pages = {
    '': blank,
    'Penghitung Berat Badan Ideal (pria)': diet_m,
    'Penghitung Berat Badan Ideal (wanita)': diet_w,
    'Menghitung Diskon': diskon,
    'Konversi Mata Uang Euro ke Rupiah': mata_uang,
    'Menghitung Luas Segitiga': Menghitung_Segitiga,
    'Menghitung Volume Kubus': Menghitung_Kubus,
    'Konversi jarak Km ke Mil' : Konverter_Jarak,
    'Konversi Celcius ke Fahrenheit'  : Konverter_Suhu,
    'Konversi Jam ke Menit' : jam,
    'Konversi Yard ke Meter' : yard,
    '-': kiw,

}
selected_page = st.selectbox(
    'pilih alat',
    pages.keys()
)
pages[selected_page]()
