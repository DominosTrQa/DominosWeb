Login
=====================


Login - Success Scenario
----------------
tags:login_successScenario

* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Login - Failed Scenario
----------------
tags:login_failedScenario

* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Login - Failed Scenario2
----------------
tags:login_failedScenario2

* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Login - Screen Check Scenario
----------------
tags:login_screenCheckScenario

* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Login - Parolamı Unuttum Scenario
----------------
tags:login_parolamiUnuttumScenario

* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Login -Sign Up - Screen Control Scenario
----------------
tags:login_signup_screenControlScenario

* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Login -Sign Up - New Account Create Success Scenario
----------------
tags:login_signup_newAccountCreateSuccessScenario

* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Login -Sign Up - New Account Create Fail Scenario
----------------
tags:login_signup_newAccountCreateFailScenario

* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Login - Sign Up - New Account Create Success Scenario2
----------------
tags:login_signup_newAccountCreateSuccessScenario2

* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Login - Üye Olmadan Devam Et - Button Control
----------------
tags:login_uyeOlmadanDevamEt_buttonKontrol

* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Login - Üye Olmadan Devam Et - Screen Control
----------------
tags:login_uyeOlmadanDevamEt_screenKontrol

* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"