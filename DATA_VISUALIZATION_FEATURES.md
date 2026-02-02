# 🆕 Veri Analizi Özellikleri

**Eklenen Tarih:** 15 Ocak 2026  
**Versiyon:** 2.5

---

## 📊 Yeni Veri Görselleştirme Özellikleri

Proje artık veriler hakkında kapsamlı bilgi vermek için 5 yeni metodla donatılmıştır.

---

## 🎯 Eklenen 5 Metod

### 1. `plot_feature_importance()` - En İyi 10 Özellik Grafiği

**Amaç:** Model tarafından kullanılan en önemli özellikleri göster

**Görüntüler:**
- Bar grafik (Horizontal)
- Her özelliğin önem seviyesi
- Renklendirilmiş görünüm
- Değerleri yazılı

**Çıktı:**
```
feature_importance.png
```

**Örnek Çıktı:**
```
📊 En İyi 10 Özelliğin Önem Seviyeleri:
──────────────────────────────────────
1. PAY_STAT                0.225847 ████████████████████
2. AGE                     0.156432 ███████████████
3. BILL_AMT1               0.142156 ██████████████
4. PAY_AMT1                0.128945 ████████████
...
```

---

### 2. `display_sample_data()` - Örnek Veri Tablosu

**Amaç:** Training setinden rastgele 10 örnek göster

