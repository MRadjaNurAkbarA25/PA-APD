import csv
import os
import time
from data import akun, laporan  
from colorama import Fore, Style, init
from prettytable import PrettyTable
from datetime import datetime
init(autoreset=True)

def cyan(pesan, jumlah):
    warna = (Fore.CYAN + Style.BRIGHT + pesan * int(jumlah) )
    print(warna)
    
def clear():
    os.system('cls || clear')
    
def delay():
    time.sleep(1)
    
def tabel():
    table = PrettyTable()
    table.field_names = ['No Laporan', 'Pelapor', 'Keluhan', 
                        'Deskripsi', 'Status', 'Respon', 'Waktu']
    
    table.max_width['Keluhan'] = 15
    table.max_width['Respon'] = 15
    table.max_width['Waktu'] = 16
    table.max_width['Deskripsi'] = 16
    
    table.align['No Laporan'] = 'c'
    table.align['Pelapor'] = 'l'
    table.align['Keluhan'] = 'l'
    table.align['Status'] = 'l'
    table.align['Respon'] = 'l'
    table.align['Waktu'] = 'c'
    
    for item, data in laporan.items():
        table.add_row([item, 
                    data['pelapor'], 
                    data['keluhan'],
                    data['deskripsi'],
                    data['status'], 
                    data['respon'], 
                    data['date']])
    return table

def tabul():
    kotak= PrettyTable()
    kotak.field_names = ['Username', 'Role']
    
    kotak.max_width['Username'] = 15
    kotak.max_width['Role'] = 12
    
    kotak.align['Username'] = 'c'
    kotak.align['Role'] = 'c'
    
    for username, role in akun.items():
        kotak.add_row([username, role['role']])
    return kotak 
    
def pilih_opsi(pesan, daftar_valid, pesan_error='Pilihan tidak valid!'):
    while True:
        pilihan = input(pesan).strip()
        if pilihan in daftar_valid:
            return pilihan
        print(Fore.RED + Style.BRIGHT + pesan_error)
        delay()
        
def input_str(pesan):
    while True:
        fakta = input(pesan).strip()
        if fakta:
            return fakta
        print(Fore.RED + Style.BRIGHT + 'Input tidak boleh kosong!')

def max_input(pesan, max_len):
    while True:
        teks = input(pesan).strip()
        if teks == '':
            print(Fore.RED + Style.BRIGHT + 'Tidak boleh kosong!')
        elif len(teks) > max_len:
            print(Fore.RED + Style.BRIGHT + f'Tidak boleh lebih dari {max_len} karakter!')
        else:
            return teks

def filter_status(status):
    hasil = {}
    for nomor, data in laporan.items():
        if data['status'].lower() == status.lower():
            hasil[nomor] = data 
    return hasil

def tampil_filter(laporan_filter):
    if not laporan_filter:
        print(Fore.YELLOW + Style.BRIGHT + 'Tidak ada laporan dengan status tersebut!')
        return
    table = PrettyTable()
    table.field_names = ['No Laporan', 'Pelapor', 'Keluhan', 
                        'Deskripsi', 'Status', 'Respon', 'Waktu']
    
    table.max_width['Keluhan'] = 15
    table.max_width['Respon'] = 15
    table.max_width['Waktu'] = 16
    table.max_width['Deskripsi'] = 16
    
    table.align['No Laporan'] = 'c'
    table.align['Pelapor'] = 'l'
    table.align['Keluhan'] = 'l'
    table.align['Status'] = 'l'
    table.align['Respon'] = 'l'
    table.align['Waktu'] = 'c'
    
    for item, data in laporan_filter.items():
        table.add_row([item, 
                    data['pelapor'], 
                    data['keluhan'],
                    data['deskripsi'],
                    data['status'], 
                    data['respon'], 
                    data['date']])
    print(table)
    print(Fore.CYAN + f' Total: {len(laporan_filter)} laporan ditemukan')

