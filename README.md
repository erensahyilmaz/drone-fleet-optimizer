
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
| Python 3.10+   | Algoritma ve simülasyon ortamı             |
| Google Colab   | Etkileşimli notebook geliştirme ve testler |
| matplotlib     | Grafik ve görselleştirme                   |
| numpy / pandas | Veri işleme ve analiz                      |
| heapq          | A* algoritmasındaki öncelik kuyruğu yapısı |
| time / math    | Performans ölçümü, matematiksel işlemler  |

---

## 📁 Proje Yapısı

```
📦 drone-fleet-optimizer/
├── 📜 grup9_rapor.pdf             # IEEE formatlı detaylı proje raporu
├── 📒 rapor_için.ipynb            # Tüm algoritma ve simülasyon kodları
├── 📁 results/                    # Çıktı grafikleri, karşılaştırmalar
└── 📄 README.md                   # Proje tanıtımı (bu dosya)
```

---

## ⚙️ Nasıl Çalıştırılır?

1. [Google Colab](https://colab.research.google.com/) ortamında `drone-fleet-optimizer.ipynb` dosyasını açın  
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

![Senaryo 1 Grafik](https://github.com/erensahyilmaz/drone-fleet-optimizer/blob/1a5461db6e8857f3c53b6855be9aa8c43d22fda9/results/scenario1_comparison%20(1).png)

### Senaryo 2 – 10 Drone, 50 Teslimat
- ✅ A*: %68 teslimat başarı, 4.2s süre  
- ❌ GA: %20 başarı, 0.05s süre  

![Senaryo 2 Grafik](https://github.com/erensahyilmaz/drone-fleet-optimizer/blob/1a5461db6e8857f3c53b6855be9aa8c43d22fda9/results/scenario2_comparison%20(1).png)

> Haritalar üzerinden dronelara atanmış teslimat noktaları, no-fly zone çevresi ve zaman penceresi etkileri görselleştirilmiştir.

---


### ⚡ Benchmark: Büyük Ölçekli Testler (3 Tekrar Ortalaması)

| Algoritma | Ortalama Süre (s) | < 1 dk Kriteri |
|-----------|--------------------|----------------|
| A*        | 3.67               | ✅ Başarılı     |
| GA        | 5.98               | ✅ Başarılı     |

> Detaylı analizler `drone-fleet-optimizer.ipynb` dosyasında ve raporda yer almaktadır.

---

## 🗺️ Performans Görselleştirmeleri

Senaryolara ait algoritmaların performans karşılaştırması ve zaman karmaşıklığı grafiği:

![Performan Karşılaştırması](https://github.com/erensahyilmaz/drone-fleet-optimizer/blob/1a5461db6e8857f3c53b6855be9aa8c43d22fda9/results/performance_comparison.png)

### ⏱️ Zaman Karmaşıklığı Analizi (n: Teslimat Sayısı)

- **A\***: ~O(n²) — Katsayı: 0.006096  
- **GA**: ~O(n²) — Katsayı: 0.000782  

![Zaman Karmaşıklığı](https://github.com/erensahyilmaz/drone-fleet-optimizer/blob/1a5461db6e8857f3c53b6855be9aa8c43d22fda9/results/time_complexity_analysis.png)

> A* algoritması küçük örneklerde hızlı çalışsa da, teslimat sayısı arttıkça GA ile rekabet zorlaşıyor.

---


## 📄 Detaylı Proje Raporu

📎 Daha fazla detay için [grup9_rapor.pdf dosyası](https://github.com/erensahyilmaz/drone-fleet-optimizer/blob/1a5461db6e8857f3c53b6855be9aa8c43d22fda9/grup9_rapor.pdf)'na göz atabilirsiniz.

---

## 🧩 Öne Çıkan Özellikler

- ✔️ **Zaman penceresi kontrolü** (TimeManager modülü)  
- ✔️ **No-fly zone kontrolü**  
- ✔️ **Enerji modellemesi ve hesaplamaları**  
- ✔️ **Dinamik senaryo üretimi**  
- ✔️ **Görselleştirme: Haritalar + İstatistik Grafikler**  
- ✔️ **Performans karşılaştırmaları: Tablo + Grafik + Rota haritaları**  

---

## 🌐 Google Colab Bağlantıları

- ✔️ [https://colab.research.google.com/drive/1bftxnmM-SsSEeiSm7DLs04CEf-QSJg7a?usp=sharing](https://colab.research.google.com/drive/1wublP0dxUKPdEeq1xTyb6ALofQE7kx32?usp=sharing#scrollTo=D_XDYBsuJdqJ&uniqifier=2)
---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Her hakkı proje sahibine aittir.

---

