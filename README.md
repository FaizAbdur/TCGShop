# TugasPBP
Tugas  pembuatan MVT TCG 

Nama    : Faiz Abdurrachman 

NPM     : 2201233210
     
Kelas   : PBP B


Link Adaptable : 



# Tugas 6

1. **Perbedaan antara Asynchronous Programming dan Synchronous Programming**:

   - **Synchronous Programming**: Dalam synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu. Setiap tugas harus menunggu tugas sebelumnya selesai sebelum tugasnya sendiri dapat dijalankan. Ini berarti bahwa jika ada tugas yang memerlukan waktu lama untuk selesai, maka seluruh eksekusi program akan terhenti hingga tugas tersebut selesai.

   - **Asynchronous Programming**: Dalam asynchronous programming, tugas-tugas dieksekusi secara konkuren atau tidak berurutan. Tugas-tugas yang memerlukan waktu lama tidak akan menghentikan eksekusi program secara keseluruhan. Sebaliknya, program akan melanjutkan eksekusi tugas-tugas lain sambil menunggu tugas asinkron untuk selesai. Ini memungkinkan aplikasi untuk tetap responsif dan efisien.

2. **Paradigma Event-Driven Programming**:
   
   Paradigma event-driven programming adalah pendekatan di mana program merespon kejadian atau peristiwa yang terjadi, seperti klik tombol, masukan pengguna, atau permintaan jaringan. Ini mengharuskan penggunaan callback atau listener untuk menangani kejadian tersebut. Contoh penerapannya adalah dalam JavaScript, di mana Anda dapat menggunakan event listeners untuk merespons peristiwa seperti klik mouse, pengisian formulir, atau pemrosesan data dari permintaan jaringan AJAX.

   Contoh penerapannya pada tugas ini mungkin adalah menambahkan event listener untuk tombol "Kirim" dalam formulir web. Ketika tombol ini diklik, sebuah fungsi dapat dipanggil untuk mengirim data melalui AJAX ke server.

3. **Penerapan Asynchronous Programming pada AJAX**:

   Penerapan asynchronous programming pada AJAX memungkinkan permintaan jaringan (seperti mengambil data dari server) dilakukan tanpa menghentikan eksekusi program secara keseluruhan. Dalam JavaScript, Anda dapat menggunakan callback atau Promise untuk menangani respons dari permintaan jaringan tanpa menghentikan eksekusi program. Contoh penggunaannya adalah sebagai berikut:

   ```javascript
   fetch('https://api.example.com/data')
     .then(response => response.json())
     .then(data => {
       // Lakukan sesuatu dengan data yang diterima
     })
     .catch(error => {
       // Tangani kesalahan jika ada
     });
   ```

4. **Perbandingan Fetch API dan jQuery**:

   - **Fetch API** adalah standar JavaScript yang memungkinkan Anda melakukan permintaan jaringan asinkron dengan cara yang modern dan bersih. Ini lebih ringan dan memiliki dukungan yang baik di sebagian besar peramban.

   - **jQuery** adalah sebuah library JavaScript yang memiliki banyak fitur, termasuk AJAX. Namun, itu adalah library yang lebih besar dan mungkin memakan lebih banyak sumber daya. Selain itu, dengan perbaikan terbaru dalam Fetch API dan standar JavaScript, penggunaan jQuery mungkin tidak lagi diperlukan dalam banyak kasus.

   Pilihan antara keduanya tergantung pada proyek Anda. Jika Anda hanya membutuhkan kemampuan AJAX sederhana, Fetch API adalah pilihan yang baik. Jika Anda telah berinvestasi dalam penggunaan jQuery dalam proyek Anda atau memerlukan fitur-fitur tambahan yang ditawarkan oleh jQuery, maka jQuery mungkin tetap relevan.

5. **Cara Mengimplementasikan Checklist Secara Step-by-Step**:

   - Tentukan apakah Anda akan menggunakan Fetch API atau jQuery untuk AJAX, berdasarkan kebutuhan proyek.
   - Implementasikan event-driven programming dengan menambahkan event listeners untuk elemen-elemen yang perlu merespons peristiwa pengguna.
   - Gunakan asynchronous programming (misalnya, Promise) untuk mengelola permintaan jaringan (AJAX) tanpa menghentikan eksekusi program.
   - Tangani respons dari permintaan jaringan dan lakukan tindakan yang sesuai berdasarkan data yang diterima atau tangani kesalahan jika ada.
   - Pertimbangkan keuntungan dan kerugian dari penggunaan Fetch API dan jQuery, dan pilih teknologi yang paling sesuai untuk proyek Anda.
   
