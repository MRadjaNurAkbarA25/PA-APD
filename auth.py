from function import *
from data import akun
from colorama import Fore, Style, init
init(autoreset=True)

def login():
    clear()
    print(Fore.CYAN + Style.BRIGHT + '=== LOGIN ===')
    username = input('Username : ').strip()
    password = input('Password : ')

    if username in akun and akun[username]['password'] == password:
        print(Fore.GREEN + Style.BRIGHT + 'Login berhasil!')
        delay()
        return username, akun[username]['role']
    else:
        print(Fore.RED + Style.BRIGHT + 'Username atau password salah!')
        delay()
        return None, None

def register():
    clear()
    print(Fore.CYAN + Style.BRIGHT + '===SIGN IN===')
    username = input('Masukkan Username: ').strip()
    
    if not username:
        print(Fore.RED + Style.BRIGHT + 'Username tidak boleh kosong!')
        delay()
        return
    if len(username) < 3 or len(username) > 20:  
        print(Fore.RED + Style.BRIGHT + 'Username harus 3-20 karakter!')
        delay()
        return
    if not username.isalnum():
        print (Fore.RED + Style.BRIGHT + 'Username hanya boleh huruf dan angka!')
        delay()
        return
    if username in akun:
        print(Fore.RED + Style.BRIGHT + 'Username sudah digunakan!')
        delay()
        return
    
    password = input ('Masukkan Password: ')
    if len(password) < 3:
        print (Fore.RED + Style.BRIGHT + 'Password minimal 3 karakter!')
        delay()
        return
    while True:
        konfirmasi = input('Konfirmasi password: ').strip()
        if password != konfirmasi:
            print (Fore.RED + Style.BRIGHT + 'Password tidak cocok!')
            delay()
            continue
        else:
            akun[username] ={'password': password, 'role': 'warga'}
            print (Fore.GREEN + Style.BRIGHT + 'Akun berhasil didaftarkan!')
            simpan_akun_ke_csv()
            delay()
            clear()
            return