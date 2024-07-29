import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

# Добавляем тесты в TestSuite
test_suite.addTests(test_loader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(test_loader.loadTestsFromTestCase(TournamentTest))

# Создаем TestRunner с verbosity=2
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
