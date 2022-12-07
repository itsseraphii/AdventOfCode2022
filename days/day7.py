from utils.aoc_utils import AOCDay, day


@day(7)
class Day7(AOCDay):
    def common(self):
        # Dictionary containing index of last accessed directory
        self.duplicateDirectoryIndex = {}
        self.directorySizes = {}

        # Build file system
        self.fileSystem = {'/': self.recursivePathBuilder('/')}

        return 0

    def part1(self):
        wantedSize = 0
        self.getDirectorySizePart1(self.fileSystem)
        for key, value in self.directorySizes.items():
            print(key, value)
            if value <= 100000:
                print('added')
                wantedSize += value

        return wantedSize

    def getDirectorySizePart1(self, directory: dict):
        size = 0
        for key, value in directory.items():
            if type(value) == dict:
                self.directorySizes[key] = self.getDirectorySizePart1(value)
                size += self.directorySizes[key]
            else:
                size += value

        return size

    def part2(self):
        return 0

    def recursivePathBuilder(self, directoryName: str):
        directory = {}

        offset = 0 if directoryName not in self.duplicateDirectoryIndex else self.duplicateDirectoryIndex[
            directoryName]

        pain = self.inputData[offset:]

        cdIndex = pain.index('$ cd ' + directoryName)

        self.duplicateDirectoryIndex[directoryName] = cdIndex

        line = cdIndex + 2

        while len(self.inputData) > line and self.inputData[line][0] != '$':
            if self.inputData[line][:3] == 'dir':
                directoryName: str = self.inputData[line][4:]

                directory[directoryName] = self.recursivePathBuilder(
                    directoryName)
            else:
                size, name = self.inputData[line].split(' ')
                directory[name] = int(size)

            line += 1

        return directory
