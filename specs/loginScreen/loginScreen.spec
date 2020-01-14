Specification Heading
=====================


     
Login - Success Scenario
----------------
Tags:login_successScenario
* "sevgialkan011@gmail.com" kullanıcısı ve "Sevgi1234" şifresi ile üye girişi yapılır
* Element var mı kontrol et "gelAlButon"
* Element var mı kontrol et "adreseTeslimButon"
gti

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
Tags:login_screenCheckScenario
* Elementi bekle ve sonra tıkla "loginButton"
* Elementi bekle ve sonra tıkla "parolamıUnuttumButton"
