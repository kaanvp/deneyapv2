# Deneyap Atölyesi - Depo ve Stok Yönetim Sistemi

![Deneyap Depo Sistemi](frontend/assets/deneyap_logo.png)

Bu proje, Deneyap atölyelerinde bulunan elektronik bileşenlerin, sarf malzemelerin ve demirbaşların düzenli bir şekilde kayıt altında tutulmasını, atölyeler arası transferlerin yönetilmesini ve anlık stok takibini sağlamak amacıyla geliştirilmiş kapsamlı bir **Full-Stack Web Uygulamasıdır**.

## 🚀 Projenin Amacı ve Çözdüğü Sorunlar
Atölyelerde binlerce farklı malzeme bulunmaktadır. Bu malzemelerin hangi depoda, hangi dolapta ve rafta olduğunun bilinmemesi büyük bir zaman kaybı yaratır. Ayrıca kritik seviyeye düşen malzemelerin fark edilmemesi eğitim süreçlerini aksatabilir. 

Bu otomasyon sistemi sayesinde:
* Tüm ürünler kategorize edilerek aranabilir hale getirilmiştir.
* Excel listeleri tek tıkla sisteme entegre edilebilir.
* Kritik stoka düşen ürünler sistem tarafından otomatik raporlanır.
* Gönderim modülü sayesinde malzemelerin ne zaman kime teslim edildiği kayıt altına alınır.

## 💻 Kullanılan Teknolojiler
Proje, modern ve yüksek performanslı araçlar kullanılarak modüler (SPA) bir mimaride tasarlanmıştır:

**Backend (Sunucu & Veritabanı):**
* **Python & FastAPI:** Yüksek performanslı ve asenkron API altyapısı.
* **SQLAlchemy:** Nesne İlişkisel Eşleme (ORM) ile güvenli veritabanı iletişimi.
* **SQLite:** (Supabase/PostgreSQL mimarisine tamamen uyumlu yapıda) lokal veritabanı.
* **OpenPyXL & ReportLab:** Excel üzerinden veri okuma/yazma ve dinamik PDF raporları üretme.
* **Bcrypt & JWT (JSON Web Token):** Güvenli şifreleme ve yetkilendirme (Admin / Normal Kullanıcı) sistemi.

**Frontend (Kullanıcı Arayüzü):**
* **Vanilla JavaScript (SPA - Single Page Application):** Sayfa yenilenmeden hızlı modül geçişleri.
* **Tailwind CSS:** Modern, duyarlı (responsive) ve estetik tasarım.
* **Glassmorphism UI:** Yarı saydam, cam efektli modern arayüz tasarımı.

## ✨ Temel Özellikler (Features)
1. **Gelişmiş Ürün Yönetimi:**
   - Ürünlere fotoğraf, açıklama, kategori, mevcut ve ideal stok değerleri atama.
   - Durum takibi (Çalışan, Bozuk, Garantide, Demirbaş vb.).
   - **Akıllı Excel İçe Aktarma:** Gelişmiş algoritma ile Excel dosyalarındaki karmaşık başlıkları bulup (Malzeme Adı) toplu halde saniyeler içinde ürün ekleyebilme.

2. **Depo ve Hiyerarşi Yönetimi:**
   - Sınırsız sayıda depo oluşturma.
   - Depo içerisine **Dolap > Raf > Bölme** şeklinde derinlemesine fiziksel konumlandırma haritası çıkartabilme.

3. **Gönderim ve Transfer (Shipment):**
   - Seçilen atölyelere/merkezlere ürün transfer etme.
   - "Düşülen Miktar" ile "Talep Edilen Miktar" karşılaştırması ve hata kontrolü.
   - İşlemlerin tarih ve saat bazlı (Türkiye GMT+3 saat dilimine entegre) loglanması.

4. **Kritik Stok ve Raporlama:**
   - Kritik stoğa inen ürünler için UI üzerinde kırmızı renkli "Kritik Stok" alarmları.
   - Depo veya kategori bazında anlık envanter durumunun **PDF** ve **Excel** olarak dışarı aktarılabilmesi.

5. **Güvenlik ve Kullanıcı Yönetimi:**
   - Admin ve yetkisi kısıtlandırılmış standart personel hesapları.
   - Admin dışındaki kullanıcıların ürün silme/ekleme yetkilerinin engellenmesi.

## 🛠 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

**Gereksinimler:** Python 3.8+

```bash
# 1. Projeyi bilgisayarınıza indirin
git clone https://github.com/gizembocek/depo-deneyap.git

# 2. Proje klasörüne girin
cd depo-deneyap/backend

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 4. Sunucuyu başlatın
uvicorn main:app --reload
```

Sunucu başladıktan sonra tarayıcınızdan **`http://localhost:8000`** adresine giderek sistemi kullanmaya başlayabilirsiniz.
*Not: Sistem ilk kez çalıştığında tabloları otomatik oluşturur. Varsayılan yönetici hesabı oluşturmak için sisteme ilk kez kayıt olmanız yeterlidir.*

---
**Geliştirici:** Gizem
