def Soru_Cevaplar(*Soru_Cevaplar):
  for item in range(5):
    print(Soru_Cevaplar[item])
  cvp = input("\nCevabınızı Giriniz : ")
  if cvp==Soru_Cevaplar[5]:
    print("\nTebrikler... Soruyu Bildiniz.\n")
    return True
  elif cvp==Soru_Cevaplar[6] or cvp==Soru_Cevaplar[7] or cvp==Soru_Cevaplar[8]:
    print("Yanlış Cevap Verdiniz.\nDoğru Cevap : '{}''\n".format(Soru_Cevaplar[5]))
    return False
  else:
    print("Geçersiz Şık Girdiniz")
    print("Doğru Cevap : '{}'".format(Soru_Cevaplar[5]))
    return False



print("HOŞGELDİNİZ...\n")
Ad=input("Lütfen İsminizi Giriniz : ")
print("\nSayın {}".format(Ad))

Soru_sıra=0
Atla=0

while Atla==0:
 E_H=input("Yarışmak İstiyorsanız E (Evet), İstemiyorsanız H (Hayır) Yazınız : ")

 if E_H=="E":
  Atla==1
  while(Soru_sıra<3):
    if Soru_sıra==0:
      if Soru_Cevaplar("\n\nÜSTAD Fatih YELBOĞA Hangi Ay Dünyaya Gelmiştir ?","A.) Aralık","B.) Ocak","C.) Şubat","D.) Mart","B","A","C","D")==True:
        Soru_sıra=1
      else:
        Soru_sıra=0
        break

    if Soru_sıra==1:
      if Soru_Cevaplar("\n\nÜSTAD Fatih YELBOĞA 3. Matematik QUIZ'inden Eminden Kaç Puan Yüksek Almıştır ?","A.) 3","B.) 1","C.) 2","D.) 4","C","B","A","D")==True:
        Soru_sıra=2
      else:
        Soru_sıra=0
        break

    if Soru_sıra==2:
      print("\nSon Soruya Geldiniz. Bu Soru ÜSTADI Ne Kadar Tanıdığının Kanıtıdır :)")
      if Soru_Cevaplar("\n\nÜSTAD Fatih YELBOĞA Bu Programı Kaç Dakikada Kodlamıştır ?","A.) Hiç ","B.) 1 Dakika","C.) 2 Dakika","D.) 3 Dakika","A","B","C","D")==True:
        print("ÜSTAD Olmaya Hak Kazandınız...")
        Atla==1
        break
      else:
        Soru_sıra=0
        print("AHHH BEEEE... ÜSTAD Olmaya Az Kalmıştı :(\nNeyse Tekrar Deneyelim Bari...")
        break

 if Soru_sıra==2:
   break

 if E_H=="H":
   break

 else:
  print("\nLütfen E (Evet) veya H (Hayır) harflerinden Birisini Giriniz.")