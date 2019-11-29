from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import platform
import time


class Main(object):
    _url = 'https://www.instagram.com/explore/tags'
    _opts = Options()
    _browser = None

    def __init__(self):
        self._opts.add_argument("--headless")
        if platform.system().__contains__('Windows'):
            self._browser = webdriver.Chrome(
                executable_path=r"./webdriver/windows/chromedriver.exe",
                options=self._opts
            )

    def get_tag_list(self, tag=None):
        """
        image list based in tag
        :param tag
        :rtype: list
        """
        if tag is None:
            raise Exception('Tag is required.')

        self._browser.get('{0}/{1}'.format(self._url, tag))

        time.sleep(1)

        lst = self._browser.find_element_by_class_name("KC1QD")
        res = lst.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div').get_attribute("innerHTML")
        soup = BeautifulSoup(res, "html.parser")
        tags = soup.findAll('img')

        self._browser.close()

        return tags
