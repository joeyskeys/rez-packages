import platform

name = "de256"

version = "1.0.15"

authors = [
    "Dr. Dirk Farin"
]

description = \
    """
    libde265 is an open source implementation of the h.265 video codec. It is
    written from scratch and has a plain C API to enable a simple integration
    into other software.
    """

build_requires = [
    "cmake",
    "gcc"
]

requires = [
    "jpeg-2.1.0",
    "png-1.6.37",
    "zlib-1.2.11",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.de256"


def commands():
    env.CPATH.append("{root}/include")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
