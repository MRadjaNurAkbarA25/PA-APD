from function import *
from data import *
from warga import *

def ubah_data_petugas():
    print('Ubah laporan')
    
    cari_nomor = input_str('Masukkan nomor laporan yang ingin diubah: ')
    lapor = laporan.get(cari_nomor)
    desk = desc.get(cari_nomor)
    
    if not lapor:
        clear()
        print('Nomor barang tidak ditemukan')
        delay()
        return
    
    while True:
        clear()
        print(f''' Laporan saat ini:
Nomor laporan\t\t: {cari_nomor}
Pelapor\t\t: {lapor['pelapor']}
Keluhan\t\t: {lapor['keluhan']}
Status\t\t: {lapor['status']}
respon\t\t: {lapor['respon']}
Waktu\t\t: {lapor['date']}
Deskripsi\t\t {desk}''')
        
        print('''===MENU UBAH DATA===
1. Ubah keluhan
2. Ubah respon
3. Ubah deskripsi
4. Ubah status
5. Kembali ke menu petugas''')
        
        pilihan = pilih_opsi('Pilih mmenu', 
                            ['1', '2', '3', '4', '5'], 
                            'Pilihan tidak valid!')
        
        if pilihan == '1':
            lapor['keluhan'] = max_input('Keluhan (max 30 karakter):', 30)
            clear()
            print('Laporan berhasil diupdate')