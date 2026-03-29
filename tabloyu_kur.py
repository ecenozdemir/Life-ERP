import sqlite3

# Veritabanına bağlan (yoksa oluşturur)
conn = sqlite3.connect('life_erp.db')
cursor = conn.cursor()

# Tabloyu oluşturma komutu
tablo_komutu = '''
CREATE TABLE IF NOT EXISTS Gunluk_Veri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarih TEXT,
    mood_puani INTEGER,
    kod_satiri INTEGER,
    kitap_sayfasi INTEGER,
    dolar_kuru REAL,
    hava_derece INTEGER,
    hava_durumu TEXT,
    sosyal_temas INTEGER
);
'''

try:
    cursor.execute(tablo_komutu)
    conn.commit()
    print("✅ Tablo basariyla kuruldu/kontrol edildi!")
except Exception as e:
    print(f"❌ Bir hata olustu: {e}")
finally:
    conn.close()