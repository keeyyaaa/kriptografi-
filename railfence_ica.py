def enkripsi_rail_fence(teks, rel):
    teks = teks.replace(" ", "").upper()
    if rel <= 1: 
        return teks
    
    jalur = [""] * rel
    baris = 0
    arah_turun = True
    
    for karakter in teks:
        jalur[baris] += karakter
        
        # Penentuan arah zig-zag
        if baris == 0:
            arah_turun = True
        elif baris == rel - 1:
            arah_turun = False
            
        baris += 1 if arah_turun else -1
        
    return "".join(jalur)

print("--- Program Rail Fence | Ica Rizqiah ---")
pesan = input("Masukkan plainteks: ")
kunci = int(input("Masukkan jumlah rel (misal: 3): "))

hasil_cipherteks = enkripsi_rail_fence(pesan, kunci)
print(f"\nHasil Cipherteks: {hasil_cipherteks}")