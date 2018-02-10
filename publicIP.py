# -*- coding: utf-8 -*-

import urllib2  
import re  
import time

  

#url = "http://city.ip138.com/ip2city.asp"

class PublicIPDetecter():
  def __init__(self):
    self.url = "http://cn.bing.com/search?q=ip&go=%E6%8F%90%E4%BA%A4&qs=n&form=QBLH&pq=ip&sc=8-2&sp=-1&sk=&cvid=14b93b305cdc4183875411c3d9edf938"
    self.html_re = re.compile(r'ip: (.+?) 广东省深圳市 天威视讯',re.DOTALL)

  def detect(self, tostop = True, stopCount = 10):
    while True:
      html = urllib2.urlopen(self.url, timeout=1000).read()
      if None != html:
        ret = html.find("ip: ")
        print('Found ip address: {}'.format(ret))
        ips = self.html_re.findall(html)
        #print(len(ips))

        # Only one ip address will be in the web content
        for ip in ips:
          print "Public IP:" + ip

        if(len(ips) == 1 and tostop): 
		      return ips[0]        
          
      stopCount = stopCount - 1
      if tostop and stopCount <= 0:
          return None

      time.sleep(1)

if __name__=="__main__":
  PIPD = PublicIPDetecter()
  PIPD.detect()



