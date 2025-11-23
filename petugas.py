from function import *
from data import *
from warga import *
from colorama import Fore, Style, init
init(autoreset=True)

def ubah_data_petugas():
    print(Fore.CYAN + Style.BRIGHT + 'Ubah laporan')
    print(tabel())
    cari_nomor = input_str('Masukkan nomor laporan yang ingin diubah: ')
    lapor = laporan.get(cari_nomor)
    
    if not lapor:
        clear()
        print(Fore.RED + Style.BRIGHT + 'Nomor laporan tidak ditemukan!')
        delay()
        return
    
    while True:
        clear()
        print(f'''Laporan saat ini:
Nomor laporan   : {cari_nomor}
Pelapor         : {lapor['pelapor']}
Keluhan         : {lapor['keluhan']}
Status          : {lapor['status']}
Respon          : {lapor['respon']}
Waktu           : {lapor['date']}
Deskripsi       : {lapor['deskripsi']}''')
        
        print('''===MENU UBAH DATA===
1. Ubah keluhan
2. Ubah respon
3. Ubah deskripsi
4. Ubah status
5. Kembali ke menu petugas''')
        
        pilihan = pilih_opsi('Pilih menu: ', 
                            ['1', '2', '3', '4', '5'])
        
        if pilihan == '1':
            lapor['keluhan'] = max_input('Keluhan (max 30 karakter): ', 30)
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '2':
            lapor['respon'] = max_input('Respon (max 30 karakter): ', 30)
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '3':
            lapor['deskripsi'] = max_input('Deskripsi (max 50 karakter): ', 50)
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '4':
            print('''===MENU UBAH STATUS===
1. Diajukan
2. Diproses
3. Selesai
4. Ditolak
5. Kembali''')
            aksi = pilih_opsi('Pilih menu status: ', ['1', '2',
                            '3', '4'])
            if aksi == '1':
                lapor['status'] = 'diajukan'
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '2':
                lapor['status'] = 'diproses'
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '3':
                lapor['status'] = 'selesai'
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '4':
                lapor['status'] = 'ditolak'
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()               
            
        elif pilihan == '5':
            return

