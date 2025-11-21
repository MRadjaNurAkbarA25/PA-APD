from function import *
from data import *
from warga import *

def ubah_data_petugas():
    print('Ubah laporan')
    
    cari_nomor = input_str('Masukkan nomor laporan yang ingin diubah: ')
    lapor = laporan.get(cari_nomor)
    
    if not lapor:
        clear()
        print('Nomor laporan tidak ditemukan')
        delay()
        return
    
    while True:
        clear()
        print(f''' Laporan saat ini:
Nomor laporan\t\t: {cari_nomor}
Pelapor\t\t: {lapor['pelapor']}
Keluhan\t\t: {lapor['keluhan']}
Status\t\t: {lapor['status']}
Respon\t\t: {lapor['respon']}
Waktu\t\t: {lapor['date']}
Deskripsi\t\t {lapor['deskripsi']}''')
        
        print('''===MENU UBAH DATA===
1. Ubah keluhan
2. Ubah respon
3. Ubah deskripsi
4. Ubah status
5. Kembali ke menu petugas''')
        
        pilihan = pilih_opsi('Pilih menu', 
                            ['1', '2', '3', '4', '5'], 
                            'Pilihan tidak valid!')
        
        if pilihan == '1':
            lapor['keluhan'] = max_input('Keluhan (max 30 karakter): ', 30)
            clear()
            print('Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '2':
            lapor['respon'] = max_input('Respon (max 30 karakter): ', 30)
            clear()
            print('Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '3':
            lapor[cari_nomor] = max_input('Deskripsi (max 50 karakter): ', 50)
            clear()
            print('Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '4':
            print('''===MENU UBAH STATUS===
1. Diajukan
2. Diproses
3. Selesai
4. Kembali''')
            aksi = pilih_opsi('Pilih menu status', ['1', '2',
                            '3', '4'], 'Pilihan tidak valid!')
            if aksi == '1':
                lapor['status'] = 'diajukan'
                print('Status berhasil diubah menjadi diajukan!')
                delay()
            elif aksi == '2':
                lapor['status'] = 'diproses'
                print('Status berhasil diubah menjadi diproses!')
                delay()
            elif aksi == '3':
                lapor['status'] = 'selesai'
                print('Status berhasil diubah menjadi selesai!')
                delay()               
            
        elif pilihan == '5':
            return

def hapus():
    cari_nomor = input_str('Masukkan nomor laporan yang ingin dihapus: ')
    lapor = laporan.get(cari_nomor)
    
    if not lapor:
        clear()
        print('Nomor laporan tidak ditemukan')
        delay()
        return
    
    clear()
    print(f''' Laporan saat ini:
Nomor laporan   : {cari_nomor}
Pelapor         : {lapor['pelapor']}
Keluhan         : {lapor['keluhan']}
Status          : {lapor['status']}
Respon          : {lapor['respon']}
Waktu           : {lapor['date']}
Deskripsi       : {lapor['deskripsi']}''')
    
    konfirmasi = pilih_opsi('Hapus laporan?(y/n)', ['y','n'], 
                            'Pilihan tidak valid!').lower()
    
    if konfirmasi == 'y':
        del laporan[cari_nomor]
        clear()
        print('Laporan berhasil dihapus!')
        delay()
    else:
        clear()
        print('Penghapusan dibatalkan')
        delay()
