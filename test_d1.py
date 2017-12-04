import unittest
import uncaptcha

results = [{'input':1122, 'output':3, 'offset':1},
            {'input':1111, 'output':4, 'offset':1},
            {'input':1234, 'output':0, 'offset':1},
            {'input':9123456789, 'output':9, 'offset':1},
            {'input':1212, 'output':6, 'offset':2},
            {'input':1122, 'output':0, 'offset':2},
            {'input':123425, 'output':4, 'offset':3},
            {'input':123123, 'output':12, 'offset':3},
            {'input':12131415, 'output':4, 'offset':4},
            ]
class UnCaptchaTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking {} with offset {} creates {}'.format(r['input'], r['offset'], r['output']))
            self.assertEqual(uncaptcha.uncaptcha(str(r['input']),r['offset']), r['output'])


if __name__ == '__main__':
    print('hekki wirkd')
    unittest.main()


