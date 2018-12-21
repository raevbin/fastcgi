 # redirectURL = "/?r=%s" % random.randint(0,100000000)
#import cgitb
#import random
import datetime
import pprint



# преобразование нежелательнх символов в строке
def html_special_chars(text):
    return text \
    .replace(u"&", u"&amp;") \
    .replace(u'"', u"&quot;") \
    .replace(u"'", u"&#039;") \
    .replace(u"<", u"&lt;") \
    .replace(u">", u"&gt;")

    #a = "<a href='test'>Test</a>"
    #print html_special_chars(a)





def line_wr(inpdata,data=1,newstr=1):
   dt = (str(str(datetime.datetime.now()))+' >> ') if data==1 else ''
   ns = '\n' if newstr==1 else ''
   f = open('/home/evgeniy/temp/test/log.txt','a')
   f.write(dt+pprint.pformat(inpdata)+ns)
  
   f.close()


