import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
from datetime import datetime

'''
1. Chromedriver version : 90
2. Please take note that your path of driver is correct.
3. Please make sure that you Chormebrowser version as same as Chromedriver.
'''
try:
    # 指定chromedriver路徑
    driver = webdriver.Chrome('/Users/howard/Desktop/hahow/chromedriver')

    driver.get('https://github.com/hahow/hahow-recruit/graphs/contributors')
    time.sleep(5)
    names = driver.find_elements_by_xpath(
        './/a[@class="text-normal"]')
    contributors = []
    for name in names:
        contributors.append(name.get_attribute("href"))

    print("contributors_list:", contributors)

    time.sleep(5)

    #第二題, 檢查圖片是否存在
    # 打開前端頁面
    # 回hahow
    driver.find_element_by_xpath(
        '//a[contains(text(),"hahow-recruit")]').click()
    time.sleep(2)

    driver.find_element_by_xpath(
        '// body/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/article[1]/ul[1]/li[1]/a[1]').click()

    time.sleep(2)

    try:
        hero_list_page = driver.find_element_by_xpath(
            '//img[@src="/hahow/hahow-recruit/raw/master/assets/hero-list-page.png"]')
        hero_profile_page = driver.find_element_by_xpath(
            '//img[@src="/hahow/hahow-recruit/raw/master/assets/hero-profile-page.png"]')
        print("All imgs exist")
    except:
        print("Imgs does not exist")

    # 第三題

    driver.find_element_by_xpath(
        '//a[contains(text(),"hahow-recruit")]').click()
    time.sleep(2)

    # 進到測試端小專案說明頁面
    driver.find_element_by_xpath("//a[contains(text(), '測試端小專案說明')]").click()
    time.sleep(2)

    author = driver.find_element_by_xpath(
        '//body[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]')
    print("The last commiter is:", author.get_attribute("href"))

    driver.quit()
except Exception as e:
    print('Error! Code: {c}, Message, {m}'.format(
        c=type(e).__name__, m=str(e)))
