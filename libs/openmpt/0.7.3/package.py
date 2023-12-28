import platform

name = "openmpt"

version = "0.7.3"

authors = [
    "Olivier Lapicque"
]

description = \
    """
    OpenMPT is an open-source audio module tracker for Windows (with an
    intended Wine-functionality for UNIX and Linux x86-systems).
    """

build_requires = [
    "cmake",
    "gcc",
]

requires = [
    "zlib-1.2.11",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.openmpt"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")