# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AssetIndex(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.type_mapping_count = self._io.read_u4le()
        self.type_mapping = []
        for i in range(self.type_mapping_count):
            self.type_mapping.append(AssetIndex.TypeMappingEntry(self._io, self, self._root))

        self.asset_count = self._io.read_u4le()
        self.assets = []
        for i in range(self.asset_count):
            self.assets.append(AssetIndex.AssetInfo(self._io, self, self._root))

        self.dependency_count = self._io.read_u4le()
        self.magic_31 = self._io.read_u4le()
        self.magic_32 = self._io.read_u4le()
        self.dependencies = []
        for i in range(self.dependency_count):
            self.dependencies.append(AssetIndex.DependencyInfo(self._io, self, self._root))

        self.preload_blocks_count = self._io.read_u4le()
        self.preload_blocks = []
        for i in range(self.preload_blocks_count):
            self.preload_blocks.append(self._io.read_u4le())

        self.preload_shader_blocks_count = self._io.read_u4le()
        self.preload_shader_blocks = []
        for i in range(self.preload_shader_blocks_count):
            self.preload_shader_blocks.append(self._io.read_u4le())

        self.block_group_count = self._io.read_u4le()
        self.block_groups = []
        for i in range(self.block_group_count):
            self.block_groups.append(AssetIndex.BlockGroup(self._io, self, self._root))

        self.block_info_count = self._io.read_u4le()
        self.block_infos = []
        for i in range(self.block_info_count):
            self.block_infos.append(AssetIndex.BlockInfo(self._io, self, self._root))


    class BlockInfo(KaitaiStruct):
        """Specifies which assets this specific block contains and their offsets in the BLK file."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_id = self._io.read_u4le()
            self.asset_offset_count = self._io.read_u4le()
            self.asset_offsets = []
            for i in range(self.asset_offset_count):
                self.asset_offsets.append(AssetIndex.AssetOffsetInfo(self._io, self, self._root))



    class BlockListMagic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_list = self._io.read_u4le()
            self.magic = self._io.read_u2le()
            self.magic_2 = self._io.read_u1()


    class TypeMappingEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = AssetIndex.String(self._io, self, self._root)
            self.mapped_to = AssetIndex.String(self._io, self, self._root)


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u4le()
            self.data = (self._io.read_bytes(self.len)).decode(u"UTF-8")


    class DependencyInfo(KaitaiStruct):
        """Describes that asset asset_id depends on assets from the specified list."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.asset_id = self._io.read_u4le()
            self.dependency_info_count = self._io.read_u4le()
            self.dependencies_list = []
            for i in range(self.dependency_info_count):
                self.dependencies_list.append(self._io.read_u4le())



    class AssetOffsetInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.path_hash_pre = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self.size = self._io.read_u4le()


    class BlockGroup(KaitaiStruct):
        """List of BLKs in a directory specified by the group_id."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.group_id = self._io.read_u4le()
            self.block_count = self._io.read_u4le()
            self.block_list = []
            for i in range(self.block_count):
                self.block_list.append(AssetIndex.BlockListMagic(self._io, self, self._root))



    class AssetInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.path_hash_pre = self._io.read_u1()
            self.path_hash_last = self._io.read_u4le()
            self.magic = []
            for i in range(3):
                self.magic.append(self._io.read_u1())

            self.magic_real = self._io.read_u1()
            self.magic_2 = self._io.read_u1()
            self.sub_asset_id = self._io.read_u4le()
            if self.magic_real == 2:
                self.magic_conditional = []
                for i in range(5):
                    self.magic_conditional.append(self._io.read_u1())





