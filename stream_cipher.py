def xor_encrypt_decrypt(data, keystream):
    return bytes([data[i] ^ keystream[i] for i in range(len(data))])

while True:
    # Menampilkan menu utama
    print("\nMenu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1/2/3): ")
    
    if pilihan == "1":
        # Meminta input plaintext dari pengguna
        plaintext = input("Masukkan teks yang ingin dienkripsi: ").encode()
        # Meminta input keystream dengan panjang yang sama dengan plaintext
        keystream_input = input(f"Masukkan keystream sepanjang {len(plaintext)} karakter: ").encode()
        
        # Validasi panjang keystream harus sama dengan plaintext
        if len(keystream_input) != len(plaintext):
            print("Keystream harus memiliki panjang yang sama dengan plaintext!")
            continue
        
        # Melakukan enkripsi dengan XOR
        encrypted_text = xor_encrypt_decrypt(plaintext, keystream_input)
        # Menampilkan hasil enkripsi dalam format hex
        print("Ciphertext (hex):", encrypted_text.hex())
    
    elif pilihan == "2":
        # Meminta input ciphertext dalam format hex
        encrypted_text = bytes.fromhex(input("Masukkan ciphertext dalam format hex: "))
        # Meminta input keystream dengan panjang yang sama dengan ciphertext
        keystream_input = input(f"Masukkan keystream sepanjang {len(encrypted_text)} karakter: ").encode()
        
        # Validasi panjang keystream harus sama dengan ciphertext
        if len(keystream_input) != len(encrypted_text):
            print("Keystream harus memiliki panjang yang sama dengan ciphertext!")
            continue
        
        # Melakukan dekripsi dengan XOR (XOR dengan keystream yang sama mengembalikan plaintext asli)
        decrypted_text = xor_encrypt_decrypt(encrypted_text, keystream_input)
        # Menampilkan hasil dekripsi sebagai teks
        print("Decrypted Text:", decrypted_text.decode())
    
    elif pilihan == "3":
        # Keluar dari program jika pengguna memilih opsi 3
        print("Keluar dari program.")
        break
    else:
        # Menampilkan pesan jika input tidak valid
        print("Pilihan tidak valid, silakan coba lagi.")
