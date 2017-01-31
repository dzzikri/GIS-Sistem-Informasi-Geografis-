PENDAHULUAN
Latar Belakang:

Penggunaan Google Maps saat ini sangatlah bermanfaat,baik itu untuk menemukan sebuah daerah,jalan,bangunan,tempat dan lain-lain.Namun apakah anda terbayang untuk dapat membuat “Google Maps” kita sendiri?

ISI:

Jalankan Map Proxy dan Map Server di ubuntu,caranya adalah:

1.Untuk meload data geospasial, anda perlu menyiapkannya dulu agar dapat ditampilkan nantinya di Map Proxy. Anda dapat mendownload data geospasial d http://www.halaman.download/ ,kemudian pilih "Producer" dan klik "Indonesia Mapproxy".
2.Jika sudah di download ekstrak file tersebut (Anda harus mengetahui dimana anda mengekstrak file tersebut, karena path-nya akan digunakan untuk mengedit file yang ada di direktori yang telah di ekstrak tersebut.Disini saya simpan di direktori Downloads (Huruf kecil dan besar harus perhatikan.)
3.Pada file indomap -> mapproxy,  terdapat 3 file. Lalu buka file agm.yaml
4.Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktori dimana anda menyimpan file tersebut :

- pada baris

binary: /usr/libexec/mapserver

ubah menjadi

binary: /usr/lib/cgi-bin/mapserv


- pada baris

map: var/mapdata/mapfile/indo.map

ubah menjadi

map: /home/dzikri/Downloads/indomap/mapfile/indo.map


- Kemudian direktori baru dengan nama tmp pada direktori indomap

ubah baris

working_dir: /var/mapdata/tmp

menjadi

/home/dzikri/Downloads/indomap/tmp (Kemudian Save)

5.Kemudian pada direktori mapproxy(di terminal/cmd), gunakan perintah : vi mapproxy.ini

edit baris

chdir = /var/mymapproxy/

menjadi

chdir = /home/dzikri/Downloads/indomap/mapproxy (Kemudian Save)

6.Edit file config.py pada direktori mapproxy

ubah

application = make_wsgi_app(r'/var/mymapproxy/agm.yaml')

menjadi

application = make_wsgi_app(r'/home/dzikri/Downloads/indomap/mapproxy/agm.yaml') 

7.Untuk menjalankan programnya gunakan perintah : uwsgi mapproxy.ini

8.Untuk mengetahui apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080

9.Klik demo atau ketik localhost:8080/demo

10.Pada bagian WMTS klik di bawah Image Format yaitu png

11.Tunggu beberapa saat karena datanya sedang di load.

12.Map Peta akan muncul


PENUTUP
Kesimpulan

Jadi pada pertemuan kali ini ,kita dapat mengetahui bagaimana cara menjalankan map server dan map proxy di ubuntu.
Saran

Sebaiknya mencari referensi refereni lagi baik dari internet ataupun dari buku agar lebih paham cara kerja map server dan map proxy dan lakukan praktek prakteknya.


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

Smallseotools link : https://drive.google.com/open?id=0B0ibOfzWLbxrM0dZMVhNODRUR28

Duplichecker link : https://drive.google.com/open?id=0B0ibOfzWLbxrR3NMU0p5QXZ3aVk