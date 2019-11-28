import unittest
import logging

logging.basicConfig(
    filename="log/test.log",
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s,%(msecs)d %(levelname)-8s[%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S'
)


class FeedTest(unittest.TestCase):

    def test_run(self):
        result = True
        self.assertEquals(True, result)
        logging.debug('Test: {}'.format(result))


if __name__ == '__main__':
    unittest.main()
