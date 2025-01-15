import logging
import unittest
from rt_with_exceptions import Runner, Tournament


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.t = Tournament(101)

    def test_walk(self):
        try:
            test_w = Runner('Вася', -5)
            test_w.walk()
            self.assertTrue(test_w.distance < 101)
            logging.info(f"test_walk выполнен успешно")
        except ValueError as err:
            logging.error(err)
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            test_r = Runner(256, 5)
            test_r.run()
            logging.info(f"test_run выполнен успешно")
            self.assertTrue(test_r.distance > 101)
        except TypeError as err:
            logging.error(err)
            logging.warning("Неверный тип данных для объекта Runner")


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")