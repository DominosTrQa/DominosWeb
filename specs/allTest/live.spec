All Test Live
=====================


Üye Girişi
---------------------------------
tags:live_uyeGirisi

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Giriş - Başarısız giriş 2
-------------------------------
tags:live_uyeGirisiBasarisizGiris

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Başarısız giriş 2
------------------------------
tags:live_uyeGirisiBasarisizGiris2

* Dominos - Live ortamına gidilir
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Ekran kontrolü
------------------------------
tags:live_uyeGirisiEkranKontrolu

* Dominos - Live ortamına gidilir
* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:live_uyeGirisiParolamiUnuttum

* Dominos - Live ortamına gidilir
* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma
-------------------------------
tags:live_uyeOlma

* Dominos - Live ortamına gidilir
* Üye olmak için bilgiler girilir
* Mesafeli satış sözleşmesi işaretlenir
* KVKK ve Ye Kazan E-Posta seçilir ve üye olunur


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:live_uyeOlmaEkrankontrolu

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:live_uyeOlmazBasariliUyeOlma

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarısız Üye Olma
-------------------------------
tags:live_uyeOlmazBasarisizUyeOlma

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:live_uyeOlmazBasariliUyeOlma

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:live_uyeOlmadanDevamEtButtonKontrol

* Dominos - Live ortamına gidilir
* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:live_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Live ortamına gidilir
* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Adrese Teslim - Üye
-----------------------------------------------------
tags:live_uyeAdresEklemeAdreseTeslimUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Profilim popup eklenen adres silinir


Üye Adres Ekleme - Adrese Teslim - Yeni Üye
----------------------------------------------------------
tags:live_uyeAdresEklemeAdreseTeslimYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
tags:live_uyeAdresEklemeGelAlUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
tags:live_uyeAdresEklemeGelAlYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
tags:live_uyeAdresDuzenlemeAdreseTeslimUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Adrese Teslim - Yeni Üye
------------------------------------------
tags:live_uyeAdresDuzenlemeAdreseTeslimYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
tags:live_uyeAdresDuzenlemeGelAlUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Yeni Üye
------------------------------------------
tags:live_uyeAdresDuzenlemeGelAlYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Kampanya 1
-----------------------------------------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeAdreseTeslimUyeKampanya1

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 2 orta boy sosyal pizza kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Yeni Üye -  Kampanya 2
--------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeAdreseTeslimYeniUyeKampanya2

* Dominos - Live ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 2 orta boy sosyal pizza kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Kampanya 3
-----------------------------------------------------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeAdreseTeslimUyeliksizKampanya3

* Dominos - Live ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 2 orta boy sosyal pizza kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye -  Kampanya 4
-----------------------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeGelAlUyeKampanya4

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Gel Al orta boy pizza kahve kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Kampanya 5
--------------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeGelAlYeniUyeKampanya5

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Gel Al orta boy pizza kahve kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz - Kampanya 6
----------------------------------------------------------------------------------------
tags:live_sepeteKampanyaEklemeGelAlUyeliksizKampanya6

* Dominos - Live ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Gel Al orta boy pizza kahve kampanyası secilir
* 2 pizzali kampanya icin siparis olusturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
tags:live_pizzaEklemeAdreseTeslimUye

* Dominos - Live ortamına gidilir
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
tags:live_pizzaEklemeAdreseTeslimYeniUye

* Dominos - Live ortamına gidilir
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
tags:live_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Live ortamına gidilir
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
tags:live_pizzaEklemeGelAlUye

* Dominos - Live ortamına gidilir
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
tags:live_pizzaEklemeGelAlYeniUye

* Dominos - Live ortamına gidilir
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
tags:live_pizzaEklemeGelAlUyeliksiz

* Dominos - Live ortamına gidilir
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
tags:live_sepeteYanUrunEklemeAdreseTeslimUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Yeni Üye
--------------------------------------------------
tags:live_sepeteYanUrunEklemeAdreseTeslimYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
tags:live_sepeteYanUrunEklemeAdreseTeslimUyeliksiz

* Dominos - Live ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Üye
----------------------------------------------
tags:live_sepeteYanUrunEklemeGelAlUye

* Dominos - Live ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Yeni Üye
----------------------------------------------
tags:live_sepeteYanUrunEklemeGelAlYeniUye

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepete Yan Ürün Ekleme - Gel Al - Üyeliksiz
---------------------------------------------
tags:live_sepeteYanUrunEklemeGelAlUyeliksiz

