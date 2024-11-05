import unittest
class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


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
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.party_1 = Runner("Усейн",10)
        self.party_2 = Runner("Андрей",9)
        self.party_3 = Runner("Ник",3)
    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_run_1(self):
        self.tournament_1 = Tournament(90,self.party_1,self.party_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.party_2, self.party_3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.party_1, self.party_2, self.party_3)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