**Çıktılar:**
- `sample_data.txt` - Metin formatı (istatistikler dahil)
- `sample_data.csv` - CSV formatı (Excel'de açılabilir)

**Tablo İçeriği:**
```
| Feature1 | Feature2 | ... | Feature10 | Vadesi_Geçti | Sonuç      |
|----------|----------|-----|-----------|--------------|------------|
| 0.234    | 0.567    | ... | 0.891     | 0            | ✗ Geçmedi  |
| 0.456    | 0.789    | ... | 0.234     | 1            | ✓ Geçti    |
| ...      | ...      | ... | ...       | ...          | ...        |
```

**Dosya Örneği:**

**sample_data.txt:**
```
════════════════════════════════════════════
ÖRNEK VERİ (Training Set'ten Rastgele 10 Örnek)
════════════════════════════════════════════

Veri Seti Özellikleri:
- Toplam Özellik: 10
- Gösterilen Örnekler: 10
- Sınıf Dağılımı: Vadesi Geçti = 1, Geçmedi = 0

[Detaylı Tablo ve İstatistikler]

İstatistiksel Bilgiler:
    count mean std min 25% 50% 75% max
...
```

**sample_data.csv:**
```
Feature1,Feature2,...,Vadesi_Geçti,Sonuç
0.234,0.567,...,0,✗ Geçmedi
0.456,0.789,...,1,✓ Geçti
...
```

---

### 3. `plot_data_distribution()` - Sınıf Dağılımı Grafiği

**Amaç:** Eğitim ve test setinin sınıf dağılımını 3 panelde göster

**Çıktı:**
```
data_distribution.png
```

**3 Panel:**

1. **Eğitim Seti Sınıf Dağılımı**
   - Vadesi Geçmedi vs Vadesi Geçti
   - Bar grafik + sayılar + yüzde

2. **Test Seti Sınıf Dağılımı**
   - Vadesi Geçmedi vs Vadesi Geçti
   - Bar grafik + sayılar + yüzde

3. **Vadesi Geçti Oranı Karşılaştırması**
   - Eğitim setinde % oranı
   - Test setinde % oranı
   - Karşılaştırmalı bar

**Konsol Çıktı:**
```
📊 Veri Seti İstatistikleri:
──────────────────────────────
Eğitim Seti Toplam: 14952 örnek
  • Vadesi Geçmedi: 7523 (50.3%)
  • Vadesi Geçti:   7429 (49.7%)

Test Seti Toplam: 3738 örnek
  • Vadesi Geçmedi: 2880 (77.1%)
  • Vadesi Geçti:   858  (22.9%)
```

---

### 4. `plot_feature_statistics()` - Özellik Dağılımı (Box Plot)

**Amaç:** Her özelliğin Vadesi Geçti/Geçmedi ile dağılımını göster

**Çıktı:**
```
feature_statistics.png
```

**Görüntü:**
- 10 x 10 grid (10 özellik için)
- Her özellik için Box plot
- Yeşil: Vadesi Geçmedi
- Kırmızı: Vadesi Geçti
- Min, Q1, Median, Q3, Max değerleri

**Yorumlama:**
- Box yüksekliği = İç Çeyrek Aralığı
- Çizgi = Medyan
- Nokta = Aykırı değer
- Genellikle, kırmızı ve yeşil boxlar faklı ise = Discriminative özellik

---

### 5. `generate_data_summary_report()` - Veri Özet Raporu

**Amaç:** Veri seti hakkında kapsamlı rapor oluştur

**Çıktı:**
```
data_summary.txt
```

**İçerik:**

```
════════════════════════════════════════════════════════════════
VERİ SETI KAPSAMLI ÖZET RAPORU
════════════════════════════════════════════════════════════════

📊 VERİ SETI BİLGİLERİ
─────────────────────────────────────────────────────────────
Kaynak: UCI Default of Credit Card Clients Dataset (ID: 350)
İndirme Tarihi: 2026-01-15 14:30:45

📈 ÖZELLİK BİLGİLERİ
─────────────────────────────────────────────────────────────
Toplam Özellik Sayısı (Orijinal): 23
Seçilen Özellik Sayısı: 10
Özellikler: PAY_STAT, AGE, BILL_AMT1, PAY_AMT1, ...

🎯 SINIF DAĞILIMI
─────────────────────────────────────────────────────────────
Eğitim Seti: 14952 örnek
  • Vadesi Geçmedi (0): 7523 (50.3%)
  • Vadesi Geçti (1): 7429 (49.7%)

Test Seti: 3738 örnek
  • Vadesi Geçmedi (0): 2880 (77.1%)
  • Vadesi Geçti (1): 858 (22.9%)

📊 İSTATİSTİKSEL ÖZET
─────────────────────────────────────────────────────────────
count    mean     std    min    25%    50%    75%     max
PAY_STAT 14952.0 -0.5234 1.2345 -2.5 -0.8 -0.1  0.7   3.2
AGE      14952.0 35.4821 8.9234 21.0 29.0 35.0 42.0  79.0
...

🔗 ÖZELLİKLER ARASI KORELASYON (Top 5)
─────────────────────────────────────────────────────────────
1. BILL_AMT1 ↔ PAY_AMT1: 0.7234
2. AGE ↔ EXPERIENCE: 0.6123
3. LIMIT_BAL ↔ BILL_AMT1: 0.5456
...

🔄 VERİ HAZIRLAMA ADIMLARI
─────────────────────────────────────────────────────────────
1. Feature Engineering: 6 yeni özellik eklenmiştir
2. Sınıf Dengeleme: SMOTE kullanılmıştır (78:22 → 50:50)
3. Train-Test Split: %80 eğitim, %20 test
4. Normalizasyon: Min-Max Scaling [0,1]
════════════════════════════════════════════════════════════════
```

---

## 📁 Oluşturulan Dosyalar (Toplam 10 Yeni)

### Veri Analizi Grafikleri (3 PNG)
```
feature_importance.png
   ├─ En iyi 10 özellik bar grafik
   ├─ Önem seviyeleri gösterir
   └─ Renklendirme + değerler

data_distribution.png
   ├─ 3 panel sınıf dağılımı
   ├─ Eğitim seti, Test seti, Karşılaştırma
   └─ % oranlar ve sayılar

feature_statistics.png
   ├─ 10 özellik için box plot
   ├─ Vadesi Geçti/Geçmedi karşılaştırması
   └─ Aykırı değerleri gösterir
```

### Veri Raporları (3 TXT + 1 CSV)
```
sample_data.txt
   ├─ 10 örnek veri
   ├─ İstatistiksel özet
   └─ Konsola da yazdırılır

sample_data.csv
   ├─ 10 örnek veri CSV formatı
   └─ Excel'de açılabilir

data_summary.txt
   ├─ Kapsamlı veri raporu
   ├─ Sınıf dağılımı
   ├─ İstatistikler
   ├─ Korelasyon analizi
   └─ Veri hazırlama adımları
```

### Model Performansı (Önceki dosyalar)
```
roc_comparison.png
confusion_matrices.png
performance_metrics.png
model_performance_comparison.txt
```

---

## 🚀 Çalıştırma

Artık proje çalıştırıldığında bu dosyaları otomatik olarak oluşturur:

```bash
cd src/
python CreditDefaultClassifierWithStackingEnsemble.py
```

**Beklenen Çalışma Süresi:** ~70-80 saniye (Veri grafikleri eklenmiştir)

---

## 📊 Çıktılar Özeti

```
✅ OLUŞTURULAN DOSYALAR
════════════════════════════════════════════════════════════════

📊 Veri Analizi Grafikleri:
  • feature_importance.png - En iyi 10 özelliğin önem seviyeleri
  • data_distribution.png - Sınıf dağılımı (3 panel)
  • feature_statistics.png - Özellik dağılımı (10 box plot)

📄 Veri Raporları:
  • sample_data.txt - 10 örnek veri (metin + istatistik)
  • sample_data.csv - 10 örnek veri (CSV formatı)
  • data_summary.txt - Kapsamlı veri seti raporu

🔬 Model Performansı Grafikleri:
  • roc_comparison.png - ROC eğrisi karşılaştırması
  • confusion_matrices.png - Confusion matrix'leri
  • performance_metrics.png - 4 metrik karşılaştırması

📋 Model Raporları:
  • model_performance_comparison.txt - Detaylı karşılaştırma
════════════════════════════════════════════════════════════════
```

---

## 💡 Kullanım Örnekleri

### Örnek 1: Sadece Veri Analizi Grafiklerini Görmek

Grafikler otomatik olarak oluşturulur ve kaydedilir. Projeyi çalıştırınız.

### Örnek 2: Örnek Veriyi Excel'de Açmak

```
sample_data.csv → Excel'de aç
```

### Örnek 3: Veri Raporu Oku

```
data_summary.txt → Metin editörde aç
```

### Örnek 4: Feature Importance'ı Analiz Et

```
feature_importance.png → Görüntüle
```

Hangi özelliklerin model tarafından en çok kullanıldığını görürsünüz.

---

## 🎓 Öğrenme Değeri

Bu yeni özellikler sayesinde öğrenciler şunları görebilir:

1. **Veri Keşfi:** En iyi 10 özellik neler?
2. **Sınıf Dağılımı:** Dengeli mi? Dengesiz mi?
3. **Özellik Dağılımı:** Normal dağılım mı? Çarpık mı?
4. **Korelasyon:** Hangi özellikler ilişkili?
5. **Pratik Veri:** Gerçek veri örnekleri

---

## 📈 Proje Gelişimi

| Versiyon | Tarih | Yenilik |
|----------|-------|---------|
| v1.0 | 15 Oca | İlk sürüm (Model + Rapor) |
| v2.0 | 15 Oca | Stacking Ensemble + Grafik |
| v2.5 | 15 Oca | ✅ Veri Analizi Grafikleri |

---

**Tüm yeni özellikler otomatik olarak çalışır ve dosya oluşturur!** 🎉

Made with ❤️ for Data Analysis
