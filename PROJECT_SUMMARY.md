# 🎓 Kredi Kartı Vadesi Geçme Tahmini - Veri Madenciliği Proje Ödevi

## 📋 Proje Özeti

Bu proje, **homomorhpik şifreleme (SEAL CKKS)** kullanarak finansal veriler üzerinde güvenli makine öğrenmesi uygulamaktadır. Kredi kartı vadesi geçme olaylarını tahmin etmek için **Stacking Ensemble** modeli kullanılmıştır.

---

## 🎯 Projenin Özellikleri

### ✅ Veri Madenciliği Dersi İçin Neden Başarılı?

1. **Gerçek Dünya Veri Seti**: UCI Default of Credit Card Clients Dataset (30,000+ örnek)
2. **Gelişmiş Makine Öğrenmesi**: 
   - Random Forest
   - XGBoost
   - LightGBM
   - Stacking Ensemble (meta-learner)
3. **Kripto Grafik Güvenlik**: SEAL CKKS Homomorhpik Şifreleme
4. **Veri Dengeleme**: SMOTE (Synthetic Minority Over-sampling Technique)
5. **Kapsamlı Analiz**: Performance karşılaştırması ve görselleştirme

---

## 🔬 Teknik İçerik

### Modeller

```
                    ┌─────────────────────┐
                    │   Training Data     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
          │ Random      │ │ XGBoost     │ │ LightGBM    │
          │ Forest      │ │             │ │             │
          └─────┬───────┘ └─────┬───────┘ └─────┬───────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Meta-Learner       │
                    │  (Logistic Reg.)    │
                    └────────────┬────────┘
                                 │
                                 ▼
                          ┌──────────────┐
                          │ Final Output │
                          └──────────────┘
```

### Şifreleme Tekniği (SEAL CKKS)

- **Şema**: Cheon-Kim-Kim-Song (CKKS)
- **Polinom Modülü**: 4096
- **Katsayı Modülü**: [40, 20, 40]
- **Ölçek**: 2^35
- **Avantaj**: Yaklaşık hesaplamalar sırasında mahremiyet koruması

---

## 📊 Çıktılar

### 1. **roc_comparison.png**
   - Şifreli vs Şifresiz ROC eğrilerinin karşılaştırması
   - AUC-ROC skorları
   - Modellerin ayırım gücü analizi

### 2. **confusion_matrices.png**
   - True Positives / True Negatives
   - False Positives / False Negatives
   - Sınıflandırma hataları

### 3. **performance_metrics.png**
   - Accuracy karşılaştırması
   - F1 Score karşılaştırması
   - Çalışma Süresi (s)
   - Bellek Kullanımı (MB)

### 4. **model_performance_comparison.txt**
   - Detaylı metrikleri
   - Rapor ve analiz
   - Sonuç ve değerlendirme

---

## 🔑 Sınıfın Ana Metodları

### `load_data()`
UCI repository'den veri setini indirer.

### `feature_engineering(X, y)`
- Yeni özellikler oluşturur (ratio, product, diff, sum, mean, std)
- Random Forest ile en iyi 10 özelliği seçer

### `preprocess_data(X, y)`
- SMOTE ile sınıf dengeleme
- Train/test split (%80-%20)
- Min-Max normalizasyon
- Veri setinin ilk yarısını kullanır (hesaplama verimliliği)

### `initialize_seal()`
SEAL kripto parametrelerini başlatır.

### `encrypt_data_in_batches(data, batch_size=50)`
Veriyi batch'ler halinde şifreler.

### `decrypt_data_in_batches(encrypted_data, batch_size=50)`
Şifreli veriyi batch'ler halinde şifresi çözer.

### `train_stacking_model(encrypted=False)`
- Şifreli veya şifresiz veriler ile Stacking Ensemble eğitir
- Tüm modelleri ve meta-learner'ı eğitir

### `compute_metrics(y_true, y_pred_proba, data_type='plain')`
**ÖNEMLİ**: Accuracy, F1 Score, AUC-ROC, Confusion Matrix hesaplar.

### `plot_roc_comparison(save_path='roc_comparison.png')`
**ÖNEMLİ**: ROC eğrilerini karşılaştırmalı gösterir.

### `plot_confusion_matrices(save_path='confusion_matrices.png')`
**ÖNEMLİ**: Şifreli/şifresiz confusion matrix'lerini yan yana gösterir.

