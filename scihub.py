'''
Download tool for sci-hub

Qijia Zhang
22/10/2020
'''
# encoding:utf-8

import requests
import urllib
import re
import socket
from bs4 import BeautifulSoup
def download_scihub():
	weburl = 'https://www.sci-hub.ren/'
	socket.setdefaulttimeout(3000)

	while 1:
		a=input("doi : ")
		print("正在连接",weburl+a)
		page=requests.get(weburl+a).text
		
		if page=='':
			print("连接失败!doi格式不对！")
			continue
		#print(page)
		#if page.find
		print("连接成功")


		soup=BeautifulSoup(page,'lxml')
		#print(soup)

		dt_list=soup.find_all('li')
		#print(dt_list)
		if(dt_list==[]):
			print("下载不下来！")
			continue
		ok=0
		for tag in dt_list:
			#print(tag)
			if (tag.get_text().find('save')>0):
				tag_a=tag.find('a').attrs['onclick']
				fileurl=re.findall(re.compile('\'+(.*pdf)\?'),tag_a)
				print("发现了",fileurl)
				filename = re.findall(re.compile('(\w+.pdf)'),fileurl[0])
				if (fileurl[0].startswith('//')):
					fileurl[0]='https:'+fileurl[0]
					ok=1
					return fileurl[0],filename[0]
					'''
				print("开始下载:",filename[0])

				urllib.request.urlretrieve(fileurl[0], filename[0])
				print("下载完毕！")
				'''
				
				#return
				'''
			else:
				print("无法下载!")
				'''
		if (ok==0):
			print("无法下载!没有对应的文章,检查一下doi号")
			continue

def recu_down(url,filename): # recurrent download with ContentTooShortError
    print("开始下载:",filename)
    try:
    	
        urllib.request.urlretrieve(url,filename)#也可以用request下载

    except urllib.error.ContentTooShortError:
        print ('网络不稳定导致中断，再次尝试...\n或者用迅雷下载这个链接吧: %s'%url)
        recu_down(url,filename)
    print("下载完毕！")
if __name__=='__main__':
	url,name=download_scihub()
	recu_down(url,name)

'''
num=1
#print(dt_list)
for tag_dt in dt_list:
    print("tag_dt",tag_dt)
    tag_a=tag_dt.find('a',text=re.compile('.*?[p|P][d|D][f|F].*?'))
    print("tag_a",tag_a)
    if tag_a:
        if num>int(a):
            break
        #tag_dd=tag_a.parent.next_sibling.next_sibling
        tag_dd=tag_a.parent.next_sibling

        #print(tag_dd,"\n",tag_a,"\n")

        #filename=tag_dd.find('b',
        filename=tag_dd.get_text().strip().replace(' ','_').replace('\n','_')+'.pdf'
        print('下载文件%d：'%num,filename)
        #tag_dt=tag_div.parent.previous_sibling.previous_sibling
        #tag_a=tag_dt.find('a',attrs={'href':re.compile('(/pdf/.+?)')})
        pdf_url='https://eprint.iacr.org/'+tag_a.attrs['href']
        print(pdf_url)
        urllib.request.urlretrieve(pdf_url, filename)
        
        #r = requests.get(pdf_url)
 
        #with open(filename, "wb") as f:
            #f.write(r.content)
        #print(filename,'下载结束')
        num+=1
        
  '''      
                 
#print htmlcode

# reg = r'<a href="(/pdf/.+?)" title'
# reg_pdf = re.compile(reg)
# pdf_list_all = reg_pdf.findall(htmlcode)

# pdf_list = []
# n=0
# for i in range(a) :
#     pdf_list.append(pdf_list_all[n])
#     n += 1


# n=0
# pdf_name = []
# for i in pdf_list:
#     pdf_name_tmp=pdf_list[n]
#     pdf_name_tmp=pdf_name_tmp.replace(".","_")
#     pdf_name_tmp=pdf_name_tmp.replace("/pdf/","")
#     pdf_name.append(pdf_name_tmp)
#     n += 1



# x=0


# for pdf in pdf_list[0:a]:
#     pdf_url = 'https://arxiv.org' + pdf + '.pdf'
#     print ('downloading %s \n' %pdf_name[x])
#     urllib.urlretrieve(pdf_url, '%s.pdf' %pdf_name[x])
#     print ('finish downloading NO.%d\n\n'%(x+1))
#     x += 1
