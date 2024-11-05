import unittest

class Runner:
    # здесь в бегуне всего один аргумент,
    # имя, вы передаете два, скорость и имя, этот класс нужно исправить

    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed




    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False,"Тесты в этом кейсе замороженны")
    def test_walk(self):
        runner = Runner("a","b") # а здесь передаете только один аргумент, хотя нужно два
        for i in range (10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_run(self):
        runner = Runner("a","b")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_challenge(self):
        runner = Runner("a","b")
        runner = Runner("b","b")
        for i in range(10):
            runner.run()
        for i in range(10):
            runner.walk()
        self.assertNotEqual(runner.distance, 100)
        self.assertNotEqual(runner.distance, 50)

if __name__ == "__main__":
    unittest.main()


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.party_1 = Runner("Усейн", 10)
        self.party_2 = Runner("Андрей", 9)
        self.party_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.party_1, self.party_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.party_2, self.party_3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.party_1, self.party_2, self.party_3)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertFalse(last_runner_name == "Ник")
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()



