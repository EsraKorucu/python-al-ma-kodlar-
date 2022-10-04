"""liste içerisindeki sayıların 12 ye bölünüp bölünmediğini kontrol eder ve bölünenleri listeye atar"""
liste=[23,45,67,42,53,89,65,24,36,48]
toplam=0
adet=[]
for item in liste:
  toplam+= item%12
  if item%12==0:
      adet.append(item)
      
print("adet",adet)
print("toplam",toplam)
