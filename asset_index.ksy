meta:
  id: asset_index
  file-extension: funnycat
  endian: le
  encoding: UTF-8

seq:
  - id: type_mapping_count
    type: u4
  - id: type_mapping
    type: type_mapping_entry
    repeat: expr
    repeat-expr: type_mapping_count
    doc: This specifies what specific type is serialized into (?)
    
  - id: asset_count
    type: u4
  - id: assets
    type: asset_info
    repeat: expr
    repeat-expr: asset_count
    doc: List of all the assets in the game, with their names, hashes and types
    
  - id: dependency_count
    type: u4
  - id: magic_31
    type: u4
  - id: magic_32
    type: u4
  - id: dependencies
    type: dependency_info
    repeat: expr
    repeat-expr: dependency_count
    doc: List of inter-asset dependencies
    
  - id: preload_blocks_count
    type: u4
  - id: preload_blocks
    type: u4
    repeat: expr
    repeat-expr: preload_blocks_count
    doc: Blocks to be preoaded during the game start (?)
    
  - id: preload_shader_blocks_count
    type: u4
  - id: preload_shader_blocks
    type: u4
    repeat: expr
    repeat-expr: preload_shader_blocks_count
    doc: Blocks containing shaders to be preloaded during the game startup (?)
    
  - id: block_group_count
    type: u4
  - id: block_groups
    type: block_group
    repeat: expr
    repeat-expr: block_group_count
    doc: Info about distribution of BLKs in file system directories
    
  - id: block_info_count
    type: u4
  - id: block_infos
    type: block_info
    repeat: expr
    repeat-expr: block_info_count
    doc: Info about distribution of assets in BLKs
    
  - id: sort_list_count
    type: u4
  - id: sort_list
    type: u4
    repeat: expr
    repeat-expr: sort_list_count
    doc: Info about sort?
    
types:
  string:
    seq:
      - id: len
        type: u4
      - id: data
        type: str
        size: len
        
  type_mapping_entry:
    seq:
      - id: name
        type: string
      - id: mapped_to
        type: string
        
  asset_info:
    seq:
      - id: path_hash_pre
        type: u1
        
      - id: path_hash_last
        type: u4
        
      - id: magic
        type: u1
        repeat: expr
        repeat-expr: 3
      
      - id: magic_real
        type: u1
      
      - id: magic_2
        type: u1
        
      - id: sub_asset_id
        type: u4
      
      - id: magic_conditional
        type: u1
        if: magic_real == 2
        repeat: expr
        repeat-expr: 5
        
        
        
  dependency_info:
    doc: Describes that asset asset_id depends on assets from the specified list
    seq:
      - id: asset_id
        type: u4
      - id: dependency_info_count
        type: u4
      - id: dependencies_list
        type: u4
        repeat: expr
        repeat-expr: dependency_info_count
        
  block_info:
    doc: Specifies which assets this specific block contains and their offsets in the BLK file
    seq:
      - id: block_id
        type: u4
      - id: asset_offset_count
        type: u4
      - id: asset_offsets
        type: asset_offset_info
        repeat: expr
        repeat-expr: asset_offset_count
        
  asset_offset_info:
    seq:
      - id: path_hash_pre
        type: u4
      - id: offset
        type: u4
      - id: size
        type: u4
        
  block_group:
    doc: List of BLKs in a directory specified by the group_id
    seq:
      - id: group_id
        type: u4
      - id: block_count
        type: u4
      - id: block_list
        type: block_list_magic
        repeat: expr
        repeat-expr: block_count
  
  block_list_magic:
    seq:
      - id: block_list
        type: u4
      - id: magic
        type: u2
      - id: magic_2
        type: u1
