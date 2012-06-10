#!/usr/bin/env python2

import cgi
import cgitb; cgitb.enable()
import hashlib
import sys #for debugging via command line

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()
toshorten = form['toshorten'].value
#toshorten=sys.argv[1]

#get sha1 hash of input
urlhash=hashlib.sha1(toshorten).hexdigest()

#ugly hack to make the hash shorter. collisions imminent.
urlhash=urlhash[0:10]

redirect_begin='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TRp/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <meta http-equiv="Refresh" content="0;url=http://'''

redirect_end='''"/>
  </head>
</html>

'''

with open('s/' + urlhash, 'w') as file:
     file.write(redirect_begin + toshorten + redirect_end)

print("shortened url: s.devrandom.co/s/%s" % urlhash)