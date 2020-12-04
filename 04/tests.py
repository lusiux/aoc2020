import unittest
from main import answer_one, answer_two
from main import Passport

valid_passport = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""

invalid_passport = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""

passport_wo_cid = """hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm"""

another_invalid_passport = """hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

class AoC03Test(unittest.TestCase):

    def testCalculation(self):
        pass

    def testCalculationTwo(self):
        pass

    def testParsingAndValidPassport(self):
        passport = Passport.from_string(valid_passport)
        self.assertTrue(passport.is_valid())

    def testParsingAndInvalidPassport(self):
        passport = Passport.from_string(invalid_passport)
        self.assertFalse(passport.is_valid())

    def testParsingAndAnotherInvalidPassport(self):
        passport = Passport.from_string(another_invalid_passport)
        self.assertFalse(passport.is_valid())

    def testPassportWithoutCID(self):
        passport = Passport.from_string(passport_wo_cid)
        self.assertTrue(passport.is_valid())

if __name__ == "__main__": 
    unittest.main()