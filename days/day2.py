from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        # Rock (+1)
        # Paper (+2)
        # Scissors (+3)
        # Lose (+0)
        # Draw (+3)
        # Win (+6)
        return 0

    def part1(self):
        # Score matrix
        # i = enemy pick
        # j = player pick
        scoreGuidePartOne = {
            'A': {'X': 4, 'Y': 8, 'Z': 3},
            'B': {'X': 1, 'Y': 5, 'Z': 9},
            'C': {'X': 7, 'Y': 2, 'Z': 6},
        }
        score = 0
        for line in self.inputData:
            score += scoreGuidePartOne[line[0]][line[2]]
        return score

    def part2(self):
        # Score matrix
        # i = enemy pick
        # j = game result
        scoreGuidePartTwo = {
            'A': {'X': 3, 'Y': 4, 'Z': 8},
            'B': {'X': 1, 'Y': 5, 'Z': 9},
            'C': {'X': 2, 'Y': 6, 'Z': 7},
        }
        score = 0
        for line in self.inputData:
            score += scoreGuidePartTwo[line[0]][line[2]]
        return score