import unittest
import logging
from main import Main
import platform

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
        logging.debug('System: {}'.format(platform.system()))

        if platform.system().__contains__('Windows'):
            tags = main.get_tag_list('ecvitoria')
            print(tags)
            self.assertEqual(True, len(tags) > 1)
            logging.debug('Test: length {}'.format(len(tags)))
            logging.debug('\n'.join(set(tag['src'] for tag in tags)))
        else:
            self.assertEqual(platform.system().__contains__('Windows'), False)


if __name__ == '__main__':
    unittest.main()