* Dominos - Live ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepette coca cola var mı kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
tags:live_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
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


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
tags:live_sepettenUpsellEklemeAdreseTeslimYeniUye

* Dominos - Live ortamına gidilir
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
tags:live_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
tags:live_sepettenUpsellEklemeGelAlUye

* Dominos - Live ortamına gidilir
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
tags:live_sepettenUpsellEklemeGelAlYeniUye

* Dominos - Live ortamına gidilir
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
tags:live_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiAdreseTeslim

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al
----------------------------
tags:live_servisTipiSecimiGelAl

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
tags:live_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
tags:live_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
-----------------------------------------------------------------------------------------
tags:live_servisTipiSecimiAdreseTeslimUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiGelAlVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
tags:live_servisTipiSecimiGelAlYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
tags:live_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
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
tags:live_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Live ortamına gidilir
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
tags:live_adresSecimiVarOlanUyeAdresTeslimManuelAdresSecimi

* Dominos - Live ortamına gidilir
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
tags:live_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
tags:live_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* Dominos - Live ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
tags:live_adresSecimiYeniUyeGelAlManuelAdresSecimi

* Dominos - Live ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
tags:live_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
tags:live_adresSecimiUyeliksizGelAlManuelAdresSecimi

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
tags:live_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Adreslerim kısmından Sarıyer adresi seçilir
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
tags:live_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Adreslerim kısmından Sarıyer adresi seçilir
* Seçili adres ile devam edilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
tags:live_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Live ortamına gidilir
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
tags:live_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimNakit

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlNakit

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlKrediKartı

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlSmartTicketKart

* Dominos - Live ortamına gidilir
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
tags:regressionLiveodemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlSmartTicketKart

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlSmartTicketKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlMultinet

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlSetCard

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimSetCard

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimPayeKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlPayeKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimPayeKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlPayeKart

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimPayeKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlPayeKart

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Live ortamına gidilir
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
tags:live_odemeTipiSecimiUyeliksizGelAlOnlineOdeme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Live ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
tags:live_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* Dominos - Live ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
tags:live_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeGelAlNotEkleme

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
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
tags:live_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Live ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
tags:live_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Live ortamına gidilir
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
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
tags:live_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Live ortamına gidilir
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
tags:live_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
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
tags:live_siparisIslemleriCanliTestAdresiManuel

* Dominos - Live ortamına gidilir
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
tags:live_siparisIslemleriCanliTestAdresiDropdown

* Dominos - Live ortamına gidilir
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


Şube Atama - Varolan Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
tags:live_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:live_subeAtamaVarolanUyeGelAlYalnizcaIl

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
tags:live_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:live_subeAtamaYeniUye_gelAlYalnizcaIl

* Dominos - Live ortamına gidilir
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
tags:live_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
tags:live_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
tags:live_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - İl İlçe
---------------------------------------------
tags:live_subeAtamaVarolanUyeGelAlIlIlce

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
tags:live_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
tags:live_subeAtamaYeniUyeGelAlIlIlce

* Dominos - Live ortamına gidilir
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
tags:live_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
tags:live_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
tags:live_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
tags:live_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:live_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
tags:live_subeAtamaYeniUyeGelAlIlIlceMahalle

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:live_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
tags:live_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Live ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
tags:live_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
tags:live_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
tags:live_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:live_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:live_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:live_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Live ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:live_uyeKVKKIzniGuncellemeVarolanUyeAyrilmaktanVazgec
//blocked:Düzelince testiniuma eklenecek
* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:live_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgec

* Dominos - Live ortamına gidilir
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
tags:live_uyeKVKKIzniGuncellemeVarolanUyeAyrilmayiOnayla

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:live_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnayla

* Dominos - Live ortamına gidilir
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
tags:live_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgecGiris

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş
---------------------------------------------------------------
tags:live_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnaylaGiris

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:live_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecUyelikBilgilerim

* Dominos - Live ortamına gidilir
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
tags:live_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecUyelikBilgilerim

//Bug OLOTR-1480 çözüldükten sonra Testinium suiteine eklenecek
* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Live ortamına gidilir
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
tags:live_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecProfilim

* Dominos - Live ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecProfilim

* Dominos - Live ortamına gidilir
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
tags:live_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaProfilim

* Dominos - Live ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaProfilim

* Dominos - Live ortamına gidilir
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisUyelikBilgilerim

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisUyelikBilgilerim

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
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
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisProfilim

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Profilim
-------------------------------------------------------------------------
tags:live_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisProfilim

* Dominos - Live ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir