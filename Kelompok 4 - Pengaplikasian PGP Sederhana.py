import pgpy

# Fungsi untuk membuat key pair
def generate_keypair(name, email):
    key = pgpy.PGPKey.new(pgpy.constants.PubKeyAlgorithm.RSAEncryptOrSign, 2048)
    uid = pgpy.PGPUID.new(name, email=email)
    key.add_uid(uid,
                usage={pgpy.constants.KeyFlags.Sign, pgpy.constants.KeyFlags.EncryptCommunications},
                hashes=[pgpy.constants.HashAlgorithm.SHA256],
                ciphers=[pgpy.constants.SymmetricKeyAlgorithm.AES256],
                compression=[pgpy.constants.CompressionAlgorithm.ZLIB])
    return key

# Fungsi untuk enkripsi pesan
def encrypt_message(message, pubkey):
    msg = pgpy.PGPMessage.new(message)
    encrypted = pubkey.encrypt(msg)
    return str(encrypted)

# Fungsi untuk dekripsi pesan
def decrypt_message(encrypted_message, privkey, passphrase=None):
    encrypted = pgpy.PGPMessage.from_blob(encrypted_message)
    with privkey.unlock(passphrase):
        decrypted = privkey.decrypt(encrypted)
    return decrypted.message

# Contoh penggunaan
if __name__ == "__main__":
    print("Membuat key pair...")
    key = generate_keypair("User", "user@example.com")
    pubkey = key.pubkey
    privkey = key

    pesan = input("\nMasukkan pesan yang ingin dienkripsi: ")
    print("\nPesan asli:", pesan)

    print("\nMengenkripsi pesan...")
    encrypted = encrypt_message(pesan, pubkey)
    print("\nPesan terenkripsi:\n", encrypted)

    print("\nMendekripsi pesan...")
    decrypted = decrypt_message(encrypted, privkey)
    print("\nPesan setelah dekripsi:", decrypted)
