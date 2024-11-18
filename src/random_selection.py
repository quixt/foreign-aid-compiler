import csv, random
SELECTION_COUNT = 50

selectionData = open("../compiled_data/selected.csv", "w")
selectionData.write("")
selectionData.close()

selectionData = open("../compiled_data/selected.csv", "w")
compiledData = open("../compiled_data/compiled.csv","r")
selectionDataWriter = csv.writer(selectionData)
compiledDataReader = csv.reader(compiledData)

compiledList = []
selectionList = []
for r in compiledDataReader:
    compiledList.append(r)

selectedList = []
while len(selectionList) < SELECTION_COUNT:
    index = random.randint(1,len(compiledList)-1)
    if not index in selectionList:
        selectionList.append(index)
print(selectionList)
for i in selectionList:
    selectedList.append(f"{compiledList[i][0]} {compiledList[i][1]}")
print(selectedList)
selectionData.close()
compiledData.close()