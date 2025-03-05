import sys
import json

from asset_index import AssetIndex

ai = AssetIndex.from_file("0000006f")

with open('mapped-updated.json', 'r') as f:
    mappedName = json.load(f)
mappedGenerate = {}

def loadTypeDict(ai):
    typeDict = {}
    for i in ai.type_mapping:
        typeDict[i.name.data] = i.mapped_to.data
    return typeDict

def loadSubAssets(ai):
    subAsset = {}
    mappedCnt = 0

    for i in ai.assets:
        try: 
            subAssetInfo = {
                "Name": mappedName[str((i.path_hash_last << 8) | i.path_hash_pre)],
                "PathHashPre": i.path_hash_pre,
                "PathHashLast": i.path_hash_last
            }
            mappedCnt += 1
            mappedGenerate[str((i.path_hash_last << 8) | i.path_hash_pre)] = subAssetInfo["Name"]

        except:
            subAssetInfo = {
                "Name": "",
                "PathHashPre": i.path_hash_pre,
                "PathHashLast": i.path_hash_last
            }
            mappedGenerate[str((i.path_hash_last << 8) | i.path_hash_pre)] = ""

        if i.sub_asset_id not in subAsset:
            subAsset[i.sub_asset_id] = []
        subAsset[i.sub_asset_id].append(subAssetInfo)

    print(f"{len(ai.assets) - mappedCnt} unmatched")
    print(f"{mappedCnt}/{len(ai.assets)} {'{0:.2%}'.format(mappedCnt/len(ai.assets))}")

    return subAsset

def loadBundleDependencyMap(ai):
    dependenciesDict = {}
    for i in ai.dependencies:
        dependenciesDict[i.asset_id] = i.dependencies_list
    return dependenciesDict


def loadBlockGroups(ai):
    blockGroups = {}
    for i in ai.block_groups:
        for j in i.block_list:
            blockGroups[j.block_list] = i.group_id
    return blockGroups

blockGroupsDict = loadBlockGroups(ai)

def loadAssets(ai, blockGroupsDict):
    assets = {}

    for i in ai.block_infos:
        for j in i.asset_offsets:
            blockInfo = {
                "Language": blockGroupsDict[i.block_id] if i.block_id in blockGroupsDict.keys() else 0,
                "Id": i.block_id,
                "Offset": j.offset
            }

            assets[j.path_hash_pre] = blockInfo
    return assets

assetindex_output = {
    "Types": loadTypeDict(ai),
    "SubAssets": loadSubAssets(ai),
    "Dependencies": loadBundleDependencyMap(ai),
    "PreloadBlocks": ai.preload_blocks,
    "PreloadShaderBlocks": ai.preload_shader_blocks,
    "Assets": loadAssets(ai, blockGroupsDict),
    # "SortList": ai.sort_list,
}

with open('output_assetindex.json', 'w', encoding='utf-8') as f:
    json.dump(assetindex_output, f, ensure_ascii=False, indent=4, sort_keys=True)

with open('output_assetindex_minify.json', 'w', encoding='utf-8') as f:
    json.dump(assetindex_output, f, ensure_ascii=False, sort_keys=True)

with open('output_mapped.json', 'w', encoding='utf-8') as f:
    json.dump(mappedGenerate, f, ensure_ascii=False, indent=4)