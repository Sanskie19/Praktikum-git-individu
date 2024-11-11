#NAMA : MUHAMMAD IHSAN ANSORI
#NIM : 2400409
#KELAS : RPL 1C

def menu_login():
    username = "Daspro2023"
    password_benar = "Latihan"
    
    kesempatan = 3
    
    print("Selamat datang di menu login!")
    print(f"Username: {username}")
    
    while kesempatan > 0:
        password_input = input("Masukkan password: ")
        
        if password_input == password_benar:
            print("Login berhasil! Selamat datang.")
            return 
        else:
            kesempatan -= 1
            print(f"Password salah. Anda memiliki {kesempatan} kesempatan tersisa.")
    
    print("Anda telah memasukkan password yang salah sebanyak 3 kali. Akses ditolak.")

menu_login()
print("hello world")