#71200644
#Freany usmany
#Universitas Kristen Duta Wacana

#pada hari minggu gereja anugerah mengadakan lomba yaitu perlombaan dipantai
#pada lomba-lomba yang dilakukan terdapat salah satu yang sangat digemari oleh anakl kecil 
# yaitu setiap peserta membuat cangkang kerang berbentuk barisan deret dengan tinggi 5cm dan lebar 3 cm
#buatlah program untuk menampilkan deret seperti diinginkan secara dinamis

panjang=int(input('tinggi:'))
lebar =int(input('lebar:'))
nilai = 1
for p in range (1, panjang+1):
	for x in range(1, lebar+1):
		print(nilai, end='	')
		nilai +=1
	print()

