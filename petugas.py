from function import *
from data import *
from warga import *
from colorama import Fore, Style, init
init(autoreset=True)

def menu_filter_laporan():
    clear()
    print(Fore.CYAN + Style.BRIGHT + 'Filter Laporan')
    print('''Pilih Filter
1. Diajukan
2. Diproses
3. Selesai
4. Ditolak
5. Semua Laporan
6. Laporan Spesifik
7. Kembali''')
    pilihan = pilih_opsi('Pilih: ', ('1', '2', '3', '4', '5', '6', '7'))
    
    STATUS_MAP = {
        '1' : 'diajukan',
        '2' : 'diproses',
        '3' : 'selesai',
        '4' : 'ditolak'
    }
    
    if pilihan in ('1', '2', '3', '4'):
        status = STATUS_MAP[pilihan]
        hasil = filter_status(status)
        tampil_filter(hasil)
        input('\nEnter untuk kembali...')
    elif pilihan == '5':
        clear()
        print(Fore.CYAN + Style.BRIGHT + '=== DAFTAR LAPORAN ===')
        print(tabel())
        input('\nEnter untuk kembali...')
    elif pilihan == '6':
        clear()
        cari_nomor = input_str('Masukkan nomor laporan yang ingin ditampilkan: ')
        lapor = laporan.get(cari_nomor)
        
        if not lapor:
            clear()
            print(Fore.RED + Style.BRIGHT + 'Nomor laporan tidak ditemukan!')
            delay()
            return
        clear()
        print(f'''Laporan saat ini:
Nomor laporan   : {cari_nomor}
Pelapor         : {lapor['pelapor']}
Keluhan         : {lapor['keluhan']}
Status          : {lapor['status']}
Respon          : {lapor['respon']}
Waktu           : {lapor['date']}
Deskripsi       : {lapor['deskripsi']}''')
        input('\nEnter untuk kembali...')
    elif pilihan == '7':
        return

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
5. Kembali''')
        
        pilihan = pilih_opsi('Pilih menu: ', 
                            ('1', '2', '3', '4', '5'))
        
        if pilihan == '1':
            lapor['keluhan'] = max_input('Keluhan (max 30 karakter): ', 30)
            simpan_laporan_ke_csv()
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '2':
            lapor['respon'] = max_input('Respon (max 30 karakter): ', 30)
            simpan_laporan_ke_csv()
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '3':
            lapor['deskripsi'] = max_input('Deskripsi (max 50 karakter): ', 50)
            simpan_laporan_ke_csv()
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
            aksi = pilih_opsi('Pilih menu status: ', ('1', '2',
                            '3', '4', '5'))
            if aksi == '1':
                lapor['status'] = 'diajukan'
                simpan_laporan_ke_csv()
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '2':
                lapor['status'] = 'diproses'
                simpan_laporan_ke_csv()
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '3':
                lapor['status'] = 'selesai'
                simpan_laporan_ke_csv()
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()
            elif aksi == '4':
                lapor['status'] = 'ditolak'
                simpan_laporan_ke_csv()
                print(Fore.GREEN + Style.BRIGHT + 'Status berhasil diubah!')
                delay()               
            elif aksi == '5':
                continue
            
        elif pilihan == '5':
            return

