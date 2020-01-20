myProfilePopup
=====================
Created by testinium on 16.01.2020

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
50- Profilim Popup - Ye-Kazan - Sayfa Kontrolü
-----------------------------------------------------
Tags:profilimPopup_yeKazanSayfaKontrolu

* Üye olarak giriş yapılır ve profilim butonuna tıklanır
* Elementi bekle ve sonra tıkla "Profilim_Popup_Ye_Kazan_Buton"
* Element var mı kontrol et "Profilim_Popup_Ye_Kazan_Sadakat_Programı_Checkbox"
* Element var mı kontrol et "Profilim_Popup_Ye_Kazan_Ye_Kazana_Katıl_Buton"
* Element var mı kontrol et "Profilim_Popup_Ye_Kazan_Sıkca_Sorulan_Sorular_Text"

51- Profilim Popup - Üyelik Koşulları Sayfa Kontrolü
---------------------------------------------------
Tags:profilimPopup_uyelikKosullariSayfaKontrolu

* Üye olarak giriş yapılır ve profilim butonuna tıklanır
* Elementi bekle ve sonra tıkla "Profilim_Popup_Ye_Kazan_Buton"
* Elementi bekle ve sonra tıkla "Profilim_Popup_Ye_Kazan_Uyelik_Kosulları_Linktext"
* Element var mı kontrol et "Profilim_Popup_Ye_Kazan_Uyelik_Kosulları_Yedikce_Kazan_Text"

52- Profilim Popup - Üyelik Bilgilerim - Zorunlu alanların kontrolü
------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimZorunluAlanKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Element var mı kontrol et "Profilim_Popup_Uyelik_Bilgilerim_Eposta_Textbox"
* Element var mı kontrol et "Profilim_Popup_Uyelik_Bilgilerim_Telefon_Textbox"


53- Profilim Popup - Üyelik Bilgilerim - Değiştirilebilir alanların kontrolü
-------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimDegistirebilirimAlanKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Element var mı kontrol et "üyelik_Bilgilerim_Ad_Textbox"
* Element var mı kontrol et "üyelik_Bilgilerim_Soyad_Textbox"
* Element var mı kontrol et "üyelik_Bilgilerim_Dogum_Tarihi_Textbox"
* Element var mı kontrol et "üyelik_Bilgilerim_Takım_Dropdown"
* Element var mı kontrol et "üyelik_Bilgilerim_Meslek_Dropdown"
* Element var mı kontrol et "üyelik_Bilgilerim_Acık_Rıza_Metni_Checkbox"
* Element var mı kontrol et "üyelik_Bilgilerim_Ye_Kazan_Checkbox"

54- Profilim Popup - Üyelik Bilgilerim - Değişikliklerin başarılı bir şekilde yapıldığının kontrolü (Bitmedi)
----------------------------------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimDegisikliklerinBasariliBirSekildeYapidigininKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Ad_Textbox"
* "üyelik_Bilgilerim_Ad_Textbox" elementine random isim yaz
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Degisiklikleri_Kaydet_Buton"

55- Profilim Popup - Üyelik Bilgilerim - Üyelikten ayrılmak için tıklayın kontrolü
----------------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimUyeliktenAyrilmakicinTiklayinKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Linktext"
* Element var mı kontrol et "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Popup"

56- Profilim Popup - Üyelik Bilgilerim - Üyelikten ayrılmanın başarılı bir şekilde yapılması kontrolü
---------------------------------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimUyeliktenAyrilmaninBasariliBirSekildeYapilmasiKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Linktext"
* Element var mı kontrol et "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Popup"
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Üyelikten_Ayrılmak_İstiyorum_Buton"
* Element var mı kontrol et "Anasayfa_Kontrol"

57- Profilim Popup - Üyelik Bilgilerim - Üyelikten ayrılmadan vazgeçme kontrolü
-------------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimUyeliktenAyrilmadanVazgecmeKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Linktext"
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Vazgec_Buton"
* Element var mı kontrol et "üyelik_Bilgilerim_Üyelikten_Ayrılmak_Linktext"

58- Profilim Popup - Üyelik Bilgilerim - KVKK Aydınlatma Metni kontrolü
----------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimKvkkAydinlatmaMetniKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_KVKK_Aydınlatma_Metni_Linktext"
* Element var mı kontrol et "üyelik_Bilgilerim_KVKK_Aydınlatma_Metni_Kontrol"

59- Profilim Popup - Üyelik Bilgilerim - Açık Rıza Metni kontrolü
---------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimAcikRizaMetniKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Acık_Rıza_Metni_Linktext"
* Element var mı kontrol et "üyelik_Bilgilerim_Acık_Rıza_Metni_Kontrol"

60- Profilim Popup - Üyelik Bilgilerim - Ye-Kazan Sadakat Programı Üyelik Koşulları Metni kontrolü
--------------------------------------------------------------------------------------------------
Tags:profilimPopup_uyelikBilgilerimYeKazanSadakatProgramiUyelikKosullariMetniKontrolu

* Üye olarak giriş yapılır ve üyelik bilgilerime git
* Elementi bekle ve sonra tıkla "üyelik_Bilgilerim_Ye_Kazan_Linktext"
* Element var mı kontrol et "üyelik_Bilgilerim_Ye_Kazan_Kontrol"

61- Profilim Popup - Siparişlerim - Sipariş Alanları Kontrolü
--------------------------------------------------------------
Tags:profilimPopup_SiparislerimSiparisAlanlariKontrolu

* Üye olarak giriş yapılır ve siparislerime git
* Element var mı kontrol et "Profilim_Popup_Siparislerim_Aktif_Siparislerim_Text"
* Element var mı kontrol et "Profilim_Popup_Siparislerim_Tek_Tikla_Siparislerim_Text"
* Element var mı kontrol et "Profilim_Popup_Siparislerim_Eski_Siparislerim_Text"

74- Profilim Popup - Çıkış Yap - Var Olan Kullanıcı ile Çıkış Kontrolü
----------------------------------------------------------------------
Tags:profilimPopup_cikisYapVarOlanKullaniciileCikisKontrolu

* Üye olarak giriş yapılır ve profilim butonuna tıklanır
* Elementi bekle ve sonra tıkla "Profilim_Popup_Cikis_Yap_LinkText"

75- Profilim Popup - Çıkış Yap - Yeni Kullanıcı ile Çıkış Kontrolü
----------------------------------------------------------------
Tags:profilimPopup_cikisYapYeniKullaniciileCikisKontrolu

* Üye olarak giriş yapılır ve profilim butonuna tıklanır
* Elementi bekle ve sonra tıkla "Profilim_Popup_Cikis_Yap_LinkText"



