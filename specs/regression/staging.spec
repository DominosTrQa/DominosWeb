Staging
===================


Üye Girişi
---------------------------------
tags:regressionStaging_uyeGirisi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Giriş - Başarısız giriş 2
-------------------------------
tags:regressionStaging_uyeGirisiBasarisizGiris

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Başarısız giriş 2
------------------------------
tags:regressionStaging_uyeGirisiBasarisizGiris2

* "https://dpe-staging.dominos.com.tr/" adresine git
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Ekran kontrolü
------------------------------
tags:regressionStaging_uyeGirisiEkranKontrolu

* "https://dpe-staging.dominos.com.tr/" adresine git
* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:regressionStaging_uyeGirisiParolamiUnuttum

* "https://dpe-staging.dominos.com.tr/" adresine git
* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma
-------------------------------
tags:regressionStaging_uyeOlma

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olmak için bilgiler girilir
* Mesafeli satış sözleşmesi işaretlenir
* KVKK ve Ye Kazan E-Posta seçilir ve üye olunur


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:regressionStaging_uyeOlmaEkrankontrolu

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:regressionStaging_uyeOlmazBasariliUyeOlma

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarısız Üye Olma
-------------------------------
tags:regressionStaging_uyeOlmazBasarisizUyeOlma

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:regressionStaging_uyeOlmazBasariliUyeOlma

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:regressionStaging_uyeOlmadanDevamEtButtonKontrol

* "https://dpe-staging.dominos.com.tr/" adresine git
* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:regressionStaging_uyeOlmadanDevamEtEkranKontrolu

* "https://dpe-staging.dominos.com.tr/" adresine git
* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Adrese Teslim - Üye
-----------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeAdreseTeslimUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Profilim popup eklenen adres silinir


Üye Adres Ekleme - Adrese Teslim - Yeni Üye
----------------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeAdreseTeslimYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeGelAlUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeGelAlYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeAdreseTeslimUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Adrese Teslim - Yeni Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeAdreseTeslimYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeGelAlUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Yeni Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeGelAlYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Orta Boy Barbekü Soslu Sucuklu pizza kampanyası
-----------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeAdreseTeslimUyeBarbekuSosluSucukluPizzaKampanyasi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
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
 tags:regressionStaging_sepeteKampanyaEklemeAdreseTeslimYeniUye3Al1Ode

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Haftanın kampanyalarına gidilir (Staging)
* 3 Al 1 öde kampanyası seçilir
* 3 Al 1 öde kampanyası için sipariş oluşturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Orta Boy Barbekü Soslu Sucuklu pizza kampanyası - Kalp şeklinde
-----------------------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeAdreseTeslimUyeliksizortaBoyBarbekuSosluSucukluPizzaKalpSeklindeHamurSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
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


Sepete Kampanya Ekleme - Gel Al - Üye - Orta Boy Barbekü Soslu Sucuklu pizza kampanyası
-----------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeGelAlUyeBarbekuSosluSucukluPizzaKampanyasi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Kampanyalar Butonuna tıklanır
* Şubene özel fırsatlar(Staging)
* Orta boy barbekü soslu sucuklu pizza kampanyası seçilir (Staging)
* İlk ürün düzenlemeye tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Orta boy ballı hardal soslu tavuklu
--------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeGelAlYeniUyeOrtaBoyBalliHardalSosluTavuklu

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Orta boy ballı hardal soslu tavuklu pizza kampanyası seçilir ve düzenle (Staging)
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz -  Orta boy ballı hardal soslu tavuklu
----------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeGelAlUyeliksizOrtaBoyBalliHardalSosluTavuklu

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Orta boy ballı hardal soslu tavuklu pizza kampanyası seçilir ve düzenle (Staging)
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
 tags:regressionStaging_pizzaEklemeAdreseTeslimUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Yeni Üye
------------------------------------------------
 tags:regressionStaging_pizzaEklemeAdreseTeslimYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_pizzaEklemeAdreseTeslimUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_pizzaEklemeGelAlUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Yeni Üye
------------------------------------------------
 tags:regressionStaging_pizzaEklemeGelAlYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_pizzaEklemeGelAlUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_sepeteYanUrunEklemeAdreseTeslimUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Adrese Teslim - Yeni Üye
