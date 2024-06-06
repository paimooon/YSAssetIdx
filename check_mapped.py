import hashlib, json

mapped = {
    "146042475129": "Data/_BinOutput/MonsterPreview/MonsterPreview_Tower4_8",
}


with open('output_assetindex.json', 'r') as f:
    ai = json.load(f)
    
typeList = list(set(ai["Types"].values()))

def compute_name_hash(path, t):
    path = (path + t).encode('ascii')
    pad = ((len(path) >> 8) + 1) << 8
    bts = path + bytes([0] * (pad - len(path)))
    m = hashlib.md5()
    m.update(bts)
    output = m.digest()
    num = 0
    for i in range(4, -1, -1):
        num <<= 8
        num |= output[i]
    return num
    
if __name__ == '__main__':

    answer = []
    with open("match.txt", "r") as file:
        for line in file:
            answer.append(line.strip()) # compute hash first instead of below code, this is super slow
    sadge = 0 # when nothing matches in match.txt

    for i in mapped.keys():

        if mapped[i] == "": # if there's blank text

            for ans in answer: # find from match.txt first
                testline = "Data/_ExcelBinOutput/" + ans # or just put all path data in the match.txt 
                
                flag = False
                for t in typeList:
                    if compute_name_hash(testline, t) == int(i):
                        # print(f"{i}: {mapped[i]}") 
                        flag = True
                        break
                
                if flag:
                    break
            
            if flag:
                print(f"{testline} matches on {i}")
                mapped[i] = testline
            else:
                print(f"Nothing matched on {i} in match.txt")
                sadge += 1
            continue

        flag = False
        for t in typeList: # t = ".MiHoYoBinData" for Excel and BinOutput to prevent hash collide
            if compute_name_hash(mapped[i], t) == int(i):
                # print(f"{i}: {mapped[i]}") 
                flag = True
                break

        if flag == False:
            print(f"{i} is not correct")
