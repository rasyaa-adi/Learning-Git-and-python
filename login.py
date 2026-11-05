### USERNAME & PASSWORD

print("===== SISTEM LOGIN =====")

username = input("USERNAME: ")  # Meminta pengguna memasukan username
username = True

input_password = input("MASUKAN PASSWORD: ") # Meminta pengguna memasukan pasword


if len(input_password) != 6:
    print("Password Harus terdiri dari 6 angka!")
elif  not input_password.isdigit ():
    print("Password hanya berupa angka!")
elif input_password == "":
    print("Password tidak boleh kosong!")
else:
    print("Password benar")

print("========================")

if username and input_password:
    print("Login Berhasil")
else:
    print("Masukan password dengan benar!")






