#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from bs4 import BeautifulSoup
import requests
import json
import re
import io
import sys
import codecs
import bs4
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #Change the default encoding of standard output
def Scraping(url='https://www.coronazaehler.de'):
  response = requests.get(url)
  response.encoding=response.apparent_encoding
  soup = BeautifulSoup(response.text ,'lxml')
  scrapDaily(soup)
  scrapToday(soup)

#get the daily statistik 
def scrapDaily(soup):   
  script_reg = re.compile(".*?overallChart.*?")
  jscode = soup.find('script',text = script_reg)
  ptn = r"[\[].*?]"
  result = re.findall(ptn,str(jscode))
  if result:
    date = result[0]
    cofirmedlist =  result[1]
    curedlist = result[2]  
  datepro = re.findall(r"\d\d\.\d\d",date)#date list
  cofirmedlistpro = re.findall(r"\d+",cofirmedlist)#daily confirmed list
  curedlistpro = re.findall(r"\d+",curedlist)#daily cured list
  #let the length of cured list, date list and confirmed list be the same  
  r = len(curedlistpro)
  l = len(cofirmedlistpro)
  cofirmedlistpro = cofirmedlistpro[(l-r):]
  datepro = datepro[(l-r):]
  l = len(cofirmedlistpro)
  datepro = datepro[:l]
  cofirmedlistpro = list(map(int, cofirmedlistpro))#convert string to int
  curedlistpro = list(map(int,curedlistpro))
  curvedata = {}
  #curvedata['date'] = datepro
  curvedata['confirmed'] = cofirmedlistpro
  curvedata['cured'] = curedlistpro
  with open('../covid19map/src/assets/daily.json', 'w') as f:#save data
    json.dump(curvedata,f)

#today statistik
def scrapToday(soup):  
  TotalResult = soup.find_all('h1',{"class":"card-number-big"})#Total cases in Germany
  res = {}
  total = {} 
  total['confirmed'] = TotalResult[0].get_text().replace(".",",")#Total confirmed cases in Germany
  total['cured'] = TotalResult[1].get_text().replace(".",",")#Total number of cures in Germany 
  total['death'] = TotalResult[2].get_text().replace(".",",")#Total deaths in Germany
  total['newconfirm'] = soup.find('span',{"class":"lightred"}).get_text().replace(".",",")#new confirmed cases today in Germany
  total['newdeath'] = soup.find('span', {"class":"card-number-small"}).get_text().replace(".",",")#new deaths today in Germany
  res['germantotal'] = total  
  stateInfo = soup.find_all('div',{"class":"col-xs-12 col-lg-6 col-xl-4 d-flex flex-column"})
  states = []
  for s in stateInfo:
    state = {}
    state['name'] = s.find('h4').get_text()
    state['death'] = int(s.find_all('h5')[0].get_text().replace(".",""))
    state['confirm'] = int(s.find_all('h5')[1].get_text().replace(".",""))
    trs = s.find('table').tbody.find_all('tr')
    cities =  []  
    for tr in trs: 
      city = {}
      city['name'] = tr.find_all('td')[0].get_text()
      city['death'] = tr.find_all('td')[2].get_text().replace(".","")
      city['confirm'] = tr.find_all('td')[3].get_text().replace(".","")
      #curedhtml = tr.find_all('td')[4].get_text()
      #city['cured'] = re.search(r"^\d+(.\d+)*",curedhtml).group()
      cities.append(city)
    state['city'] = cities
    states.append(state)
  res['children'] = states   
  with open('../covid19map/src/assets/today.json','w',encoding="utf-8") as f:
    json.dump(res,f,ensure_ascii=False)
  
if __name__=="__main__":
  Scraping()