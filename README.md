# Tugas2PBP
Tugas 2 pembuatan MVT TCG 


Nama    : Faiz Abdurrachman 

NPM     : 2201233210
     
Kelas   : PBP B


Link Adaptable : 


Jawaban Pertanyaan : 

1. Penjelasan setiap projek Django : 
    # cek box 1 
    Proses dimulai dengan pertama membuat proyek Django baru, pertama yang dilakukan adalah membuat sebuah repositori git baru untuk menampung proyek aplikasi django. Setelah selesai men-setup repositori di lokal dan di git mulai dengan install Django, karena Django sudah terinstall maka dimulai dengan inisiasi Proyek Django. Ini dimulai dengan membuat direktori dimana aplikasi akan dibuat dan mengaktifkan Virtual Enviroment di Folder tersebut. Setelah itu install dependencies, jika sudah bisa mulai dengan mengaktifkan startproject di command shell

    # cek box 2 
    membuat aplikasi baru bernama main dengan menjalankan command startapp main.  Setelah itu saat sudah dicek bahwa di folder terdapat folder bernama main masukkan main ke installed apps agar aplikasi dapat dibaca oleh django, setelah itu kita membuat direktori baru bernama templates dalam folder yang berisi direktori main dan di direktori template kita membuat main.HTML yang menjadi pengaturan tampilan HTML dan logika presentasi 
    
    # cek box 3
    untuk menghubungkan rute url terhadap agar perubahan pada main terlihat kita perlu setup pathingnya di urls.py yang kita akan buat di direktori main 

    # cek box 4
    Kita dapat membuat model pada aplikasi main dengan cara mengubahnya di models.py dan sesuai dengan ketentuan kita membuat dalam bentuk 
    
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    sesuai dengan ketentuan terdapat name amount dan description yang masing masing bersisi charfield, IntegerField, dan TextField

    # cek box 5
    Untuk menentukan fungsi di views untuk dikembalikan ke dalam sebuah template HTML kita membuat dictionary yang berisi data-data yang sesuai kita isi yang akan ditampilkan. di sana terdapat 3 konteks yaitu nama,class,dan title,dimana itu adalah data nama,data kelas,data title. dibawahnya terdapat line return render dan main.HTML yang berarti dia akan merender tampilannya di template main.HTML. Setelah itu di Main.HTML diubah agar output nama dan kelas dan title sesuai dengan views dengan cara mengubah datanya menjadi dictionary yang sudah kita set 

    # cek box 6 

    seperti tadi kita kembali ke urls.py yang sudah kita buat dan meroutenya agar dia ke ke aplikasi main. Hal ini dengan cara 
    
    path('', show_main, name='show_main'),

    hal ini memperlihatkan bahwa dia akan meroute filenya ke path dan meakses show_main dari views.py yang sudah kita edit tadi

    # cek box 7 

    Setelah itu kita mendeploy di adaptable dengan cara membuat repo membuka halaman adaptable dan memilih repo yang tadi kita buat untuk menjadi aplikasi. dan juga memilih branch yang akan dipilih. setelah itu pilih python app template sebagai template dan PostgreSQL sebagai data yang digunakan, terus mengubah versi python sesuai dengan python yang terinstall, masukkan start command yaitu python manage.py migrate && gunicorn car_mart.wsgi. Setelah melakukan step2 diatas kita bisa memberi nama aplikasi dan setelah itu aplikasi sudah siap. 

2. Kaitan antara berkas dalam aplikasi web Django:
    ![Image Alt Text](Pictures/Bagan.jpg)


3. Mengapa menggunakan virtual environment (lingkungan virtual):

    Virtual Environtment atau VE banyak fungsinya dan kelebihannya, Seperti memungkinkan isolasi proyek Python, menghindari konflik antar-paket, dan memastikan penggunaan versi paket yang sesuai untuk setiap proyek. Alasan utama pengguanaan virtual environment adalah  dalam pengembangan Python yang membantu Anda mengelola dependensi proyek Anda dengan lebih baik, menjaga isolasi antar proyek, dan memastikan konsistensi dan stabilitas lingkungan pengembangan Anda.


4. Penjelasan MVC,MVT,MVVM, dan perbedaannya
    
    MVC (Model-View-Controller):

    Model       :       Menangani data dan logika bisnis.
    View        :       Menampilkan data kepada pengguna.
    Controller  :       Mengatur interaksi antara Model dan View.

    MVT (Model-View-Template):

    Model       :       Dibanding MVC model-nya lebih difokuskan sebagai objek yang mendefinisikan entitas pada konfigurasinya
    View        :       Menampilkan data kepada pengguna.
    Template    :       Mengatur tampilan HTML dan logika presentasi.

    MVVM (Model-View-ViewModel):    

    Model       :       Menangani data dan logika bisnis.
    View        :       Menampilkan data kepada pengguna.
    ViewModel   :       Memproses data dari Model agar sesuai dengan kebutuhan tampilan yang diatur oleh View.

    Perbedaan utama adalah bagaimana mereka saling mengatur interaksi antara komponen-komponennya, dengan MVC menggunakan Controller, MVT menggunakan Template, dan MVVM menggunakan ViewModel. Pilihan tergantung pada kebutuhan aplikasi dan preferensi pengembang.
