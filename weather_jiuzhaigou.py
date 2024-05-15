# -*- coding: utf-8 -*-'''
'''
Author       : Yuanting Ma
Github       : https://github.com/YuantingMaSC
LastEditors  : yuanting 
Date         : 2024-05-15 10:25:46
LastEditTime : 2024-05-15 10:30:31
FilePath     : /Jiuzhaigou_Crawler/weather_jiuzhaigou.py
Description  : 
Copyright (c) 2024 by Yuanting_Ma@163.com, All Rights Reserved. 
'''
# env    : python
# coding : utf-8

"""
@File       :  weather_jiuzhaigou.py.py
@Copyright  :  deeplearning
@Author     :  Yuanting Ma
@Date       :  2022/4/14
"""
import random
import re

from bs4 import BeautifulSoup
import time
from selenium import webdriver

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'tianqi.2345.com',
    'Referer': 'http://tianqi.2345.com/wea_history/60925.htm',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

if __name__ == "__main__":
    target_site = {'jiuzhaigou':60925, 'siguniangshan':70752}
    target = 'siguniangshan'
    request_url = f'http://tianqi.2345.com/wea_history/{target_site[target]}.htm'
    driver = webdriver.PhantomJS()
    driver.get(request_url)
    f = open('./weather.txt','a+')
    f.write('date,temperature_high,temperature_low,weather,wind,air_quality,')
    f.close()
    page_num = 0
    while True:
        address = BeautifulSoup(driver.page_source, 'lxml')
        weather_response = address.find_all('td')
        # print(weather_response)
        for item,loc_num in zip(weather_response,range(len(weather_response))):
            if re.match('.*\d{4}-\d{2}-\d{2}.*', item.text) is None:
                f = open('./weather.txt', 'a+')
                f.write('{},'.format(item.text))
                f.close()
            else:
                f = open('./weather.txt', 'a+')
                f.write('\n{},'.format(item.text))
                f.close()
            # print(item.text)
        print('page {} has been finished !'.format(page_num))
        page_num+=1
        driver.find_element_by_xpath("//a[contains(text(),'上一月')]").click()
        time.sleep(random.randint(1,5))

    # print(weather_response)
    # numbers_response = address.find_all('td',attrs={'class':'list-title'})
    # for i in range(len(dates_response)):
    #     file = open('./tourism_num_jiuzhaigou.txt', 'a+')
    #     file.write(dates_response[i].text.strip()+','+numbers_response[i].text.strip()+'\n')
    #     file.close()
    # time.sleep(random.randint(1,5))
    # print('the {} page has been patched !'.format(loc_num))