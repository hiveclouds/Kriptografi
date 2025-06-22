import random  # Mengimpor modul random untuk pemilihan acak

# Tabel enkripsi yang memetakan huruf alfabet ke beberapa kemungkinan pengganti (homofon)
table = {
    "A": ["BU", "CP", "AV", "AH", "BT", "BS", "CQ", "1@", "3#"],
    "B": ["AT", "4$", "7%"],
    "C": ["DL", "BK", "AU", "9^", "6&"],
    "D": ["BV", "DY", "DM", "AI", "5*", "8(", "2)"] ,
    "E": ["DK", "CO", "AW", "BL", "AA", "CR", "BM", "CS", "AF", "AG", "BO", "BN", "BE", "0!", "#@"],
    "F": ["BW", "CM", "CN", "$%", "*&"],
    "G": ["DN", "BJ", "!2", "&^"] ,
    "H": ["AS", "CL", "CK", "()", "{%"],
    "I": ["DJ", "BI", "AX", "CJ", "AB", "BP", "CU", "CT", "~`", "=+"] ,
    "J": ["BX", "<>", "|#"] ,
    "K": ["DI", "_-"] ,
    "L": ["AR", "BH", "CI", "AJ", ";:", "?/"],
    "M": ["DH", "BG", "AY", "%^", "&*"] ,
    "N": ["BY", "DG", "DF", "CH", "AC", "BR", "DU", "DT", "[ ]", "\\"] ,
    "O": ["DZ", "BF", "DX", "AK", "CG", "BQ", "DR", "`~", "!@"],
    "P": ["BZ", "DE", "AZ", "<>", ":;"] ,
    "Q": ["DD", "|\\"] ,
    "R": ["AQ", "DC", "DQ", "AL", "CE", "CF", "CV", "DS", "*^", "$#"] ,
    "S": ["AP", "AN", "AO", "CD", "DW", "DV", "(%)", "@!"] ,
    "T": ["CB", "DB", "DP", "CC", "AD", "CY", "CW", "CX", "AE", "+-", "^&"] ,
    "U": ["CA", "AM", "BA", "{{", "!%"] ,
    "V": ["BB", "=>"] ,
    "W": ["CZ", "?/"],
    "X": ["BD", "|*"] ,
    "Y": ["DO", "DA", "`#"] ,
    "Z": ["BC", "@~"],
    " ": ["SP", "ZB"]  # Karakter spasi juga memiliki pengganti
}

# Membalik tabel enkripsi untuk proses dekripsi
reverse_table = {cipher: plain for plain, ciphers in table.items() for cipher in ciphers}

def encrypt(plaintext):
    plaintext = plaintext.upper()  # Mengonversi teks ke huruf besar
    ciphertext = []  # Menyimpan hasil enkripsi
    for char in plaintext:  # Iterasi setiap karakter dalam plaintext
        if char in table:
            ciphertext.append(random.choice(table[char]))  # Pilih acak dari daftar pengganti
        else:
            print("Tidak Valid!")  # Jika karakter tidak ditemukan dalam tabel, tampilkan pesan kesalahan
            print("-------------------")
            return  # Keluar dari fungsi
    return " ".join(ciphertext)  # Gabungkan hasil enkripsi dengan spasi

def decrypt(ciphertext):
    cipher_pairs = ciphertext.split()  # Memisahkan ciphertext berdasarkan spasi
    plaintext = []  # Menyimpan hasil dekripsi
    for pair in cipher_pairs:  # Iterasi setiap pasangan karakter dalam ciphertext
        if pair in reverse_table:
            plaintext.append(reverse_table[pair])  # Ambil huruf asli dari tabel pembalik
        else:
            print("Chipertext salah!")  # Jika pasangan karakter tidak ditemukan, tampilkan pesan kesalahan
            print("-------------------")
            return  # Keluar dari fungsi
    return "".join(plaintext)  # Gabungkan hasil dekripsi menjadi teks asli

if __name__ == "__main__":  # Program utama
    while True:
        print("\n----------------------------------")
        print(" PROGRAM KRIPTOGRAFI HOMOPHONIC ")
        print("------------------------------------")
        print(" CREATE BY KELOMPOK 2 ")
        print("------------------------------------")
        print("\nPilih mode:\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Masukkan pilihan (1/2/3): ").strip()  # Meminta input dari pengguna
        
        if choice == "1":  # Jika memilih enkripsi
            text = input("Masukkan plaintext: ")
            print("Ciphertext:", encrypt(text))  # Panggil fungsi encrypt dan tampilkan hasilnya
        elif choice == "2":  # Jika memilih dekripsi
            text = input("Masukkan ciphertext: ")
            print("Plaintext:", decrypt(text))  # Panggil fungsi decrypt dan tampilkan hasilnya
        elif choice == "3":  # Jika memilih keluar
            print("Keluar dari program.")
            break  # Hentikan loop dan keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Jika input tidak valid
