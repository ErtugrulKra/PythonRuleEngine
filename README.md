# Rule Engine vs Branching Complexity Comparison

Bu proje, indirim hesaplama işlemlerinde **Branching** ve **Rule Engine** yaklaşımlarının **Cyclomatic Complexity** ve **Cognitive Complexity** metriklerine göre karşılaştırılmasını yapar.

## 📋 Proje Açıklaması

Proje, kullanıcı üyelik türü, yaş ve bölge bilgilerine göre fiyat indirimleri hesaplayan iki farklı yaklaşımı karşılaştırır:

1. **Branching Yaklaşımı**: Geleneksel if-elif-else yapıları kullanarak koşullu mantık
2. **Rule Engine Yaklaşımı**: Kurallar ve aksiyonlar tanımlayarak esnek bir sistem

## 🚀 Özellikler

- ✅ İki farklı yaklaşımın sonuçlarını karşılaştırma
- ✅ Cyclomatic Complexity analizi
- ✅ Cognitive Complexity analizi
- ✅ Sonuç doğrulama ve tutarlılık kontrolü
- ✅ Detaylı complexity metrikleri ve karşılaştırma raporu

## 📊 Complexity Metrikleri

### Cyclomatic Complexity
- **Branching**: 5
- **Rule Engine**: 4

### Cognitive Complexity
- **Branching**: 8
- **Rule Engine**: 6

## 🛠️ Kurulum

### Gereksinimler
- Python 3.6+
- Hiçbir ek kütüphane gerekmez (sadece standart kütüphaneler kullanılır)

### Kurulum Adımları
```bash
# Repository'yi klonlayın
git clone https://github.com/ErtugrulKra/PythonRuleEngine.git

# Proje dizinine gidin
cd PythonRuleEngine

# Kodu çalıştırın
python main.py
```

## 📁 Proje Yapısı

```
RuleEngine/
├── main.py              # Ana uygulama dosyası
├── rule_engine.py       # Rule Engine sınıfı
└── README.md           # Bu dosya
```

## 🔧 Kullanım

### Temel Kullanım
```python
python main.py
```

### Çıktı Örneği
```
======================================================================
COMPLEXITY KARŞILAŞTIRMASI
======================================================================

1. BRANCHING YÖNTEMİ COMPLEXITY ANALİZİ:
--------------------------------------------------
   Fonksiyon: calculate_discount_branching
   Cyclomatic Complexity: 5
   Cognitive Complexity: 8

2. RULE ENGINE YÖNTEMİ COMPLEXITY ANALİZİ:
--------------------------------------------------
   Engine Method:
     Cyclomatic Complexity: 0
     Cognitive Complexity: 0
   Rules:
     Cyclomatic Complexity: 4
     Cognitive Complexity: 6
   Toplam:
     Cyclomatic Complexity: 4
     Cognitive Complexity: 6

3. COMPLEXITY KARŞILAŞTIRMASI:
--------------------------------------------------
   Cyclomatic Complexity:
     Daha basit: Rule Engine
     Fark: 1 puan
   Cognitive Complexity:
     Daha basit: Rule Engine
     Fark: 2 puan

4. GENEL DEĞERLENDİRME:
--------------------------------------------------
   ✓ Rule Engine yöntemi her iki complexity metrikinde de daha basit
   ✓ Rule Engine yöntemi daha kolay anlaşılır ve bakımı yapılabilir
```

## 📈 Sonuçlar ve Analiz

### Complexity Karşılaştırması

| Metrik | Branching | Rule Engine | Kazanan |
|--------|-----------|-------------|---------|
| Cyclomatic Complexity | 5 | 4 | Rule Engine |
| Cognitive Complexity | 8 | 6 | Rule Engine |

### Avantajlar

#### Rule Engine Yaklaşımı
- ✅ Daha düşük complexity skorları
- ✅ Kuralların kolayca eklenmesi/çıkarılması
- ✅ Daha modüler ve esnek yapı
- ✅ Test edilebilirlik

#### Branching Yaklaşımı
- ✅ Daha basit ve anlaşılır kod
- ✅ Daha az overhead
- ✅ Doğrudan kontrol akışı

## 🔍 Kod Örnekleri

### Branching Yaklaşımı
```python
def calculate_discount_branching(user):
    if user["membership"] == "gold":
        if user["age"] > 18:
            message = f"{user['membership'].title()} adult member"
            final_price = user["base_price"] * 0.80  # %20 indirim
        else:
            message = f"{user['membership'].title()} young member"
            final_price = user["base_price"] * 0.85  # %15 indirim
    elif user["membership"] == "silver":
        if user["region"] == "EU":
            message = f"{user['membership'].title()} EU member"
            final_price = user["base_price"] * 0.95  # %5 indirim
        else:
            message = "Regular member"
            final_price = user["base_price"]
    else:
        message = "Regular member"
        final_price = user["base_price"]
    
    return {"message": message, "final_price": final_price}
```

### Rule Engine Yaklaşımı
```python
def setup_rule_engine():
    engine = RuleEngine()
    
    engine.add_rule(
        lambda u: u["membership"] == "gold" and u["age"] > 18,
        lambda u: {
            "message": f"{u['membership'].title()} adult member",
            "final_price": u["base_price"] * 0.80
        }
    )
    
    engine.add_rule(
        lambda u: True,  # default
        lambda u: {
            "message": "Regular member",
            "final_price": u["base_price"]
        }
    )
    
    return engine
```

## 🧪 Test Verileri

Proje, 10 farklı kullanıcı profili ile test edilmiştir:

```python
users = [
    {"age": 25, "membership": "gold", "region": "EU", "base_price": 100},
    {"age": 17, "membership": "gold", "region": "US", "base_price": 120},
    {"age": 30, "membership": "silver", "region": "EU", "base_price": 80},
    # ... daha fazla test verisi
]
```

## 📚 Complexity Metrikleri Hakkında

### Cyclomatic Complexity
- Kodun kaç farklı yoldan çalışabileceğini ölçer
- if, elif, else, for, while, try-except gibi dallanma noktalarını sayar
- Düşük değerler daha basit kod anlamına gelir

### Cognitive Complexity
- Kodun anlaşılması için gereken zihinsel çabayı ölçer
- İç içe geçmiş yapıları ve mantıksal operatörleri dikkate alır
- Düşük değerler daha kolay anlaşılır kod anlamına gelir

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 👨‍💻 Geliştirici

**Ertugrul Kara**
- GitHub: [@ErtugrulKra](https://github.com/ErtugrulKra)

 
## 📞 İletişim

Sorularınız için GitHub Issues kullanabilir veya [@ErtugrulKra](https://github.com/ErtugrulKra) ile iletişime geçebilirsiniz.

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
