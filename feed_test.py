import unittest
import logging
from main import Main

logging.basicConfig(
    filename="log/test.log",
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s,%(msecs)d %(levelname)-8s[%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S'
)


class FeedTest(unittest.TestCase):

    def test_run(self):
        main = Main()
        tags = main.get_tag_list('beach')
        self.assertEquals(True, len(tags) > 1)

        logging.debug('Test: length {}'.format(len(tags)))
        logging.debug('\n'.join(set(tag['src'] for tag in tags)))


if __name__ == '__main__':
    unittest.main()
