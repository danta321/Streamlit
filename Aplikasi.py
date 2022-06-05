import streamlit as st
import requests
import pandas as pd
st.title('Kosan Bersama')
st.write('kosan kosan kosan')

def kiw () :
    st.header('hampter')
    st.write('hampter')
    st.image('https://memezila.com/wp-content/Hampter-meme-8263.png')
def blank () :
    st.write ('Silahkan Pilih Kosan')

def kos4 () :
    st.image('https://www.sewakost.com/files/02-2022/ad75368/kost-petojo-sabangan-696958619_large.jpg')
    st.header('Kosan Berlian')
    st.write('kamar mandi luar')
    st.write('Sudah termasuk Iuran Air,Listrik,Wifi,Ada Dapur Dikamar')
    st.write('Kasur,Bantal disediakan')
    st.write('harga Rp 500.000/Bulan')


def kos3 () :
    st.image('https://www.sewakost.com/files/03-2021/ad52407/kos-kosan-bebas-aman-dan-2110797795_large.jpg')
    st.header('Kosan udin')
    st.write('Kamar Mandi Luar,Sudah termasuk Iuran Air,Listrik')
    st.write('harga Rp 300.000/Bulan')

def kos1 () :
    st.image("https://www.sewakost.com/files/03-2020/ad34268/rumah-kost-kosan-damkar-1220752865_large.jpeg")
    st.header('Kosan Duar')
    st.write("Sudah termasuk Iuran Air,Listrik,Wifi")
    st.write("kamar mandi dalam,Almari,Kasur,Meja Belajar")
    st.write("harga Rp 800.000/Bulan")

def kos2 () :
    st.image("https://www.sewakost.com/files/03-2020/ad34268/rumah-kost-kosan-damkar-823273766_large.jpeg")
    st.header('kosan diw')
    st.write("sudah termasuk Iuran Air,Listrik,Wifi")
    st.write("kamar mandi Luar,almari,Kasur,AC")
    st.write("harga Rp 750.000/Bulan")

def kos5 () :
    st.image("https://s3.us-east-2.amazonaws.com/dlba-production-bucket/property_images/9425816/aaf0eaa4-3790-4594-8ff2-610040df4896.jpg")
    st.header('kosan herman')
    st.write('Kamar mandi luar,Kasur,Kipas Tangan')
    st.write('sudah termasuk iuran air, Listrik tidak tersedia')
    st.write('harga Rp 100.000/Bulan')

pages = {
    '': blank,
    '-': kiw,
    'kos1' : kos1,
    'kos2' : kos2,
    'kos3' : kos3,
    'kos4' : kos4,
    'kos5' : kos5,

}
selected_page = st.selectbox(
    'Pilih Kosan',
    pages.keys()
)
pages[selected_page]()


total1 = 0
total2 = 0
harga = []
kosan = ["",'kos1',"kos2",'kos3','kos4','kos5']


nama = st.text_input('nama penyewa')
telp = st.text_input('nomor telpon')
jenis = st.selectbox('pilih jenis kos',kosan)
bulan = st.number_input('berapa bulan',0)



enter = st.button('enter')

if jenis == "kos1":
    harga = 500000
    total1 = harga*bulan
elif jenis == 'kos2':
    harga = 600000
    total1 = harga*bulan
elif jenis == "kos3" :
    harga = 800000
    total1 = harga*bulan
elif jenis == "kos4" :
    harga = 650000
    total1 = harga*bulan
elif jenis == "kos5" :
    harga = 100000
    total1 = harga*bulan


total = total1
if enter :
    st.write("")
    ("======================Bukti Pemesanan==========================")
    ("")
    ("1.Nama Anda = ", nama)
    ('2.No telp =',telp)
    ('3.Lama Sewa = %0.0f bulan ' %bulan)
    ('4.Kosan = ', jenis)
    ('5.Total biaya = %0.0f'% total)
    ('Pemilik kosan akan menghubungi anda, harap simpan bukti ini')
    ("")
    ("=============================================================")
