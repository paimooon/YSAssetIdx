import hashlib, json

mapped = {
    "688719560637": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Iktomisaurus",
    "185956052726": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Koholasaurus",
    "751878815404": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Market",
    "584663114425": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Mine",
    "971200459757": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Qucusaurus",
    "81796283625": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Tepetlisaurus",
    "888428371075": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Yumkasaurus",
    "678182105808": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Field_Nature",

    "761500094002": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Interior_Nt_Room_Hotel",
    "1091854801032": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Interior_Nt_Room_Office",
    "421881998455": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Interior_Nt_Room_Universal",
}

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

    t = ".MiHoYoBinData" # t = ".MiHoYoBinData" for Excel and BinOutput to prevent hash collide
        
    for i in mapped.keys():

        if mapped[i] == "": # if there's blank text
            continue

        if compute_name_hash(mapped[i], t) == int(i):
            # print(f'    "{i}": "{mapped[i]}",') 
            continue
        else:
            print(f"{i} is not correct")
