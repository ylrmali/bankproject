hesapali={
    'isim': 'Ali Yildirim',
    'hesno': '123456',
    'password':'1425',
    'bakiye': 2500,
    'avans': 3000
}

hesapmelih={
    'isim': 'Melih Yildirim',
    'hesno': '456789',
    'password':'1425',
    'bakiye': 2000,
    'avans': 1000
}
hesno = input('Hosgeldiniz, lufen hesap numaranizi giriniz: ')
passw = input('Lutfen sifrenizi giriniz: ')
if hesno == '123456':
    if passw=='1425':
        print('Hosgeldiniz '+(hesapali['isim']))
        secim = input('Yapmak istediginiz islemi seciniz:\n 1. Para Cekme\n 2. Para Yatirma\n 3.Bakiye Sorgu\n')
        if secim =='1':
                cekim =int(input('Cekmek istediginiz tutar: '))
                if cekim <= hesapali['bakiye']:
                    print("Paranızı alabilirsiniz.Kalan bakiye:" + str(hesapali['bakiye']-cekim))
                else:
                    cevap = input('Yetersiz bakiye. Avans kullanmak ister misiniz?(e/h): ')
                    toplam = (hesapali['bakiye'])+(hesapali['avans'])
                    print('Avansiniz: '+ str(hesapali['avans']))
                    print('Avans hesabinizla toplam bakiyeniz: '+ str(toplam))
                    if cevap=='e':
                      kalan =toplam - cekim
                      print('Cekilecek tutar: '+ str(cekim))
                      print('Kalan bakiyeniz:' + str(kalan))
                    else:
                       print('Hesabinizdan cikis yapiliyor.')
        elif secim =='2':
            yatirma = int(input('Yatirmak isterdiginiz tutar: '))
            ybakiye = hesapali['bakiye']+ yatirma
            print('Yeni bakiyeniz: '+ str(ybakiye))
        elif secim=='3':
            print("Bakiyeniz: "+str(hesapali['bakiye']))
            print('Avansınız: '+ str(hesapali['avans']))
        else:
            print('Yanlis secim yaptiniz lutfen kontrol ediniz.')
    else:
        print('Yanlıs parola!')
elif hesno =='456789':
    if passw=='1425':
        print('Hosgeldiniz '+(hesapali['isim']))
        secim = input('Yapmak istediginiz islemi seciniz:\n 1. Para Cekme\n 2. Para Yatirma\n 3.Bakiye Sorgu\n')
        if secim =='1':
                cekim =int(input('Cekmek istediginiz tutar: '))
                if cekim <= hesapali['bakiye']:
                    print("Paranızı alabilirsiniz.Kalan bakiye:" + str(hesapali['bakiye']-cekim))
                else:
                    cevap = input('Yetersiz bakiye. Avans kullanmak ister misiniz?(e/h): ')
                    toplam = (hesapali['bakiye'])+(hesapali['avans'])
                    print('Avansiniz: '+ str(hesapali['avans']))
                    print('Avans hesabinizla toplam bakiyeniz: '+ str(toplam))
                    if cevap=='e':
                      kalan =toplam - cekim
                      print('Cekilecek tutar: '+ str(cekim))
                      print('Kalan bakiyeniz:' + str(kalan))
                    else:
                       print('Hesabinizdan cikis yapiliyor.')
        elif secim =='2':
            yatirma = int(input('Yatirmak isterdiginiz tutar: '))
            ybakiye = hesapali['bakiye']+ yatirma
            print('Yeni bakiyeniz: '+ str(ybakiye))
        elif secim=='3':
            print("Bakiyeniz: "+str(hesapali['bakiye']))
            print('Avansınız: '+ str(hesapali['avans']))
        else:
            print('Yanlis secim yaptiniz lutfen kontrol ediniz.')
    else:
        print('Yanlıs parola!')
else:
    print('Boyle bir hesap bulunamadi')
