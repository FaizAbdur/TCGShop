# Tugas2PBP
Tugas 2 pembuatan MVT TCG 


Nama    : Faiz Abdurrachman 

NPM     : 2201233210
     
Kelas   : PBP B


Link Adaptable : 


Jawaban Pertanyaan : 

MVC (Model-View-Controller):

Model       :       Menangani data dan logika bisnis.
View        :       Menampilkan data kepada pengguna.
Controller  :       Mengatur interaksi antara Model dan View.

MVT (Model-View-Template):

Model       :       Dibanding MVC model-nya lebih difokuskan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasiny
View        :       Menampilkan data kepada pengguna.
Template    :       Mengatur tampilan HTML dan logika presentasi.

MVVM (Model-View-ViewModel):    

Model       :       Menangani data dan logika bisnis.
View        :       Menampilkan data kepada pengguna.
ViewModel   :       Memproses data dari Model agar sesuai dengan kebutuhan tampilan yang diatur oleh View.

Perbedaan utama adalah bagaimana mereka mengatur interaksi antara komponen-komponen ini, dengan MVC menggunakan Controller, MVT menggunakan Template, dan MVVM menggunakan ViewModel. Pilihan tergantung pada kebutuhan aplikasi dan preferensi pengembang.

Kaitan antara berkas dalam aplikasi web Django:

urls.py: Mengatur URL dan mengarahkan permintaan klien ke fungsi atau kelas tampilan di views.py.
views.py: Berisi logika bisnis, mengambil data dari models.py, dan mengembalikan respons, seringkali dalam bentuk halaman HTML.
models.py: Mendefinisikan struktur data dan relasi database yang digunakan oleh aplikasi.
Berkas HTML: Digunakan untuk menghasilkan tampilan yang diberikan kepada pengguna, seringkali dengan menggunakan data dari model.

Mengapa menggunakan virtual environment (lingkungan virtual):

Memungkinkan isolasi proyek Python, menghindari konflik antar-paket, dan memastikan penggunaan versi paket yang sesuai untuk setiap proyek.
Meskipun mungkin memungkinkan, sangat disarankan untuk menggunakan virtual environment saat mengembangkan aplikasi web Django untuk manajemen yang lebih baik dan kebersihan kode.