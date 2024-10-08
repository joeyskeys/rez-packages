import platform, os

name = "minizip"

version = "3.0.7"

authors = [
    "Nathan Moinvaziri",
]

description = \
    """
    The GIFLIB project maintains the giflib service library,
    which has been pulling images out of GIFs since 1989. 
    """

build_requires = [
    "cmake",
    "gcc"
]

requires = [
    "zlib-1.2"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.minizip"


def commands():
    env.PATH.append("{root}/lib")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/minizip")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
