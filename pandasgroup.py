import csv

dirpath = '/home/zdong/PENGRUI/'
PTT = []
dive_num = []
ptt_dive = []
depth = []
with open(dirpath+"tu102withModels.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    depthstr = ""
    for row in reader:
        if row['PTT'] in PTT:
            if row["PTT"] + "_" +row["dive_num"] in ptt_dive:
                depthstr += ","
                depthstr += row["depth"]
            else:
                PTT.append(row["PTT"])
                dive_num.append(row["dive_num"])
                ptt_dive.append(row["PTT"] + "_" +row["dive_num"])
                depth.append(depthstr)
                depthstr = row["depth"]
        else:
            PTT.append(row["PTT"])
            dive_num.append(row["dive_num"])
            ptt_dive.append(row["PTT"] + "_" + row["dive_num"])
            if depthstr != "":
                depth.append(depthstr)
            depthstr = row["depth"]
    depth.append(depthstr)

print("PTT",len(PTT),PTT)
print("dive_num",len(dive_num),dive_num)
print("depth",len(depth),depth)
with open(dirpath+"after.csv", 'w') as csvfile:
    fieldnames = ['PTT', 'dive_num', 'depth']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for ptt, dive, dep in zip(PTT,dive_num,depth):
        writer.writerow({'PTT': ptt, 'dive_num': dive, 'depth': dep})


