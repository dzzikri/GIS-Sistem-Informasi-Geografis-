GIS Pertemuan 5 Pembuatan CRUD Data Geospasial


Latar Belakang Masalah :
Dalam Penggunaan Sistem Informasi geografis , masih minimnya pengetahuan mengenai bagaimana cara memanipulasi data CRUD (Create, Retrieve, Update, Delete), pada pertemuan kali ini saya akan menjelaskan bagaimana caranya dengan menggunakan data shapefile geospasial CRUD.

1. Bagaimana cara membuat shapefile?
2. Bagaimana cara mengedit shapefile?
3. Bagaimana cara menghapus shapefile?

Solusi Masalah :
CREATE DATA GEOSPASIAL
Pembuatan data geospasial ini menggunakan libarary pyshp. Untuk membuat data geospasial diperlukan file “namafile”.shp beserta “namafile”.dbf.
Adapun langkahnya adalah sebagai berikut:
1. Import shapefile
2. Instansiasi writer method
Sf = shapefile.Writer(param)
Dimana param disini adalah pilih shapetype:
1. shapeType = 1
2. shapeType = 3
3. shapeType = 5
c. Sama seperti read, kita lakukan metode dbf dan shp.

Untuk Penggunaan Shapefile (shp)
Untuk menambahkan record tergantung dengan type ESRInya.
1. sf.point (x,y)
3. sf.line = (parts: [[x,y],[z,w],...])
5. sf.poly = (parts: [[x,y],[z,w],...])

Untuk Penggunaan Database file (dbf)
Tahapannya adalah sebagai berikut:

a.Membuat atribut dahulu kemudian menambahkan record.
Contoh:
sf.field (‘Nama Filed’,’C’,’40’)
Dimana C adalah Character, dan 40 adalah length. Dalam arti nama atribut, nama field dengan panjang 40 karakter.
b.Tambahkan record dibawah ini
sf.record(‘Bandung’)
sf.record(‘Bandung’,’Sarijadi’)
c.Setelah selesai maka simpan, dengan perintah:
sf.save(‘namafile.shp’)

EDITING DATA GEOSPASIAL
Editor berfungsi untuk melakukan editing pada shapefile. Contohmya delete road. Selain editor ada juga Writer, Writer adalah method di shape file untuk membuat file shp baru (shp dan dbt)
Untuk langkag-langkah dalam melakukan editor sebagai berikut :
Import shape file
Sf = shape file.editor(war.shp)
Sf.point(16,10,0,0)
Sf.record (‘padang’)
Sf.save
Sf.save (‘war.shp’)
a=shapefile.reoder(‘war.shp’)
a.recorders()
a.shapes().points
a.shape()[0]
a.shape()[0] points

[(10,0,10,0)]

DELETE DATA GEOSPASIAL
Sf.delete(0)
a.shapes()[0].points [(10,0,10,0)]
sf.points [16,10,0,0]
sf.record(‘padang’)
sf.saver(‘wr.shp’)


Penutup 
Kesimpulan
jadi pada pertemuan kali ini , kita dapat mengetahui bagaimana cara membuat, mengedit, dan menghapus (CRUD) data geospasial

Saran
Lebih banyak di pelajari lebih dalam lagi, dengan mencari referensi referensi di internet maupun di buku. Serta perbanyak lakukan praktek agar lebih memahami materi kali ini


Nama : Dzikri Ahmad Ghifari
NPM : 1144077
Kelas : 3A
Prodi : D4 Teknik Informatika 
Mata Kuliah : Sistem Informasi Geografis
Link Github : https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-

Referensi :
https://pypi.python.org/pypi/pyshp
https://docs.python.org/3.3/tutorial/datastructures.html

Scan Plagiarisme 
1.	Smallseotools : https://drive.google.com/open?id=0B0ibOfzWLbxrR1duV0R4WWdIWGM
2.	Searchenginereports : https://drive.google.com/open?id=0B0ibOfzWLbxrcDMzZXZjelFyRk

