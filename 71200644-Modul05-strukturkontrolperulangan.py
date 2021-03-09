#71200644
#Freany usmany
#Universitas Kristen Duta Wacana

#Freany setiap bulan mengeluarkan uang untuk membeli pakaian,sembako dan keperluan penting lainnya 
# namun freany tidak tau jumlah pengeluaran uang yang selalu ia keluarkan.Buatlah program untuk mengetahui 
# jumlah uang yang uang yang dikeluarkan oleh freany setiap bulannya?

#Input saldo awal : 1000000
#pengeluaran untuk pakaian : 200000
#pengeluaran untuk sembako : 300000

#output: saldo tidak cukup

#proses
saldo= 0
pemasukkan = int(input('Masukkan jumlah saldo: '))
saldo = saldo + pemasukkan
pengeluaran = 0
daftar = []
while True:
    print('''..........................................
silahkan pilih:
1. pengeluaran
2. cek saldo
3. keluar ''')
    a = int(input('Masukkan pilihan:'))
    if a == 1:
        penggunaan = input('Masukkan nama barang: ')
        daftar.append(penggunaan)
        pengeluaran = int(input('Masukkan jumlah uang yang digunakan: '))
        saldo = saldo - pengeluaran
        pengeluaran += pengeluaran
        if saldo >= 0:
            continue 
        else:
            print('Uang anda tidak mencukupi, harap hitung ulang.')
            break
    elif a == 2:
            print(f'Total saldo kamu sekarang : {saldo}')
    elif a == 3:
            print(f'Keperluan sebulan: {daftar}')
            print (f't=Total pengeluaran: {pengeluaran}')
            break 
    else:
            print('pilihan Anda tidak ada, silahkan masukkan ulang.')