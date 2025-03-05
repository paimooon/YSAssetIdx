import hashlib, json

mapped = {
    "582632831089": "Data/_BinOutput/MonsterPreview/MonsterPreview_Tower5_5",
    "861866692353": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Build_Tatankasaurus",
    "222171214136": "Data/_BinOutput/HomeworldFurnitureSuit/Home_Suite_Exterior_Nt_Field_Saurus",
    "1048067939797": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_16102",
    "644002813599": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_16102_Ex_1",
    "934074493651": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_16103",
    "481968810323": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_17094",
    "809577456262": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_17102",
    "878886976800": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_17103",
    "914971917883": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_17104",
    "446233248860": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_17105",
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
