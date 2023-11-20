#!/usr/bin/env python
# coding: utf-8

# Soru 1, 5 farklı meyve isminin olduğu bir list oluşturun ve 3. meyvenin adını ekrana yazdırın.

# In[4]:


meyve_listesi = ["Elma" , "Karpuz" , "Mango" , "Çilek" , "Mandalina"]

print("3. meyve:", meyve_listesi[2])


# Soru 2, En az 3 tane key-value çifti içeren bir dictionary oluşturun. Key’ler ülke isimleri, value’lar
# ülkelerin başkentleri olsun. Bir ülkenin başkentini ekrana yazdırın.

# In[6]:


ulkeler = {
    
    "Türkiye": "Ankara",
    "Kore": "Seul",
    "Fransa": "Paris"
    
}

print("Türkiye'nin Başkenti", ulkeler["Türkiye"])


# Soru 3, Bir sayının tek mi çift mi olduğunu kontrol eden ve sonucu ekrana yazdıran program yazın.

# In[11]:


sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")
else:
    print(f"{sayi} tek bir sayıdır.")


# Soru 4, Bir listedeki sayıları loop ile dolaşarak sayıların karelerini ekrana yazdırın.

# In[13]:


sayilar = [1, 2, 3, 4, 5]

print("Sayıların kareleri:")
for sayi in sayilar:
    kare = sayi ** 2
    print(f"{sayi} sayısının karesi: {kare}")
    


# Soru 5, Öğrencilerin isimlerinin Key, ve aldıkları notların Value’lar olduğu bir dictionary oluşturun.
# Tüm öğrencilerin notlarını ekrana yazdırın.

# In[17]:


ogrenci_notlari = {
    "Abdullah Dol": 100,
    "Beyza Taş": 95,
    "Muhammed Barutçu": 80,
    "Efe Can Eser": 85,
    "Ahmed Kallo": 93
}

for ogrenci, notu in ogrenci_notlari.items():
    print(f"{ogrenci}: {notu}")


# Soru 6, Verilen iç içe (nested) listede geçen tüm elemanları loop ile ekrana yazdırın: [[“Elma”,
# “Armut”, “Muz”, “Portakal”], [“Havuç”, “Brokoli”, “Lahana”], [“Peynir”, “Süt”]]

# In[18]:


nested_liste = [["Elma", "Armut", "Muz", "Portakal"], ["Havuç", "Brokoli", "Lahana"], ["Peynir", "Süt"]]

for liste in nested_liste:
    for eleman in liste:
        print(eleman)


# Soru 7, Bir elemanın listede olup olmadığını kontrol eden bir program yazın. Elemanı ve listeyi
# değişken olarak tanımlayabilirsiniz.

# In[22]:


aranan_eleman = "Portakal"
liste = ["Elma", "Armut", "Muz", "Portakal"]

if aranan_eleman in liste:
    print(f"{aranan_eleman} listede bulunuyor.")
else:
    print(f"{aranan_eleman} listede bulunmuyor.")


# Soru 8, Kullanıcıdan bir sayı alan, ve bu sayı 50’nin üstündeyse “Yüksek”, 25 ile 50 arasındaysa (25
# hariç, 50 dahil) “Orta”, 25 ve altındaysa “Düşük” yazdıran bir program yazın.

# In[23]:


sayi = float(input("Lütfen bir sayı girin: "))

if sayi > 50:
    print("Yüksek")
elif 25 < sayi <= 50:
    print("Orta")
elif sayi <= 25:
    print("Düşük")


# Soru 9, Çalışanların isminin Key, aldıkları maaşın float tipinde Value’lar olduğu bir dictionary
# tanımlayın. 5000 TL’nin altında maaş alanlara %25, üstünde maaş alanlara %15 zam yapan
# bir program yazın. Daha sonra güncellenmiş listeyi ekrana yazdırın.

# In[25]:


maaslar = {
    "Abdullah": 4800.0,
    "Beyza": 5200.0,
    "Ahmet": 6000.0,
    "Efe": 4500.0
}

