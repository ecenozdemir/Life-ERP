import requests
import sqlite3
from datetime import datetime

def veri_cek_ve_kaydet():
    print("\n--- 🤖 Life-ERP Otomasyonu Baslatiliyor ---")
    
    # 1. İnternetten Dolar ve Hava Durumu Çekme
    try:
        # Dolar Kuru
        dolar_url = "https://api.exchangerate-api.com/v4/latest/USD"
        dolar_kuru = requests.get(dolar_url).json()['rates']['TRY']
        
        # Hava Durumu (Hata payini azalttik)
        hava_url = "https://wttr.in/Istanbul?format=j1"
        hava_verisi = requests.get(hava_url).json()
        derece = int(hava_verisi['current_condition'][0]['temp_C'])
        
        # Turkce yoksa varsayilan degere gec
        try:
            durum = hava_verisi['current_condition'][0]['lang_tr'][0]['value']
        except KeyError:
            durum = hava_verisi['current_condition'][0]['weatherDesc'][0]['value']
            
        print(f"✅ Veriler Alindi: Dolar {dolar_kuru} TL | Hava {derece}°C")
    except Exception as e:
        print(f"❌ Veri alinirken hata olustu: {e}")
        dolar_kuru, derece, durum = 0.0, 0, "Bilinmiyor"

    # 2. Manuel Veri Girisi
    print("\n--- 🧠 Gunluk Oz-Gozlem ---")
    mood = input("Bugun modun nasildi? (1-10): ")
    sosyal = input("Sosyal temas/iletisim nasildi? (1-10): ")
    kod = input("Kac satir kod yazdin?: ")
    kitap = input("Kac sayfa kitap okudun?: ")
    tarih = datetime.now().strftime('%Y-%m-%d')

    # 3. Veritabanina Kaydetme
    try:
        conn = sqlite3.connect('life_erp.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Gunluk_Veri (tarih, mood_puani, kod_satiri, kitap_sayfasi, dolar_kuru, hava_derece, hava_durumu, sosyal_temas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (tarih, mood, kod, kitap, dolar_kuru, derece, durum, sosyal))
        
        conn.commit()
        conn.close()
        print(f"\n🚀 Harika Ece Nur! {tarih} verileri sisteme islendi.")
    except Exception as e:
        print(f"❌ SQL Hatasi: {e}")

if __name__ == "__main__":
    veri_cek_ve_kaydet()
