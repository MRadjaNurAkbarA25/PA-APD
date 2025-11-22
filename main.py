from function import *
from auth import *
from data import akun
from menu import *
from colorama import Fore, Style

clear()
while True:
    user_login = None
    print(f'''=== SELAMAT DATANG DI LAPOR AJA!!!===
Laporkan keluhan anda, lalu petugas akan menanganinya!
Silahkan login untuk lanjut
1. Login
2. Register
3. Keluar Program''')

    pilihan = pilih_opsi('Pilih opsi: ', ['1', '2', '3'], 'Pilihan tidak valid!')
    
    if pilihan == '1':
        if user_login:
            print('Anda sudah login!')
            delay()
        else:
            username, role = login()
            if username:
                    user_login = (username, role)
                    if role == "petugas":
                        menu_petugas(username)
                    else:
                        menu_warga(username)
                    user_login = None
    elif pilihan == '2':
        clear()
        register()
    
    elif pilihan == '3':
        clear()
        print('Terima kasih telah menggunakan LAPOR AJA!!!')
        delay()
        exit()    