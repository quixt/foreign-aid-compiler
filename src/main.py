import csv
#Constants
COMPILED_FILENAME = "compiled.csv"
#File overwrite
compiledDataOverwrite = open(f"../compiled_data/{COMPILED_FILENAME}","w",newline='')
compiledDataOverwrite.write("")
compiledDataOverwrite.close()
#Compiling variables
header = ["country","year","aid_per_cap","eiu_dem_index","gdp_per_cap","hum_rights_index","pop_growth","pop_density","regime_type"]

#Final raw dataset
compiledData = open(f"../compiled_data/{COMPILED_FILENAME}","w",newline='')

#Create writing object to write to compiled data CSV
writer = csv.writer(compiledData)
writer.writerow(header)

#Reading data
countryAid = open("../data/countryAid.csv","r")
countryDemocracyIndex = open("../data/countryDemocracyIndex.csv","r")
countryGDPperCapita = open("../data/countryGDPperCapita.csv","r")
countryHumanRightsIndex = open("../data/countryHumanRightsIndex.csv","r")
countryPopulation = open("../data/countryPopulation.csv","r")
countryPopulationDensity = open("../data/countryPopulationDensity.csv","r")
countryRegimeType = open("../data/countryRegimeType.csv","r")
#CSV readers
countryAidReader = csv.reader(countryAid)
countryDemocracyIndexReader = csv.reader(countryDemocracyIndex)
countryGDPperCapitaReader = csv.reader(countryGDPperCapita)
countryHumanRightsIndexReader=csv.reader(countryHumanRightsIndex)
countryPopulationReader = csv.reader(countryPopulation)
countryPopulationDensityReader = csv.reader(countryPopulationDensity)
countryRegimeTypeReader = csv.reader(countryRegimeType)

#Main block
rowContainer = {}
rowList = []

#Sort and clean raw data from datasets
for r in countryAidReader:
    try:
        if int(r[8]) > 2005 and r[7] == "Obligations":
            rowContainer[r[1]+"_" + r[8]] = [r[1],int(r[8]),int(r[10])]
    except:
        continue

for r in countryDemocracyIndexReader:
    if r[0]+"_"+r[2] in rowContainer:
        rowContainer[r[0]+"_"+r[2]].append(float(r[3]))

for r in countryGDPperCapitaReader:
    for i in range(50,67):
        if len(r) > 0 and r[0]+"_"+str(i+1956) in rowContainer:
            try:
                rowContainer[r[0]+"_"+str(i+1956)].append(float(r[i]))
            except:
                continue

for r in countryHumanRightsIndexReader:
    if f"{r[0]}_{r[2]}" in rowContainer:
        rowContainer[f"{r[0]}_{r[2]}"].append(float(r[3]))

for r in countryPopulationReader:
    if f"{r[0]}_{r[2]}" in rowContainer:
        rowContainer[f"{r[0]}_{r[2]}"].append(int(r[3]))

for r in countryPopulationDensityReader:
    if f"{r[0]}_{r[2]}" in rowContainer:
        rowContainer[f"{r[0]}_{r[2]}"].append(float(r[3]))

def regimeType(num:int):
    regimeNum = ["CA","EA","ED","LD"]
    return regimeNum[num]

for r in countryRegimeTypeReader:
    if f"{r[0]}_{r[2]}" in rowContainer:
        rowContainer[f"{r[0]}_{r[2]}"].append(regimeType(int(r[3])))

delKeys = []
for key in rowContainer:
    if len(rowContainer[key]) < len(header):
        delKeys.append(key)

for k in delKeys:
    del rowContainer[k]

for key in rowContainer:
    rowList.append(rowContainer[key])
writer.writerows(rowList)
#Close files
compiledData.close()
countryAid.close()
countryDemocracyIndex.close()
countryGDPperCapita.close()
countryHumanRightsIndex.close()
countryPopulation.close()
countryPopulationDensity.close()
countryRegimeType.close()