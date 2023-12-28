import platform

name = "heif"

version = "1.17.6"

authors = [
    "Dr. Dirk Farin"
]

description = \
    """
    libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format)
    file format decoder and encoder. There is partial support for ISO/IEC
    23008-12:2022 (2nd Edition) capabilities.
    """

build_requires = [
    "cmake",
    "gcc"
]

requires = [
    "jpeg-2.1.0",
    "png-1.6.37",
    "de256-1.0.15",
    "zlib-1.2.11",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.heif"


def commands():
    env.CPATH.append("{root}/include")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
