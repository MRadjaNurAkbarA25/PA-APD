from data import *
from datetime import *
from function import *
from colorama import Fore, Style, init
init(autoreset=True)

def lihat_laporan_spesifik(pelapor):
    milik = {k: v for k, v in laporan.items() if v["pelapor"] == pelapor}
    if not milik:
        print(Fore.YELLOW + Style.BRIGHT + "Belum ada laporan.")
        return
    for nomor, data in milik.items():
        print(f"\nLaporan #{nomor}")
        print(f"Pelapor: {data['pelapor']}")
        print(f"Keluhan: {data['keluhan']}")
        print(f"Status: {data['status']}")
        print(f"Respon: {data['respon']}")
        print(f"Tanggal: {data['date']}")
        print(f"Deskripsi: {data['deskripsi']}")
    
def ubah_laporan_warga(pelapor):
    lihat_laporan_spesifik(pelapor)
    cari_nomor = input_str('Masukkan nomor laporan yang ingin diubah: ')
    lapor = laporan.get(cari_nomor)
    
    if not lapor:
        clear()
        print(Fore.RED + Style.BRIGHT + 'Nomor laporan tidak ditemukan!')
        delay()
        return
    
    if lapor['pelapor'] != pelapor:
        clear()
        print(Fore.YELLOW + Style.BRIGHT + 'Anda tidak dapat mengubah laporan ini')
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
2. Ubah deskripsi
3. Kembali ke menu warga''')
        
        pilihan = pilih_opsi('Pilih menu: ', 
                        ['1', '2', '3'])
        
        if pilihan == '1':
            lapor['keluhan'] = max_input('Keluhan (max 30 karakter): ', 30)
            simpan_laporan_ke_csv()
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '2':
            lapor['deskripsi'] = max_input('Deskripsi (max 50 karakter): ', 50)
            simpan_laporan_ke_csv()
            clear()
            print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil diupdate!')
            delay()
        
        elif pilihan == '3':
            return