from selenium import webdriver
import time
import pymongo
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from utils.db import mongo_client

res = []


def next_crawler(web_url, title_xpath, content_xpath, content_url, time_xpath, writer_xpath, button_xpath, website_name,
                 lang, column, resource_type):
    # website_name网站名
    # lang语言
    # column相关栏目
    # resource_type资源类型
    # 加载启动项
    global res
    res = []
    print('%s 开始爬取: ' % datetime.now() + web_url)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('--ignore-certificate-errors')  # 主要是该条
    option.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=option)
    driver.get(url=web_url)
    # db
    myclient = pymongo.MongoClient(mongo_client)
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        raise Exception('cloud_academic数据库不存在')
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    content = None
    for str in collist:
        if str == 'news_content':
            content = mydb[str]
        else:
            continue

    count = 0

    while True:
        flags = {'title': 1, 'writer': 1, 'date': 1, 'content': 1, 'url': 1}

        try:
            title_list = driver.find_elements_by_xpath(title_xpath)
            temp_title = title_list[0].text
            temp_query = {"title": temp_title}
            if content.count_documents(temp_query) != 0:
                print('%s %s %s' % (datetime.now(), web_url, '发现重复标题，提前退出'))
                break
            if len(title_list) == 0:
                flags['title'] = 0
        except NoSuchElementException:
            flags['title'] = 0
        except Exception as e:
            flags['title'] = 0
            print(e)
        try:
            # print(writer_xpath)
            writer_list = driver.find_elements_by_xpath(writer_xpath)
            if (len(writer_list) == 0):
                flags['writer'] = 0
        except NoSuchElementException:
            flags['writer'] = 0
        except Exception as e:
            flags['writer'] = 0
            print(e)
        try:
            date_list = driver.find_elements_by_xpath(time_xpath)
            if (len(date_list) == 0):
                flags['date'] = 0
        except NoSuchElementException:
            flags['date'] = 0
        except Exception as e:
            flags['date'] = 0
            print(e)
        try:
            print(content_xpath)
            content_list = driver.find_elements_by_xpath(content_xpath)
            if (len(content_list) == 0):
                flags['content'] = 0
        except NoSuchElementException:
            flags['content'] = 0
        except Exception as e:
            flags['content'] = 0
            print(e)
        try:
            url_list = driver.find_elements_by_xpath(content_url)
            if (len(url_list) == 0):
                flags['url'] = 0
        except NoSuchElementException:
            flags['url'] = 0
        except Exception as e:
            print(e)
            flags['url'] = 0

        print(flags)
        try:
            for i in range(len(title_list)):
                temp_title = title_list[i].text if flags['title'] == 1 else 'null'
                temp_writer = writer_list[i].text if flags['writer'] == 1 else 'null'
                temp_date = date_list[i].text if flags['date'] == 1 else 'null'
                temp_content = content_list[i].text if flags['content'] == 1 else 'null'
                temp_url = url_list[i].get_attribute('href') if flags['url'] == 1 else 'null'

                filter = {'column_url': web_url,
                          'title': temp_title,
                          'content': temp_content,
                          'url': temp_url,
                          'writer': temp_writer}
                query = {'column_url': web_url,
                         'title': temp_title,
                         'content': temp_content,
                         'time': temp_date,
                         'url': temp_url,
                         'writer': temp_writer,
                         'website_name': website_name,
                         'lang': lang,
                         'column': column,
                         'resource_type': resource_type
                         }
                print(query)

                count = count + 1
                if (count % 10 == 0):
                    print('%s %s %s %d' % (datetime.now(), web_url, '写入数据库进度:', count))
                content.update_one(filter, {'$set': query}, upsert=True)
        except IndexError:
            pass
        try:
            element = driver.find_element_by_xpath(button_xpath)
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            # WebDriverWait(driver, timeout=15).until(
            #     lambda driver: driver.execute_script('return document.readyState === "complete"')
            # )
            # print(driver.execute_script('return document.readyState'))
        except NoSuchElementException:
            break

    print('%s %s %s %d' % (datetime.now(), web_url, '爬取数目:', count))
    driver.quit()
    temp = content.find({"website_name": website_name, "column": column})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res


if __name__ == '__main__':
    myclient = pymongo.MongoClient(mongo_client)
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        raise Exception('cloud_academic数据库不存在')
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    content = None
    for str in collist:
        if str == 'news_xpath':
            xpath = mydb[str]
        else:
            continue
        myquery = {"type": 0}
        myclient.close()
        for x in xpath.find(myquery):
            next_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                         x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                         x['website_name'], x['lang'], x['column'], x['resource_type'])
