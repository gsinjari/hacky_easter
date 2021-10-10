#!/usr/bin/env python
# Hacky Easter 2015
# Challenge 24 - SHAM Hash
# By Govand Sinjari @ 2015-03-30
# Divided 30 char string
# md2(char 1-6) , md5(char 7-12), sha1(13-18), sha256(18-24), sha512(25-30)
# author			: @g0vandS
# license           : MIT
# py version        : 2.7


# https://docs.python.org/2/library/hashlib.html

import hashlib
from datetime import datetime
from Crypto.Hash import MD2


#md5x = hashlib.md5()
#md5x.update("govand")
#print md5x.digest()
#print md5x.digest_size
#print md5x.block_size

#print md5x.hexdigest()
#print hashlib.sha1("govand").hexdigest()
#print hashlib.sha224("govand").hexdigest()
#print hashlib.sha256("govand").hexdigest()
#print hashlib.sha512("govand").hexdigest()

#h = hashlib.new('ripemd160')
#h.update("govand")
#print h.hexdigest()
#print
#print hashlib.algorithms

#h1 = hashlib.new('mdc2')
#h1.update("govand")
#print h1.hexdigest()

stx = "afpmqtaads{{a{krrlangecaa|vjzo"

md2x = stx[0:6]
md5x = stx[6:12]
sha1x = stx[12:18]
sha256x = stx[18:24]
sha512x = stx[24:30]
print stx
print	md2x+" "+md5x+" "+sha1x+" "+sha256x+" "+sha512x

z=MD2.new()
z.update(md2x)

print z.hexdigest()[0:6]+hashlib.md5(md5x).hexdigest()[6:12]+hashlib.sha1(sha1x).hexdigest()[12:18]+hashlib.sha256(sha256x).hexdigest()[18:24]+hashlib.sha512(sha512x).hexdigest()[24:30]

# Check what time the scan started
t1 = datetime.now()

findx = "757c479895d6845b2b0530cd9a2b11"
print "The hash is: "+findx

mystr = []

def md2f():
        for c1 in range(97,126):
                for c2 in range(97,126):
                        for c3 in range(97,126):
                                for c4 in range(97,126):
                                        for c5 in range(97,126):
                                                for c6 in range(97,126):
                                                        px = chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
                                                        #print px + " -> " + hashlib.md5(px).hexdigest()[6:12]
							h=MD2.new()
							h.update(px)
                                                        if findx[0:6] == h.hexdigest()[0:6]:
                                                                print "Found: " + px
                                                                mystr.append(px)
                                                                print "OK"
                                                                return







def md5f():
	for c1 in range(97,126):
		for c2 in range(97,126):
			for c3 in range(97,126):
				for c4 in range(97,126):
					for c5 in range(97,126):
						for c6 in range(97,126):				
							px = chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
							#print px + " -> " + hashlib.md5(px).hexdigest()[6:12]
							if findx[6:12] == hashlib.md5(px).hexdigest()[6:12]:
								print "Found: " + px
								mystr.append(px)
								print hashlib.md5(px).hexdigest()
								return
def sha1f():
	for c1 in range(97,126):
		for c2 in range(97,126):
			for c3 in range(97,126):
				for c4 in range(97,126):
					for c5 in range(97,126):
						for c6 in range(97,126):				
							px = chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
							#print px + " -> " + hashlib.md5(px).hexdigest()[6:12]
							if findx[12:18] == hashlib.sha1(px).hexdigest()[12:18]:
								print "Found: " + px
								mystr.append(px)
								print hashlib.sha1(px).hexdigest()
								return

def sha256f():
	for c1 in range(97,126):
		for c2 in range(97,126):
			for c3 in range(97,126):
				for c4 in range(97,126):
					for c5 in range(97,126):
						for c6 in range(97,126):				
							px = chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
							#print px + " -> " + hashlib.md5(px).hexdigest()[6:12]
							if findx[18:24] == hashlib.sha256(px).hexdigest()[18:24]:
								print "Found: " + px
								mystr.append(px)
								print hashlib.sha256(px).hexdigest()
								return
def sha512f():
	for c1 in range(97,126):
		for c2 in range(97,126):
			for c3 in range(97,126):
				for c4 in range(97,126):
					for c5 in range(97,126):
						for c6 in range(97,126):				
							px = chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
							#print px + " -> " + hashlib.md5(px).hexdigest()[6:12]
							if findx[24:30] == hashlib.sha512(px).hexdigest()[24:30]:
								print "Found: " + px
								mystr.append(px)
								print hashlib.sha512(px).hexdigest()
								return


print "\nlooking for MD2[6:12]: " + findx[0:6]
md2f()
								
print "\nlooking for MD5[6:12]: " + findx[6:12]
md5f()

print "\nlooking for SHA1[12:18]: " + findx[12:18]	
sha1f()

print "\nlooking for SHA256[18:24]: " + findx[18:24]	
sha256f()

print "\nlooking for SHA512[24:30]: " + findx[24:30]	
sha512f()


# Checking the time again
t2 = datetime.now()
 
# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

print "\nThe cracked hash is: ", mystr

# Printing the information to screen
print 'HASH cracking completed in: ', total




