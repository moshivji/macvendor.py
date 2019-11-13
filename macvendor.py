#!/usr/bin/python

#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
#Script creatd by Mo Shivji 2019


import urllib2
import json
import codecs
import sys

#print str(sys.argv[1])

#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
#Mac address to lookup vendor from
#mac_address = "00:1e:0b:eb:33:b2"
mac_address = str(sys.argv[1])

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

#Print company name
print (obj['result']['company']);
