Latar Belakang Masalah :

Dalam pemanfaatan di bidang geografis pada sistem digital ada berbagai macam cara, bahkan sudah sampai ada yang menyediakan map yang dapat kita custom sesuai dengan keinginan kita. yaitu "Google Maps". Siapa yang tidak tahu google maps? Penggunaannya di Indonesia maupun dunia sudah menjadi kebutuhan pokok banyak orang, tetapi apakah kalian tahu bahwa kita dapat membuat Maps Custom kita sendiri?

1. Apa itu Map Proxy?
2. Apa itu Map Server?
3. Bagaimana cara install Map Proxy?
4. Bagaimana cara install Map Server?

Solusi Masalah :

- Map Server adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG). MapServer dikembangkan oleh University of Minnesota - jadi, sering dan lebih khusus disebut sebagai "UMN MapServer", untuk membedakannya dari komersial "peta server". MapServer awalnya dikembangkan dengan dukungan dari NASA, yang membutuhkan cara untuk membuat citra satelit yang tersedia untuk umum.

- Map Proxy (mapproxy.org) adalah open source ubin geospasial proxy yang mendukung proyeksi ulang. Awalnya dikembangkan oleh Omniscale Mapproxy adalah server proxy python untuk gambar geospasial. Hal ini dapat membaca data dari WMS, ubin, mapserver dan mapnik, dan cache dan melayani data bahwa sebagai WMS, WMTS, TMS dan KML. Hal ini juga dapat melakukan reprojections antara berbagai sistem koordinat referensi

Installasi Map server & map proxy
Menggunakan Linux Ubuntu 
1. Persiapkan terlebih dahulu sistem operasi ubuntu (bisa menggunakan versi linux yang lain, karena perintahnya kurang lebih sama). 
2. Buka terminal kemudian ketik perintah : sudo apt-get install cgi-mapserver 
3.Untuk mengetahui struktur direktori Map Server, gunakan perintah : dpkg -L cgi-mapserver 
4. Karena saya mengeksekusinya menggunakan python, install python dengan perintah: sudo apt-get install python-pip python-dev
5. Kemudian install uwsgi, dengan perintah : sudo pip install uwsgi
6. Kemudian install Map Proxy, dengan perintah :sudo pip install MapProxy 

Penutup
Kesimpulan
jadi pada pertemuan kali ini , kita dapat mengetahui bagaimana cara menginstall map server dan map proxy di dalam sistem operasi ubuntu.

Saran
Lebih banyak di pelajari lag mengenai materi inii, dengan mencari referensi referensi di internet maupun di buku dan juga melakukan praktek praktek agar lebih memahami materi kali ini.



Nama : Dzikri Ahmad Ghifari
NPM : 1144077
Kelas : 3A
Prodi : D4 Teknik Informatika 
Mata Kuliah : Sistem Informasi Geografis
Link Github : https://github.com/dzzikri/GIS-Sistem-Informasi-Geografis-

Referensi :
https://mapproxy.org/
https://dennycharter.wordpress.com/2008/05/09/cara-kerja-mapserver/

Scan Plagiarisme

    Smallseotools link : https://drive.google.com/open?id=0B0ibOfzWLbxrb3F2c1lnLUVxZ0E
    Duplichecker link : https://drive.google.com/open?id=0B0ibOfzWLbxrU29lMDNSOTJIcDQ 