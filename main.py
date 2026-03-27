# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

# VERİTABANI BAĞLANTISI
conn = sqlite3.connect('life_erp.db')
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ic_Faktorler (
    tarih DATE PRIMARY KEY,
    mood_puani INT,
    kod_satiri INT,
    kitap_sayfa INT
)
''')
conn.commit()

print("\n--- Life-ERP Sistemine Hos Geldin Ece Nur! ---")
tarih = datetime.now().strftime('%Y-%m-%d')

# VERİ GİRİŞİ
try:
    mood = int(input("Bugunku Mood Puanin (1-10): "))
    kod = int(input("Bugun kac satir kod yazdin?: "))
    kitap = int(input("Kac sayfa kitap okudun?: "))

    cursor.execute('''
    INSERT OR REPLACE INTO Ic_Faktorler (tarih, mood_puani, kod_satiri, kitap_sayfa)
    VALUES (?, ?, ?, ?)
    ''', (tarih, mood, kod, kitap))

    conn.commit()
    print(f"\nBasardik! {tarih} verileri kaydedildi. 🚀")
except Exception as e:
    print("Bir hata olustu:", e)
finally:
    conn.close()