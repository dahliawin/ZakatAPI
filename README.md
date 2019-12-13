# ZakatAPI

Zakat API adalah sebuah Application Programming Interface yang dapat digunakan untuk 
melakukan perhitungan nilai zakat tahunan untuk kategori zakat maal dan zakat penghasilan.
Selain itu, Zakat API juga dapat memberikan informasi lokasi rumah zakat yang ada disekitar
lokasi. Untuk menggunakan API ini, pengguna harus melakukan registrasi terlebih dahulu untuk
mendapatkan API KEY.

Mekanisme penggunaan API:

1. Akses URL registrasi pengguna: https://{url}/registrasi/user={USERNAME}&password={PASSWORD}

2. Akses URL penghitungan zakat maal: https://{url}/zakat=maal&harta={TOTAL_HARTA_TAHUNAN}&key={KEY}

3. Akses URL penghitungan zakat penghasilan: https://{url}/zakat=penghasilan&pendapatan={TOTAL_PENGHASILAN_BULANAN}&pengeluaran={TOTAL_KEBUTUHAN_BULANAN}&key={KEY}

4. Akses URL lokasi lembaga penyalur zakat: https://{url}/lokasi/key={KEY}
