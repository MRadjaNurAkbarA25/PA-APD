import os
import time
from data import *
from colorama import Fore, Style
from prettytable import PrettyTable

def tabel():
    table = PrettyTable()
    table.field_names = ['No Laporan', 'Pelapor', 'Keluhan', 'Status', 'Respon', 'Waktu']
    
    table.max_width['Keluhan'] = 15
    table.max_width['Respon'] = 15
    table.max_width['Waktu'] = 16
    
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
                    data['status'], 
                    data['respon'], 
                    data['date'],])
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
        print(Fore.RED + Style.BRIGHT + pesan_error)
        delay()
        
def input_str(pesan):
    while True:
        fakta = input(pesan).strip()
        if fakta:
            return fakta
        print(Fore.RED + Style.BRIGHT + 'Input tidak boleh kosong!')