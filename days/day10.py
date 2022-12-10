from utils.aoc_utils import AOCDay, day


@day(10)
class Day10(AOCDay):
    def common(self):
        self.cycle = 1
        self.register = 1
        self.instructions = list(map(lambda x: (x[0:4], int(x[5:]) if x[3] != 'p' else 0), self.inputData))
        self.signalStrength = []
        self.CRT = []

        for instruction, value in self.instructions:
            if instruction == 'noop':
                self.computeCycle()
            elif instruction == 'addx':
                self.computeCycle()
                self.computeCycle()
                self.register += value

        return 0

    def part1(self):
        return sum(map(lambda x: x[0]*x[1], self.signalStrength))

    def part2(self):
        # Split CRT into lines
        screen = []
        for i in range(0, len(self.CRT), 40):
            screen.append(self.CRT[i:i+40])
        
        for line in screen:
            print(''.join(line))

        return 0

    def computeCycle(self):
        sprite = (self.register - 1, self.register, self.register + 1)
        if self.cycle % 40 in sprite:
            self.CRT.append('#')
        else:
            self.CRT.append('.')

        if (((self.cycle - 20) % 40 ) == 0):
            self.signalStrength.append((self.cycle, self.register))

        self.cycle += 1