import hashlib, json

mapped = {
    "826070285539": "Data/_BinOutput/Avatar/ConfigAvatar_Manekin_Chasca",
    "498285959886": "Data/_BinOutput/Avatar/ConfigAvatar_Manekin_MavuikaPre",
    "154420150922": "Data/_BinOutput/Avatar/ConfigAvatar_Manekin_Olorun",
    "818503059268": "Data/_BinOutput/Avatar/ConfigAvatar_MavuikaPre",
    "412561007750": "Data/_BinOutput/Avatar/ConfigAvatar_Olorun",
    "1048750020482": "Data/_BinOutput/Ability/Temp/AvatarAbilities/ConfigAbility_Avatar_Olorun",
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
