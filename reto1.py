c = float(input())
ica= -1 
if c >= 0 and c < 0.054:
   ica = (((50 - 0) / (0.053 - 0)) * (c - 0) + 0)
elif c >= 0.054 and c < 0.101:
   ica = (((100 - 51) / (0.100 - 0.054)) * (c - 0.054) + 51) 
elif c >= 0.101 and c < 0.361:
   ica = (((150 - 101) / (0.360 - 0.101)) * (c - 0.101) + 101)
elif c >= 0.361 and c < 0.650:
   ica = (((200 - 151) / (0.649 - 0.361)) * (c - 0.361) + 151)
elif c >= 0.650 and c < 1.250: 
   ica = (((300 - 201) / (1.249 - 0.650)) * (c - 0.650) + 201)
elif c >= 1.250 and c < 1.650:
   ica = (((400 - 301) / (1.649 - 1.250)) * (c - 1.250) + 301)
elif c >= 1.650 and c < 2.050:
   ica = (((500 - 401) / (2.049 - 1.650)) * (c - 0.650) + 401)
alert= "error en los datos"
if ica != -1:
  if ica >= 0 and ica <= 50:
    alert = ("verde")
  elif ica > 50 and ica <= 100:
    alert = ("amarillo")
  elif ica > 100 and ica <= 150:
    alert = ("naranja")
  elif ica > 150 and ica <= 200:
    alert = ("rojo")
  elif ica > 200 and ica <= 300:
    alert = ("morado")
  elif ica > 300:
    alert = ("marron")
  print ('{0:.2f} '.format(ica) + alert)
 
  
else:
    print(str(ica) + " " + alert)
    