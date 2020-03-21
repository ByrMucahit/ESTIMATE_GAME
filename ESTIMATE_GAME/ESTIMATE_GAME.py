
import random
import time


    
while True:     
      print ("Merhaba,Oyuna hoş geldiniz!")
      time.sleep(2)
      print("Sisli bir gecede, saat gece yarısına yaklaşırken karanlık bir ormanda yolunu kaybettin.")
      time.sleep(2)
      print("Biraz ilerledikten sonra 4'e ayrılan yol ayrımıyla karşılaştın.")
      time.sleep(2)
      print("Önünde 4 yol var ve bunlardan sadece ikisi güvenli.")
      a=["birinci yol","ikinci yol","üçüncü yol","dördüncü yol"]
      for i in range(len(a)):
          print(i+1,a[i])
          
      soru=int(input("Hangi yolu seçeceksin? [1/2/3/4]"))
      if soru in [1]:
              print("Güvenli yollardan birini buldun.")
              soru=str(input("Bu yolda hızlıca koşarken büyük bir çukura düştün. Çukurdan çıkmaya mı çalışacaksın yoksa yardım mı bekleyeceksin? [çukurdan çıkmak/yardım beklemek]"))
              if soru in ['yardım bekle','yardım beklemek']:
                  print("İyi bir fikir değildi fazla bekledin ve kaybettin!")
              else:
                      print("Çukurdan çıkmayı başardın. Yoluna devam ederken karşına bir adam çıktı")
                      soru=str(input("Adamdan yardım mı isteyeceksin yoluna devam mı edeceksin? [Adamdan yardım iste/Yoluna devam et]"))
                      if soru in ['Adamdan yardım iste','adam','yardım iste']:
                          print("Güvenmekle hata yaptın ve kaybettin!")
                      else:
                          print("Yoluna devam etmeyi seçtin. İlerde bir arabaya ulaştın ve ormandan güvenli bir şekilde ayrıldın.Tebrikler")
                              
      elif soru in [2]:
            print("Güvenli yollardan birini buldun.")
            soru = str(input("Bu yolda hızlıca ilerlerken kurtlar senin yolunu kesti. Savaşmak mı istiyorsun kaçmak mı? [savaşmak/kaçmak]: "))
            if soru in ['savaşmak','savaş']:
                          print("İyi bir fikir değildi, seni yendiler ve kaybettin!")
            elif soru in ['kaç','kaçmak']:
                          print("Kaçmakla iyi yaptın. Biraz ilerledikten sonra önüne bir bisiklet ve araba çıktı.")
                          soru = str(input("Bisikleti mi alacaksın arabayı mı? [bisiklet/araba]"))
                          if soru in ['bisiklet','b']:
                              print("İyi bir fikir değildi. Kurtlar kısa sürede sana yetiştiler. Kaybettin!")
                          else:
                              print("Tebrikler,ormandan güvenli bir şekilde ayrıldın.")
            
      elif soru in [3]:
                print("Tehlikeli yolu seçtin ve kaybettin!")
      elif soru in [4]:
           print("Tehlikeli yolu seçtin ve kaybettin!")
         
      secim=str(input("Oyunu tekrar oynamak ister misiniz ? (evet yada hayır?)"))
      if secim=='evet' or secim=='EVET' :
        print("Yeniden")
      elif secim == 'hayır' or secim== 'HAYIR':
        print("Çıkıyorsunuz, oynadığınız için teşekkürler.")
        break

    

    





    

    