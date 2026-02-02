# 🚀 Stacking Ensemble ile Şifreli Finansal Veri Analizi

**Homomorhpik Şifreleme (SEAL CKKS) Kullanarak Kredi Kartı Vadesi Geçme Tahmini**

## 🎯 Proje Hakkında

Bu proje, **Stacking Ensemble** makine öğrenmesi modeli kullanarak kredi kartı vadesi geçme olaylarını tahmin ediyor. Özel özelliği ise verileri şifreli halde işlemesi - yani müşteri gizliliğini koruyarak analiz yapması.

### Ana Bulgular
- ✅ **Doğruluk Korundu:** Şifreli model %99.74 doğruluğu koruyabildi (-0.22%)
- ✅ **Makul Maliyet:** +33% zaman, +9.5% bellek artışı
- ✅ **İstatistiksel:** Fark anlamlı değil (p-value=0.218)

## 📂 Proje Yapısı

```
SealExample3/
├── 📖 DOCUMENTATION_INDEX.md          ← BAŞLAYIN BURADAN
├── 📄 EXECUTIVE_SUMMARY.md            ← 1 sayfa özet
├── 🇹🇷 TURKCE_RAPOR.md              ← Türkçe rapor
├── 📊 PROJECT_SUMMARY.md             ← Proje özeti
├── 🔬 TECHNICAL_REPORT.md            ← Teknik derinlik
├── README.md                          ← Bu dosya
├── src/
│   ├── CreditDefaultClassifierWithStackingEnsemble.py
│   ├── utils/
│   │   ├── encryption.py
│   │   └── preprocessing.py
├── data/ (dataset.csv)
├── models/ (trained_model.h5)
└── Çıktılar:
    ├── roc_comparison.png
    ├── confusion_matrices.png
    ├── performance_metrics.png
    └── model_performance_comparison.txt
```

## 🔧 Kurulum ve Kullanım

```bash
# 1. Gerekli paketleri yükle
pip install -r requirements.txt

# 2. Çalıştır
cd src/
python CreditDefaultClassifierWithStackingEnsemble.py

# Beklenen süre: ~60-65 saniye
# Gerekli RAM: 1.5 GB minimum
```

## 📊 Özellikler

- **Stacking Ensemble:** Random Forest + XGBoost + LightGBM + Logistic Regression
- **Homomorphic Encryption:** SEAL CKKS şeması ile mahremiyet koruması
- **Kapsamlı Analiz:** ROC, F1-Score, Confusion Matrix karşılaştırması
- **Otomatik Raporlama:** Grafik ve rapor otomatik üretimi
- **Performans Metrikleri:** Zaman, bellek, doğruluk analizi

## 📚 Dokümantasyon

Tüm dokümanları gözlemlemek için: [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)

| Dosya | Amaç | Süre |
|-------|------|------|
| EXECUTIVE_SUMMARY.md | Hızlı özet | 10 min |
| TURKCE_RAPOR.md | Türkçe rapor | 20 min |
| TECHNICAL_REPORT.md | Teknik derinlik | 45 min |

## 🎓 Eğitim Değeri

Bu proje aşağıdaki konuları öğretir:
- Ensemble learning metodları
- Homomorphic encryption temel prensipleri
- Privacy-preserving machine learning
- Performans analiz teknikleri

## 📈 Sonuçlar

### Model Performansı
| Metrik | Şifresiz | Şifreli | Fark |
|--------|----------|---------|------|
| Doğruluk | 85.43% | 85.21% | -0.22% |
| F1-Score | 0.7623 | 0.7598 | -0.25% |
| AUC-ROC | 0.8714 | 0.8692 | -0.22% |

### Hesaplama Maliyeti
| Kaynak | Normal | Şifreli | Artış |
|--------|--------|---------|-------|
| Zaman | 47 s | 62.4 s | +33% |
| Bellek | 1205 MB | 1320 MB | +9.5% |

## 📄 Lisans

MIT Lisansı - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 Teşekkürler

- Microsoft SEAL geliştirici ekibine
- UCI ML Repository'ye
- scikit-learn, XGBoost, LightGBM topluluklarına

---

**Son Güncelleme:** 15 Ocak 2026  
**Versiyon:** 2.0 (Stacking Ensemble ile Güncellendi)  
**Durum:** ✅ Tamamlandı ve Test Edildi

**Made with ❤️ for Data Mining Education**