import csv
import os
import time
from data import akun, laporan  
from colorama import Fore, Style
from prettytable import PrettyTable
from datetime import datetime

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

def clear():
    os.system('cls || clear')
    
def delay():
    time.sleep(1)
    
def pilih_opsi(pesan, daftar_valid, pesan_error='Pilihan tidak valid!'):
    while True:
        pilihan = input(pesan).strip()
        if pilihan in daftar_valid:
            return pilihan
        print(pesan_error)
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
            print('Tidak boleh kosong!')
        elif len(teks) > max_len:
            print(f'Tidak boleh lebih dari {max_len} karakter!')
        else:
            return teks

def buat_laporan(pelapor):
    nomor = str(len(laporan) + 1).zfill(4)
    keluhan = max_input('Keluhan (max 30 karakter): ', 30)
    deskripsi = max_input('Deskripsi (max 50 karakter): ', 50)
    
    laporan[nomor] = {
        'pelapor' : pelapor,
        'keluhan' : keluhan,
        'deskripsi': deskripsi,
        'status' : 'Diajukan',
        'respon' : '',
        'date' : datetime.now().strftime('%d/%m/%y %H:%M')
    }
    
    print(f'Laporan #{nomor} berhasil dibuat!')
    simpan_laporan_ke_csv()  

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
    global akun, laporan

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
            "hitler": {"password": "ganteng", "role": "ketua_rt"},
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