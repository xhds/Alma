import datetime
import io
import os
import re

class UnusedTextmapIDScanner:
    def ScanAllTextmap(self, directory, outputPath):
        allScanFiles = [directory +"\\" + i for i in os.listdir(directory) if re.match("Textmap", i)]
        stringio = io.StringIO()
        for path in allScanFiles:
            with open(path, "r") as inputFile:
                for line in inputFile:
                    stringio.write(line[:line.find("\n")])
                    stringio.write("\n")

        with open(self._getOutputFileName(outputPath), "x") as outputFile:
            outputFile.write(stringio.getvalue())
        stringio.close()
        return None

    def _getOutputFileName(self, outputPath):
        t = datetime.datetime.now()
        return outputPath + r"\UnusedTextmapIDs-%s%02d%02d-%02d%02d%02d.txt" % (t.year, t.month, t.day, t.hour, t.minute, t.second)


if __name__ == "__main__":
    s = UnusedTextmapIDScanner()
    s.ScanAllTextmap(r"C:\Work", r"C:\Work")
    #x = [r"C:\Work" +"\\" + i for i in os.listdir(r"C:\Work") if re.match("Textmap", i)]
    #print(x)
    