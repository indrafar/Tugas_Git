data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1000,
            'jagung': 1200,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}
print("Semua Data Panen")
for lokasi, data in data_panen.items():
    print(f"{data['nama_lokasi']} - Hasil Panen: {data['hasil_panen']}")

jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah Hasil Panen Jagung dari Lokasi 2: {jumlah_jagung_lokasi2}")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama Lokasi dari Lokasi 3: {nama_lokasi3}")

jumlah_padi = {lokasi : data ['hasil_panen']['padi']for lokasi, data in data_panen.items()}
jumlah_kedelai = {lokasi : data ['hasil_panen']['kedelai']for lokasi, data in data_panen.items()}

print('\nJumlah Hasil Panen Padi per lokasi:', jumlah_padi)
print('\nJumlah Hasil Panen Kedelai per lokasi:', jumlah_kedelai)

print('\nKondisi lokasi:')
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    kondisi = "Memerlukan perhatian khusus" if padi > 1300 or jagung > 800 else "Dalam kondisi baik"
    print(f"data['nama_lokasi']: {kondisi}")