import string

def cipher_caesar(teks, shift, mode='enkripsi'):
    abjad_kecil = string.ascii_lowercase
    abjad_besar = string.ascii_uppercase
    hasil = []
    
    if mode == 'dekripsi':
        shift = -shift
        
    for char in teks:
        if char in abjad_kecil:
            idx = (abjad_kecil.index(char) + shift) % 26
            hasil.append(abjad_kecil[idx])
        elif char in abjad_besar:
            idx = (abjad_besar.index(char) + shift) % 26
            hasil.append(abjad_besar[idx])
        else:
            hasil.append(char)
    return "".join(hasil)

print("--- Program Caesar Cipher | Ica Rizqiah ---")
pesan = input("Masukkan pesan: ")
kunci = int(input("Masukkan kunci (angka): "))

terenkripsi = cipher_caesar(pesan, kunci, 'enkripsi')
print(f"\nHasil Enkripsi: {terenkripsi}")
print(f"Hasil Dekripsi: {cipher_caesar(terenkripsi, kunci, 'dekripsi')}")