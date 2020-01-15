Specification Heading
=====================


     
Login - Success Scenario
----------------
Tags:login_successScenario
* "sevgialkan011@gmail.com" kullanıcısı ve "Sevgi1234" şifresi ile üye girişi yapılır
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"



Login - Failed Scenario
----------------
Tags:login_failedScenario
* "sevgialkan011@gmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Element var mı kontrol et "epostaVeyaSifreYanlisText"



Login - Failed Scenario2
----------------
Tags:login_failedScenario2
* "test@gmail.com" kullanıcısı ve "Sevgi1234" şifresi ile üye girişi yapılır
* Element var mı kontrol et "epostaVeyaSifreYanlisText"



Login - Screen Check Scenario
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



Login - Parolamı Unuttum Scenario
----------------
Tags:login_parolamiUnuttumScenario
* Elementi bekle ve sonra tıkla "loginButton"
* Elementi bekle ve sonra tıkla "parolamıUnuttumButton"
* "3" saniye bekle
* "sevgialkan011@gmail.com" textini "parolamıUnuttumEmailTextbox" elemente yaz
* Elementi bekle ve sonra tıkla "sifremiHatirlatButon"
* Element var mı kontrol et "sifremDegistirmeMailiGonderildiText"



Sign Up - Screen Control Scenario
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
* Element var mı kontrol et "uyeOlSayfasiYeKazanCheckbox"
* Elementi bekle ve sonra tıkla "uyeOlSayfasiKVKCheckbox"
* Element var mı kontrol et "uyeOlSayfasiEpostaCheckbox"
* Element var mı kontrol et "uyeOlSayfasiSmsCheckbox"
* Element var mı kontrol et "uyeOlSayfasiTelefonCheckbox"
* Elementi bekle ve sonra tıkla "uyeOlSayfasiKVKCheckbox"
* Elementi bekle ve sonra tıkla "uyeOlSayfasiYeKazanCheckbox"
* Element var mı kontrol et "uyeOlSayfasiEpostaCheckbox"
* Element var mı kontrol et "uyeOlSayfasiSmsCheckbox"
* Element var mı kontrol et "uyeOlSayfasiTelefonCheckbox"



Sign Up - New Account Create Success Scenario
----------------
Tags:signup_newAccountCreateSuccessScenario
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"

