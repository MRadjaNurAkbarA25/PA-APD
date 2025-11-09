import os
import time
from colorama import Fore, Style

def clear():
    os.system('cls || clear')
    
def delay():
    time.sleep(1)
    
def pilih_opsi(pesan, daftar_valid, pesan_error="Pilihan tidak valid!"):
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
        print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong!")