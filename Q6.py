#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
6. You are given a text that are full of words below. Your code should count the number of occurence of “ve” as conjunction. For instance, “ve” in the phrase “Ahmet ve Ayşe” is a conjunction but not in “kahve”. Then your code should convert these conjunctions to the symbol “&”. Moreover, you are suspicious about typos for the cases like “Ahmet veAyse” or “Ahmetve Ayse” or “AhmetveAyse” as well as for “kahve içtim”. Thus, you are also expected to count the number of potential typos are print the total number of these potential typos. You do not need to write a function for this but you should demonstrate them separately for detected and suspicious cases. For the text given below: if you receive problems with the Turkish characters such as “ü”, you can convert them into the similar forms like “u”.
“Kapıdan girince sağ tarafta bir yük, onun biraz ötesinde yüksek bir konsol vardı. Konsolun üzerinde bir cam fanusun altına konulmuş eski usûl bir saat, kırmızı gaz bezleriyle örtülü, abajurlu iki petrol lambası, sarı yaldız t çerçeveli büyükçe bir ayna veaynanın üst tarafında, duvarda, kılıflarıyla asılmış bir çift çakmaklı tabanca duruyordu. Karşıda, perdeleri tamamen inik olan pencerelerin önünde, bütün duvar boyunca uzanan, üzerine halı döşeli alçak bir sedir ve sedirin köşelerinde pazen yüzlü minderlerle yastıklar, yastıkların üzerinde ise fiyango yapılmış sırma işlemeli yağlıklar vardı. Sedirle kapı arasında, ayakucu kapıya doğru bir yatak duruyor; yatağın üzeri tamamen örten veuçları biraz da yere uzanan yorganı hareketsiz iki insan vücudu kabartıyordu. Yatağın kenarında başlayıp odanın ortasına kadar yayılan ve orada ufak bir gölcük meydana getiren pıhtılaşmış kanlar bu odada birtakım hadiseler olduğunu söylüyordu.” (Sabahattin Ali – Kuyucaklı Yusuf)
"""

###start python code for question 6
fromBook = "Kapıdan girince sag tarafta bir yuk, onun biraz otesinde yuksek bir konsol vardi. Konsolun uzerinde bir cam fanusun altına konulmus eski usul bir saat, kirmizi gaz bezleriyle ortulu, abajurlu iki petrol lambasi, sari yaldiz t cerceveli buyukce bir ayna veaynanin ust tarafinda, duvarda, kiliflariyla asilmis bir cift cakmakli tabanca duruyordu. Karsida, perdeleri tamamen inik olan pencerelerin onunde, butun duvar boyunca uzanan, uzerine hali doseli alcak bir sedir ve sedirin koselerinde pazen yuzlu minderlerle yastiklar, yastiklarin uzerinde ise fiyango yapilmis sirma islemeli yagliklar vardi. Sedirle kapı arasinda, ayakucu kapiya dogru bir yatak duruyor; yatagin uzeri tamamen orten veuclari biraz da yere uzanan yorgani hareketsiz iki insan vucudu kabartiyordu. Yatagin kenarinda baslayip odanin ortasina kadar yayilan ve orada ufak bir golcuk meydana getiren pihtilasmis kanlar bu odada birtakim hadiseler oldugunu soyluyordu.Ahmet ve Ayse, Ahmet veAyse, Ahmetve Ayse, AhmetveAyse, kahve ictim"

#added extra conjunctions and  typos in the given text like "Ahmet ve Ayse, Ahmet veAyse, Ahmetve Ayse, AhmetveAyse, kahve ictim"
#converted all turkish chars to eng char

#regular expression
import re
#starts with 0 or more words, one white space, "ve", one white space, ends with 0 or more words
regex = r'\w*\sve\s\w*'
match = re.findall(regex, fromBook)
print "“ve” conjunctions:"
for x in match:
    print "-> " + x
print "Total count of “ve” as conjunction: " + str(len(match))

#converting "ve" conjunctions to the symbol “&”
import re
regex = r'\sve\s'
newfromBook = re.sub(regex, ' & ', fromBook)
print newfromBook


#suspicious about typos for the cases like “Ahmet veAyse” or “Ahmetve Ayse” or “AhmetveAyse” as well as for “kahve içtim”
import re
#for first regex \w*\sve\w+: starts with 0 or more words,one white space,"ve",ends with 1 or more words
#for second regex \w+ve\s\w*: starts with 1 or more words,"ve",one white space,ends with 0 or more words
regex = r'\w*\sve\w+|\w+ve\s\w*'
match = re.findall(regex, fromBook)
print "Potential typos:"
for x in match:
    print "-> " + x
print "Total count of potential typos: " + str(len(match))
###end python code for question 6
