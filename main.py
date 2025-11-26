from function import *
from ketua import *
from auth import *
from menu import *
from data import *
from colorama import Fore, Style, init
init(autoreset=True)

muat_data_dari_csv()

while True:
    clear()
    user_login = None
    cyan('=', '36')
    print(Fore.CYAN + Style.BRIGHT + f'| SELAMAT DATANG DI LAPORIN AJA!!! |')
    cyan('=', '36')
    print(Fore.CYAN + 'Laporkan keluhan anda, lalu petugas akan menanganinya!')
    print('''Silahkan login untuk lanjut
1. Login
2. Register
3. Keluar Program''')
    pilihan = pilih_opsi('Pilih opsi: ', ('1', '2', '3'))
    
    if pilihan == '1':
        if user_login:
            print(Fore.YELLOW + 'Anda sudah login!')
            delay()
        else:
            username, role = login()
            if username:
                    user_login = (username, role)
                    if role == "petugas":
                        menu_petugas(username)
                    elif role == "ketua_rt":
                        menu_ketua_rt(username)
                    else:
                        menu_warga(username)
                    user_login = None
    elif pilihan == '2':
        clear()
        register()
    elif pilihan == '3':
        keluar()
