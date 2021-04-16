Regression Preprod
=====================


Üye Girişi - Ekran kontrolü
------------------------------
tags:regressionPreprod_uyeGirisiEkranKontrolu

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:regressionPreprod_uyeGirisiParolamiUnuttum

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


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


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:regressionPreprod_uyeOlmazBasariliUyeOlmaİki

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:regressionPreprod_uyeOlmadanDevamEtButtonKontrol

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:regressionPreprod_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
tags:regressionPreprod_uyeAdresEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
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
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adalar adresi eklenir
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
tags:regressionPreprod_uyeAdresDuzenlemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
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


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Kampanya 1
----------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimUyeKampanya1

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Yeni Üye -  Kampanya 2
---------------------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimYeniUyeKampanya2

* Dominos - Preprod ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Kampanya 3
-----------------------------------------------------------------------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeAdreseTeslimUyeliksizKampanya3

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye -  Kampanya 4
-----------------------------------------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeGelAlUyeKampanya4

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Kampanya 5
--------------------------------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeGelAlYeniUyeKampanya5

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz - Kampanya 6
----------------------------------------------------------------------------------------
tags:regressionPreprod_sepeteKampanyaEklemeGelAlUyeliksizKampanya6

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
tags:regressionPreprod_pizzaEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Pre)
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üyeliksiz
------------------------------------------------
tags:regressionPreprod_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Pre)
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üye
------------------------------------------------
tags:regressionPreprod_pizzaEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Pre)
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üyeliksiz
------------------------------------------------
tags:regressionPreprod_pizzaEklemeGelAlUyeliksiz

* Dominos - Preprod ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Pre)
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
tags:regressionPreprod_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında Çikolatalı Sufle yazısının geldiği kontrol edilir


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
tags:regressionPreprod_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
tags:regressionPreprod_sepettenUpsellEklemeGelAlUye

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest7@hotmail.com" ve "a1w2d3r4D" şifre girilir
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
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepetteki ürünlerden Sufle eklenir
* Sepetim ikonuna tıklanır
* Sepette Sufle olduğu kontrol edilir


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
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
tags:regressionPreprod_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
tags:regressionPreprod_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
tags:regressionPreprod_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
tags:regressionPreprod_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Kayitli adres cikarsa adres sec yoksa servis tipi sec
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
tags:regressionPreprod_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
tags:regressionPreprod_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir

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
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
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
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Şubenin Ayazağa Şubesi olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
tags:regressionPreprod_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
tags:regressionPreprod_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Adres Seçimi - Yeni Üye - Gel Al - Adreslerim - Adres Seçimi
-------------------------------------------------------------
tags:regressionPreprod_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Gel al olarak devam edilip adreslerime girilerek adrese teslim için İstanbul/Adalar/Burgazada eklenir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Nakit
----------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Nakit
----------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Kredi Kartı
-----------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Kredi Kartı
--------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Sodexo Kart
-------------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Sodexo Yemek Çeki
----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Sodexo Yemek Çeki
-------------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartTicketKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme smartTicket kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Yemek Çeki
-----------------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Yemek Çeki
--------------------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Multinet
--------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Multinet
----------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlMultinet

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Setcard
-------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Setcard
---------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Setcard
--------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Paye Kart
---------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlPayeKart

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Paye Kart
------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
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
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Paye Kart
---------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimPayeKart

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
tags:regressionPreprod_odemeTipiSecimiUyeliksizGelAlPayeKart

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Online Ödeme
------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Online Ödeme
--------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Online Ödeme
------------------------------------------------------------
tags:regressionPreprod_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* "dominostest8@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Cookie varsa kapat butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Siparis tamamlanir(guest) 2
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar siparis ver butonunu ve mesafeli satis tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Cookie varsa kapat butonuna tıklanır
* Adrese teslim servis tipi secilir ve kontrolu yapilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Lütfen zile basmayınız seçilir
* Siparis tamamlanir(guest) 2
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar siparis ver butonunu ve mesafeli satis tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Preprod ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* "dominostest8@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Cookie varsa kapat butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir(guest)
* Siparis tamamlanir(guest) 2
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar siparis ver butonunu ve mesafeli satis tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
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
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
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
* Anasayfadaki dominos logosuna tıklanır
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
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Varolan Notu Ekleme
-----------------------------------------------------------------
tags:regressionPreprod_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza eklerken kampanyali urunlere gidilir ve kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
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
tags:regressionPreprod_siparisIslemleriCanliTestAdresiDropdown

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Cookie kapat butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeGelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
* "dominostest8@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUye_gelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe
-------------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Akçakoca Şubesi olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Pre)
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube Atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Preprod ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Preprod ortamına gidilir
* Giris Yap butonuna tiklanir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Cookie kapat butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionPreprod_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionPreprod_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube Atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
tags:regressionPreprod_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Preprod ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:regressionPreprod_uyeKVKKIzniGuncellemeVarolanUyeAyrilmaktanVazgec

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Uye - Ayrilmaktan Vazgeç
-----------------------------------------------------------
tags:regressionPreprod_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgec

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeKVKKIzniGuncellemeVarolanUyeAyrilmayiOnayla

* Dominos - Preprod ortamına gidilir
* "dominostest7@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
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
tags:regressionPreprod_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnayla

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgecGiris

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnaylaGiris

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecUyelikBilgilerim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecUyelikBilgilerim

//Bug OLOTR-1480 çözüldükten sonra Testinium suiteine eklenecek
* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecProfilim

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecProfilim

* Dominos - Preprod ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
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


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Profilim
--------------------------------------------------------------------------
tags:regressionPreprod_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaProfilim

* Dominos - Preprod ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Pre)
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaProfilim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisUyelikBilgilerim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisUyelikBilgilerim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisProfilim

* Dominos - Preprod ortamına gidilir
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
tags:regressionPreprod__uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisProfilim

* Dominos - Preprod ortamına gidilir
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