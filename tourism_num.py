# env    : python
# coding : utf-8

"""
@File       :  weather.py
@Copyright  :  deeplearning
@Author     :  Yuanting Ma
@Date       :  2022/4/14
"""
import random

from bs4 import BeautifulSoup
import requests
import time
import re

if __name__ == "__main__":
    pattern = re.compile('-?[1-9]\d*')
    file = open('./tourism_num_jiuzhaigou.txt', 'a+')
    file.write('date' + ',' + 'tourism_num' + '\n')
    file.close()
    for loc_num in range(143):
        if loc_num == 0:
            start_num = ''
        else:
            start_num = '?start='+str(loc_num*20)
        request_url = 'https://www.jiuzhai.com/news/number-of-tourists'+start_num
        address = BeautifulSoup(requests.get(request_url).text,features="lxml")
        dates_response = address.find_all('td',attrs={'class':'list-date small'})
        numbers_response = address.find_all('td',attrs={'class':'list-title'})
        for i in range(len(dates_response)):
            file = open('./tourism_num_jiuzhaigou.txt', 'a+')
            file.write(dates_response[i].text.strip()+','+str(pattern.search(numbers_response[i].text.strip()).group())+'\n')
            file.close()
        time.sleep(random.randint(1,5))
        print('the {} page has been patched !'.format(loc_num))
