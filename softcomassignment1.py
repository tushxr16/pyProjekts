import requests
import os
import re
from bs4 import BeautifulSoup

path = 'C:\\'
os.chdir(path)
os.makedirs('WebScrapingInPython')
path = 'C:\\WebScrapingInPython\\'
os.chdir(path)
flder = ['India','World','Buisness','Homepage']
for i in flder :
    os.makedirs(i)
    os.chdir(path)

paths_url = {
             "INDIA":['C:\\WebScrapingInPython\\India\\','https://timesofindia.indiatimes.com/india/'],
             "WORLD":['C:\\WebScrapingInPython\\World\\','https://timesofindia.indiatimes.com/world/'],
             "BUISNESS":['C:\\WebScrapingInPython\\Buisness\\','https://timesofindia.indiatimes.com/business/'],
             "HOMEPAGE":['C:\\WebScrapingInPython\\Homepage\\','https://timesofindia.indiatimes.com/']
            }

def writing_ntp(elems,z,):
    if elems == "HOMEPAGE":
        url_dic = z[1]
        r = requests.get(url_dic)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        lin_ks = soup.find_all(href=re.compile('.cms'),limit=43)
        lin_ksz = list()
        i=1
        for hyji in lin_ks:
            if i >40:
                lin_ksz.append('https://timesofindia.indiatimes.com' + hyji.get('href'))
            else:
                i=i+1
    else:
        url_dic = z[1]
        r = requests.get(url_dic)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        lin_ks = soup.find_all(href=re.compile('.cms'),limit=11)
        lin_ksz = list()
        i=1
        for hyji in lin_ks:
            if i >8:
                lin_ksz.append(hyji.get('href'))
            else:
                i=i+1

    try :
        path_dic = z[0]
        url_dic = lin_ksz[0]
        rps = requests.get(url_dic)
        htmlContent = rps.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        hhwp = soup.find('div', class_='ga-headlines')
        dtete = soup.find('div', class_='_3Mkg- byline')
        ttl = soup.title
        url_da_title =ttl.text
        url_da_para = "\n\n" + hhwp.text + "\n\n"
        url_da_date = dtete.text
        os.chdir(path_dic)
        material__i = ("TITLE :\n"+url_da_title+"\n\nLINK :\n"+url_dic+"\n\nSource and Time :\n"+url_da_date+"\n\nTEXT :"+url_da_para)
        fh = open(elems + str(".txt") ,'w')
        fh.write (material__i)
        fh.close()
        os.chdir(path)
        i = 1
        while i<4:
            path_dic = z[0]
            url_dic = lin_ksz[i]
            rps = requests.get(url_dic)
            htmlContent = rps.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            hhwp = soup.find('div', class_='ga-headlines')
            dtete = soup.find('div', class_='_3Mkg- byline')
            ttl = soup.title
            url_da_title =ttl.text
            url_da_para = "\n\n" + hhwp.text + "\n\n"
            url_da_date = dtete.text
            os.chdir(path_dic)
            material__i = ("\n\n\nTITLE :\n"+url_da_title+"\n\nLINK :\n"+url_dic+"\n\nSource and Time :\n"+url_da_date+"\n\nTEXT :"+url_da_para)
            fh = open(elems + str(".txt") ,'a')
            fh.write (material__i)
            fh.close()
            os.chdir(path)
            i=i+1

    except:
        pass

for elems in paths_url:
    z = paths_url[elems]
    writing_ntp(elems,z)