from utils.aoc_utils import AOCDay, day

@day(6)
class Day6(AOCDay):
    def common(self):
        return 0

    def part1(self):
        return self.getStartMarkerPos(4)

    def part2(self):
        return self.getStartMarkerPos(14)

    def getStartMarkerPos(self, markerLength):
        for i in range(len(self.inputData[0])):
            codeSet = set()
            for j in range(markerLength):
                codeSet.add(self.inputData[0][i+j])

            if len(codeSet) == markerLength:
                return i + markerLength
        return 0
