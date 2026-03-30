import sqlite3

# Veritabanına bağlan (Dosya yolunun doğru olduğundan emin ol)
conn = sqlite3.connect('life_erp.db')
cursor = conn.cursor()

try:
    # İşte o eksik çekmeceyi buraya ekliyoruz
    cursor.execute("ALTER TABLE Gunluk_Veri ADD COLUMN dinlenen_sarki TEXT;")
    conn.commit()
    print("✅ Başardık! 'dinlenen_sarki' sütunu veritabanına eklendi.")
except Exception as e:
    print(f"⚠️ Bir sorun çıktı veya sütun zaten var: {e}")

conn.close()