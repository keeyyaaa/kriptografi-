import codecs

def proses_rot13(teks):
    # Menggunakan library bawaan Python khusus untuk ROT13
    return codecs.encode(teks, 'rot_13')

print("--- Program ROT13 Cipher | Ica Rizqiah ---")
pesan = input("Masukkan teks: ")

sandi = proses_rot13(pesan)
print(f"\nTeks Tersandi: {sandi}")
print(f"Teks Kembali : {proses_rot13(sandi)}")