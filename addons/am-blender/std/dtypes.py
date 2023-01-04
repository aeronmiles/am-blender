from typing import (Union, List)
from enum import Enum
from bpy.types import Image
# from ..std import *


class Compat:
    class Size:
        def __init__(self, value: int):
            self.value = value

        def filename_suffixes(self) -> List[str]:
            # return multiple strings for backwards compatibility
            if self.value == 4096:
                return ["_4096.", "_4k."]
            if self.value == 2048:
                return ["_2048.", "_2k."]
            if self.value == 1024:
                return ["_1024.", "_1k."]
            if self.value == 512:
                return ["_512.", "_0.5k."]
            if self.value == 256:
                return ["_256."]
            if self.value == 128:
                return ["_128."]

            return []


class FileFormat(Enum):
    GLTF_SEPARATE = "GLTF_SEPARATE"
    GLTF_EMBEDDED = "GLTF_EMBEDDED"
    GLB = "GLB"
    FBX = "FBX"
    OBJ = "OBJ"
    STL = "STL"
    USDZ = "USDZ"


class Size(Enum):
    P2_4096 = 4096
    P2_2048 = 2048
    P2_1024 = 1024
    P2_512 = 512
    P2_256 = 256
    P2_128 = 128

    def filename_suffix(self) -> str:
        # return multiple strings for backwards compatibility
        if self.value == 4096:
            return "_4096."
        if self.value == 2048:
            return "_2048."
        if self.value == 1024:
            return "_1024."
        if self.value == 512:
            return "_512."
        if self.value == 256:
            return "_256."
        if self.value == 128:
            return "_128."

        return ""

    @staticmethod
    def from_image(image: 'Image', ) -> Union['Size', None]:
        # check multiple strings for backwards compatibility
        name = image.name.lower()
        if any([s in name for s in Compat.Size(4096).filename_suffixes()]):
            return Size.P2_4096
        if any([s in name for s in Compat.Size(2048).filename_suffixes()]):
            return Size.P2_2048
        if any([s in name for s in Compat.Size(1024).filename_suffixes()]):
            return Size.P2_1024
        if any([s in name for s in Compat.Size(512).filename_suffixes()]):
            return Size.P2_512
        if "_256." in name:
            return Size.P2_256
        if "_128." in name:
            return Size.P2_128

        return None

    @staticmethod
    def from_size(size: int) -> Union['Size', None]:
        if size == 4096:
            return Size.P2_4096
        if size == 2048:
            return Size.P2_2048
        if size == 1024:
            return Size.P2_1024
        if size == 512:
            return Size.P2_512
        if size == 256:
            return Size.P2_256
        if size == 128:
            return Size.P2_128

        return None

    @property
    def compat(self) -> 'Compat.Size':
        return Compat.Size(self.value)
