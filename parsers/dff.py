# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import zlib


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dff(ReadWriteKaitaiStruct):
    """This file format is used to store both
    game assets and metadata that is used by the game or its editor.
    
    A dff file is sometimes? or always accompanied by a .resblock file
    which stores large assets that for some
    reason cannot fit into the dff itself.
    """

    class ChunkType(IntEnum):
        entity = 1796
        embedded_asset = 1814
        class_registry = 1820
        resource_catalogue = 3135023873
        resource_cache_global = 3135023874
        resource_cache_level = 3135023875

    class PacketEntryType(IntEnum):
        class_name = 536870912
        instance_guid = 1073741824
        attribute_section = 2147483648
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Dff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self._raw__raw_rw_stream = self._io.read_bytes_full()
        self._raw_rw_stream = zlib.decompress(self._raw__raw_rw_stream)
        self.rw_stream__inner_size = len(self._raw_rw_stream)
        _io__raw_rw_stream = KaitaiStream(BytesIO(self._raw_rw_stream))
        self.rw_stream = Dff.RwCompressedFileStream(_io__raw_rw_stream, self, self._root)
        self.rw_stream._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.rw_stream._fetch_instances()


    def _write__seq(self, io=None):
        super(Dff, self)._write__seq(io)
        _io__raw_rw_stream = KaitaiStream(BytesIO(bytearray(self.rw_stream__inner_size)))
        self._io.add_child_stream(_io__raw_rw_stream)
        _pos2 = self._io.pos()
        self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))
        def handler(parent, _io__raw_rw_stream=_io__raw_rw_stream):
            self._raw_rw_stream = _io__raw_rw_stream.to_byte_array()
            self._raw__raw_rw_stream = zlib.compress(self._raw_rw_stream)
            parent.write_bytes(self._raw__raw_rw_stream)
            if not parent.is_eof():
                raise kaitaistruct.ConsistencyError(u"raw(rw_stream)", 0, parent.size() - parent.pos())
        _io__raw_rw_stream.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
        self.rw_stream._write__seq(_io__raw_rw_stream)


    def _check(self):
        if self.rw_stream._root != self._root:
            raise kaitaistruct.ConsistencyError(u"rw_stream", self._root, self.rw_stream._root)
        if self.rw_stream._parent != self:
            raise kaitaistruct.ConsistencyError(u"rw_stream", self, self.rw_stream._parent)
        self._dirty = False

    class AttributePacket(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.AttributePacket, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                _t_entries = Dff.PacketEntry(self._io, self, self._root)
                try:
                    _t_entries._read()
                finally:
                    self.entries.append(_t_entries)
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.AttributePacket, self)._write__seq(io)
            for i in range(len(self.entries)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"entries", 0, self._io.size() - self._io.pos())
                self.entries[i]._write__seq(self._io)

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"entries", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.entries)):
                pass
                if self.entries[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entries", self._root, self.entries[i]._root)
                if self.entries[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entries", self, self.entries[i]._parent)

            self._dirty = False


    class Chunk(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = Dff.ChunkHeader(self._io, self, self._root)
            self.header._read()
            _on = self.header.type
            if _on == Dff.ChunkType.class_registry:
                pass
                self.body = Dff.ClassRegistry(self._io, self, self._root)
                self.body._read()
            elif _on == Dff.ChunkType.embedded_asset:
                pass
                self.body = Dff.EmbeddedAsset(self._io, self, self._root)
                self.body._read()
            elif _on == Dff.ChunkType.entity:
                pass
                self.body = Dff.Entity(self._io, self, self._root)
                self.body._read()
            elif _on == Dff.ChunkType.resource_cache_global:
                pass
                self.body = Dff.ResCacheGlobal(self._io, self, self._root)
                self.body._read()
            elif _on == Dff.ChunkType.resource_cache_level:
                pass
                self.body = Dff.ResCacheLevel(self._io, self, self._root)
                self.body._read()
            elif _on == Dff.ChunkType.resource_catalogue:
                pass
                self.body = Dff.ResourceCatalogue(self._io, self, self._root)
                self.body._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.header.type
            if _on == Dff.ChunkType.class_registry:
                pass
                self.body._fetch_instances()
            elif _on == Dff.ChunkType.embedded_asset:
                pass
                self.body._fetch_instances()
            elif _on == Dff.ChunkType.entity:
                pass
                self.body._fetch_instances()
            elif _on == Dff.ChunkType.resource_cache_global:
                pass
                self.body._fetch_instances()
            elif _on == Dff.ChunkType.resource_cache_level:
                pass
                self.body._fetch_instances()
            elif _on == Dff.ChunkType.resource_catalogue:
                pass
                self.body._fetch_instances()


        def _write__seq(self, io=None):
            super(Dff.Chunk, self)._write__seq(io)
            self.header._write__seq(self._io)
            _on = self.header.type
            if _on == Dff.ChunkType.class_registry:
                pass
                self.body._write__seq(self._io)
            elif _on == Dff.ChunkType.embedded_asset:
                pass
                self.body._write__seq(self._io)
            elif _on == Dff.ChunkType.entity:
                pass
                self.body._write__seq(self._io)
            elif _on == Dff.ChunkType.resource_cache_global:
                pass
                self.body._write__seq(self._io)
            elif _on == Dff.ChunkType.resource_cache_level:
                pass
                self.body._write__seq(self._io)
            elif _on == Dff.ChunkType.resource_catalogue:
                pass
                self.body._write__seq(self._io)


        def _check(self):
            if self.header._root != self._root:
                raise kaitaistruct.ConsistencyError(u"header", self._root, self.header._root)
            if self.header._parent != self:
                raise kaitaistruct.ConsistencyError(u"header", self, self.header._parent)
            _on = self.header.type
            if _on == Dff.ChunkType.class_registry:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == Dff.ChunkType.embedded_asset:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == Dff.ChunkType.entity:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == Dff.ChunkType.resource_cache_global:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == Dff.ChunkType.resource_cache_level:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            elif _on == Dff.ChunkType.resource_catalogue:
                pass
                if self.body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"body", self._root, self.body._root)
                if self.body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"body", self, self.body._parent)
            self._dirty = False


    class ChunkHeader(ReadWriteKaitaiStruct):
        """12-byte on-disk chunk header."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ChunkHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Dff.ChunkType, self._io.read_u4le())
            self.length = self._io.read_u4le()
            self.version = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.ChunkHeader, self)._write__seq(io)
            self._io.write_u4le(int(self.type))
            self._io.write_u4le(self.length)
            self._io.write_u4le(self.version)


        def _check(self):
            self._dirty = False


    class ClassRegistry(ReadWriteKaitaiStruct):
        """A chunk containing a list of classes that the dff uses.
        Not read or used by the game itself, so it must be editor related.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ClassRegistry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_entries = self._io.read_u4le()
            self.entries = []
            for i in range(self.num_entries):
                _t_entries = Dff.ClassRegistryEntry(self._io, self, self._root)
                try:
                    _t_entries._read()
                finally:
                    self.entries.append(_t_entries)

            self.reserved = self._io.read_u8le()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.ClassRegistry, self)._write__seq(io)
            self._io.write_u4le(self.num_entries)
            for i in range(len(self.entries)):
                pass
                self.entries[i]._write__seq(self._io)

            self._io.write_u8le(self.reserved)


        def _check(self):
            if len(self.entries) != self.num_entries:
                raise kaitaistruct.ConsistencyError(u"entries", self.num_entries, len(self.entries))
            for i in range(len(self.entries)):
                pass
                if self.entries[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entries", self._root, self.entries[i]._root)
                if self.entries[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entries", self, self.entries[i]._parent)

            self._dirty = False


    class ClassRegistryEntry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ClassRegistryEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.reserved = self._io.read_bytes((4 - (len(self.name) + 1) % 4) % 4)
            self.instance_count = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.ClassRegistryEntry, self)._write__seq(io)
            self._io.write_bytes((self.name).encode(u"UTF-8"))
            self._io.write_u1(0)
            self._io.write_bytes(self.reserved)
            self._io.write_u4le(self.instance_count)


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"name", -1, KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0))
            if len(self.reserved) != (4 - (len(self.name) + 1) % 4) % 4:
                raise kaitaistruct.ConsistencyError(u"reserved", (4 - (len(self.name) + 1) % 4) % 4, len(self.reserved))
            self._dirty = False


    class EmbeddedAsset(ReadWriteKaitaiStruct):
        """A game file/asset fully located inside of the dff.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.EmbeddedAsset, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.len_header = self._io.read_u4le()
            self._raw_header = self._io.read_bytes(self.len_header)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = Dff.EmbeddedAssetHeader(_io__raw_header, self, self._root)
            self.header._read()
            self.len_data = self._io.read_u4le()
            self.data = self._io.read_bytes(self.len_data)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


        def _write__seq(self, io=None):
            super(Dff.EmbeddedAsset, self)._write__seq(io)
            self._io.write_u4le(self.len_header)
            _io__raw_header = KaitaiStream(BytesIO(bytearray(self.len_header)))
            self._io.add_child_stream(_io__raw_header)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.len_header))
            def handler(parent, _io__raw_header=_io__raw_header):
                self._raw_header = _io__raw_header.to_byte_array()
                if len(self._raw_header) != self.len_header:
                    raise kaitaistruct.ConsistencyError(u"raw(header)", self.len_header, len(self._raw_header))
                parent.write_bytes(self._raw_header)
            _io__raw_header.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.header._write__seq(_io__raw_header)
            self._io.write_u4le(self.len_data)
            self._io.write_bytes(self.data)


        def _check(self):
            if self.header._root != self._root:
                raise kaitaistruct.ConsistencyError(u"header", self._root, self.header._root)
            if self.header._parent != self:
                raise kaitaistruct.ConsistencyError(u"header", self, self.header._parent)
            if len(self.data) != self.len_data:
                raise kaitaistruct.ConsistencyError(u"data", self.len_data, len(self.data))
            self._dirty = False


    class EmbeddedAssetHeader(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.EmbeddedAssetHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name_len = self._io.read_u4le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"ASCII")
            self._raw_guid = self._io.read_bytes(16)
            _io__raw_guid = KaitaiStream(BytesIO(self._raw_guid))
            self.guid = Dff.Guid(_io__raw_guid, self, self._root)
            self.guid._read()
            self.type_len = self._io.read_u4le()
            self.type = (self._io.read_bytes(self.type_len)).decode(u"ASCII")
            self.str2_len = self._io.read_u4le()
            self.str2 = (self._io.read_bytes(self.str2_len)).decode(u"ASCII")
            self.extra = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.guid._fetch_instances()


        def _write__seq(self, io=None):
            super(Dff.EmbeddedAssetHeader, self)._write__seq(io)
            self._io.write_u4le(self.name_len)
            self._io.write_bytes((self.name).encode(u"ASCII"))
            _io__raw_guid = KaitaiStream(BytesIO(bytearray(16)))
            self._io.add_child_stream(_io__raw_guid)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (16))
            def handler(parent, _io__raw_guid=_io__raw_guid):
                self._raw_guid = _io__raw_guid.to_byte_array()
                if len(self._raw_guid) != 16:
                    raise kaitaistruct.ConsistencyError(u"raw(guid)", 16, len(self._raw_guid))
                parent.write_bytes(self._raw_guid)
            _io__raw_guid.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.guid._write__seq(_io__raw_guid)
            self._io.write_u4le(self.type_len)
            self._io.write_bytes((self.type).encode(u"ASCII"))
            self._io.write_u4le(self.str2_len)
            self._io.write_bytes((self.str2).encode(u"ASCII"))
            self._io.write_bytes(self.extra)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"extra", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len((self.name).encode(u"ASCII")) != self.name_len:
                raise kaitaistruct.ConsistencyError(u"name", self.name_len, len((self.name).encode(u"ASCII")))
            if self.guid._root != self._root:
                raise kaitaistruct.ConsistencyError(u"guid", self._root, self.guid._root)
            if self.guid._parent != self:
                raise kaitaistruct.ConsistencyError(u"guid", self, self.guid._parent)
            if len((self.type).encode(u"ASCII")) != self.type_len:
                raise kaitaistruct.ConsistencyError(u"type", self.type_len, len((self.type).encode(u"ASCII")))
            if len((self.str2).encode(u"ASCII")) != self.str2_len:
                raise kaitaistruct.ConsistencyError(u"str2", self.str2_len, len((self.str2).encode(u"ASCII")))
            self._dirty = False


    class Entity(ReadWriteKaitaiStruct):
        """This chunk is used to tell the game engine to place/create an entity with specified attributes.
        What class to spawn, should it be spawned in this build of the game,
        what class specific attributes have been set for it, etc.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.Entity, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pad = self._io.read_u4le()
            self.data_config_mask_lo = self._io.read_u4le()
            self.data_config_mask_hi = self._io.read_u4le()
            self._raw_packet = self._io.read_bytes(self._parent.header.length - 12)
            _io__raw_packet = KaitaiStream(BytesIO(self._raw_packet))
            self.packet = Dff.AttributePacket(_io__raw_packet, self, self._root)
            self.packet._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.packet._fetch_instances()


        def _write__seq(self, io=None):
            super(Dff.Entity, self)._write__seq(io)
            self._io.write_u4le(self.pad)
            self._io.write_u4le(self.data_config_mask_lo)
            self._io.write_u4le(self.data_config_mask_hi)
            _io__raw_packet = KaitaiStream(BytesIO(bytearray(self._parent.header.length - 12)))
            self._io.add_child_stream(_io__raw_packet)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._parent.header.length - 12))
            def handler(parent, _io__raw_packet=_io__raw_packet):
                self._raw_packet = _io__raw_packet.to_byte_array()
                if len(self._raw_packet) != self._parent.header.length - 12:
                    raise kaitaistruct.ConsistencyError(u"raw(packet)", self._parent.header.length - 12, len(self._raw_packet))
                parent.write_bytes(self._raw_packet)
            _io__raw_packet.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.packet._write__seq(_io__raw_packet)


        def _check(self):
            if self.packet._root != self._root:
                raise kaitaistruct.ConsistencyError(u"packet", self._root, self.packet._root)
            if self.packet._parent != self:
                raise kaitaistruct.ConsistencyError(u"packet", self, self.packet._parent)
            self._dirty = False

        @property
        def data_config_mask(self):
            """I believe this is used by the engine to selectively ignore certain entities
            to create depending on the engines build type. (debug, release, etc)
            """
            if hasattr(self, '_m_data_config_mask'):
                return self._m_data_config_mask

            self._m_data_config_mask = self.data_config_mask_hi * 4294967296 + self.data_config_mask_lo
            return getattr(self, '_m_data_config_mask', None)

        def _invalidate_data_config_mask(self):
            del self._m_data_config_mask

    class Guid(ReadWriteKaitaiStruct):
        """16 byte guid."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.Guid, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data1 = self._io.read_u4le()
            self.data2 = self._io.read_u2le()
            self.data3 = self._io.read_u2le()
            self.data4 = self._io.read_u1()
            self.data5 = self._io.read_u1()
            self.data6 = []
            for i in range(6):
                self.data6.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.data6)):
                pass



        def _write__seq(self, io=None):
            super(Dff.Guid, self)._write__seq(io)
            self._io.write_u4le(self.data1)
            self._io.write_u2le(self.data2)
            self._io.write_u2le(self.data3)
            self._io.write_u1(self.data4)
            self._io.write_u1(self.data5)
            for i in range(len(self.data6)):
                pass
                self._io.write_u1(self.data6[i])



        def _check(self):
            if len(self.data6) != 6:
                raise kaitaistruct.ConsistencyError(u"data6", 6, len(self.data6))
            for i in range(len(self.data6)):
                pass

            self._dirty = False


    class PacketEntry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.PacketEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.size = self._io.read_u4le()
            self.type = KaitaiStream.resolve_enum(Dff.PacketEntryType, self._io.read_u4le())
            if self.size != 0:
                pass
                _on = self.type
                if _on == Dff.PacketEntryType.attribute_section:
                    pass
                    self._raw_data = self._io.read_bytes(self.size - 8)
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Dff.PacketStr(_io__raw_data, self, self._root)
                    self.data._read()
                elif _on == Dff.PacketEntryType.class_name:
                    pass
                    self._raw_data = self._io.read_bytes(self.size - 8)
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Dff.PacketStr(_io__raw_data, self, self._root)
                    self.data._read()
                elif _on == Dff.PacketEntryType.instance_guid:
                    pass
                    self._raw_data = self._io.read_bytes(self.size - 8)
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Dff.Guid(_io__raw_data, self, self._root)
                    self.data._read()
                else:
                    pass
                    self.data = self._io.read_bytes(self.size - 8)

            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.size != 0:
                pass
                _on = self.type
                if _on == Dff.PacketEntryType.attribute_section:
                    pass
                    self.data._fetch_instances()
                elif _on == Dff.PacketEntryType.class_name:
                    pass
                    self.data._fetch_instances()
                elif _on == Dff.PacketEntryType.instance_guid:
                    pass
                    self.data._fetch_instances()
                else:
                    pass



        def _write__seq(self, io=None):
            super(Dff.PacketEntry, self)._write__seq(io)
            self._io.write_u4le(self.size)
            self._io.write_u4le(int(self.type))
            if self.size != 0:
                pass
                _on = self.type
                if _on == Dff.PacketEntryType.attribute_section:
                    pass
                    _io__raw_data = KaitaiStream(BytesIO(bytearray(self.size - 8)))
                    self._io.add_child_stream(_io__raw_data)
                    _pos2 = self._io.pos()
                    self._io.seek(self._io.pos() + (self.size - 8))
                    def handler(parent, _io__raw_data=_io__raw_data):
                        self._raw_data = _io__raw_data.to_byte_array()
                        if len(self._raw_data) != self.size - 8:
                            raise kaitaistruct.ConsistencyError(u"raw(data)", self.size - 8, len(self._raw_data))
                        parent.write_bytes(self._raw_data)
                    _io__raw_data.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                    self.data._write__seq(_io__raw_data)
                elif _on == Dff.PacketEntryType.class_name:
                    pass
                    _io__raw_data = KaitaiStream(BytesIO(bytearray(self.size - 8)))
                    self._io.add_child_stream(_io__raw_data)
                    _pos2 = self._io.pos()
                    self._io.seek(self._io.pos() + (self.size - 8))
                    def handler(parent, _io__raw_data=_io__raw_data):
                        self._raw_data = _io__raw_data.to_byte_array()
                        if len(self._raw_data) != self.size - 8:
                            raise kaitaistruct.ConsistencyError(u"raw(data)", self.size - 8, len(self._raw_data))
                        parent.write_bytes(self._raw_data)
                    _io__raw_data.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                    self.data._write__seq(_io__raw_data)
                elif _on == Dff.PacketEntryType.instance_guid:
                    pass
                    _io__raw_data = KaitaiStream(BytesIO(bytearray(self.size - 8)))
                    self._io.add_child_stream(_io__raw_data)
                    _pos2 = self._io.pos()
                    self._io.seek(self._io.pos() + (self.size - 8))
                    def handler(parent, _io__raw_data=_io__raw_data):
                        self._raw_data = _io__raw_data.to_byte_array()
                        if len(self._raw_data) != self.size - 8:
                            raise kaitaistruct.ConsistencyError(u"raw(data)", self.size - 8, len(self._raw_data))
                        parent.write_bytes(self._raw_data)
                    _io__raw_data.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
                    self.data._write__seq(_io__raw_data)
                else:
                    pass
                    self._io.write_bytes(self.data)



        def _check(self):
            if self.size != 0:
                pass
                _on = self.type
                if _on == Dff.PacketEntryType.attribute_section:
                    pass
                    if self.data._root != self._root:
                        raise kaitaistruct.ConsistencyError(u"data", self._root, self.data._root)
                    if self.data._parent != self:
                        raise kaitaistruct.ConsistencyError(u"data", self, self.data._parent)
                elif _on == Dff.PacketEntryType.class_name:
                    pass
                    if self.data._root != self._root:
                        raise kaitaistruct.ConsistencyError(u"data", self._root, self.data._root)
                    if self.data._parent != self:
                        raise kaitaistruct.ConsistencyError(u"data", self, self.data._parent)
                elif _on == Dff.PacketEntryType.instance_guid:
                    pass
                    if self.data._root != self._root:
                        raise kaitaistruct.ConsistencyError(u"data", self._root, self.data._root)
                    if self.data._parent != self:
                        raise kaitaistruct.ConsistencyError(u"data", self, self.data._parent)
                else:
                    pass
                    if len(self.data) != self.size - 8:
                        raise kaitaistruct.ConsistencyError(u"data", self.size - 8, len(self.data))

            self._dirty = False


    class PacketStr(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.PacketStr, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.PacketStr, self)._write__seq(io)
            self._io.write_bytes((self.value).encode(u"ASCII"))
            self._io.write_u1(0)


        def _check(self):
            if KaitaiStream.byte_array_index_of((self.value).encode(u"ASCII"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"value", -1, KaitaiStream.byte_array_index_of((self.value).encode(u"ASCII"), 0))
            self._dirty = False


    class ResCacheConfig(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResCacheConfig, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self.num_blocks = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.ResCacheConfig, self)._write__seq(io)
            self._io.write_bytes((self.name).encode(u"UTF-16LE"))
            self._io.write_u4le(self.num_blocks)


        def _check(self):
            if len((self.name).encode(u"UTF-16LE")) != 64:
                raise kaitaistruct.ConsistencyError(u"name", 64, len((self.name).encode(u"UTF-16LE")))
            self._dirty = False


    class ResCacheGlobal(ReadWriteKaitaiStruct):
        """Global resource cache."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResCacheGlobal, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_entries = self._io.read_u4le()
            self.entries = []
            for i in range(self.num_entries):
                _t_entries = Dff.ResCacheGlobalEntry(self._io, self, self._root)
                try:
                    _t_entries._read()
                finally:
                    self.entries.append(_t_entries)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.ResCacheGlobal, self)._write__seq(io)
            self._io.write_u4le(self.num_entries)
            for i in range(len(self.entries)):
                pass
                self.entries[i]._write__seq(self._io)



        def _check(self):
            if len(self.entries) != self.num_entries:
                raise kaitaistruct.ConsistencyError(u"entries", self.num_entries, len(self.entries))
            for i in range(len(self.entries)):
                pass
                if self.entries[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entries", self._root, self.entries[i]._root)
                if self.entries[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entries", self, self.entries[i]._parent)

            self._dirty = False


    class ResCacheGlobalEntry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResCacheGlobalEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.block_size = self._io.read_u4le()
            self.type = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.ResCacheGlobalEntry, self)._write__seq(io)
            self._io.write_u4le(self.block_size)
            self._io.write_bytes((self.type).encode(u"UTF-16LE"))


        def _check(self):
            if len((self.type).encode(u"UTF-16LE")) != 64:
                raise kaitaistruct.ConsistencyError(u"type", 64, len((self.type).encode(u"UTF-16LE")))
            self._dirty = False


    class ResCacheLevel(ReadWriteKaitaiStruct):
        """Level resource cache."""
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResCacheLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_entries = self._io.read_u4le()
            self.entries = []
            for i in range(self.num_entries):
                _t_entries = Dff.ResCacheLevelEntry(self._io, self, self._root)
                try:
                    _t_entries._read()
                finally:
                    self.entries.append(_t_entries)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.ResCacheLevel, self)._write__seq(io)
            self._io.write_u4le(self.num_entries)
            for i in range(len(self.entries)):
                pass
                self.entries[i]._write__seq(self._io)



        def _check(self):
            if len(self.entries) != self.num_entries:
                raise kaitaistruct.ConsistencyError(u"entries", self.num_entries, len(self.entries))
            for i in range(len(self.entries)):
                pass
                if self.entries[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entries", self._root, self.entries[i]._root)
                if self.entries[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entries", self, self.entries[i]._parent)

            self._dirty = False


    class ResCacheLevelEntry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResCacheLevelEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.type = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self.block_size = self._io.read_u4le()
            self.num_configs = self._io.read_u4le()
            self.configs = []
            for i in range(self.num_configs):
                _t_configs = Dff.ResCacheConfig(self._io, self, self._root)
                try:
                    _t_configs._read()
                finally:
                    self.configs.append(_t_configs)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.configs)):
                pass
                self.configs[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.ResCacheLevelEntry, self)._write__seq(io)
            self._io.write_bytes((self.type).encode(u"UTF-16LE"))
            self._io.write_u4le(self.block_size)
            self._io.write_u4le(self.num_configs)
            for i in range(len(self.configs)):
                pass
                self.configs[i]._write__seq(self._io)



        def _check(self):
            if len((self.type).encode(u"UTF-16LE")) != 64:
                raise kaitaistruct.ConsistencyError(u"type", 64, len((self.type).encode(u"UTF-16LE")))
            if len(self.configs) != self.num_configs:
                raise kaitaistruct.ConsistencyError(u"configs", self.num_configs, len(self.configs))
            for i in range(len(self.configs)):
                pass
                if self.configs[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"configs", self._root, self.configs[i]._root)
                if self.configs[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"configs", self, self.configs[i]._parent)

            self._dirty = False


    class ResourceCatalogue(ReadWriteKaitaiStruct):
        """Resource catalog chunks contain a table of contents to be used with
        the dff files corresponding .resblock file.
        This chunk has a malformed length in its chunk header in the official
        dff files that crackdown 2 uses. So the size is grabbed dynamically
        instead.
        """
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResourceCatalogue, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.file_name_length = self._io.read_u4le()
            self.file_name = (self._io.read_bytes(self.file_name_length)).decode(u"UTF-16LE")
            self.num_entries = self._io.read_u4le()
            self.entries = []
            for i in range(self.num_entries):
                _t_entries = Dff.ResourceCatalogueEntry(self._io, self, self._root)
                try:
                    _t_entries._read()
                finally:
                    self.entries.append(_t_entries)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.ResourceCatalogue, self)._write__seq(io)
            self._io.write_u4le(self.file_name_length)
            self._io.write_bytes((self.file_name).encode(u"UTF-16LE"))
            self._io.write_u4le(self.num_entries)
            for i in range(len(self.entries)):
                pass
                self.entries[i]._write__seq(self._io)



        def _check(self):
            if len((self.file_name).encode(u"UTF-16LE")) != self.file_name_length:
                raise kaitaistruct.ConsistencyError(u"file_name", self.file_name_length, len((self.file_name).encode(u"UTF-16LE")))
            if len(self.entries) != self.num_entries:
                raise kaitaistruct.ConsistencyError(u"entries", self.num_entries, len(self.entries))
            for i in range(len(self.entries)):
                pass
                if self.entries[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entries", self._root, self.entries[i]._root)
                if self.entries[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entries", self, self.entries[i]._parent)

            self._dirty = False


    class ResourceCatalogueEntry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.ResourceCatalogueEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name = (self._io.read_bytes(256)).decode(u"UTF-16LE")
            self.block_type = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self.ofs_resource = self._io.read_u8le()
            self.len_resource = self._io.read_u4le()
            self.compressed_size = self._io.read_u4le()
            self.actual_compressed_size = self._io.read_u4le()
            self.checksum = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Dff.ResourceCatalogueEntry, self)._write__seq(io)
            self._io.write_bytes((self.name).encode(u"UTF-16LE"))
            self._io.write_bytes((self.block_type).encode(u"UTF-16LE"))
            self._io.write_u8le(self.ofs_resource)
            self._io.write_u4le(self.len_resource)
            self._io.write_u4le(self.compressed_size)
            self._io.write_u4le(self.actual_compressed_size)
            self._io.write_u4le(self.checksum)


        def _check(self):
            if len((self.name).encode(u"UTF-16LE")) != 256:
                raise kaitaistruct.ConsistencyError(u"name", 256, len((self.name).encode(u"UTF-16LE")))
            if len((self.block_type).encode(u"UTF-16LE")) != 64:
                raise kaitaistruct.ConsistencyError(u"block_type", 64, len((self.block_type).encode(u"UTF-16LE")))
            self._dirty = False


    class RwCompressedFileStream(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Dff.RwCompressedFileStream, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                _t_chunks = Dff.Chunk(self._io, self, self._root)
                try:
                    _t_chunks._read()
                finally:
                    self.chunks.append(_t_chunks)
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.chunks)):
                pass
                self.chunks[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Dff.RwCompressedFileStream, self)._write__seq(io)
            for i in range(len(self.chunks)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"chunks", 0, self._io.size() - self._io.pos())
                self.chunks[i]._write__seq(self._io)

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"chunks", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.chunks)):
                pass
                if self.chunks[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"chunks", self._root, self.chunks[i]._root)
                if self.chunks[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"chunks", self, self.chunks[i]._parent)

            self._dirty = False



