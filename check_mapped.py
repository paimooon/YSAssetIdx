import hashlib, json

mapped = {
    "797802415888": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Card_Vehicle_1230311",
    "686756681236": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Card_Vehicle_1270321",
    "1060551960464": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Card_Vehicle_3130041",
    "109919125460": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_16092",
    "319336298872": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_23038",
    "720340533231": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24062",
    "415325181813": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24063",
    "141757576946": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24064",
    "421923331317": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24065",
    "238907478846": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24066",
    "770988029432": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_24067",
    "222408494106": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_27032",
    "154169197142": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_27033",
    "125279570135": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_27035",
    "715532354207": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_33094",
    "647765639613": "Data/_BinOutput/MonsterPreview/MonsterPreview_Tower5_1",
    "459491337317": "Data/_BinOutput/Ability/Temp/AvatarAbilities/ConfigAbility_Avatar_Xilonen",
    "501312312901": "Data/_BinOutput/Avatar/ConfigAvatar_Xilonen",
    "724663471228": "Data/_BinOutput/Avatar/ConfigAvatar_Manekin_Xilonen",
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
