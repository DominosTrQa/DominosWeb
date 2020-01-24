Specification Heading
=====================
Created by sahabt on 2020-01-24

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Tüm Kampanyalar Sayfa Kontrolü
------------------------
tags:tümkampanyalarsayfakontrolü
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Element var mı kontrol et "tümkampanyalar2"
* Element var mı kontrol et "HaftaninKampanyalari"
* Element var mı kontrol et "TekKisilikKampanyalar"
* Element var mı kontrol et "TekKisilikKampanyalar"
* Element var mı kontrol et "2-3-KisilikKampanyalar"
* Element var mı kontrol et "4KisiveÜzeriKampanyalar"
* Element var mı kontrol et "GelAlHaftaninKampanyalari"
* Element var mı kontrol et "SiparisVer"
* Elementine tıkla "okİsareti"
* Element var mı kontrol et "tümkampanyalar2"


Haftanın Kampanyaları sayfa kontrolü (buton ve yan okla geçme)
-------------------------------------------------------------
tags:HaftanınKampanyalarısayfakontrolü(butonveyanoklageçme)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Wait "2" seconds
* Element var mı kontrol et "HaftaninKampanyalari"
* Elementine tıkla "okİsareti"
* Wait "3" seconds
* Element var mı kontrol et "TekKisilikKampanyalar2"




Tek Kişilik Kampanyalar sayfa kontrolü (buton ve yan okla geçme)
---------------------------------------------
tags:TekKişilikKampanyalarsayfakontrolü(butonveyanoklageçme)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Elementi bekle ve sonra tıkla "TekKisilikKampanyalar"
* Element var mı kontrol et "TekKisilikKampanyalar2"



2-3 Kişilik Kampanyalar sayfa kontrolü (buton ve yan okla geçme)
----------------------------------------
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Elementi bekle ve sonra tıkla "2-3-KisilikKampanyalar"
* "SiparisVer2" elementi "Sipariş Ver" değerini içeriyor mu kontrol et
* "2-3-KisilikKampanyalar2" elementi "2-3 Kişilik Kampanyalar" değerini içeriyor mu kontrol et
* Elementine tıkla "okİsareti"

4 Kişi ve üzeri kampanyalar sayfa kontrolü (buton ve yan okla geçme)
----------------------------------------------------
tags:4Kişiveüzerikampanyalarsayfakontrolü(butonveyanoklageçme)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Wait "3" seconds
* Elementine tıkla "4KisiveÜzeriKampanyalar"
* Wait "3" seconds
* Element var mı kontrol et "4KisiveÜzeriKampanyalar2"


Gel Al Haftanın Kampanyaları sayfa kontrolü (buton ve yan okla geçme)
--------------------------------------------
tags:GelAlHaftanınKampanyalarısayfakontrolü(butonveyanoklageçme)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Wait "3" seconds
* Elementine tıkla "GelAlHaftaninKampanyalari"
* Element var mı kontrol et "GelAlHaftaninKampanyalari2"




Üst Bar Sayfalar arası geçiş kontrolü (Tüm Kampanyalar- Tüm Pizzalar- Ekstralar&İçecekler)
----------------------------------------------------------------------------------
tags:ÜstBarSayfalararasıgeçişkontrolü(TümKampanyalarTümPizzalarEkstralar&İçecekler)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* "tümkampanyalar2" elementi "Tüm Kampanyalar" değerini içeriyor mu kontrol et
* "tümpizzalar" elementi "Tüm Pizzalar" değerini içeriyor mu kontrol et
* "ekstralaricecekler" elementi "Ekstralar & İçecekler" değerini içeriyor mu kontrol et




Üst Bar Profilim popup başarılı açılıyor mu kontrolü
--------------------------------------------------
tags:ÜstBarProfilimpopupbaşarılıaçılıyormukontrolü
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Element var mı kontrol et "Profilim"





Üst Bar Sepetim popup başarılı açılıyor mı kontrolü
--------------------------------------------------
tags:ÜstBarSepetimpopupbaşarılı çılıyormıkontrolü
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Element var mı kontrol et "Sepetim"



Alt Bar yazıları doğru geliyor mu kontrolü
-----------------------------------------







Her tab da Sipariş Ver buton kontrolü (Haftanın Kampanyaları, Tek Kişilik Kampanyalar, 2-3 Kişilik Kampanyalar, 4 Kişi ve üzeri Kampanyalar, Gel Al Haftanın Kampanyaları)
---------------------------------------------------------------------------------------------------------------------
tags:HertabdaSiparişVerbutonkontrolü(HaftanınKampanyalarıTekKişilikKampanyalar2-3KişilikKampanyalar4KişiveüzeriKampanyalarGelAlHaftanınKampanyaları)
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Elementi bekle ve sonra tıkla "TümKampanyalar"
* Element var mı kontrol et "HaftaninKampanyalariSiparisKontrol"
* Element var mı kontrol et "TekKisilikKampanyalarSiparisKontrol"
* Element var mı kontrol et "2-3KisilikKampanyalarSiparisKontrol"
* Element var mı kontrol et "4KisilikKampanyalarSiparisKontrol"
* Element var mı kontrol et "GelAlHaftaninKampanyalariSiparisKontrol"
