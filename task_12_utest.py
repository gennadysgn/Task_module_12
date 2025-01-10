import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results.values():
            result = {}
            for k, v in res.items():
                result[k] = v.name
            print(result)

    def test_tournament_1(self):
        test1 = rt.Tournament(90, self.runner_1, self.runner_3)
        test1_res = test1.start()
        TournamentTest.all_results['test_tournament_1'] = test1_res
        self.assertTrue(test1_res[max(test1_res)] == 'Ник')

    def test_tournament_2(self):
        test2 = rt.Tournament(90, self.runner_2, self.runner_3)
        test2_res = test2.start()
        TournamentTest.all_results['test_tournament_2'] = test2_res
        self.assertTrue(test2_res[max(test2_res)] == 'Ник')

    def test_tournament_3(self):
        test3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        test3_res = test3.start()
        TournamentTest.all_results['test_tournament_3'] = test3_res
        self.assertTrue(test3_res[max(test3_res)] == 'Ник')


if __name__ == "__main__":
    unittest.main()

# Консоль:
# {1: 'Усэйн', 2: 'Ник'}
# {1: 'Андрей', 2: 'Ник'}
# {1: 'Усэйн', 2: 'Андрей', 3: 'Ник'}
