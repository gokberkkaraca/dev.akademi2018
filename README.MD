# Sorun
sahibinden.com internet sitesi Türkiye'nin en popüler internet sitelerinden biri olup çeşitli özelliklere sahip kullanıcılar tarafından ziyaret edilmektedir. Bu kullanıcılar sahibinden.com için farklı kullanım alışkanlıklarına sahip olabilirler. Örneğin, bazı kullanıcılar mobil cihazlarından gün içerisinde hızlıca ilanlara göz gezdirirken bazıları da akşam bilgisayar başında saatlerini harcayarak site üzerinde detaylı aramalar yapar.

Site kullanım şekillerindeki farklılıklar, kişilerin bazı özelliklerine göre gruplandırılabilir. Bu değişkenler; meslek, cinsiyet, eğitim durumu, evlilik durumu ve şehir olabilir. Site kullanımındaki farklılıklar, kullanıcıların gördükleri reklamlara tıklama oranına da yansıyacaktır. Örneğin öğrenci grubundaki kullanıcılar reklamlara en çok akşam saatlerinde tıklarken, çalışmayan kullanıcılar gün içerisinde de yüksek tıklama oranları gösterebilir. Eğer bu konuda detaylı bir analiz yapılıp reklam gösterim yoğunluğu zamana göre optimize edilebilirse, reklam verenlerin ayırdığı reklam bütçesi en yüksek tıklama oranı elde edilerek etkili şekilde kullanılmış olur. Bu projenin amacı, yukarıda bahsedilen soruna bir çözüm oluşturmak amacıyla veri analizi gerçekleştirmektir.

# Çözüm
Öncelikle, günü farklı saat dilimlerine ayırmak kullanıcıların hangi saatlerde reklamlara tıklama açısından daha aktif olduğunu görmeye yardımcı olur. Bu amaçla, kullanıcıların aktiviteleri
    
    1. 00.00 - 03.00
    2. 03.00 - 06.00 
    3. 06.00 - 09.00
    4. 09.00 - 12.00
    5. 12.00 - 15.00
    6. 15.00 - 18.00
    7. 18.00 - 21.00
    8. 21.00 - 24.00
    
Olmak üzere 8 gruba ayrılmış ve her kullanıcının kullanım alışkanlıkları ayrı ayrı analiz edilmiştir. Daha sonra bu kullanıcılar ortak özelliklerine göre gruplandırılarak her grubun kullanım alışkanlıkları istatistiksel olarak hesaplanmıştır. Her gruba ait veriler, sonuçların çıkarımlarını kolaylaştırmak amacıyla grafiklere dökülerek görselleştirilmiştir.

# Kullanım
Terminal uygulaması Python3.7 ile geliştirilmiştir.
   
    1. json
    2. matplotlib
    3. datetime

Kütüphaneleri kullanılmıştır ve uygulamanın düzgün çalışması için yüklü olmaları gerekmektedir. Ön koşullar sağlandıktan sonra ```python3 devakademi2018.py``` komutu ile çalıştırılabilir. Üretilen grafikler ```./plots/``` klasöründe bulunmaktadır.

# Sonuç
Yapılan analiz sonucunda üretilen grafikler, reklam bütçelerinin yararlı kullanımı için önemli bilgiler vermektedir. Kullanıcıların reklamlara tıklama oranlarının düşük olduğu saatlerde reklamların daha az gösterimi, kullanıcıların reklamlara tıklama oranlarının yüksek olduğu saatlerde ise reklamların daha sık gösterimi kullanıcı gruplarına. özelleştirilmiş şekilde yapılabilir. Analiz sonucunda üretilen grafikler şu şekildedir;

## Meslek Grubu
![alt text](https://raw.githubusercontent.com/gokberkkaraca/dev.akademi2018/master/plots/jobs.png)

## Eğitim Durumu
![alt text](https://raw.githubusercontent.com/gokberkkaraca/dev.akademi2018/master/plots/education_levels.png)

## Evlilik Durumu
![alt text](https://raw.githubusercontent.com/gokberkkaraca/dev.akademi2018/master/plots/martial_statuses.png)

## Cinsiyet
![alt text](https://raw.githubusercontent.com/gokberkkaraca/dev.akademi2018/master/plots/genders.png)

## Şehir
![alt text](https://raw.githubusercontent.com/gokberkkaraca/dev.akademi2018/master/plots/cities.png)