Dengan mengikuti langkah-langkah ini, Anda dapat mengimplementasikan asynchronous programming dan paradigma event-driven programming pada proyek Anda dengan baik, serta memilih teknologi yang paling sesuai untuk kebutuhan Anda.




























# Tugas 5 
1. Manfaat dari Setiap Element Selector:

   - **Universal Selector (*):** Selector ini memilih semua elemen dalam dokumen HTML. Waktu yang tepat untuk menggunakannya adalah ketika Anda ingin mengaplikasikan gaya ke seluruh elemen pada halaman web. Namun, sebaiknya digunakan dengan hati-hati karena dapat mengakibatkan overhead yang tidak perlu jika tidak diperlukan.

   - **Element Selector (e.g., p, h1, div):** Selector ini memilih semua elemen dengan nama tag yang sesuai. Ini berguna ketika Anda ingin mengaplikasikan gaya ke semua elemen dari jenis tertentu pada halaman web. Contohnya, jika Anda ingin mengubah font untuk semua elemen <p> dalam dokumen.

   - **Class Selector (.classname):** Selector ini memilih semua elemen yang memiliki atribut class yang sesuai. Ini sangat berguna ketika Anda ingin mengaplikasikan gaya khusus ke sekelompok elemen yang memiliki class yang sama. Ini adalah salah satu selector yang paling umum digunakan dalam CSS.

   - **ID Selector (#idname):** Selector ini memilih elemen dengan atribut ID yang sesuai. Waktu yang tepat untuk menggunakannya adalah ketika Anda ingin mengaplikasikan gaya khusus pada satu elemen tertentu dalam dokumen. ID selector harus unik dalam satu halaman web.

   - **Pseudo-class Selector (e.g., :hover, :nth-child):** Selector ini memilih elemen berdasarkan kondisi tertentu, seperti saat elemen dihover oleh mouse atau elemen berada pada urutan ke-n dalam suatu elemen parent. Ini berguna untuk memberikan efek interaktif dan gaya yang dinamis pada halaman web.

2. HTML5 Tag yang Umum:

   HTML5 memperkenalkan banyak tag baru. Beberapa yang umumnya digunakan termasuk:
   - `<header>`: Untuk mengelompokkan elemen-elemen kepala seperti logo, judul, dan navigasi.
   - `<nav>`: Untuk mengelompokkan elemen navigasi, seperti menu.
   - `<section>`: Untuk mengelompokkan konten dalam bagian-bagian tematik pada halaman.
   - `<article>`: Untuk mengelompokkan konten independen yang dapat berdiri sendiri.
   - `<aside>`: Untuk mengelompokkan konten terkait yang seringkali muncul di samping konten utama.
   - `<footer>`: Untuk mengelompokkan elemen-elemen kaki halaman seperti informasi kontak atau hak cipta.

3. Perbedaan antara Margin dan Padding:

   - **Margin:** Margin adalah ruang di luar batas elemen. Ini mempengaruhi jarak antara elemen tersebut dengan elemen-elemen lain di sekitarnya. Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya.

   - **Padding:** Padding adalah ruang di dalam batas elemen. Ini mempengaruhi jarak antara konten elemen dan batasnya sendiri. Padding digunakan untuk mengatur jarak antara konten elemen dengan batasnya.

4. Perbedaan antara Framework CSS Tailwind dan Bootstrap:

   - **Bootstrap:**
     - Bootstrap adalah framework CSS yang lebih berat dan kompleks.
     - Memiliki desain dan komponen yang sudah siap pakai, yang memungkinkan pembuatan situs web dengan cepat.
     - Lebih mengutamakan konvensi dan gaya yang konsisten.
     - Cocok untuk proyek besar dan situs web yang memerlukan komponen yang kaya.

   - **Tailwind:**
     - Tailwind adalah framework CSS yang lebih ringan dan fleksibel.
     - Menggunakan pendekatan utility-first, yang memungkinkan pengguna untuk membangun komponen sesuai kebutuhan dengan menggabungkan kelas-kelas utilitas.
     - Memungkinkan pengguna untuk mengontrol setiap aspek desain secara detail.
     - Cocok untuk proyek kecil hingga menengah, serta untuk pengembang yang ingin tingkat fleksibilitas yang tinggi dalam desain.

    Kapan sebaiknya Anda menggunakan Bootstrap atau Tailwind tergantung pada kebutuhan proyek Anda. Bootstrap cocok jika Anda ingin cepat dalam membangun situs dengan komponen siap pakai dan desain yang lebih konsisten. Tailwind cocok jika Anda ingin memiliki kendali yang lebih besar atas desain Anda dan ingin menghindari overhead yang tidak perlu.


5. Perubahan yang di checklist tersebut adalah

    Penggunaan checklist yang dilakukan adalah mengedit main,base dan register.html 
    ```html
    {% extends 'base.html' %}

    {% block content %}
        <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #aaaaaa;">
        <div class="container">
                <a class="navbar-brand" href="#" style="font-weight: bold; font-size: 24px;">TCG Store</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item">
                            <a class="nav-link name-link" href="#" style="font-size: 20px; font-weight: bold; font-family: 'cursive';">Name: {{ name }}</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link class-link" href="#" style="font-size: 20px; font-weight: bold; font-family: 'cursive';">Class: {{ class }}</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link logout-link" href="{% url 'main:logout' %}" style="font-size: 20px; font-weight: bold; font-family: 'cursive';">Logout</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h1 class="mb-4">Products</h1>

            <div class="row">
                {% for product in products %}
                    <div class="col-md-4">
                        <div class="outer-card" style="background-color: {% if forloop.last %}#D3D3D3{% else %}#ffffff{% endif %};">
                            <div class="inner-card card mb-4 {% if forloop.last %}last-row{% endif %}">
                                <img src="https://upload.wikimedia.org/wikipedia/en/2/2b/Yugioh_Card_Back.jpg" alt="The back side of a card" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title" style="font-size: 18px; font-weight: bold; font-family: 'Arial, sans-serif';">Product Name: {{ product.name }}</h5>
                                    <p class="card-text" style="font-size: 16px; font-family: 'Times New Roman', serif;">Description: {{ product.description }}</p>
                                    <p class="card-text" style="font-size: 16px; font-family: 'Courier New', monospace;">Price: {{ product.price }}</p>
                                    <p class="card-text" style="font-size: 16px; font-family: 'Verdana, sans-serif';">Amount: {{ product.amount }}</p>
                                    <a href="{% url 'main:edit_product' product.pk %}" class="btn btn-primary btn-sm">Edit</a>
                                    <a href="{% url 'main:delete_product' product.pk %}" class="btn btn-danger btn-sm">Delete</a>
                                </div>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>

            <p class="mt-4">Kamu menyimpan {{ products|length }} item pada aplikasi ini.</p>

            <div class="mt-4">
                <a href="{% url 'main:create_product' %}" class="btn btn-success">Add New Product</a>
            </div>

            <h5 class="mt-4">Sesi terakhir login: {{ last_login }}</h5>

            <div class="mt-4">
                <a href="{% url 'main:logout' %}" class="btn btn-secondary">Logout</a>
            </div>
        </div>

        <style>
            .outer-card {
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #ccc; 
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            
            .inner-card {
                background-color: #f7f7f7;
                border: none;
                border-radius: 15px; /* Rounded edges for inner cards */
            }
            
            .inner-card.last-row {
                background-color: beige; /* Background color for the last row */
            }

        </style>
        {% endblock content %}
    ```

ini mengubah sehingga terdapat background color saat dipencet dan terdapat warna perubahan di inner card dan outercard sehingga bisa terdapat perbedaan warna dan lebih rapih




















# Tugas 4

## 1. Django UserCreationForm:

Django UserCreationForm adalah formulir bawaan yang disediakan oleh Django untuk mempermudah pembuatan akun pengguna (user account) dalam aplikasi web yang dibangun dengan Django. Formulir ini menyediakan bidang-bidang seperti username, password, dan konfirmasi password untuk memungkinkan pengguna mendaftar dengan mudah. Kelebihan dari UserCreationForm adalah:

* Kemudahan Penggunaan: UserCreationForm menyediakan alat yang kuat dan mudah digunakan untuk mengelola proses pendaftaran pengguna.
* Validasi Bawaan: Form ini juga mencakup validasi bawaan, seperti memeriksa apakah password dan konfirmasi password cocok,     sehingga mengurangi risiko kesalahan pengguna.
Namun, ada beberapa kekurangan dari UserCreationForm,  ketika ingin menyesuaikan proses pendaftaran pengguna secara signifikan. Dalam situasi seperti itu, Anda mungkin perlu membuat formulir pendaftaran kustom.

## 2. Perbedaan Antara Autentikasi dan Otorisasi:

* Autentikasi (Authentication): Autentikasi adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini berarti memeriksa apakah pengguna yang mencoba mengakses aplikasi telah berhasil masuk atau belum.

* Otorisasi (Authorization): Otorisasi adalah proses pengendalian akses ke sumber daya berdasarkan hak atau izin yang dimiliki oleh pengguna. Setelah pengguna berhasil diautentikasi, Django memeriksa izin apa yang dimiliki oleh pengguna tersebut untuk mengakses berbagai bagian dari aplikasi. 

Keduanya penting dalam konteks Django karena autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi Anda, sementara otorisasi memungkinkan Anda mengendalikan apa yang dapat dilakukan oleh pengguna yang telah diautentikasi.

## 3. Cookies dalam Konteks Aplikasi Web dan Penggunaan di Django:

* Cookies: Cookies adalah data kecil yang disimpan di sisi klien (biasanya dalam browser) dan digunakan untuk menyimpan informasi tentang sesi pengguna atau preferensi pengguna dalam aplikasi web. Mereka dapat digunakan untuk mengidentifikasi pengguna yang telah masuk atau untuk menyimpan data sesi, seperti keranjang belanja dalam toko online.

* Penggunaan Cookies dalam Django: Django menggunakan cookies untuk mengelola data sesi pengguna secara default. Ini berarti bahwa informasi seperti ID sesi pengguna dapat disimpan dalam cookie untuk mengidentifikasi pengguna yang telah masuk. Django memiliki dukungan bawaan untuk mengelola cookies melalui modul 
    ```
    django.contrib.sessions.middleware.SessionMiddleware.

## 4. Keamanan Penggunaan Cookies:

* Secara Default Relatif Aman: Penggunaan cookies dalam pengembangan web umumnya relatif aman, terutama jika Anda mengikuti praktik terbaik dalam mengelola cookies. Django memberikan beberapa perlindungan bawaan terhadap serangan yang umum terkait cookies, seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF).

* Potensi Risiko: Namun, penggunaan cookies dapat menjadi risiko jika tidak dikelola dengan baik. Risiko potensial termasuk peretasan sesi (session hijacking), di mana peretas mencoba mencuri ID sesi pengguna dari cookie untuk mengakses akun pengguna. Oleh karena itu, Anda perlu mengimplementasikan praktik keamanan seperti menggunakan HTTPS untuk mengenkripsi data yang ditransmisikan melalui cookie dan mengelola cookie dengan hati-hati.

Penting untuk memahami bahwa cookie hanya aman sejauh pengembang aplikasi web memastikan bahwa mereka tidak digunakan untuk tujuan jahat. Selalu penting untuk memahami praktik terbaik dalam mengelola cookies dan mengamankannya sesuai kebutuhan aplikasi Anda.

## 5. Per-Checkpoint

### 1. Implementasi fungsi registrasi, login, dan logout 
Mengimplementasikan fungsi registrasi, login, dan logout dengan mengimport "redirect", "UserCreationForm", dan "Messages". Kita menggunakan user creation form untuk menjadi formulir pendaftaran. Setelah itu, implementasikan fungsi register di views.py.

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Setelah menambah register buatlah template html untuk menampilkannya, setelah itu buat fungsi login untuk bisa authenticate yaitu
untuk memperlihatkan autentikasi dan login 

```python

from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
setelah itu buatlah html untuk bisa menjadi template terhadap views yaitu login.html, setelah itu tambahkan main dan path
Terakhir buatlah import logout agar bisa menambah fungsi 

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

setelah implementasi logout tambahkan path ke url dan views 

### 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Registrasikan akun di web lokal sehingga terdapat 2 akun setelah itu tambah 3 product dengan model menggunakan create product 
kita bisa melakukan 2 akun dengan registrasi.
### 3. Menghubungkan model Item dengan User.

Kita menghubungkan objek produk dengan user kita menggunakan ForeignKey sebagai relationship antara user dan product
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
### 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Kita bisa menggunakan cookies dengan cara implementasi kode cookies ini adalah 
```python

if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

    last_login': request.COOKIES['last_login'],

    response.delete_cookie('last_login')
```
kode ini dipakai untuk menggunakan last_login dan dicatat dan dipakai sebagai set cookie di data sessionid dan crsftoken








# Tugas 3
Jawaban Pertanyaan : 

# 1. Apa perbedaan antara form "POST" dan form "GET" dalam django?
*  Metode Pengiriman data : 
    1. Form POST mengirim data dari forms ke server dengan menyembunyikan data saat permintaan http, sehingga tidak terlihat di url 
    2. Form GET mengirim data sebagai bagian dair URL, sehingga data terlihat dalam URL. 

*   1. Form POST lebih aman untuk mengirim data sensitif karena data tidak terlihat dalam URL dan terlindungi dengan baik.
    2. Form GET kurang aman karena data terlihat dalam URL dan dapat dengan mudah diakses atau disadap oleh pihak ketiga.
            
              
# 2.  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML (Extensible Markup Language):
- Digunakan untuk menyimpan dan mentransfer data terstruktur.

JSON (JavaScript Object Notation):
- Digunakan untuk mentransfer data dalam bentuk objek yang terstruktur.

HTML (Hypertext Markup Language):
- Digunakan untuk membuat tampilan halaman web, bukan untuk pertukaran data.

# 3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena:

- Ringkas dan Mudah Dibaca: JSON memiliki format yang ringkas dan mudah dibaca oleh manusia, membuatnya ideal untuk pertukaran data antara aplikasi web.

- Objek Terstruktur: JSON memungkinkan representasi data dalam bentuk objek yang terstruktur, yang mirip dengan struktur data dalam bahasa pemrograman, sehingga mudah diolah oleh kode.

- Ringan dan Efisien: JSON memiliki overhead yang minimal, sehingga memungkinkan pertukaran data dengan cepat dan efisien melalui jaringan.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

+ Membuat berkas forms.py untuk dapat menerima produk baru. isi forms dengan fields yang sesuai fields dari model ini, dan definisikan model menjadi objek apa agar saat form disimpan akan membuat objek itu 
+ Kita dapat membuat fungsi dengan pertama membuat variabel yang dipakai untuk menyimpan semua hasil query data yang ada di produk yaitu adalah 
    ```
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

 return function untuk  HTML, XML, JSON, dapat diganti saat return function serializers. Diganti dengan format yang akan diserialize agar sesuai dengan format yang diinginkan. 

+ Untuk yang show id dilakukan dengan cara mengubah data menjadi

    ```
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
ini dilakukan agar product terfilter agar fungsi menyimpan query dari data dengan id tertentu 
untuk return functionnya sama dengan return function sebelumnya 

+ Terakhir untuk routing url kita menambah sesuai dengan views yang sudah kita buat yaitu 

    ```
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 

url akan menerima argumen berupa fungsi views yang akan kita pakai, seperti 
1. 'create-product': Mencocokkan URL dengan create_product view.
2. '<int:id>/': Mencocokkan URL dengan view yang memiliki parameter <int:id> (integer ID).
3. 'show_main', 'show_xml', 'show_json', 'show_xml_by_id', dan 'show_json_by_id': Mencocokkan URL dengan views yang sesuai dengan nama yang disebutkan.

# 5. Screenshot Postman 

1. HTML
![Image Alt Text](Pictures/HMTL.png)

2. JSON
![Image Alt Text](Pictures/JSON.png)

3. JSON berdasarkan id
![Image Alt Text](Pictures/JSONID.png)

4. XML
![Image Alt Text](Pictures/XML.png)

5. XML berdasarkan id
![Image Alt Text](Pictures/XMLID.png)



# 6 Bonus
saya membuat kode
    
    ```html
        {% with total_items=products|length %}
        <p>Kamu menyimpan {{ total_items }} item pada aplikasi ini.</p>
        {% endwith %}

Menggunakan {% with %} tag untuk membuat variabel baru di django templates setelah itu di definisikan sebagai jumlah item pada product dengan cara menjumlahkan item di dalam products dengan 'length'.



# Tugas 2 PBP
s

Jawaban Pertanyaan : 

MVC (Model-View-Controller):
1. Penjelasan setiap projek Django : 

# Cek Box 1 

Proses dimulai dengan pertama membuat proyek Django baru, pertama yang dilakukan adalah membuat sebuah repositori git baru untuk menampung proyek aplikasi django. Setelah selesai men-setup repositori di lokal dan di git mulai dengan install Django, karena Django sudah terinstall maka dimulai dengan inisiasi Proyek Django. Ini dimulai dengan membuat direktori dimana aplikasi akan dibuat dan mengaktifkan Virtual Enviroment di Folder tersebut. Setelah itu install dependencies, jika sudah bisa mulai dengan mengaktifkan startproject di command shell

Model       :       Menangani data dan logika bisnis.
View        :       Menampilkan data kepada pengguna.
Controller  :       Mengatur interaksi antara Model dan View.

# Cek Box 2 
membuat aplikasi baru bernama main dengan menjalankan command startapp main.  Setelah itu saat sudah dicek bahwa di folder terdapat folder bernama main masukkan main ke installed apps agar aplikasi dapat dibaca oleh django, setelah itu kita membuat direktori baru bernama templates dalam folder yang berisi direktori main dan di direktori template kita membuat main.HTML yang menjadi pengaturan tampilan HTML dan logika presentasi 

# Cek Box 3
untuk menghubungkan rute url terhadap agar perubahan pada main terlihat kita perlu setup pathingnya di urls.py yang kita akan buat di direktori main 

MVT (Model-View-Template):
# Cek Box 4
Kita dapat membuat model pada aplikasi main dengan cara mengubahnya di models.py dan sesuai dengan ketentuan kita membuat dalam bentuk 

    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

Model       :       Dibanding MVC model-nya lebih difokuskan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasiny
View        :       Menampilkan data kepada pengguna.
Template    :       Mengatur tampilan HTML dan logika presentasi.
    sesuai dengan ketentuan terdapat name amount dan description yang masing masing bersisi charfield, IntegerField, dan TextField

MVVM (Model-View-ViewModel):    
# Cek Box 5
Untuk menentukan fungsi di views untuk dikembalikan ke dalam sebuah template HTML kita membuat dictionary yang berisi data-data yang sesuai kita isi yang akan ditampilkan. di sana terdapat 3 konteks yaitu nama,class,dan title,dimana itu adalah data nama,data kelas,data title. dibawahnya terdapat line return render dan main.HTML yang berarti dia akan merender tampilannya di template main.HTML. Setelah itu di Main.HTML diubah agar output nama dan kelas dan title sesuai dengan views dengan cara mengubah datanya menjadi dictionary yang sudah kita set 

    Model       :       Menangani data dan logika bisnis.
    View        :       Menampilkan data kepada pengguna.
    viewModel   :       Memproses data dari Model agar sesuai dengan kebutuhan tampilan yang diatur oleh View.

# Cek Box 6 

Perbedaan utama adalah bagaimana mereka mengatur interaksi antara komponen-komponen ini, dengan MVC menggunakan Controller, MVT menggunakan Template, dan MVVM menggunakan ViewModel. Pilihan tergantung pada kebutuhan aplikasi dan preferensi pengembang.
seperti tadi kita kembali ke urls.py yang sudah kita buat dan meroutenya agar dia ke ke aplikasi main. Hal ini dengan cara 

    path('', show_main, name='show_main'),

Kaitan antara berkas dalam aplikasi web Django:
hal ini memperlihatkan bahwa dia akan meroute filenya ke path dan meakses show_main dari views.py yang sudah kita edit tadi

urls.py: Mengatur URL dan mengarahkan permintaan klien ke fungsi atau kelas tampilan di views.py.
views.py: Berisi logika bisnis, mengambil data dari models.py, dan mengembalikan respons, seringkali dalam bentuk halaman HTML.
models.py: Mendefinisikan struktur data dan relasi database yang digunakan oleh aplikasi.
Berkas HTML: Digunakan untuk menghasilkan tampilan yang diberikan kepada pengguna, seringkali dengan menggunakan data dari model.
# Cek Box 7 

Mengapa menggunakan virtual environment (lingkungan virtual):
Setelah itu kita mendeploy di adaptable dengan cara membuat repo membuka halaman adaptable dan memilih repo yang tadi kita buat untuk menjadi aplikasi. dan juga memilih branch yang akan dipilih. setelah itu pilih python app template sebagai template dan PostgreSQL sebagai data yang digunakan, terus mengubah versi python sesuai dengan python yang terinstall, masukkan start command yaitu python manage.py migrate && gunicorn car_mart.wsgi. Setelah melakukan step2 diatas kita bisa memberi nama aplikasi dan setelah itu aplikasi sudah siap. 

Memungkinkan isolasi proyek Python, menghindari konflik antar-paket, dan memastikan penggunaan versi paket yang sesuai untuk setiap proyek.
Meskipun mungkin memungkinkan, sangat disarankan untuk menggunakan virtual environment saat mengembangkan aplikasi web Django untuk manajemen yang lebih baik dan kebersihan kode.

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





