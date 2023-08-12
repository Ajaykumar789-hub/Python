from googletrans import Translator
translator = Translator()
k = translator.translate("who are you", dest='hindi')
print(k)
print(k.text)
p = translator.translate(k.text,dest='hindi')#convert same language to same to get
                                             #pronunciation
print(p)
print(p.pronunciation)