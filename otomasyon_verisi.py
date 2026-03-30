import os
import sqlite3
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from datetime import datetime

# --- Ayarlar ---
load_dotenv()
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

def ekrani_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def sarki_cek():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-read-recently-played",
                                               open_browser=False))
        results = sp.current_user_recently_played(limit=1)
        if results['items']:
            track = results['items'][0]['track']
            return f"{track['artists'][0]['name']} - {track['name']}"
        return "Müzik bulunamadı."
    except:
        return "Spotify bağlantısı kurulamadı."

def veri_cek_ve_kaydet():
    ekrani_temizle()
    print("===========================================")
    print("   🌟 LIFE-ERP: GÜNLÜK VERİ GİRİŞİ 🌟")
    print("===========================================\n")
    
    # Otomatik veriler çekilirken kullanıcıyı bekletme hissi verelim
    print("⏳ Sistem verileri senkronize ediliyor...")
    
    try:
        dolar_url = "https://api.exchangerate-api.com/v4/latest/USD"
        dolar_kuru = requests.get(dolar_url).json()['rates']['TRY']
        
        hava_url = "https://wttr.in/Istanbul?format=j1"
        hava_verisi = requests.get(hava_url).json()
        derece = int(hava_verisi['current_condition'][0]['temp_C'])
        
        sarki = sarki_cek()
    except:
        dolar_kuru, derece, sarki = 0.0, 0, "Bilinmiyor"

    ekrani_temizle()
    print("===========================================")
    print(f"📅 TARİH: {datetime.now().strftime('%d.%m.%Y')}")
    print(f"💵 DOLAR: {dolar_kuru} TL  |  🌡️ HAVA: {derece}°C")
    print(f"🎵 SON DİNLENEN: {sarki}")
    print("===========================================\n")

    # Temiz Giriş Alanı
    mood = input("✨ Bugün modun nasıldı? (1-10): ")
    sosyal = input("🤝 Sosyal temas puanın? (1-10): ")
    kod = input("💻 Kaç satır kod yazdın?: ")
    kitap = input("📚 Kaç sayfa kitap okudun?: ")
    tarih = datetime.now().strftime('%Y-%m-%d')

    # Kayıt
    conn = sqlite3.connect('life_erp.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Gunluk_Veri (tarih, mood_puani, kod_satiri, kitap_sayfasi, dolar_kuru, hava_derece, hava_durumu, sosyal_temas, dinlenen_sarki)
        VALUES (?, ?, ?, ?, ?, ?, 'Güneşli', ?, ?)
    ''', (tarih, mood, kod, kitap, dolar_kuru, derece, sosyal, sarki))
    conn.commit()
    conn.close()

    print("\n✅ Veriler başarıyla SQL'e mühürlendi.")
    print("🚀 GitHub yedeklemesi için hazırlanılıyor...")

if __name__ == "__main__":
    veri_cek_ve_kaydet()
