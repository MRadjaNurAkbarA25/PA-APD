from function import *
from data import akun

def login():
    clear()
    print('=== LOGIN ===')
    username = input('Username : ').strip()
    password = input('Password : ').strip()

    if username in akun and akun[username]['password'] == password:
        print('Login berhasil!')
        delay()
        return username, akun[username]['role']
    else:
        print('Username atau password salah!')
        delay()
        return None, None

#Register belum selesai
def register():
    clear()
    print('===Daftar Akun===')
    username = input('Masukkan Username: ').strip()
    if not username.isalnum():
        print ('Username hanya boleh huruf dan angka!')
        delay()
        return
    
    if username in akun:
        print('Username sudah digunakan!')
        return
    
    password = input ('Masukkan Password: ').strip()
    if len(password) < 3:
        print ('Password minimal 3 karakter!')
        delay()
        return
    
    konfirmasi = input('Konfirmasi password: ').strip()
    if password != konfirmasi:
        print ('Password tidak cocok!')
        delay()
        return
    
    akun[username] ={'password': password, 'role': 'warga'}
    print ('Akun berhasil didaftarkan sebagai warga!')
    delay()
