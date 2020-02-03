Specification Heading
=====================


     
1-Login - Success Scenario
----------------
Tags:login_successScenario
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"



2-Login - Failed Scenario
----------------
Tags:login_failedScenario
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Element var mı kontrol et "epostaVeyaSifreYanlisText"



2-Login - Failed Scenario2
----------------
Tags:login_failedScenario2
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Element var mı kontrol et "epostaVeyaSifreYanlisText"



3-Login - Screen Check Scenario
----------------
Tags:login_screenCheckScenario
* Elementi bekle ve sonra tıkla "loginButton"
* Element var mı kontrol et "loginEmailTextbox"
* Element var mı kontrol et "loginPasswordTextbox"
* Element var mı kontrol et "girisYapButon"
* Element var mı kontrol et "uyeOlmadanDevamEtButon"
* Element var mı kontrol et "parolamıUnuttumButton"
* Element var mı kontrol et "beniHatirlaCheckbox"
* Element var mı kontrol et "facebookIleGirisButon"
* Element var mı kontrol et "googleIleGirisButon"



4-Login - Parolamı Unuttum Scenario
----------------
Tags:login_parolamiUnuttumScenario
* Elementi bekle ve sonra tıkla "loginButton"
* Elementi bekle ve sonra tıkla "parolamıUnuttumButton"
* "3" saniye bekle
* "dominostest2@hotmail.com" textini "parolamıUnuttumEmailTextbox" elemente yaz
* Elementi bekle ve sonra tıkla "sifremiHatirlatButon"
* Element var mı kontrol et "sifremDegistirmeMailiGonderildiText"



7-Sign Up - Screen Control Scenario
----------------
Tags:signup_screenControlScenario
* Üye ol butonuna tıklanır
* Element var mı kontrol et "uyeOlAdTextbox"
* Element var mı kontrol et "uyeOlSoyadTextbox"
* Element var mı kontrol et "uyeOlTelefonTextbox"
* Element var mı kontrol et "uyeOlSifreTexbox"
* Element var mı kontrol et "uyeOlSifreyTekrarTextbox"
* Element var mı kontrol et "uyeOlMesafeliSatisSozlesmesi"
* Element var mı kontrol et "uyeOlSayfasiÜyeOlButon"
* Element var mı kontrol et "facebookIleGirisButon"
* Element var mı kontrol et "googleIleGirisButon"
* Element var mı kontrol et "uyeOlSayfasiKVKCheckbox"
* Elementi bekle ve sonra tıkla "uyeOlSayfasiKVKCheckbox"
* Element var mı kontrol et "uyeOlSayfasiEpostaCheckbox"
* Element var mı kontrol et "uyeOlSayfasiSmsCheckbox"
* Element var mı kontrol et "uyeOlSayfasiTelefonCheckbox"
* Element var mı kontrol et "uyeOlSayfasiYeKazanCheckbox"
* Elementi bekle ve sonra tıkla "uyeOlSayfasiYeKazanCheckbox"
* Element var mı kontrol et "uyeOlSayfasiyeKazanEpostaCheckbox"
* Element var mı kontrol et "uyeOlSayfasiYeKazanSmsCheckbox"
* Element var mı kontrol et "uyeOlSayfasiYeKazanTelefonCheckbox"




8-Sign Up - New Account Create Success Scenario
----------------
Tags:signup_newAccountCreateSuccessScenario
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"


9-Sign Up - New Account Create Fail Scenario
----------------
Tags:signup_newAccountCreateFailScenario
* Üye ol butonuna tıklanır
* Elementi bekle ve sonra tıkla "uyeOlSayfasiÜyeOlButon"
* Element var mı kontrol et "uyeOlAdBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlSoyaddBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlTelefonBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlEpostaBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlSifreBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlSifreTekrarBosBirakilamazUyariText"
* Element var mı kontrol et "uyeOlUyelikSozlesmesiBosBirakilamazUyariText"



10-Sign Up - New Account Create Success Scenario2
----------------
Tags:signup_newAccountCreateSuccessScenario2
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"


11-Üye Olmadan Devam Et - Button Control
----------------
Tags:uyeOlmadanDevamEt_buttonKontrol
* Elementi bekle ve sonra tıkla "loginButton"
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


12-Üye Olmadan Devam Et - Screen Control
----------------
Tags:uyeOlmadanDevamEt_screenKontrol
* Elementi bekle ve sonra tıkla "loginButton"
* Üye olmadan devam et
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"