def buat_laporan(pelapor):
    if laporan:
        nomor_terakhir = max(int(k) for k in laporan.keys())
        nomor = str(nomor_terakhir + 1).zfill(4)
    else:
        nomor = '0001'
    keluhan = max_input('Keluhan (max 30 karakter): ', 30)
    deskripsi = max_input('Deskripsi (max 50 karakter): ', 50)
    
    laporan[nomor] = {
        'pelapor' : pelapor,
        'keluhan' : keluhan,
        'deskripsi': deskripsi,
        'status' : 'diajukan',
        'respon' : '',
        'date' : datetime.now().strftime('%d/%m/%y %H:%M')
    }
    
    print(f'Laporan #{nomor} berhasil dibuat!')
    simpan_laporan_ke_csv() 

def hapus_laporan():
    print(tabel())
    cari_nomor = input_str('Masukkan nomor laporan yang ingin dihapus: ')
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
    
    konfirmasi = pilih_opsi('Hapus laporan?(y/n): ', ('y','n')).lower()
    
    if konfirmasi == 'y':
        del laporan[cari_nomor]
        clear()
        simpan_laporan_ke_csv()
        print(Fore.GREEN + Style.BRIGHT + 'Laporan berhasil dihapus!')
        delay()
    else:
        clear()
        print(Fore.YELLOW + Style.BRIGHT + 'Penghapusan dibatalkan')
        delay()

def logout():
    clear()
    kembali = pilih_opsi('Konfirmasi log-out?(y/n): ', ('y', 'n')).lower()
    
    if kembali == 'y':
        clear()
        print(Fore.CYAN + Style.BRIGHT + 'Kamu menekan tombol log-out!')
        delay()
        return True
    elif kembali == 'n':
        print(Fore.YELLOW + Style.BRIGHT + 'Log-out dibatalkan')  
    delay()
    return False

def keluar(): #Fungsi untuk keluar dari program
    clear()
    while True:
        konfirmasi = pilih_opsi('Yakin ingin keluar dari program?(y/n): ', ('y', 'n')).lower()
        
        if konfirmasi == 'y':
            clear()
            simpan_semua()
            print(Fore.CYAN + Style.BRIGHT + '=' * 45)
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 'Terima kasih telah menggunakan LAPORIN AJA!!!')
            print(Fore.CYAN + Style.BRIGHT + '=' * 45)
            delay()
            exit()
        elif konfirmasi == 'n':
            print('Kembali ke program')
            delay()
            clear()
            return

def simpan_akun_ke_csv():
    with open('akun.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'password', 'role'])
        for username, data in akun.items():
            writer.writerow([username, data['password'], data['role']])

def simpan_laporan_ke_csv():
    with open('laporan.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nomor', 'pelapor', 'keluhan', 'deskripsi', 'status', 'respon', 'waktu'])
        for nomor, data in laporan.items():
            writer.writerow([
                nomor,
                data['pelapor'],
                data['keluhan'],
                data['deskripsi'],
                data['status'],
                data['respon'],
                data['date']
            ])

def simpan_semua():
    simpan_akun_ke_csv()
    simpan_laporan_ke_csv()

def muat_data_dari_csv():

    if os.path.exists('akun.csv'):
        with open('akun.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            akun_default = {}
            for row in reader:
                akun_default[row['username']] = {
                    'password': row['password'],
                    'role': row['role']
                }
    else:
        akun_default = {
            "adit": {"password": "002", "role": "ketua_rt"},
            "radja": {"password": "012", "role": "petugas"},
            "denny": {"password": "011", "role": "warga"}
        }
        with open('akun.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['username', 'password', 'role'])
            for user, data in akun_default.items():
                writer.writerow([user, data['password'], data['role']])

    if os.path.exists('laporan.csv'):
        with open('laporan.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            laporan_baru = {}
            for row in reader:
                laporan_baru[row['nomor']] = {
                    'pelapor': row['pelapor'],
                    'keluhan': row['keluhan'],
                    'deskripsi': row['deskripsi'],
                    'status': row['status'],
                    'respon': row['respon'],
                    'date': row['waktu']
                }
    else:
        laporan_baru = {}
        with open('laporan.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['nomor', 'pelapor', 'keluhan', 'deskripsi', 'status', 'respon', 'waktu'])


    akun.clear()
    akun.update(akun_default)
    laporan.clear()
    laporan.update(laporan_baru)