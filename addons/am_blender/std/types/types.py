from typing import (Union, List)
from enum import Enum


class FileFormat(Enum):
    GLTF_SEPARATE = "GLTF_SEPARATE"
    GLTF_EMBEDDED = "GLTF_EMBEDDED"
    GLB = "GLB"
    FBX = "FBX"
    OBJ = "OBJ"
    STL = "STL"
    USDZ = "USDZ"


class Size(Enum):
    P2_8192 = 8192
    P2_4096 = 4096
    P2_2048 = 2048
    P2_1024 = 1024
    P2_512 = 512
    P2_256 = 256
    P2_128 = 128
    P2_64 = 64
    P2_32 = 32

    def filename_suffix(self) -> str:
        if self.value == 8192:
            return "_8192."
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
        if self.value == 64:
            return "_64."
        if self.value == 32:
            return "_32."

        return ""

    @staticmethod
    def from_name(filepath: str) -> Union['Size', None]:
        # check multiple strings for backwards compatibility
        fp = filepath.lower()
        if Size(8192).filename_suffix() in fp:
            return Size.P2_8192
        if Size(4096).filename_suffix() in fp:
            return Size.P2_4096
        if Size(2048).filename_suffix() in fp:
            return Size.P2_2048
        if Size(1024).filename_suffix() in fp:
            return Size.P2_1024
        if Size(512).filename_suffix() in fp:
            return Size.P2_512
        if "_256." in fp:
            return Size.P2_256
        if "_128." in fp:
            return Size.P2_128
        if "_64." in fp:
            return Size.P2_64
        if "_32." in fp:
            return Size.P2_32

        return None

    @staticmethod
    def from_size(size: int) -> Union['Size', None]:
        if size == 8192:
            return Size.P2_8192
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
        if size == 64:
            return Size.P2_64
        if size == 32:
            return Size.P2_32

        return None