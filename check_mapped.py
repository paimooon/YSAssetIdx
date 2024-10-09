import hashlib, json

mapped = {
    "69286664419": "Data/_BinOutput/GCG/Gcg_DeclaredValueSet/Char_Skill_74012",
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