--------------------------------------------------
 tags:regressionStaging_sepeteYanUrunEklemeAdreseTeslimYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:regressionStaging_sepeteYanUrunEklemeAdreseTeslimUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)

Sepete Yan Ürün Ekleme - Gel Al - Üye
----------------------------------------------
 tags:regressionStaging_sepeteYanUrunEklemeGelAlUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Gel Al - Yeni Üye
----------------------------------------------
 tags:regressionStaging_sepeteYanUrunEklemeGelAlYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Gel Al - Üyeliksiz
---------------------------------------------
 tags:regressionStaging_sepeteYanUrunEklemeGelAlUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeGelAlUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest6@hotmail.com" ve "Testinium123" şifre girilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Gel Al - Yeni Üye
---------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeGelAlYeniUye

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Gel Al - Üyeliksiz
--------------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeGelAlUyeliksiz

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir


Servis Tipi Seçimi - Adrese Teslim
-----------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslim

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al
----------------------------
 tags:regressionStaging_servisTipiSecimiGelAl

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAldanAdreseTeslimGecisi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
-----------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimUyeliksizSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlVarOlanUyeSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlYeniUyeSepetteServisTipininDegistirilememesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Manuel - Adres Seçimi
------------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeAdresTeslimManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeGelAlManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
 tags:regressionStaging_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionStaging_adresSecimiUyeliksizGelAlManuelAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest9@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Gel Al - Adreslerim - Adres Seçimi
-------------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)(Stg)
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Nakit
-----------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlNakit

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Kredi Kartı
------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlKrediKartı

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme SmartTicket Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket Kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Kart
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSmartTicketKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlMultinet

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Setcard
----------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSetCard

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Kapıda ödeme Paye Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında paye kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Paye Kart
---------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlPayeKart

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlOnlineOdeme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Sipariş tamamlanır
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Sipariş tamamlanır
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeGelAlNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Not Ekleme
--------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeGelAlNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizGelAlNotEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Not alanında var olan notlar combobox'ından Test Not Başlığı geldiği kontrol edilir
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Varolan Notu Ekleme
--------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
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
* Not alanında var olan notlar combobox'ından Test Not Başlığı geldiği kontrol edilir
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Varolan Notu Ekleme
-------------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimVarolanNotuEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
* Not alanında var olan notlar combobox'ından Test Not Başlığı geldiği kontrol edilir
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Varolan Notu Ekleme
-----------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
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
* Not alanında var olan notlar combobox'ından Test Not Başlığı geldiği kontrol edilir
* Sipariş tamamlanır
 Covid-19 anket sorularından çıkılır(Covid-19 sonrası kaldırılacak)
* Ye kazan uyarı butonundan çıkılır
* Sipariş ver sayfasında sipariş notunun yazıldığı doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş İşlemleri(Canlı) - Test adresi - Manuel
------------------------------------------------
 tags:regressionstaging_siparisIslemleriCanliTestAdresiManuel

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_siparisIslemleriCanliTestAdresiDropdown

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeGelAlYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Adıyaman adresi için ilk şube seçilir
* Adıyaman adresi için ilk şubenin geldiği kontrol edilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUye_gelAlYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlYalnizcaIl

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Adıyaman adresi için ilk şube seçilir
* Adıyaman adresi için ilk şubenin geldiği kontrol edilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir
* Gel Al da Şubeleri Göster butonuna tıklanır


Şube atama - Varolan Üye - Gel Al - İl İlçe
---------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeGelAlIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Düzce/Akcakoca adresi için ilk şube seçilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeGelAlIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
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
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Düzce ili seçilir
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir
* Gel Al da Şubeleri Göster butonuna tıklanır


Şube atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlIlIlce

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Akcakoca eklenir
* Düzce/Akcakoca adresi için ilk şube seçilir
* Seçili şube ile devam edilir(Gel Al)
* Anasayfada Düzce/Akcakoca adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeGelAlIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeGelAlIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlIlIlceMahalle

* "https://dpe-staging.dominos.com.tr/" adresine git
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa 99362 - Siparişe Kapalı Şubesi adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* "https://dpe-staging.dominos.com.tr/" adresine git
* "dominostest6@hotmail.com" kullanıcısı ve "Testinium123" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* "https://dpe-staging.dominos.com.tr/" adresine git
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* "https://dpe-staging.dominos.com.tr/" adresine git
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır



