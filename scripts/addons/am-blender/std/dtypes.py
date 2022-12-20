from enum import Enum
import typing
from bpy.types import (Image,)


class ImageScale(Enum):
    SCALE_2048 = 2048
    SCALE_1024 = 1024
    SCALE_512 = 512

    def append_str(self) -> str:
        if self.value == 2048:
            return "_2k"
        elif self.value == 1024:
            return "_2k"
        elif self.value == 512:
            return "_0.5k"

        return "None"

    def size(self) -> int:
        return self.value

    @staticmethod
    def from_image(image: 'Image', ) -> typing.Union['ImageScale', None]:
        if "_2k." in image.name:
            return ImageScale.SCALE_2048
        elif "_1k." in image.name:
            return ImageScale.SCALE_1024
        elif "_0.5k." in image.name:
            return ImageScale.SCALE_512

    @staticmethod
    def from_size(size: int) -> typing.Union['ImageScale', None]:
        if size == 2048:
            return ImageScale.SCALE_2048
        elif size == 1024:
            return ImageScale.SCALE_1024
        elif size == 512:
            return ImageScale.SCALE_512

        return None
