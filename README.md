Infix'ten Postfix'e Dönüşüm (Shunting Yard Algoritması): <br /> İnsanın okuyabildiği matematiksel ifadeyi (3 + 4) <br /> 
bilgisayarın daha rahat işlem yapabileceği sıraya (3 \ 4 \ +) dizmek. <br />
Postfix İfadenin Hesaplanması: Dönüştürülen ifadeyi yığıt (stack) kullanarak çözmek. <br /> <br />
<b>Algoritma Mantığı</b>
Bu işlem için Yığıt (Stack) veri yapısı hayati önem taşır.

Öncelik Sırası: <br />
Parantezler ( ) <br />
Üs Alma ^ <br />
Çarpma/Bölme * / <br />
Toplama/Çıkarma + - <br />
