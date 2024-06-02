import unittest
import project_validation


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        postcodelist = ["ST3 5NP", "faith12"]
        for n in range(0, len(postcodelist)):
            print(n)
            print(project_validation.postcode_check(postcodelist[n]))
            self.assertEqual(project_validation.postcode_check(postcodelist[n]), True)


if __name__ == '__main__':
    unittest.main()
