from utils.aoc_utils import AOCDay, day
import copy

@day(5)
class Day5(AOCDay):
    def common(self):
        self.maxInitialHeight = 0

        while self.maxInitialHeight <= len(self.inputData):
            if (self.inputData[self.maxInitialHeight][1] != '1'):
                self.maxInitialHeight += 1
            else:
                print('Something went horribly wrong')
                break

        self.nbCrateStacks = int(max(filter(lambda x: x != '', self.inputData[self.maxInitialHeight].split(' '))))

        self.crates = [[] for x in range(self.nbCrateStacks)]

        # Builds array of char arrays representing the crates
        for i in range(self.maxInitialHeight-1, -1, -1):
            for crateIndex in range(0, self.nbCrateStacks):
                crateSymbol = self.inputData[i][1 + int(crateIndex) * 4]
                if (crateSymbol != ' '):
                    self.crates[crateIndex].append(self.inputData[i][1 + int(crateIndex) * 4])

        # Tuple with (amount, from, to)
        self.moves = []
        for i in range(self.maxInitialHeight + 2, len(self.inputData)):
            splitMoves = self.inputData[i][5:].split(' ')
            self.moves.append((int(splitMoves[0]), int(splitMoves[2]), int(splitMoves[4])))

        return 0

    def part1(self):
        crateStack = copy.deepcopy(self.crates)
        for move in self.moves:
            for x in range(move[0]):
                # Move crates one at a time
                if (len(crateStack[move[1]-1])):
                    crateStack[move[2]-1].append(crateStack[move[1]-1].pop())
                else:
                    break

        return "".join(list(map(lambda x: x.pop(), crateStack)))

    def part2(self):
        crateStackTwo = copy.deepcopy(self.crates)
        for move in self.moves:
            # Move crates in batches
            moveAmount = move[0]

            # No crates to move, nothing else to do with this move
            if (len(crateStackTwo[move[1]-1]) == 0):
                continue
            # Prevent out of bounds, move ALL the crates
            elif (len(crateStackTwo[move[1]-1]) - moveAmount <= 0):
                moveAmount = len(crateStackTwo[move[1]-1])
            
            # Get array in order to insert in target. Then pop one by one because I couldn't find the function to mass pop XD
            crateStackTwo[move[2]-1].extend(crateStackTwo[move[1]-1][-moveAmount:])
            for x in range(moveAmount):
                crateStackTwo[move[1]-1].pop()

        return "".join(list(map(lambda x: x.pop() if (len(x)) else '', crateStackTwo)))
