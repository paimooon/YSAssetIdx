# YSAssetIdx

A Parser of a certain anime game's asset index (WIP)

Current target version: 5.5 beta

```
441995 unmatched
253669/695664 36.46%
```

## Requirements

- Python 3

## How to run

- Clone this repository
```shell
git clone https://github.com/paimooon/YSAssetIdx
```
- Place `0000006f`
- Run `main.py`
```shell
python main.py
```

## How to fill mapped-updated.json
- Place new version of `0000006f`
- Run `main.py`
- `output_mapped.json` will be generated, fill it yourself
- Run `check_mapped.py` to check if filled value is correct or not
- Run `output_to_updated.py`, it will convert `output_mapped.json` to `mapped-updated.json` used in `main.py`
- Run `main.py` again to get assetindex

## Credit
- Raz for [Studio](https://gitlab.com/RazTools/Studio)
- party for [AssetRumpus](https://github.com/partypooperarchive/AssetRumpus)
- 14eyes for [GI-AssetHasher](https://github.com/14eyes/GI-AssetHasher)
