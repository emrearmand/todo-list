import os

# Inisialisasi list untuk to-do list
todo_list = []

# Fungsi untuk memuat to-do list dari file
def load_todo():
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            for line in file:
                todo_list.append(line.strip())
        print("\nTo-Do List dimuat dari file.")
    else:
        print("\nFile tidak ditemukan, mulai dengan To-Do List kosong.")

# Fungsi untuk menyimpan to-do list ke file
def save_todo():
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")
    print("\nTo-Do List disimpan ke file.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Lihat To-Do List")
    print("2. Tambah To-Do")
    print("3. Hapus To-Do")
    print("4. Keluar")

# Fungsi untuk melihat to-do list
def view_todo():
    if len(todo_list) == 0:
        print("\nTo-Do List kosong.")
    else:
        print("\nDaftar To-Do:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

# Fungsi untuk menambah item ke to-do list
def add_todo():
    task = input("Masukkan tugas baru: ")
    todo_list.append(task)
    print(f'"{task}" ditambahkan ke To-Do List.')
    save_todo()  # Simpan setelah menambah

# Fungsi untuk menghapus item dari to-do list
def delete_todo():
    view_todo()
    try:
        task_num = int(input("Pilih nomor tugas yang ingin dihapus: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f'"{removed_task}" dihapus dari To-Do List.')
            save_todo()  # Simpan setelah menghapus
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor.")

# Main program
load_todo()  # Muat To-Do List dari file saat program dimulai
while True:
    show_menu()
    choice = input("\nPilih opsi (1-4): ")

    if choice == '1':
        view_todo()
    elif choice == '2':
        add_todo()
    elif choice == '3':
        delete_todo()
    elif choice == '4':
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
