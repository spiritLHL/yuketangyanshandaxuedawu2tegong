from selenium import webdriver
import time
import random
import jieba


driver = webdriver.Chrome('C:\\chromedriver.exe')
urllists = []
driver.get("https://yanshan.yuketang.cn/pro/")
driver.maximize_window()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/button').click()
time.sleep(20)
driver.get("https://yanshan.yuketang.cn/pro/lms/845zVyirudC/4637424/studycontent")
time.sleep(5)
minid=7042000
maxid=7042999
i = 0
for c in range(maxid-minid+2):
    i +=1
    tempn = minid + i
    url = "https://yanshan.yuketang.cn/pro/lms/845zVyirudC/4637424/video/" + f"{tempn}"
    urllists.append(url)
print(urllists)
t = 0
c = 0
'''
driver.get("https://yanshan.yuketang.cn/pro/lms/845zVyirudC/4637424/video/7042907")
time.sleep(8)
driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-playbutton').click()
time.sleep(5)
print("ok")
page_text = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-time/span[2]').text
print(page_text)
list_time = jieba.lcut(page_text)
print(list_time)
'''
driver.minimize_window()
for a in urllists:
    try:
        driver.get(a)
        time.sleep(8)
        driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-playbutton').click()
        time.sleep(7)
        page_text = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-time/span[2]').text
        list_time = jieba.lcut(page_text)
        #print(list_time)
        full_time = int(list_time[-3]) * 60 + int(list_time[-1])
        over_text = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-time/span[1]').text
        over_time = jieba.lcut(over_text)
        over = int(over_time[-3]) * 60 + int(over_time[-1])
        wait = full_time - over  # 播放时长获取
        time.sleep(wait)
        t += 1
        print(f'已刷{t}个视频')
    except:
        c += 1
        print(f'有{c}链接不是视频')

