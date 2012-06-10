#!/usr/bin/env python2

import cgi
import cgitb; cgitb.enable()
import hashlib
import sys #for debugging via command line
import re

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()
toshorten = form['toshorten'].value
#toshorten=sys.argv[1]

#get sha1 hash of input
urlhash=hashlib.sha1(toshorten).hexdigest()

#ugly hack to shorten hash. collisions imminent.

#actually, this might just work. 
#assuming sha1 has perfect distribution for arbitrary values, this would work for 3.5 quadrillion urls
#before a collision.
#we'll see... for SCIENCE!!!
urlhash=urlhash[0:10]

#make an html redirect page in directory dir called name
def mkhtmlredir(dir, name):
     ### redirect page templates ###
     redirect_begin='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TRp/xhtml11/DTD/xhtml11.dtd">\n<html>\n<head>\n<meta http-equiv="Refresh" content="0;url=http://'''
     redirect_end='''"/>\n</head>\n</html>'''

     with open(dir + name, 'w') as file:
          file.write(redirect_begin + toshorten + redirect_end)



def mkresultpage(srcfile):
     filebuf=[]
     
     with open(srcfile, 'r') as file:
          for line in file.readlines():
               filebuf.append(line)

     for i in range(len(filebuf)):
          filebuf[i] = re.sub('#####', 's.devrandom.co/s/' + urlhash, filebuf[i])
          filebuf[i] = re.sub('<!--!!!!!', '', filebuf[i])
          filebuf[i] = re.sub('!!!!!-->', '', filebuf[i])
          print filebuf[i]

     

### result page templates ###


mkhtmlredir('s/', urlhash)
mkresultpage('index.html')

#print("shortened url: s.devrandom.co/s/%s" % urlhash)
