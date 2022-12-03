from utils.aoc_utils import AOCDay, day


@day(3)
class Day3(AOCDay):
    def common(self):
        return 0

    def part1(self):
        return sum(map(lambda x: self.getCharPriority(self.getCommonChar(x)), self.inputData))

    def part2(self):
        total = 0
        for i in range(0, len(self.inputData)-1, 3):
            set1 = set(self.inputData[i])
            set2 = set(self.inputData[i+1])
            set3 = set(self.inputData[i+2])
            total += self.getCharPriority(set1.intersection(set2, set3).pop())
        return total

    def getCommonChar(self, rucksack):
        # Divide rucksack, set removes duplicates
        compartmentOne = set(rucksack[:len(rucksack)//2])
        compartmentTwo = set(rucksack[len(rucksack)//2:])

        return compartmentOne.intersection(compartmentTwo).pop()

    def getCharPriority(self, char):
        # a = 97
        # A = 65
        unicodeValue = ord(char)

        if (unicodeValue > 96): # Lowercase
            return unicodeValue - 96
        else: # Uppercase
            return unicodeValue - 38 # 65 - 27 offset as upper have higher value