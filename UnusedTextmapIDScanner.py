import datetime
import io
import os
import re

class UnusedTextmapIDScanner:
    def ScanAllTextmap(self, directory, outputDir):
        allScanFiles = [directory +"\\" + i for i in os.listdir(directory) if re.match("Textmap", i)]
        stringio = io.StringIO()
        for path in allScanFiles:
            with open(path, "r") as inputFile:
                for line in inputFile:
                    stringio.write(line[:line.find("\n")])
                    stringio.write("\n")

        with open(self._getCollectAllIDsOutputFileName(outputDir), "x") as outputFile:
            outputFile.write(stringio.getvalue())
        stringio.close()
        return None

    def _getCollectAllIDsOutputFileName(self, outputDir):
        t = datetime.datetime.now()
        return outputDir + r"\AllTextmapIDs-%s%02d%02d-%02d%02d%02d.txt" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

    def _getUnusedIDsOutputFileName(self, outputDir):
        t = datetime.datetime.now()
        return outputDir + r"\UnusedTextmapIDs-%s%02d%02d-%02d%02d%02d.txt" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

    def FindAllUnusedIDs(self, allIDsFilePath, targetDir, outputDir):
        allIDs = None
        with open(allIDsFilePath, "r") as allIDsFile:
            allIDs = [i.strip() for i in allIDsFile]
        allTargetFiles = [targetDir + "\\" + i for i in os.listdir(targetDir) if re.match("target", i) and (os.path.splitext(i)[1]==".txt")]
        for targetFilePath in allTargetFiles:
            with open(targetFilePath, "r") as targetFile:
                removeIDs = []
                for id in allIDs:
                    for line in targetFile:
                        if id in line:
                            removeIDs.append(id)
                            targetFile.seek(0)
                            break
                print(removeIDs)
                for id in removeIDs:
                    allIDs.remove(id)
        
        with open(self._getUnusedIDsOutputFileName(outputDir), "x") as outputFile:
            for id in allIDs:
                outputFile.write(id + "\n")
        pass

if __name__ == "__main__":
    s = UnusedTextmapIDScanner()
    s.FindAllUnusedIDs(r"C:\Work\AllTextmapIDs-20180908-170935.txt", r"C:\Work", r"C:\Work")
    #x = [r"C:\Work" +"\\" + i for i in os.listdir(r"C:\Work") if re.match("Textmap", i)]
    #print(x)
    #with open(r"C:\Work\AllTextmapIDs-20180908-170935.txt", "r") as f:
    #    x = [i.strip() for i in f]
    #    print(x)
    
