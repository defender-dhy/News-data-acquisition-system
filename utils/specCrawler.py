import requests
from lxml import etree


def getSpecTree(url):
    html = None
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()  # 状态不是200则发生HTTPError异常
        r.encoding = r.apparent_encoding
        html = r.text
    except Exception as e:
        print(e)
        return "产生了HTTPError异常"
    tree = etree.HTML(html)
    return tree


def getSpecContent(tree, xpath, key):
    ret = None
    if key == 'article_xpath':
        ret = etree.toString(tree.xpath(xpath)[0])
    else:
        ret = tree.xpath(xpath)[0].text
    return ret


def getSpecContentDriver(driver, xpath, key):
    ret = None
    if key == 'article_xpath':
        ret = etree.toString(driver.find_element_by_xpath(xpath))
    else:
        ret = driver.find_element_by_xpath(xpath).text
    return ret
