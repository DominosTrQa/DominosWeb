Regression Kubernetes
=====================


Üye Girişi
---------------------------------
tags:regressionK8s_uyeGirisi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir


Üye Giriş - Başarısız giriş 2
-------------------------------
tags:regressionK8s_uyeGirisiBasarisizGiris

* Dominos - Kubernetes ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Başarısız giriş 2
------------------------------
tags:regressionK8s_uyeGirisiBasarisizGiris2

* Dominos - Kubernetes ortamına gidilir
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Ekran kontrolü
------------------------------
tags:regressionK8s_uyeGirisiEkranKontrolu

* Dominos - Kubernetes ortamına gidilir
* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:regressionK8s_uyeGirisiParolamiUnuttum

* Dominos - Kubernetes ortamına gidilir
* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma
-------------------------------
tags:regressionK8s_uyeOlma

* Dominos - Kubernetes ortamına gidilir
* Üye olmak için bilgiler girilir
* Mesafeli satış sözleşmesi işaretlenir
* KVKK ve Ye Kazan E-Posta seçilir ve üye olunur


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:regressionK8s_uyeOlmaEkrankontrolu

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:regressionK8s_uyeOlmazBasariliUyeOlma

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarısız Üye Olma
-------------------------------
tags:regressionK8s_uyeOlmazBasarisizUyeOlma

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:regressionK8s_uyeOlmazBasarisizUyeOlma2

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:regressionK8s_uyeOlmadanDevamEtButtonKontrol

* Dominos - Kubernetes ortamına gidilir
* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:regressionK8s_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Kubernetes ortamına gidilir
* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Adrese Teslim - Üye
-----------------------------------------------------
tags:regressionK8s_uyeAdresEklemeAdreseTeslimUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Profilim popup eklenen adres silinir


Üye Adres Ekleme - Adrese Teslim - Yeni Üye
----------------------------------------------------------
tags:regressionK8s_uyeAdresEklemeAdreseTeslimYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
tags:regressionK8s_uyeAdresEklemeGelAlUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
tags:regressionK8s_uyeAdresEklemeGelAlYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
tags:regressionK8s_uyeAdresDuzenlemeAdreseTeslimUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Adrese Teslim - Yeni Üye
------------------------------------------
tags:regressionK8s_uyeAdresDuzenlemeAdreseTeslimYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
tags:regressionK8s_uyeAdresDuzenlemeGelAlUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Yeni Üye
------------------------------------------
tags:regressionK8s_uyeAdresDuzenlemeGelAlYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Kampanya 1
-----------------------------------------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeAdreseTeslimUyeKampanya1

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Yeni Üye -  Kampanya 2
--------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeAdreseTeslimYeniUyeKampanya2

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Kampanya 3
-----------------------------------------------------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeAdreseTeslimUyeliksizKampanya3

* Dominos - Kubernetes ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye -  Kampanya 4
-----------------------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeGelAlUyeKampanya4

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Kampanya 5
--------------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeGelAlYeniUyeKampanya5

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz - Kampanya 6
----------------------------------------------------------------------------------------
tags:regressionK8s_sepeteKampanyaEklemeGelAlUyeliksizKampanya6

* Dominos - Kubernetes ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
tags:regressionK8s_pizzaEklemeAdreseTeslimUye

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_pizzaEklemeAdreseTeslimYeniUye

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_pizzaEklemeGelAlUye

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_pizzaEklemeGelAlYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üyeliksiz
------------------------------------------------
tags:regressionK8s_pizzaEklemeGelAlUyeliksiz

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_sepeteYanUrunEklemeAdreseTeslimUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Yeni Üye
--------------------------------------------------
tags:regressionK8s_sepeteYanUrunEklemeAdreseTeslimYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
tags:regressionK8s_sepeteYanUrunEklemeAdreseTeslimUyeliksiz

* Dominos - Kubernetes ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Üye
----------------------------------------------
tags:regressionK8s_sepeteYanUrunEklemeGelAlUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Yeni Üye
----------------------------------------------
tags:regressionK8s_sepeteYanUrunEklemeGelAlYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Üyeliksiz
---------------------------------------------
tags:regressionK8s_sepeteYanUrunEklemeGelAlUyeliksiz

