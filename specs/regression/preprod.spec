Preprod
=====================

     
Üye Girişi
---------------------------------
 tags:regressionPreprod_uyeGirisi

* Dominos - Preprod ortamına gidilir
* "dominostest6@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Giriş - Başarısız giriş 2
-------------------------------
tags:regressionPreprod_uyeGirisiBasarisizGiris

* Dominos - Preprod ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Başarısız giriş 2
------------------------------
tags:regressionPreprod_uyeGirisiBasarisizGiris2

* Dominos - Preprod ortamına gidilir
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Ekran kontrolü
------------------------------
tags:regressionPreprod_uyeGirisiEkranKontrolu

* Dominos - Preprod ortamına gidilir
* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:regressionPreprod_uyeGirisiParolamiUnuttum

* Dominos - Preprod ortamına gidilir
* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma
-------------------------------
 tags:regressionPreprod_uyeOlma

* Dominos - Preprod ortamına gidilir
* Üye olmak için bilgiler girilir
* Mesafeli satış sözleşmesi işaretlenir
* KVKK ve Ye Kazan E-Posta seçilir ve üye olunur


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:regressionPreprod_uyeOlmaEkrankontrolu

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:regressionPreprod_uyeOlmazBasariliUyeOlma

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarısız Üye Olma
-------------------------------
tags:regressionPreprod_uyeOlmazBasarisizUyeOlma

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:regressionPreprod_uyeOlmazBasariliUyeOlma

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:regressionPreprod_uyeOlmadanDevamEtButtonKontrol

* Dominos - Preprod ortamına gidilir
* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:regressionPreprod_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Preprod ortamına gidilir
* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Adrese Teslim - Üye
-----------------------------------------------------
 tags:regressionPreprod_uyeAdresEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Profilim popup eklenen adres silinir


Üye Adres Ekleme - Adrese Teslim - Yeni Üye
----------------------------------------------------------
 tags:regressionPreprod_uyeAdresEklemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
 tags:regressionPreprod_uyeAdresEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
 tags:regressionPreprod_uyeAdresEklemeGelAlYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
 tags:regressionPreprod_uyeAdresDuzenlemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Adrese Teslim - Yeni Üye
------------------------------------------
 tags:regressionPreprod_uyeAdresDuzenlemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
 tags:regressionPreprod_uyeAdresDuzenlemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Yeni Üye
------------------------------------------
 tags:regressionPreprod_uyeAdresDuzenlemeGelAlYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Orta Boy Barbekü Soslu Sucuklu pizza kampanyası
-----------------------------------------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimUyeBarbekuSosluSucukluPizzaKampanyasi

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Tek kişilik kampanyalara tıklanır
* Orta boy barbekü soslu sucuklu pizza kampanyası seçilir
* İlk ürün düzenlemeye tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Yeni Üye -  3 Al 1 Öde
--------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimYeniUye3Al1Ode

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Haftanın kampanyalarına gidilir
* 3 Al 1 öde kampanyası seçilir
* 3 Al 1 öde kampanyası için sipariş oluşturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Orta Boy Barbekü Soslu Sucuklu pizza kampanyası - Kalp şeklinde
-----------------------------------------------------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimUyeliksizortaBoyBarbekuSosluSucukluPizzaKalpSeklindeHamurSecimi

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Tek kişilik kampanyalara tıklanır
* Orta boy barbekü soslu sucuklu pizza kampanyası seçilir
* İlk ürün düzenlemeye tıklanır
* Kalp şeklinde hamura tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye -  Orta Boy Ballı Hardal Soslu Tavuklu
-----------------------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeGelAlUyeOrtaBoyBalliHardalSosluTavuklu

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Kampanyalar Butonuna tıklanır
* Tek kişilik kampanyalara tıklanır
* Orta boy ballı hardal soslu tavuklu pizza kampanyası seçilir ve düzenle
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Orta Boy Ballı Hardal Soslu Tavuklu
--------------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeGelAlYeniUyeOrtaBoyBalliHardalSosluTavuklu

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Tek kişilik kampanyalara tıklanır
* Orta boy ballı hardal soslu tavuklu pizza kampanyası seçilir ve düzenle
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz -  Orta boy ballı hardal soslu tavuklu
----------------------------------------------------------------------------------------
 tags:regressionPreprod_sepeteKampanyaEklemeGelAlUyeliksizOrtaBoyBalliHardalSosluTavuklu

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Tek kişilik kampanyalara tıklanır
* Orta boy ballı hardal soslu tavuklu pizza kampanyası seçilir ve düzenle
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Yeni Üye
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üyeliksiz
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üye
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Yeni Üye
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeGelAlYeniUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üyeliksiz
------------------------------------------------
 tags:regressionPreprod_pizzaEklemeGelAlUyeliksiz

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Üye
----------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Yeni Üye
--------------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir

