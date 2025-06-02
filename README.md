# drone-fleet-optimizer

# 🚀 Drone Filo Optimizasyonu | Çok Kısıtlı Ortamlarda Dinamik Teslimat Planlaması

Bu proje, kısıtlı hava sahası koşullarında bir drone filosunun otonom şekilde **teslimat görevlerini zamanında, güvenli ve verimli şekilde gerçekleştirmesini sağlamak amacıyla** geliştirilmiştir. Çözümde, **A* (A-Star)** ve **Genetik Algoritma (GA)** karşılaştırmalı olarak uygulanmış, batarya yönetimi, no-fly zone'lar, zaman penceresi gibi çok sayıda kısıt modele dahil edilmiştir.

---

## 📌 Proje Özeti

- 🔍 **Amaç**: Karmaşık ortamda görevli drone filosu için rota ve görev atamasını optimize etmek  
- 🔧 **Yöntemler**: A* algoritması, Genetik Algoritma, CSP (Kısıt Tatmin Problemi)  
- 🗺️ **Zorluklar**: No-Fly-Zone, zaman kısıtları, batarya sınırları  
- 📊 **Karşılaştırmalar**: Çalışma süresi, başarı oranı, enerji tüketimi, verimlilik skoru  
- 📁 **Rapor**: Detaylı IEEE-formatlı proje raporu `grup9_rapor.pdf` dosyasında mevcuttur  

---

## 🧠 Kullanılan Teknolojiler

| Teknoloji      | Kullanım Amacı                              |
|----------------|---------------------------------------------|
| Python 3.10+   | Tüm yazılım altyapısı                       |
| Google Colab   | Kod geliştirme ve simülasyon ortamı        |
| matplotlib     | Grafik ve harita görselleştirmeleri        |
| numpy / pandas | Veri işlemleri ve hesaplamalar             |
| heapq          | A* algoritmasındaki öncelik kuyruğu yapısı |
| time / math    | Performans ölçümleri ve matematiksel işlemler |

---

## 📁 Proje Yapısı

```
📦 drone-fleet-optimizer/
├── 📜 grup9_rapor.pdf             # IEEE formatlı detaylı proje raporu
├── 📒 rapor_için.ipynb            # Tüm algoritma ve simülasyon kodları
├── 📁 görseller/                  # Çıktı grafikleri, karşılaştırmalar
└── 📄 README.md                   # Proje tanıtımı (bu dosya)
```

---

## ⚙️ Nasıl Çalıştırılır?

1. [Google Colab](https://colab.research.google.com/) ortamında `.ipynb` dosyasını açın  
2. Kod hücrelerini sırayla çalıştırın  
3. Tüm simülasyon çıktıları terminal ve grafik olarak sunulacaktır

> Gereken kütüphaneler:

```bash
numpy
pandas
matplotlib
heapq
copy
```

Colab ortamında özel bir kurulum gerekmemektedir.

---

## 📊 Örnek Sonuçlar

### Senaryo 1 – 5 Drone, 20 Teslimat
- ✅ A*: %70 teslimat başarı, 3.5s süre  
- ❌ GA: %20 başarı, 0.03s süre  

### Senaryo 2 – 10 Drone, 50 Teslimat
- ✅ A*: %68 teslimat başarı, 4.2s süre  
- ❌ GA: %20 başarı, 0.05s süre  

> Daha fazla detay için `grup9_rapor.pdf` dosyasına göz atabilirsiniz.

---

## 🧩 Öne Çıkan Özellikler

- ✔️ **Zaman penceresi kontrolü** (TimeManager modülü)  
- ✔️ **No-fly zone kontrolü**  
- ✔️ **Enerji modellemesi ve hesaplamaları**  
- ✔️ **Dinamik senaryo üretimi**  
- ✔️ **Görselleştirme: Haritalar + İstatistik Grafikler**  
- ✔️ **Performans karşılaştırmaları: Tablo + Grafik + Rota haritaları**  

---


## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Her hakkı proje sahibine aittir.

---

