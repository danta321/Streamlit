import streamlit as st
import requests
import pandas as pd
st.title('Kosan Bersama')
st.write('Menyediakan Kosan untuk di sewa')


def blank () :
    st.write ('Silahkan Pilih Kosan')

def kos4 () :
    st.image('https://www.sewakost.com/files/02-2022/ad75368/kost-petojo-sabangan-696958619_large.jpg')
    st.header('Kosan Tembaga')
    st.write('kamar mandi luar')
    st.write('Sudah termasuk Iuran Air,Listrik,Wifi,Ada Dapur Dikamar')
    st.write('Kasur,Bantal disediakan')
    st.write('harga Rp 300.000/Bulan')


def kos3 () :
    st.image('https://www.sewakost.com/files/03-2021/ad52407/kos-kosan-bebas-aman-dan-2110797795_large.jpg')
    st.header('Kosan Besi')
    st.write('Sudah termasuk Iuran Air,Listrik, dan Wifi')
    st.write('Kamar Mandi Luar,Kasur,Bantal,Almari')
    st.write('harga Rp 400.000/Bulan')

def kos1 () :
    st.image("https://www.sewakost.com/files/03-2020/ad34268/rumah-kost-kosan-damkar-1220752865_large.jpeg")
    st.header('Kosan Berlian')
    st.write("Sudah termasuk Iuran Air,Listrik, dan Wifi")
    st.write("kamar mandi dalam,Almari,Kasur,Meja Belajar")
    st.write("harga Rp 800.000/Bulan")

def kos2 () :
    st.image("https://www.sewakost.com/files/03-2020/ad34268/rumah-kost-kosan-damkar-823273766_large.jpeg")
    st.header('Kosan Emas')
    st.write("Sudah termasuk Iuran Air,Listrik, dan Wifi")
    st.write("kamar mandi Luar,almari,Kasur,AC")
    st.write("harga Rp 750.000/Bulan")

def kos5 () :
    st.image("https://s3.us-east-2.amazonaws.com/dlba-production-bucket/property_images/9425816/aaf0eaa4-3790-4594-8ff2-610040df4896.jpg")
    st.header('Kosan Tembaga')
    st.write('Sudah termasuk Iuran Air, Listrik tidak tersedia')
    st.write('Kamar mandi Luar,Kasur,Kipas tangan')
    st.write('harga Rp 100.000/Bulan')

pages = {
    '': blank,
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


totale = 0

harga = []
kosan = ["",'kos1',"kos2",'kos3','kos4','kos5']


nama = st.text_input('nama penyewa')
telp = st.text_input('nomor telepon')
jenis = st.selectbox('pilih jenis kos',kosan)
bulan = st.number_input('berapa bulan',0)



enter = st.button('Pesan!')

if jenis == "kos1":
    harga = 800000
    totale = harga*bulan
elif jenis == 'kos2':
    harga = 750000
    totale = harga*bulan
elif jenis == "kos3" :
    harga = 400000
    totale = harga*bulan
elif jenis == "kos4" :
    harga = 300000
    totale = harga*bulan
elif jenis == "kos5" :
    harga = 100000
    totale = harga*bulan


total = totale
if enter :
    st.write("")
    st.write("======================Bukti Pemesanan==========================")
    st.write("")
    st.write("1.Nama Anda = ", nama)
    st.write('2.No telpon =',telp)
    st.write('3.Lama Sewa = %0.0f bulan ' %bulan)
    st.write('4.Kosan = ', jenis)
    st.write('5.Total biaya =Rp%0.0f'% total)
    st.write('Pemilik kosan akan menghubungi anda, harap simpan bukti ini')
    st.write("")
    st.write("===============================================================")