Sepete Yan Ürün Ekleme - Gel Al - Üye
----------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Yeni Üye
----------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeGelAlYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Üyeliksiz
---------------------------------------------
 tags:regressionPreprod_sepeteYanUrunEklemeGelAlUyeliksiz

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeAdreseTeslimYeniUye

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest5@hotmail.com" ve "a1w2d3r4D" şifre girilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Yeni Üye
---------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeGelAlYeniUye

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üyeliksiz
--------------------------------------------------
 tags:regressionPreprod_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete sufle eklenir
* Sepetim ikonuna tıklanır
* Sepetteki suflenin eklendiği kontrol edilir


Servis Tipi Seçimi - Adrese Teslim
-----------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslim

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al
----------------------------
 tags:regressionPreprod_servisTipiSecimiGelAl

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
-----------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Yeni üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:regressionPreprod_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Manuel - Adres Seçimi
------------------------------------------------------------------
 tags:regressionPreprod_adresSecimiVarOlanUyeAdresTeslimManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
 tags:regressionPreprod_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
 tags:regressionPreprod_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionPreprod_adresSecimiYeniUyeGelAlManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
 tags:regressionPreprod_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionPreprod_adresSecimiUyeliksizGelAlManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
 tags:regressionPreprod_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
 tags:regressionPreprod_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
 tags:regressionPreprod_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Gel Al - Adreslerim - Adres Seçimi
-------------------------------------------------------------
 tags:regressionPreprod_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Gel al olarak devam edilip adreslerime girilerek adrese teslim için İstanbul/Adalar/Burgazada eklenir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Nakit
-----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimNakit

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Nakit
----------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Nakit
----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Nakit
-------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlNakit

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Nakit
------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Nakit
-----------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Kredi Kartı
-----------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Kredi Kartı
----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlKrediKartı

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Kredi Kartı
--------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Kredi Kartı
-------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Kredi Kartı
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Kredi Kartı
------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Sodexo Kart
-------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Sodexo Yemek Çeki
----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Sodexo Yemek Çeki
----------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Sodexo Yemek Çeki
-------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Sodexo Yemek Çeki
-------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Kart
----------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionPreprododemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme smartTicket kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme smartTicket kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Yemek Çeki
-----------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Yemek Çeki
--------------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Yemek Çeki
-------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme smartTicket YemekÇeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme smartTicket YemekÇeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Multinet
--------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Multinet
-------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Multinet
-----------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Multinet
----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlMultinet

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Multinet
--------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Setcard
-------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Setcard
------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Setcard
---------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Setcard
----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSetCard

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Setcard
----------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSetCard

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Setcard
--------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Paye Kart
---------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Paye Kart
---------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlPayeKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Paye Kart
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Paye Kart
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlPayeKart

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Paye Kart
---------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Paye Kart
------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlPayeKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Paye Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Online Ödeme
------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Online Ödeme
--------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir(guest)
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Ödeme Tipi Secimi - Üyeliksiz - Gel AL - Online Ödeme
------------------------------------------------------
 tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Online ödeme seçeneği ile devam edilir(guest)
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Not Ekleme
--------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeGelAlNotEkleme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Varolan Notu Ekleme
--------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Varolan Notu Ekleme
-------------------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Varolan Notu Ekleme
-----------------------------------------------------------------
 tags:regressionPreprod_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Preprod ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş İşlemleri(Canlı) - Test adresi - Manuel
------------------------------------------------
 tags:regressionPreprod_siparisIslemleriCanliTestAdresiManuel

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada adres bilgileri tamamlanır(Kapı No Manuel)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Ödeme şekli seçilir


Sipariş İşlemleri(Canlı) - Test adresi - Dropdown
------------------------------------------
 tags:regressionPreprod_siparisIslemleriCanliTestAdresiDropdown

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Ödeme şekli seçilir


Şube atama - Varolan Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeGelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Adıyaman adresi için ilk şube seçilir
* Adıyaman adresi için ilk şubenin geldiği kontrol edilir
* Seçili şube ile devam edilir(Gel Al)
* "10" saniye bekle
* Şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUye_gelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Adıyaman adresi için ilk şube seçilir
* Adıyaman adresi için ilk şubenin geldiği kontrol edilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - Yalnızca İl
----------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Adıyaman adresi için ilk şube seçilir
* Adıyaman adresi için ilk şubenin geldiği kontrol edilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir
* Gel Al da Şubeleri Göster butonuna tıklanır


Şube atama - Varolan Üye - Gel Al - İl İlçe
---------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeGelAlIlIlce

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Düzce/Akcakoca adresi için ilk şube seçilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeGelAlIlIlce

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Düzce/Akcakoca adresi için ilk şube seçilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir
* Gel Al da Şubeleri Göster butonuna tıklanır


Şube atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Düzce/Akcakoca adresi için ilk şube seçilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* "https://dpe-preprod.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır