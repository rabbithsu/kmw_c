# -*- coding: utf-8 -*- 

from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 

from bs4 import BeautifulSoup

from datetime import *
from datetime import datetime
import time 
import datetime
import os 
import urllib, urllib2
import codecs
import sys
import re

from selenium.webdriver.common.keys import Keys

i = 0
# set time
start = date(2015, 01, 01)
end = date(2015, 01, 01)#0628
day = timedelta(1)

#政治 i13937
#經濟貿易 i13938
#財政金融 i13939
#產業 i13940
#科技資訊 i13941
#投資理財 i13942

def getnews(f, t, setdate):
#try:
	conti = False
	a = f.strftime("%Y/%m/%d")
	b = t.strftime("%Y/%m/%d")
	browser = webdriver.Chrome('chromedriver') 
	browser.implicitly_wait(20)
	#nb = webdriver.Chrome('chromedriver')

	#switch windows handle
	browser.window_handles

	browser.get('http://kmw.chinatimes.com/') 
	#nccu login
	browser.find_element_by_xpath('//a[@style="COLOR: #0055ca"]').click()
	time.sleep(3)

	#news search
	browser.find_element_by_xpath('//td[@id="Menu1-menuItem001"]').click()
	browser.find_element_by_xpath('//td[@id="Menu1-menuItem001-subMenu-menuItem001"]').click()
	time.sleep(1)

	'''#get area frame -> six catacory
	browser.switch_to_frame("if1")
	browser.switch_to_frame(browser.find_element_by_name("fLeft"))
	browser.switch_to_frame("if1")
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13941)"]').click()
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13937)"]').click()
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13938)"]').click()
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13939)"]').click()
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13940)"]').click()
	browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(13942)"]').click()
	time.sleep(1)'''
	if(setdate):
	#get area frame -> TW
		browser.switch_to_default_content()
		browser.switch_to_frame("if1")
		browser.switch_to_frame(browser.find_element_by_name("fLeft"))
		browser.find_element_by_xpath('//td[@id="tabA"]').click()
		browser.switch_to_frame("if39")
		browser.find_element_by_xpath('//span[@onclick="pchild(this,14603)"]').click()
		time.sleep(1)
		browser.find_element_by_xpath('//span[@onclick="pchild(this,14610)"]').click()
		browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(14636)"]').click()
		time.sleep(1)
	

	#return default
	browser.switch_to_default_content()
	#get search frame
	browser.switch_to_frame("if1")
	browser.switch_to_frame(browser.find_element_by_name("fTop"))
	if(setdate):
		df = browser.find_element_by_id('txtDateFrom')
		df.clear()
		df.send_keys(a)
		t = browser.find_element_by_id('txtDateTo')
		t.clear()
		t.send_keys(b)
	#search
	browser.find_element_by_xpath('//input[@name="image"]').click()
	time.sleep(1)

	#get result
	browser.switch_to_default_content()

	#get page number
	browser.switch_to_frame("if1")
	browser.switch_to_frame(browser.find_element_by_name("fCenter"))
	browser.switch_to_frame("if1")
	page = browser.find_element_by_xpath('//font[@class="a12gray"]/font[@color="#FF0000"]').text
	pnumber = int((page.split('/'))[1])
	#print pnumber
	browser.switch_to_default_content()
	
	urlsave = codecs.open("urllog.txt", "w+", "utf-8")

	for count in range(pnumber):
		for i in range(1):
			if(True):
			
				#print browser.current_url
				
				record = "2015/01/01"
				save = ""
				end = False
				browser.switch_to_frame("if1")
				browser.switch_to_frame(browser.find_element_by_name("fCenter"))
				browser.switch_to_frame("if1")
				


				newsitems = browser.find_elements_by_xpath('//td/a[@target="new"]')
				end = (len(newsitems) == (i+1))
				for newsurl in newsitems:
					save += newsurl.get_attribute("href") + "\n"
				
				urlsave.write(save)
				#print "saved"
				

		try:	
			print "change page to " + str(count+2)
			browser.switch_to_default_content()
			browser.switch_to_frame("if1")
			browser.switch_to_frame(browser.find_element_by_name("fCenter"))
			browser.switch_to_frame("if1")
			browser.find_element_by_xpath('//a[@id="btnPgNext1"]').click()
			browser.switch_to_default_content()
			time.sleep(3)
			browser.switch_to_frame("if1")
			browser.switch_to_default_content()
		except:
			browser.get('http://kmw.chinatimes.com/') 
			#nccu login
			browser.find_element_by_xpath('//a[@style="COLOR: #0055ca"]').click()
			time.sleep(3)

			#news search
			browser.find_element_by_xpath('//td[@id="Menu1-menuItem001"]').click()
			browser.find_element_by_xpath('//td[@id="Menu1-menuItem001-subMenu-menuItem001"]').click()
			time.sleep(1)

			if(setdate):
			#get area frame -> TW
				browser.switch_to_default_content()
				browser.switch_to_frame("if1")
				browser.switch_to_frame(browser.find_element_by_name("fLeft"))
				browser.find_element_by_xpath('//td[@id="tabA"]').click()
				browser.switch_to_frame("if39")
				browser.find_element_by_xpath('//span[@onclick="pchild(this,14603)"]').click()
				time.sleep(1)
				browser.find_element_by_xpath('//span[@onclick="pchild(this,14610)"]').click()
				browser.find_element_by_xpath('//a[@href="javascript:OnItemClick(14636)"]').click()
				time.sleep(1)
			

			#return default
			browser.switch_to_default_content()
			#get search frame
			browser.switch_to_frame("if1")
			browser.switch_to_frame(browser.find_element_by_name("fTop"))
			if(setdate):
				df = browser.find_element_by_id('txtDateFrom')
				df.clear()
				df.send_keys(a)
				t = browser.find_element_by_id('txtDateTo')
				t.clear()
				t.send_keys(b)
			#search
			browser.find_element_by_xpath('//input[@name="image"]').click()
			time.sleep(1)
			
			browser.switch_to_default_content()
			browser.switch_to_frame("if1")
			browser.switch_to_frame(browser.find_element_by_name("fCenter"))
			browser.switch_to_frame("if1")
			browser.find_element_by_xpath('//*[@id="txtPage"]').send_keys(str(count+2))
			browser.find_element_by_xpath('//*[@id="txtPage"]').send_keys(Keys.RETURN)
			#browser.find_element_by_xpath('//a[@id="btnPgNext1"]').click()
			browser.switch_to_default_content()
		
		
			#browser.quit()
			print "Chrome may restart. " + record
			#er = record.split("/")
			#return date(int(er[0]), int(er[1]), int(er[2])) + day
		
	urlsave.close()		
	readurl = codecs.open("urllog.txt", "r", "utf-8")
	for r in readurl:
		browser.get(r)
		
		time.sleep(4)
		try:
			newsdate = browser.find_element_by_xpath('//td[@class="a13blue2"]').text
			content = browser.find_element_by_xpath('//td[@class="a15gray"]').text
			title = browser.find_element_by_xpath('//td[@id="newsTitle"]').text
		except:
			browser.get('http://kmw.chinatimes.com/') 
			#nccu login
			browser.find_element_by_xpath('//a[@style="COLOR: #0055ca"]').click()
			time.sleep(3)
			browser.get(r)
		#test
		
		record = newsdate.split(" ")[0]
		print record
		#save += title
		title = title.replace("|", u"｜")
		title = title.replace("/", u"／")
		title = title.replace("\\", u"＼")
		title = title.replace("\"", u"\'\'")
		title = title.replace("?", u"？")
		title = title.replace(":", u"：")

		try:
			print title
		except:
			print "Title can't decode."
		#print content
		if not os.path.exists("kmwnews"):
			os.makedirs("kmwnews");
		savedate = newsdate[0:4]+ newsdate[5:7]+ newsdate[8:10]
		source = ""
		if u"中國時報"in newsdate:
			source = u"中國時報"
		elif u"工商時報"in newsdate:
			source = u"工商時報"
		else:
			source = u"未知來源"
		
		fn = os.path.join(os.path.dirname(__file__), "kmwnews", "["+savedate+"]["+source+"]["+title.strip()+"]"+".txt")
		try:
			f = codecs.open(fn, "w+", "utf-8")
			save = content
			#save = newsdate +"\n" + content
		except:
			print "Error: title error."
			fn = os.path.join(os.path.dirname(__file__), "Error"+str(i)+".txt")
			i = i+1
			#save = content
			save = title + newsdate +"\n" + content
			try:
				f = codecs.open(fn, "w+", "utf-8")
			except:
				print "Error whatever."
				continue
		
		f.write(save)
		f.close()
				
				

	browser.quit()
	readurl.close()
	
	return end
#except:
#	print "Something wrong:", sys.exc_info()[0]
		

#while(start != end+day):
if len(sys.argv) < 2:
	print "Get today's news. "
	end = getnews(start, end, False)
elif len(sys.argv) == 3:
	if not re.search("\d\d\d\d/\d\d/\d\d", sys.argv[1]):
		print "Input error."
		sys.exit(0)
	elif not re.search("\d\d\d\d/\d\d/\d\d", sys.argv[2]):
		print "Input error."
		sys.exit(0)
	else:
		try:
			sdate = time.strptime(sys.argv[1], "%Y/%m/%d")
			edate = time.strptime(sys.argv[2], "%Y/%m/%d")
		except:
			print "Input error."
			sys.exit(0)
		start = date(sdate[0], sdate[1], sdate[2])
		end = date(edate[0], edate[1], edate[2])
        if end < start:
            print "Input error."
            sys.exit(0)
	print "Get news from " + start.strftime("%Y-%m-%d") + " to " + end.strftime("%Y-%m-%d")+"."
	end = getnews(start, end, True)
else:
	print "Input Error."
    





