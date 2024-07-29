import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            finished = []
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    finished.append(participant)
            for participant in finished:
                self.participants.remove(participant)

        return finishers


def skip_if_frozen(test_func):
    def wrapper(*args, **kwargs):
        self = args[0]
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(*args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @skip_if_frozen
    def test_run(self):
        self.usain.run()
        self.assertEqual(self.usain.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        self.nick.walk()
        self.assertEqual(self.nick.distance, 3)

    @skip_if_frozen
    def test_challenge(self):
        self.usain.run()
        self.nick.walk()
        self.assertGreater(self.usain.distance, self.nick.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(results[1].name == self.usain.name)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[1].name == self.andrey.name)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[3].name == self.nick.name)


if __name__ == '__main__':
    unittest.main()
