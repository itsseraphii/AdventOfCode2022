from utils.aoc_utils import AOCDay, day

@day(9)
class Day9(AOCDay):
    def common(self):
        self.instructions = list(map(lambda x: (x[0], int(x[2:])), self.inputData))
        return 0

    def part1(self):
        self.headPos = (0, 0)
        self.tailPos = (0, 0)
        self.visitedPos = set()
        self.visitedPos.add(self.tailPos)

        for instruction in self.instructions:
            direction, distance = instruction
            for _ in range(distance):
                self.move(direction)
        
        return len(self.visitedPos)

    def move(self, direction: str):
        if direction == 'U':
            if self.headPos[1] >= self.tailPos[1] + 1:
                self.tailPos = self.headPos
            
            self.headPos = (self.headPos[0], self.headPos[1] + 1)
        elif direction == 'D':
            if self.headPos[1] <= self.tailPos[1] - 1:
                self.tailPos = self.headPos
            
            self.headPos = (self.headPos[0], self.headPos[1] - 1)

        elif direction == 'R':
            if self.headPos[0] >= self.tailPos[0] + 1:
                self.tailPos = self.headPos
            
            self.headPos = (self.headPos[0] + 1, self.headPos[1])
        
        elif direction == 'L':
            if self.headPos[0] <= self.tailPos[0] - 1:
                self.tailPos = self.headPos
            
            self.headPos = (self.headPos[0] - 1, self.headPos[1])

        self.visitedPos.add(self.tailPos)

    def part2(self):
        tailLength = 10
        self.rope = [(0,0) for _ in range(tailLength)]
        self.visitedPosPart2 = set()
        self.visitedPosPart2.add(self.rope[0])

        for instruction in self.instructions:
            direction, distance = instruction
            for _ in range(distance):
                
                # Move head
                if direction == 'U':
                    self.rope[0] = (self.rope[0][0], self.rope[0][1] + 1)
                elif direction == 'D':
                    self.rope[0] = (self.rope[0][0], self.rope[0][1] - 1)
                elif direction == 'R':
                    self.rope[0] = (self.rope[0][0] + 1, self.rope[0][1])
                elif direction == 'L':
                    self.rope[0] = (self.rope[0][0] - 1, self.rope[0][1])
                
                # Move tail
                for ropeIndex in range(1, tailLength):
                    self.moveToTouchHead(direction, ropeIndex)

                print(self.rope[9])
                self.visitedPosPart2.add(self.rope[tailLength-1])


        return len(self.visitedPosPart2)

    def moveToTouchHead(self, direction: str, ropeIndex: int):
        if direction == 'U':
            if (self.rope[ropeIndex-1][1] - self.rope[ropeIndex][1]) > 1:
                self.rope[ropeIndex] = (self.rope[ropeIndex-1][0], self.rope[ropeIndex - 1][1] - 1)

        elif direction == 'D':
            if (self.rope[ropeIndex-1][1] - self.rope[ropeIndex][1]) < -1:
                self.rope[ropeIndex] = (self.rope[ropeIndex-1][0], self.rope[ropeIndex - 1][1] + 1)

        elif direction == 'R':
            if (self.rope[ropeIndex-1][0] - self.rope[ropeIndex][0]) > 1:
                self.rope[ropeIndex] = (self.rope[ropeIndex-1][0] - 1, self.rope[ropeIndex - 1][1])

        elif direction == 'L':
            if (self.rope[ropeIndex-1][0] - self.rope[ropeIndex][0]) < -1:
                self.rope[ropeIndex] = (self.rope[ropeIndex-1][0] + 1, self.rope[ropeIndex - 1][1])


    