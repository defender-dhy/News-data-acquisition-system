from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymongo
from utils.db import mongo_client
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

count = 0
res = []


def wechatCrawler(Name):
    # 声明一个谷歌浏览器的驱动器
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    wait = WebDriverWait(driver, 10)
    url = 'https://weixin.sogou.com/'
    title_xpath = '//div[@class="txt-box"]/h3/a'
    time_xpath = '//span[@class="s2"]'
    content_xpath = '//p[@class="txt-info"]'
    writer_xpath = '//div[@class="s-p"]/a'
    content_url = '//div[@class="txt-box"]/h3/a'
    button_xpath = '//a[@id="sogou_next"]'
    global count
    global res
    res = []
    count = 0
    print('%s 开始爬取公众号: %s' % (datetime.now(), Name))
    driver.get(url)
    # 找到输入框id
    # wait.until(EC.presence_of_element_located((By.ID, 'query')))
    query = driver.find_element_by_id('query')
    query.send_keys(Name)
    # 找到搜索按钮
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'swz')))
    swz = driver.find_element_by_class_name('swz')
    swz.click()
    # 找到登陆按钮并点击
    # wait.until(EC.presence_of_element_located((By.ID, 'top_login')))
    try:
        top_login = driver.find_element_by_id('top_login')
        top_login.click()
    except NoSuchElementException:
        print("cookie set")
    # 显示等待是否登陆成功
    WebDriverWait(driver, 1000).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'yh')
        )
    )
    print('登陆成功')
    myclient = pymongo.MongoClient(mongo_client)
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        raise Exception('cloud_academic数据库不存在')
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    content = None
    for str in collist:
        if (str == 'news_content'):
            content = mydb[str]
        else:
            continue
    while True:
        title_list = driver.find_elements_by_xpath(title_xpath)
        writer_list = driver.find_elements_by_xpath(writer_xpath)
        date_list = driver.find_elements_by_xpath(time_xpath)
        content_list = driver.find_elements_by_xpath(content_xpath)
        url_list = driver.find_elements_by_xpath(content_url)

        n = len(title_list)

        for i in range(len(title_list)):
            if (count % 10 == 0):
                print('%s 公众号:%s %s %d' % (datetime.now(), Name, '写入数据库数目:', count))
            temp_writer = writer_list[i].text
            if (temp_writer != Name):
                continue
            temp_title = title_list[i].text
            temp_date = date_list[i].text
            temp_content = content_list[i].text
            temp_url = url_list[i].get_attribute('href')
            filter = {'website_name': Name,
                      'title': temp_title,
                      'content': temp_content,
                      'writer': temp_writer}
            query = {'column_url': '',
                     'title': temp_title,
                     'content': temp_content,
                     'time': temp_date,
                     'url': temp_url,
                     'writer': temp_writer,
                     'website_name': Name,
                     'lang': '中',
                     'column': '',
                     'resource_type': ''
                     }

            count = count + 1
            print(query)
            content.update_one(filter, {'$set': query}, upsert=True)
        try:
            element = driver.find_element_by_xpath(button_xpath)
            driver.execute_script("arguments[0].click();", element)
        except NoSuchElementException:
            break
    print('%s 公众号:%s %s %d' % (datetime.now(), Name, '爬取数目:', count))
    driver.quit()
    temp = content.find({"website_name": Name})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res


def show_progress():
    return count


if __name__ == '__main__':
    print(wechatCrawler("新智元"))
