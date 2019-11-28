from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


class Main(object):
    opts = Options()
    browser = None

    def __init__(self):
        self.opts.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path=r"chromedriver.exe",
            options=self.opts
        )

    def gettaglist(self, tag=None):
        if tag is None:
            raise Exception('tag is required')

        self.browser.get("https://www.instagram.com/explore/tags/boobs")

        time.sleep(2)

        lst = self.browser.find_element_by_class_name("KC1QD")
        res = lst.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div').get_attribute("innerHTML")
        soup = BeautifulSoup(res, "html.parser")
        tags = soup.findAll('img')

        print('\n'.join(set(tag['src'] for tag in tags)))

        self.browser.close()

        return 'ok'
