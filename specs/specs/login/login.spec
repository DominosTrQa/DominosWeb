Login
=====================


1-Login - Success Scenario
----------------
Tags:login_successScenario
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


2-Login - Failed Scenario
----------------
Tags:login_failedScenario

* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


2-Login - Failed Scenario2
----------------
Tags:login_failedScenario2

* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


3-Login - Screen Check Scenario
----------------
Tags:login_screenCheckScenario

* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


4-Login - Parolamı Unuttum Scenario
----------------
Tags:login_parolamiUnuttumScenario

* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


7-Sign Up - Screen Control Scenario
----------------
Tags:signup_screenControlScenario

* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


8-Sign Up - New Account Create Success Scenario
----------------
Tags:signup_newAccountCreateSuccessScenario

* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


9-Sign Up - New Account Create Fail Scenario
----------------
Tags:signup_newAccountCreateFailScenario

* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


10-Sign Up - New Account Create Success Scenario2
----------------
Tags:signup_newAccountCreateSuccessScenario2

* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


11-Üye Olmadan Devam Et - Button Control
----------------
Tags:uyeOlmadanDevamEt_buttonKontrol

* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


12-Üye Olmadan Devam Et - Screen Control
----------------
Tags:uyeOlmadanDevamEt_screenKontrol

* Giriş Yap butonuna basılır
* Üye olmadan devam et
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"