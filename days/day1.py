from utils.aoc_utils import AOCDay, day

@day(1)
class Day1(AOCDay):
    def common(self):
        ## Add seperator at the end for the last elf
        self.inputData.append('')
        return 0

    def part1(self):
        highestCalorieCount = 0
        elfCalorieCount = 0
        for line in self.inputData :
            if (line.isnumeric()):
                elfCalorieCount += int(line)
            else :
                highestCalorieCount = elfCalorieCount if elfCalorieCount > highestCalorieCount else highestCalorieCount
                elfCalorieCount = 0
        return highestCalorieCount

    def part2(self):
        highestCalorieCount = [0,0,0]
        elfCalorieCount = 0
        for line in self.inputData :
            if (line.isnumeric()):
                elfCalorieCount += int(line)
            else :
                highestCalorieCount[0] = elfCalorieCount if elfCalorieCount > highestCalorieCount[0] else highestCalorieCount[0]
                highestCalorieCount.sort()
                elfCalorieCount = 0
        return sum(highestCalorieCount)