for isim, maas in maaslar.items():
    if maas < 5000:
        maaslar[isim] += maas * 0.25  
    else:
        maaslar[isim] += maas * 0.15  

print("Güncellenmiş Maaşlar:")
for isim, maas in maaslar.items():
    print(f"{isim}: {maas} TL")


# Soru 10, Verilen iç içe listedeki her bir listenin elemanlarının toplamlarını bir liste içinde yazdıran
# programı yazın: [[4, 2, 6, 5, 8], [10, 2, 7, 9], [5, 4, 3], [19, 1]] (Sonuç: [25, 28, 12, 20]
# olmalı)

# In[26]:


ic_ice_liste = [[4, 2, 6, 5, 8], [10, 2, 7, 9], [5, 4, 3], [19, 1]]

toplam_listesi = [sum(liste) for liste in ic_ice_liste]

print("Sonuç:", toplam_listesi)


# Soru 11, Bir listenin içinde, kitapları ifade eden dictionary objeleri olsun. Her bir kitabın başlık, yazar
# ve yılını ifade eden key’leri ve karşılarında value’ları olsun. En az 4-5 tane kitap tanımlayın.
# 2010 yılından sonra yayınlanmış ve yazar adı A ile başlayan kitapların isimlerini uppercase
# olarak yazdırın. (Buna uygun kitap örnekleri eklersiniz. Yazar adının A ile
# başlamasını .startswith() fonksiyonu ile kontrol edebilir ve kitap adını .upper() fonksiyonu
# ile büyük harfle yazabilirsiniz. Kullanımını internetten araştırın)

# In[27]:


kitap_listesi = [
    {"başlık": "Python Programlama", "yazar": "Atıl Samancıoğlu", "yıl": 2019},
    {"başlık": "Kırlangıç Çığlığı", "yazar": "Ahmet Ümit", "yıl": 2014},
    {"başlık": "Cinayet Tanrısı", "yazar": "Agatha Christie", "yıl": 2010},
    {"başlık": "Python Crash Course", "yazar": "Eric Matthes", "yıl": 2015},
    {"başlık": "Algoritma ve Programlama Mantığı", "yazar": "Burak Tungut", "yıl": 2013}
]

for kitap in kitap_listesi:
    if kitap["yıl"] > 2010 and kitap["yazar"].startswith("A"):
        print(kitap["başlık"].upper())


# Soru 12, “gün.ay.yıl” şeklinde tarihler olan bir liste tanımlayın. Bu tarihleri en yeniden, en eski olana
# doğru sıralayıp çıktı olarak veren kodu yazınız. İpucu: Listenin içinde string’ler de sort
# edilebilir.

# In[32]:


tarih_listesi = ["13.06.2004", "30.05.2022", "26.04.2006", "01.08.2020", "05.11.2019"]

siralanmis_tarihler = sorted(tarih_listesi, key=lambda x: tuple(map(int, reversed(x.split('.')))), reverse=True)

print("Sıralanmış Tarihler:")
for tarih in siralanmis_tarihler:
    print(tarih)


# Soru 13, d1 ve d2 isminde iki adet Dictionary tanımlayın. Key’ler harfler, Value’lar da sayılar olsun.
# Bu iki Dictionary yapısını birleştirip tek bir d3 Dictionary’si dönen Python kodunu yazınız.
# Örnek: d1 = {“a”:1, “b”:3, “d”:5, “f”:2} d2 = {“a”:2, “c”:4, “d”:1, “e”:7, “f”:6, “g”:8}
# Örnek Çıktı: d3 = {“a”:3, “b”:3, “c”: 4, “d”: 6, “e”: 7, “f”: 8, “g”:8}

# In[35]:


d1 = {"a": 1, "b": 3, "d": 5, "f": 2}
d2 = {"a": 2, "c": 4, "d": 1, "e": 7, "f": 6, "g": 8}

d3 = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}

print("(d3) = ", d3)


# In[ ]:




