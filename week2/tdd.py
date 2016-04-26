import unittest

## Implement roman numerals

class RomanNumeral():
    def __init__(self, numeral):
        self._num = numeral

    values = {'I': 1, 'V': 5, 'X': 10}

    def asString(self):
        return self._num.upper()

    def asArabic(self):
        cur = 0
        for x in self.asString():
            cur += self.values[x]

        return cur

class TestRomanNumeral(unittest.TestCase):
    def test_constructor(self):
        blank = RomanNumeral('')
        self.assertEqual('', blank.asString())
        fifty_five = RomanNumeral('lv')
        self.assertEqual('LV', fifty_five.asString())
#        self.assertRaises(fifty_five.num, AttributeError)

    def test_convert_to_arabic(self):
        blank = RomanNumeral('')
        self.assertEqual(0, blank.asArabic())
        twelve = RomanNumeral('xii')
        self.assertEqual(12, twelve.asArabic())

#    'LV' over 'lv'

if __name__ == '__main__':
    unittest.main()
