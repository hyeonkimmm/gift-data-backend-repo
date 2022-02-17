# https://search.shopping.naver.com/best/home?categoryCategoryId=ALL&categoryDemo=M02&categoryRootCategoryId=ALL&chartDemo=A00&chartRank=1&period=P1D&windowCategoryId=20000002&windowDemo=M02&windowRootCategoryId=20000002
'''
네이버 쇼핑 인사이트 데이터랩 샐레니움 + bs4 활용한 크롤링 자동화 구현
2022-02-15 hkim
참고 : https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
'''
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# import os

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:/Users/hyeon/Desktop/side-project/gift-data-backend-repo/driver/chromedriver')
driver.implicitly_wait(3)
driver.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
# HTTP GET Request
req = requests.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
# content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(1) > div > div:nth-child(1) > span
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[5]/a').click()

# 순위 결과 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > div > div.rank_top1000_scroll > ul')
extracted = a[0].text
extracted = extracted.replace(' ', '')
f = open("새파일.txt", 'w')
f.write(extracted)
f.close()