* Dominos - Kubernetes ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
tags:regressionK8s_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
tags:regressionK8s_sepettenUpsellEklemeAdreseTeslimYeniUye

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
tags:regressionK8s_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
tags:regressionK8s_sepettenUpsellEklemeGelAlUye

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest1@hotmail.com" ve "a1w2d3r4D" şifre girilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Yeni Üye
---------------------------------------
tags:regressionK8s_sepettenUpsellEklemeGelAlYeniUye

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
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
tags:regressionK8s_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim
-----------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslim

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al
----------------------------
tags:regressionK8s_servisTipiSecimiGelAl

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
tags:regressionK8s_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
-----------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslimUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiGelAlVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiGelAlYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
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
tags:regressionK8s_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
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
tags:regressionK8s_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
tags:regressionK8s_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_adresSecimiVarOlanUyeAdresTeslimManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
tags:regressionK8s_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
tags:regressionK8s_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
tags:regressionK8s_adresSecimiYeniUyeGelAlManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
tags:regressionK8s_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
tags:regressionK8s_adresSecimiUyeliksizGelAlManuelAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
tags:regressionK8s_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
tags:regressionK8s_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
tags:regressionK8s_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Gel al olarak devam edilip adreslerime girilerek adrese teslim için İstanbul/Adalar/Burgazada eklenir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Nakit
-----------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimNakit

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Nakit
-------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlNakit

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
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
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Nakit
-----------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Kredi Kartı
-----------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlKrediKartı

* Dominos - Kubernetes ortamına gidilir
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
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Kredi Kartı
-------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
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
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Kredi Kartı
------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Sodexo Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Sodexo Kart
-------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Sodexo Yemek Çeki
----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Sodexo Yemek Çeki
----------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Sodexo Yemek Çeki
-------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Sodexo Yemek Çeki
-------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Sodexo Yemek Çeki
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Kart
----------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme smartTicket kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlSmartTicketKart

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme smartTicket kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Yemek Çeki
-----------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Yemek Çeki
--------------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Yemek Çeki
-------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Multinet
--------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Multinet
-------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Multinet
-----------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Multinet
----------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlMultinet

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Multinet
--------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Setcard
-------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Setcard
------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Setcard
---------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Setcard
----------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlSetCard

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Setcard
----------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimSetCard

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Setcard
--------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Paye Kart
---------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimPayeKart

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Paye Kart
---------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlPayeKart

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Paye Kart
------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimPayeKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Paye Kart
------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlPayeKart

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Paye Kart
---------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimPayeKart

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Paye Kart
------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlPayeKart

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
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


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Online Ödeme
------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Online Ödeme
--------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Ödeme Tipi Secimi - Üyeliksiz - Gel AL - Online Ödeme
------------------------------------------------------
tags:regressionK8s_odemeTipiSecimiUyeliksizGelAlOnlineOdeme

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Kubernetes ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
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
tags:regressionK8s_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Kubernetes ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
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
tags:regressionK8s_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Kubernetes ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Kubernetes ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
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
tags:regressionK8s_siparisNotuEklemeVarolanUyeGelAlNotEkleme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Kubernetes ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Varolan Notu Ekleme
--------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* Dominos - Kubernetes ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Varolan Notu Ekleme
-------------------------------------------------------------------------
tags:regressionK8s_siparisNotuEklemeVarolanUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Cookie varsa kapat butonuna tıklanır
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
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
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
tags:regressionK8s_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş İşlemleri(Canlı) - Test adresi - Manuel
------------------------------------------------
tags:regressionK8s_siparisIslemleriCanliTestAdresiManuel

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
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
tags:regressionK8s_siparisIslemleriCanliTestAdresiDropdown

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
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


Şube Atama - Varolan Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeGelAlYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir (GelAl)
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:regressionK8s_subeAtamaYeniUye_gelAlYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - Yalnızca İl
----------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - İl İlçe
---------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeGelAlIlIlce

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir (GelAl)
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeGelAlIlIlce

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe
-------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir (GelAl)
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeGelAlIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Sube duzenlemeye tiklanir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionK8s_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionK8s_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionK8s_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeVarolanUyeAyrilmaktanVazgec
//blocked:Düzelince testiniuma eklenecek
* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Uye - Ayrilmaktan Vazgeç
-----------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgec

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla
----------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeVarolanUyeAyrilmayiOnayla

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla
-------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnayla

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giriş
-----------------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgecGiris

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş
---------------------------------------------------------------
tags:regressionK8s_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnaylaGiris

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Üyelik Bilgilerim
-------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecUyelikBilgilerim

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç - Üyelik Bilgilerim
-------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecUyelikBilgilerim

//Bug OLOTR-1480 çözüldükten sonra Testinium suiteine eklenecek
* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç - Profilim
--------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecProfilim

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Profilim
-------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecProfilim

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Profilim
--------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaProfilim

* Dominos - Kubernetes ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Profilim
-----------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaProfilim

* Dominos - Kubernetes ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giriş - Üyelik Bilgilerim
-----------------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisUyelikBilgilerim

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Üyelik Bilgilerim
---------------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisUyelikBilgilerim

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giris - Profilim
--------------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisProfilim

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Profilim
-------------------------------------------------------------------------
tags:regressionK8s_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisProfilim

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir