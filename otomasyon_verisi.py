import requests
import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# --- SPOTIFY AYARLARI (Buraya kendi kodlarını yapıştır) ---
CLIENT_ID = 093a3ae59ea7461a95e7030fb8654033
CLIENT_SECRET = 2501036109a94ec89fa522704eb353ec
REDIRECT_URI = "https://localhost:8888/callback" # HTTPS yaptığın için böyle kalsın

def sarki_cek():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-read-recently-played"))
        results = sp.current_user_recently_played(limit=1)
        if results['items']:
            track = results['items'][0]['track']
            return f"{track['artists'][0]['name']} - {track['name']}"
        return "Bugun sarki dinlenmemis"
    except Exception as e:
        print(f"🎵 Spotify hatasi: {e}")
        return "Spotify Baglanamadi"

def veri_cek_ve_kaydet():
    print("\n--- 🤖 Life-ERP Otomasyonu Baslatiliyor ---")
    
    # 1. İnternet Verileri (Dolar, Hava, Spotify)
    try:
        dolar_url = "https://api.exchangerate-api.com/v4/latest/USD"
        dolar_kuru = requests.get(dolar_url).json()['rates']['TRY']
        
        hava_url = "https://wttr.in/Istanbul?format=j1"
        hava_verisi = requests.get(hava_url).json()
        derece = int(hava_verisi['current_condition'][0]['temp_C'])
        durum = "Gunesli" # Basitlestirdik
        
        sarki = sarki_cek()
        print(f"✅ Veriler Alindi: Dolar {dolar_kuru} TL | Hava {derece}°C | Son Sarki: {sarki}")
    except:
        dolar_kuru, derece, durum, sarki = 0.0, 0, "Bilinmiyor", "Veri yok"

    # 2. Manuel Veri Girisi
    print("\n--- 🧠 Gunluk Oz-Gozlem ---")
    mood = input("Bugun modun nasildi? (1-10): ")
    sosyal = input("Sosyal temas/iletisim nasildi? (1-10): ")
    kod = input("Kac satir kod yazdin?: ")
    kitap = input("Kac sayfa kitap okudun?: ")
    tarih = datetime.now().strftime('%Y-%m-%d')

    # 3. Veritabanina Kaydetme
    conn = sqlite3.connect('life_erp.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Gunluk_Veri (tarih, mood_puani, kod_satiri, kitap_sayfasi, dolar_kuru, hava_derece, hava_durumu, sosyal_temas, dinlenen_sarki)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (tarih, mood, kod, kitap, dolar_kuru, derece, durum, sosyal, sarki))
    conn.commit()
    conn.close()
    print(f"\n🚀 Harika Ece Nur! Sarkinla beraber her sey kaydedildi.")

if __name__ == "__main__":
    veri_cek_ve_kaydet()
