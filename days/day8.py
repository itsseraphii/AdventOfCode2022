from utils.aoc_utils import AOCDay, day

@day(8)
class Day8(AOCDay):
    def common(self):
        self.visibleMap = [[] for _ in range(len(self.inputData))]
        self.scenicScoreMap = [[] for _ in range(len(self.inputData))]

        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])):
                treeHeight = self.inputData[i][j]
                isVisible = 0
                u, d, l, r = 0, 0, 0, 0

                # Check up
                if i - 1 >= 0:
                    for k in range(i-1, -1, -1):
                        u += 1
                        if self.inputData[k][j] >= treeHeight:
                            break
                        elif (k == 0):
                            isVisible = 1
                else:   
                    isVisible = 1

                # Check down
                if i + 1 < len(self.inputData):
                    for k in range(i+1, len(self.inputData)):
                        d += 1
                        if self.inputData[k][j] >= treeHeight:
                            break
                        elif (k == len(self.inputData) - 1):
                            isVisible = 1
                else: 
                    isVisible = 1

                # Check left
                if j - 1 >= 0:
                    for k in range(j-1, -1, -1):
                        l += 1
                        if self.inputData[i][k] >= treeHeight:
                            break
                        elif (k == 0):
                            isVisible = 1
                else:
                    isVisible = 1

                # Check right
                if j + 1 < len(self.inputData[i]):
                    for k in range(j+1, len(self.inputData[i])):
                        r += 1
                        if self.inputData[i][k] >= treeHeight:
                            break
                        elif (k == len(self.inputData[i]) - 1):
                            isVisible = 1
                else:
                    isVisible = 1

                self.visibleMap[i].append(isVisible)
                self.scenicScoreMap[i].append(u*d*l*r)

        return 0

    def part1(self):
        return sum(map(lambda x: sum(x), self.visibleMap))

    def part2(self):
        return max(map(lambda x: max(x), self.scenicScoreMap))
