from function import *
from data import laporan, akun
from auth import *
from colorama import Fore, Style, init
init(autoreset=True)

def statistik():
    clear()
    status_list = [data['status'].lower() for data in laporan.values()]
    unique = set(status_list)
    print(Fore.CYAN + Style.BRIGHT + '=== STATISTIK LAPORAN ===')
    for status in sorted(unique):
        jumlah = status_list.count(status)
        print(f'{status}: {jumlah}')
    delay()
    input('\nEnter untuk kembali...')
    clear()

def ekspor():
    import csv
    nama_file = input('Nama file (tanpa .csv): ').strip()
    if not nama_file:
        nama_file = 'laporan_rt'
    try:
        with open(f'{nama_file}.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['No', 'Pelapor', 'Keluhan', 'Deskripsi', 'Status', 'Respon', 'Waktu'])
            for no, data in laporan.items():
                writer.writerow([
                    no,
                    data['pelapor'],
                    data['keluhan'],
                    data['deskripsi'],
                    data['status'],
                    data['respon'],
                    data['date']
                ])
        print(Fore.GREEN + Style.BRIGHT + f'Laporan diekspor ke {nama_file}.csv')
    except Exception as e:
        print(Fore.YELLOW + Style.BRIGHT + f'Gagal: {e}')
    delay()

def ubah_role(pelapor):
    print(tabul())
    target = input_str('Masukkan username yang rolenya ingin diubah: ')
    if target == pelapor:
        print(Fore.RED + Style.BRIGHT + 'Tidak bisa ubah akun sendiri!')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return
    if target not in akun:
        print(Fore.RED + Style.BRIGHT + 'Akun tidak ditemukan!')
        delay()
        return
    print('1. Warga\n2. Petugas')
    role_pilih = pilih_opsi('Role baru: ', ['1','2'])
    role_map = {'1': 'warga', '2': 'petugas'}
    
    konfirmasi = pilih_opsi(f'Ganti role {target}? (y/n): ', ['y','n']).lower()
    if konfirmasi == 'y':
        akun[target]['role'] = role_map[role_pilih]
        simpan_akun_ke_csv()
        print(Fore.GREEN + Style.BRIGHT + f'Role {target} berhasil diubah!')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return
    else:
        print(Fore.YELLOW + Style.BRIGHT + 'Perubahan dibatalkan')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return

def hapus_akun(pelapor):
    print(tabul())
    target = input_str('Username dari akun yang ingin dihapus: ')
    if target == pelapor:
        print(Fore.RED + Style.BRIGHT + 'Tidak bisa hapus akun sendiri!')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return
    if target not in akun:
        print(Fore.RED + Style.BRIGHT + 'Akun tidak ditemukan!')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return
    konfirmasi = pilih_opsi(f'Hapus {target}? (y/n): ', ['y','n']).lower()
    if konfirmasi == 'y':
        del akun[target]
        simpan_akun_ke_csv()
        print(Fore.GREEN + Style.BRIGHT + f'Akun {target} berhasil dihapus!')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return
    else:
        print(Fore.YELLOW + Style.BRIGHT + 'Penghapusan Dibatalkan')
        delay()
        input('\nEnter untuk kembali...')
        clear()
        return