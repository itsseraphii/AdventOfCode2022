from utils.aoc_utils import AOCDay, day

@day(4)
class Day4(AOCDay):
    def common(self):
        self.pairs = []
        for line in self.inputData:
            pair = line.split(',')
            pairOne = tuple(int(item) for item in pair[0].split('-'))
            pairTwo = tuple(int(item) for item in pair[1].split('-'))
            self.pairs.append([pairOne, pairTwo])
        return 0

    def part1(self):
        total = 0
        for pair in self.pairs:
            if ((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or 
                (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1])):
                total += 1
        return total

    def part2(self):
        total = 0
        for pair in self.pairs:
            # 2-8
            if ((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or 
                (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0])):
                total += 1
        return total