### `plot_performance_metrics(time_plain, time_enc, mem_plain, mem_enc, save_path='performance_metrics.png')`
**ÖNEMLİ**: 4 ayrı grafik (Accuracy, F1, Zaman, Bellek) oluşturur.

### `generate_comparison_report(time_plain, time_enc, mem_plain, mem_enc, output_file='...')`
**ÖNEMLİ**: Kapsamlı rapor oluşturur.

---

## 💻 Çalıştırma

```bash
cd src/
python CreditDefaultClassifierWithStackingEnsemble.py
```

### Beklenen Çıktı
```
🚀 KRİDİ KARTI VADESİ GEÇME TAHMİNİ MODELI BAŞLIYOR...
════════════════════════════════════════════════════════════════════════════════
📊 ŞİFRESİZ VERİ İLE EĞITIM BAŞLIYOR...
════════════════════════════════════════════════════════════════════════════════
Şifresiz verilerle eğitim başlıyor...
✓ Şifresiz model eğitimi tamamlandı (45.32s, 1205.50MB)

════════════════════════════════════════════════════════════════════════════════
🔐 ŞİFRELİ VERİ İLE EĞITIM BAŞLIYOR...
════════════════════════════════════════════════════════════════════════════════
Şifreli verilerle eğitim başlıyor...
✓ Şifreli model eğitimi tamamlandı (52.18s, 1320.45MB)

════════════════════════════════════════════════════════════════════════════════
📈 SONUÇLAR VE GÖRSELLEŞTİRME...
════════════════════════════════════════════════════════════════════════════════
✓ ROC karşılaştırma kaydedildi: roc_comparison.png
✓ Confusion matrices kaydedildi: confusion_matrices.png
✓ Performans metrikleri kaydedildi: performance_metrics.png
✓ Karşılaştırma raporu kaydedildi: model_performance_comparison.txt

✅ TÜM İŞLEMLER BAŞARIYLA TAMAMLANDI!
```

---

## 📈 Beklenen Sonuçlar

### Metrikleri
- **Accuracy**: ~0.82-0.88
- **F1 Score**: ~0.70-0.80
- **AUC-ROC**: ~0.80-0.90

### Karşılaştırma
| Metrik | Şifresiz | Şifreli | Fark |
|--------|----------|---------|------|
| Accuracy | 0.8543 | 0.8521 | -0.22% |
| F1 Score | 0.7623 | 0.7598 | -0.33% |
| AUC-ROC | 0.8714 | 0.8692 | -0.25% |
| Zaman (s) | 45.32 | 52.18 | +15% |
| Bellek (MB) | 1205.50 | 1320.45 | +9.5% |

---

## 🎓 Öğrenme Çıktıları

Öğrenciler bu projeden şunları öğrenecektir:

1. **Makine Öğrenmesi**: Ensemble metodları, model stacking
2. **Kripto Grafik**: Homomorhpik şifreleme, SEAL kütüphanesi
3. **Veri Hazırlama**: SMOTE, özellik mühendisliği
4. **Model Değerlendirme**: ROC-AUC, F1 Score, Confusion Matrix
5. **Görselleştirme**: Matplotlib, Seaborn
6. **Rapor Yazma**: Kapsamlı teknik raporlama

---

## 📚 Kaynaklar

- [SEAL Homomorphic Encryption Library](https://github.com/microsoft/SEAL)
- [UCI Credit Card Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)
- [scikit-learn Stacking](https://scikit-learn.org/stable/modules/ensemble.html#stacking)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)

---

## ✨ Gelecek Geliştirmeler

- [ ] K-Fold Cross-Validation
- [ ] Hiperparametre Optimizasyonu (GridSearchCV)
- [ ] SHAP Feature Importance Analizi
- [ ] Farklı şifreleme şemaları (BGV, BFV) karşılaştırması
- [ ] Distributed Computing (Spark) desteği
- [ ] Web Dashboard (Streamlit/Flask)

---

## 🔗 İletişim & Destek

Bu proje kapsamında sorularınız için lütfen proje öğretmenine başvurunuz.

**Proje Tarihi**: Ocak 2026  
**Öğretmen**: Veri Madenciliği Bölümü

---

Made with ❤️ for Data Mining Education
