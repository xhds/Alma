import datetime
import io
import os
import re
import sys

class UnusedTextmapIDScanner:
    def ScanAllTextmap(self, directory, outputDir):
        allScanFiles = [directory +"\\" + i for i in os.listdir(directory) if (re.match("Textmap", i) or re.match("TextMap", i)) and os.path.splitext(i)[1]==".txt"]
        fileCount = len(allScanFiles)
        fileidx = 1
        stringio = io.StringIO()
        for path in allScanFiles:
            with open(path, "r", encoding="utf-8") as inputFile:
                sys.stdout.write("processing %d/%d\r" % (fileidx, fileCount))
                sys.stdout.flush()
                fileidx += 1
                skipFirstLine = True
                for line in inputFile:
                    if skipFirstLine:
                        skipFirstLine = False
                        continue
                    stringio.write(line[:line.find("\t")])
                    stringio.write("\n")

        with open(self._getCollectAllIDsOutputFileName(outputDir), "x", encoding="utf-8") as outputFile:
            outputFile.write(stringio.getvalue())
        stringio.close()
        sys.stdout.write("\nDone!")
        sys.stdout.flush()
        pass

    def _getCollectAllIDsOutputFileName(self, outputDir):
        t = datetime.datetime.now()
        return outputDir + r"\AllTextmapIDs-%s%02d%02d-%02d%02d%02d.txt" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

    def _getUnusedIDsOutputFileName(self, outputDir):
        t = datetime.datetime.now()
        return outputDir + r"\UnusedTextmapIDs-%s%02d%02d-%02d%02d%02d.txt" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

    def FindAllUnusedIDs(self, allIDsFilePath, targetDir, outputDir):
        allIDs = None
        with open(allIDsFilePath, "r", encoding="utf-8") as allIDsFile:
            allIDs = [i.strip() for i in allIDsFile]
        allTargetFiles = [targetDir + "\\" + i for i in os.listdir(targetDir) if (not re.match("TextMap", i) and not re.match("Textmap", i)) and (os.path.splitext(i)[1]==".txt")]
        fileCount = len(allTargetFiles)
        fileidx = 1
        for targetFilePath in allTargetFiles:
            with open(targetFilePath, "r", encoding="utf-8") as targetFile:
                sys.stdout.write("processing %d/%d\r" % (fileidx, fileCount))
                sys.stdout.flush()
                fileidx += 1
                removeIDs = []
                for id in allIDs:
                    for line in targetFile:
                        if id in line:
                            removeIDs.append(id)
                            targetFile.seek(0)
                            break
                #print(removeIDs)
                for id in removeIDs:
                    allIDs.remove(id)
        
        with open(self._getUnusedIDsOutputFileName(outputDir), "x", encoding="utf-8") as outputFile:
            for id in allIDs:
                outputFile.write(id + "\n")
        sys.stdout.write("\nDone!")
        sys.stdout.flush()
        pass

if __name__ == "__main__":
    s = UnusedTextmapIDScanner()
    #s.ScanAllTextmap(r"E:\ng_hsod_master\Assets\Resources\Data\_ExcelOutput", r"E:\\")
    s.FindAllUnusedIDs(r"E:\AllTextmapIDs-20180908-193508.txt", r"E:\ng_hsod_master\Assets\Resources\Data\_ExcelOutput", r"E:\\")
    #x = [r"C:\Work" +"\\" + i for i in os.listdir(r"C:\Work") if re.match("Textmap", i)]
    #print(x)
    #with open(r"C:\Work\AllTextmapIDs-20180908-170935.txt", "r") as f:
    #    x = [i.strip() for i in f]
    #    print(x)
    
