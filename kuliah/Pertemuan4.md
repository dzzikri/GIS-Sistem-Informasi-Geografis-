Sistem Informasi Geeografis Pertemuan 4

Latar Belakang Masalah :

Dalam pengaplikasian dari Sistem Informasi geografis , masih minimnya pengetahuan mengenai cara memanipulasi data retrieve(meliahat data/menghitung jumlah data), pada pembahasan kali ini saya akan menjelaskan bagaimana caranya dengan menggunakan data shapefile geospasial dan bahasa pemrograman python dan juga cara penggunaan class dan method

    Apa itu Retrieve Data?
    Apa itu Shapefile?
    Apa itu Geometri?
    Bagaimana Operasi Pengambilan Data?
    Buatlah Class Geospatial Editor?
    Buat Method Select, Where Negara?

Isi:

Retrieve data geospasial adalah meretrieve data vector

            - Data shapefile.shp

            - Operasi retrieve data menggunakan library python yang bernama py.shp

Shapefile : standar file

vector geospasial dikeluarkan oleh ESRI
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/shp.JPG


Geometri

Data koordinat yang membentuk bangun datar/ruang diantaranya:
* 1. Point/titik [1]
* 2. Line/garis [3] Shape,type
* 3. Polygon [5]

Inilah yang oleh ESRI disebut shapetype memiliki nomor standar


Operasi Pengambilan Data Library pyshp class shapefile
* 1. Buka/baca

* 2. 
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/keterangan.JPG


SHP
* Method :
* shapes() - Menampilkan semua
* shape(n) - Menampilkan dengan parameter
* 1. bbox
* 2. parts
* 3. point s 
* 4. shape type

Akses menggunakan method .(titik)

 

DBF
* Method :
* fields = nama fields
* record(n)
* Record (n) baris ke (n) records
* Akses menggunakan [ ]
* n adalah nomor sequence record

 

bbox
* bording box, merupakan batas view peta.
* contohnya :
* https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/bbox.JPG
* Koordinat a,b,c,d itu di sebut bbox

parts
* part ialah apakah record ini bagian dari record lainnya/pecahan record

points
* koordinat pembentuk peta

shapetype
* jenis geometri dari points



Praktek

Menampilkan jumlah record melalui CMD
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/menampilkan%20jmlh%20record1.JPG


Menampilkan jumlah record dengan menggunakan pyshp
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/file2.JPG
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/menampilkan%20file%20pyshp.JPG


Menampilkan urutan record dengan menggunakan class geospasial editor
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/class%20geospasial%20editor.JPG


Buat Method Select, Where Negara Indonesia
https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-/blob/master/img/melihat%20select%20where%20negara.JPG



Penutup
Kesimpulan
jadi pada pertemuan kali ini , kita dapat mengetahui bagaimana cara membuat class dan penggunaan method method yang terdapat pada retrieve data

Saran
Harus lebih banyak melakukan praktek di kelas agar melatih mahasiswa supaya lebih memahami materi kali ini



Nama : Dzikri Ahmad Ghifari

NPM : 1144077

Kelas : D4 TI 3A

Prodi : D4 Teknik Informatika

Mata Kuliah : Sistem Informasi Geografis


Link Github : https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-


Referensi : https://pypi.python.org/pypi/pyshp ?
https://docs.python.org/3.3/tutorial/datastructures.html


Scan Plagiarisme

    Duplichecker : https://drive.google.com/open?id=0B0ibOfzWLbxrV09DbzlNY3RkQ0U
    Searchenginereport : https://drive.google.com/open?id=0B0ibOfzWLbxrZjBjWElHS2VN
