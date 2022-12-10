from utils.aoc_utils import AOCDay, day


@day(10)
class Day10(AOCDay):
    def common(self):
        self.instructions = list(map(lambda x: (x[0:4], int(x[5:]) if x[3] != 'p' else 0), self.inputData))
        return 0

    def part1(self):
        register = 1
        # List of tuples (cycle, register)
        self.signalStrength = []
        cycle = 1

        for instruction, value in self.instructions:
            if instruction == 'noop':
                cycle += 1
            elif instruction == 'addx':
                cycle += 1
                self.logSignalStrength(cycle, register)
                cycle += 1
                register += value

            self.logSignalStrength(cycle, register)


        return sum(map(lambda x: x[0]*x[1], self.signalStrength))

    def logSignalStrength(self, cycle: int, register: int):
        if (((cycle - 20) % 40 ) == 0):
            self.signalStrength.append((cycle, register))

    def part2(self):
        return 0
