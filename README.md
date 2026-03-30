# 🚀 Life-ERP (Kişisel Kaynak Planlama Sistemi)

Bu proje, bir ERP (Enterprise Resource Planning) Supervisor bakış açısıyla geliştirilmiş, günlük hayat verilerini (mood, üretkenlik, finans, çevre ve müzik) tek bir merkezde toplayan ve otomatize eden kişisel bir veri takip sistemidir.

## ✨ Öne Çıkan Özellikler

- **🤖 Otomatik Veri Çekme:** Her gün manuel uğraş gerektirmeyen veri entegrasyonları.
  - **Finans:** Güncel USD/TRY kurunu anlık çeker.
  - **Hava Durumu:** Konum bazlı sıcaklık verisini alır.
  - **Müzik (Spotify):** O gün dinlediğiniz son şarkıyı Spotify API üzerinden yakalar.
- **🔐 Güvenlik Katmanı:** API anahtarları ve özel veriler `.env` dosyası ile korunur, GitHub'a asla açık sızdırılmaz.
- **📂 SQL Entegrasyonu:** Tüm veriler ilişkisel bir veritabanında (SQLite) tarihsel olarak saklanır.
- **☁️ Tek Tıkla Yedekleme:** Veri girişi yapıldığı an sistem otomatik olarak GitHub'a sessizce push yapar.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.14** (Çekirdek dil)
* **SQLite** (Veritabanı yönetimi)
* **Spotify API (Spotipy)** (Müzik entegrasyonu)
* **Git/GitHub** (Versiyon kontrol ve yedekleme)
* **Dotenv** (Güvenlik ve çevre değişkenleri)

## 📸 Ekran Görüntüsü

![Sistem Arayüzü](https://raw.githubusercontent.com/ecenozdemir/Life-ERP/main/ekran_goruntusu.png) 
*(Not: Buraya klasöründeki temiz bir ekran görüntüsünü ekleyebilirsin)*

## 🚀 Kurulum ve Çalıştırma

1. Klasördeki `.env.example` dosyasını `.env` olarak değiştirin ve Spotify API anahtarlarınızı girin.
2. `pip install -r requirements.txt` ile gerekli kütüphaneleri kurun.
3. `Life_ERP_Baslat.bat` dosyasına çift tıklayarak sistemi başlatın.

---
*Bu proje, bir yazılım geliştirme yolculuğunun ve veri analitiği disiplininin ürünüdür.*
