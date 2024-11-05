import unittest


testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest.Runner))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)