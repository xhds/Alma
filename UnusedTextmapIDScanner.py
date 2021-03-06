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
        allTargetFilesPath = [targetDir + "\\" + i for i in os.listdir(targetDir) if (not re.match("TextMap", i) and not re.match("Textmap", i)) and os.path.splitext(i)[1]==".txt"]
        #allTargetFilesPath = self._getAllCS(targetDir)
        #allIDs = allIDs[27006:27047]
        #allIDs = allIDs[3274:3315]
        #allIDs = allIDs[3371:3387]
        allIDs = allIDs[3261:]
        fileCount = len(allTargetFilesPath)
        fileidx = 1
        allFiles = []
        for targetFilePath in allTargetFilesPath:
            allFiles.append(open(targetFilePath, "r", encoding="utf-8").read())
            sys.stdout.write("loading %d/%d\r" % (fileidx, fileCount))
            sys.stdout.flush()
            fileidx += 1
        sys.stdout.write("\nloading Done!\n")
        sys.stdout.flush()
        print(len(allIDs))
        fileidx = 0

        allPatters = []
        for id in allIDs:
            allPatters.append((id, "[\s]"+id+"[\s]"))

        for targetFile in allFiles:
            fileidx += 1
            removeIDs = []
            for idp in allPatters:
                if re.match(idp[1], targetFile):
                    removeIDs.append(idp[0])
            sys.stdout.write("loading %d/%d remove %d\r" % (fileidx, fileCount, len(removeIDs)))
            sys.stdout.flush()
            for id in removeIDs:
                allIDs.remove(id)

        for targetFile in allFiles:
            targetFile.close()

        with open(self._getUnusedIDsOutputFileName(outputDir), "x", encoding="utf-8") as outputFile:
            for id in allIDs:
                outputFile.write(id + "\n")
        sys.stdout.write("\nDone!")
        sys.stdout.flush()
        pass

    def _getAllCS(self, csDir):
        result = []
        for root, dirs, files in os.walk(csDir):
            for f in files:
                if os.path.splitext(f)[1]==".cs":
                    result.append(os.path.join(root, f))
        return result

    def FindAllUnusedIDsV2(self, allIDsFilePath, targetDir, outputDir):
        print("start at %s" % datetime.datetime.now())
        allIDs = None
        with open(allIDsFilePath, "r", encoding="utf-8") as allIDsFile:
            allIDs = [i.strip() for i in allIDsFile]
        allTargetFilesPath = [targetDir + "\\" + i for i in os.listdir(targetDir) if (not re.match("TextMap", i) and not re.match("Textmap", i)) and os.path.splitext(i)[1]==".txt"]
        fileCount = len(allTargetFilesPath)
        fileidx = 1
        allFiles = []
        for targetFilePath in allTargetFilesPath:
            allFiles.append(open(targetFilePath, "r", encoding="utf-8"))
            sys.stdout.write("loading %d/%d\r" % (fileidx, fileCount))
            sys.stdout.flush()
            fileidx += 1
        sys.stdout.write("\nloading Done!\n")
        sys.stdout.flush()
        #allIDs = allIDs[27006:27047]
        #allIDs = allIDs[3274:3315]
        #allIDs = allIDs[3371:3387]
        #allIDs = allIDs[3261:]
        removeIDs = []
        idCounts = len(allIDs)
        idIndex = 0
        for id in allIDs:
            idIndex += 1
            os.sys.stdout.write("processing id %d/%d  remove %d \r" % (idIndex, idCounts, len(removeIDs)))
            os.sys.stdout.flush()
            p = "[\s]"+id+"[\s]"
            found = False
            for f in allFiles:
                f.seek(0)
                for line in f:
                    if re.search(p, line):
                        removeIDs.append(id)
                        found = True
                        break
                if found:
                    break

        for id in removeIDs:
                allIDs.remove(id)

        for targetFile in allFiles:
            targetFile.close()

        with open(self._getUnusedIDsOutputFileName(outputDir), "x", encoding="utf-8") as outputFile:
            for id in allIDs:
                outputFile.write(id + "\n")
        sys.stdout.write("\nDone!")
        sys.stdout.flush()
        print("\nends at %s" % datetime.datetime.now())
        

if __name__ == "__main__":
    os.system("cls")
    s = UnusedTextmapIDScanner()
    #s.ScanAllTextmap(r"E:\ng_hsod_master\Assets\Resources\Data\_ExcelOutput", r"E:\\")
    s.FindAllUnusedIDs(r"E:\AllTextmapIDs-20180908-193508.txt", r"E:\ng_hsod_master\Assets\Resources\Data\_ExcelOutput", r"E:\\")
    #s.FindAllUnusedIDsV2(r"E:\AllTextmapIDs-20180908-193508.txt", r"E:\ng_hsod_master\Assets\Resources\Data\_ExcelOutput", r"E:\\")
    #s.FindAllUnusedIDs(r"E:\AllTextmapIDs-20180908-193508.txt", r"E:\ng_hsod_master\Assets\MoleMole", r"E:\\")
