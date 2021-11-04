from os import system
import time

#tampilan judul
def judul():
    system('cls')
    print('='*36)
    print('  Mengkonversi Fahrenheit, Kelvin,\n       dan Reamur ke Celcius')
    print('='*36)

#tampilan menu
def menu():
    print('                 MENU')
    print('='*36)
    print(' [1] Fahrenheit ke Celcius')
    print(' [2] Kelvin ke Celcius')
    print(' [3] Reamur ke Celcius')
    print(' [4] Exit')
    print('='*36)
    time.sleep(1)

#tampilan keluar
def exit():
    system('cls')
    print('='*36)
    print('             TERIMA KASIH!')
    print('='*36)
    time.sleep(1)

#fahrenheit ke celcius
def fahrenheit():
    system('cls')
    print('='*36)
    print(' Mengkonversi Fahrenheit ke Celcius')
    print('='*36)
    suhu = float(input(' Masukkan suhu awal: '))
    F = ((9 * suhu)/ 5 + 32)
    print()
    print('='*20)
    print('',suhu,'F', '=', F,'C')
    print('='*20)

    pilihan = str(input('\n (yes/no)\n Ingin menghitung kembali? \n '))
    if pilihan == 'yes' or 'y':
        judul()
        menu()
        pil = int(input(' Masukkan Pilihan: '))
        if pil == 2:
            kelvin()
        elif pil == 3:
            reamur()
    elif pilihan == 'no' or 'n':
        exit()
    time.sleep(1)

#kelvin ke celcius
def kelvin():
    system('cls')
    print('='*36)
    print('   Mengkonversi Kelvin ke Celcius')
    print('='*36)
    suhu = float(input(' Masukkan suhu awal: '))
    K = (suhu + 273.15)
    print()
    print('='*20)
    print('',suhu,'K', '=', K,'C')
    print('='*20)

    pilihan = str(input('\n (yes/no)\n Ingin menghitung kembali? \n '))
    if pilihan == 'yes' or 'y':
        judul()
        menu()
        pil = int(input(' Masukkan Pilihan: '))
        if pil == 1:
            fahrenheit()
        elif pil == 3:
            reamur()
    elif pilihan == 'no' or 'n':
        exit()
    time.sleep(1)

#reamur ke celcius
def reamur():
    system('cls')
    print('='*36)
    print('   Mengkonversi Reamur Ke Celcius')
    print('='*36)
    suhu = float(input(' Masukkan suhu awal: '))
    R = ((5/4) * suhu)
    print()
    print('='*20)
    print('',suhu,'R', '=', R,'C')
    print('='*20)

    pilihan = str(input('\n (yes/no)\n Ingin menghitung kembali? \n '))
    if pilihan == 'yes' or 'y':
        judul()
        menu()
        pil = int(input(' Masukkan Pilihan: '))
        if pil == 1:
            fahrenheit()
        elif pil == 2:
            kelvin()
    elif pilihan == 'no' or 'n':
        exit()
    time.sleep(1)


judul()
menu()

pill = int(input(' contoh (1/2/3)\n Masukkan Pilihan: '))

if pill == 1:
    fahrenheit()
elif pill == 2:
    kelvin()
elif pill == 3:
    reamur()
elif pill == 4:
    exit()
else:
    system('cls')
    print('='*36)
    print('  Mohon maaf menu yang anda pilih\n           tidak tersedia')
    print('='*36)
    time.sleep(2)
    system('cls')
    print('='*36)
    print('       Mohon masukkan pilihan\n            dengan benar')
    print('='*36)