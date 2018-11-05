from selenium import webdriver
 
from splinter.browser import Browser
import time
# -*- coding: utf-8 -*-
#from selenium import webdriver
#import os,time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
 
executable_path = {'executable_path':'C:\Python27\selenium\webdriver\firefox\geckodriver.exe'}
 
#'firefox',**executable_path
#with Browser()as browser:
 
browser = Browser('chrome')
def openBrowser():
    # Visit 访问的URL
    url = "http://imap.url.com/admin/"
    browser.visit(url)
 
    loginPage('weidong','xxx')
 
    
    #First menu
    fistMenu = browser.find_by_xpath('//ul[@id="main-menu"]/li[4]/a/span')
    #Second menu
    secondMenu = browser.find_by_xpath('//ul[@id="main-menu"]/li[4]/ul/li[1]/a/span')
    navigatePage(fistMenu,secondMenu)
 
    #browser.find_option_by_value(100)
    chooseDisplayRecord(100)
 
    webTable = getWebTableObject()
    #table total lines
    table_rows = webTable.find_by_tag('tr')
    #tabler total columns
    table_cols = table_rows[0].find_by_tag('th')
    
    getWebTableContent(webTable)
 
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
 
#Login
def loginPage(username,passwd):
	browser.fill('username',username)
	browser.fill('passwd',passwd)
	btnSubmit = browser.find_by_xpath('//form[@id="login"]/div[4]/button')
	btnSubmit.click()
	time.sleep(5)
 
def navigatePage(first,second):
	first.click()
	time.sleep(5)
	second.click()
	time.sleep(5)
 
def chooseDisplayRecord(number):
	#browser.find_option_by_value(100)
	browser.find_by_name('userlist_length').select(100)
 
def getWebTableObject():
	webTable = browser.find_by_xpath('//table[@id="userlist"]')
	time.sleep(10)
	return webTable
 
def getWebTableContent(WebTable):
	#pageNumber
	page = browser.find_by_xpath('//div[@id="userlist_paginate"]/ul/li[8]/a').text
	tbody = browser.find_by_xpath('//*[@id="userlist"]/tbody')
	
	table_rows = WebTable.find_by_tag('tr')
	currentRows = len(table_rows) -2
	print ("total lines:",currentRows)
	#tabler total columns
	#'''find the first tr in table , then find the th label
	table_cols = table_rows[0].find_by_tag('th')
	current_cols = len(table_cols)
	print ("total columns:",current_cols)
 
#Get RowData
def combineRowData(tbody):
	tbody = browser.find_by_xpath('//*[@id="userlist"]/tbody')
 
#def saveWebTableContent():
 
 
#def 
 
 
 
openBrowser()
#browser.quit()
# --------------------- 
# 作者：DevOps卜道师 
# 来源：CSDN 
# 原文：https://blog.csdn.net/davisking85/article/details/78870218 
# 版权声明：本文为博主原创文章，转载请附上博文链接！