# Solution pour le problème

def solution(string, ending):
    return string.endswith(ending)

# Cas de tests unitaires basés sur les exemples fournis

import unittest

class TestSolution(unittest.TestCase):
    
    # Tests qui devraient retourner True
    def test_true_cases(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja",   "ja"),
            ("sensei",  "i"),
            ("abc",     "abc"),
            ("abcabc",  "bc"),
            ("fails",   "ails"),
        )
        for string, ending in fixed_tests_True:
            with self.subTest(string=string, ending=ending):
                self.assertTrue(solution(string, ending))
    
    # Tests qui devraient retourner False
    def test_false_cases(self):
        fixed_tests_False = (
            ("sumo",    "omo"),
            ("samurai", "ra"),
            ("abc",     "abcd"),
            ("ails",    "fails"),
            ("this",    "fails"),
            ("spam",    "eggs"),
        )
        for string, ending in fixed_tests_False:
            with self.subTest(string=string, ending=ending):
                self.assertFalse(solution(string, ending))

# Exécution des tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSolution))
