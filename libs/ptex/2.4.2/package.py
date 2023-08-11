import platform

name = "ptex"

version = "2.4.2"

authors = [
    "WDAS"
]

description = \
    """
    Ptex is a texture mapping system developed by Walt Disney Animation Studios
    for production-quality rendering.
    """

build_requires = [
    "cmake"
]

requires = [
    "zlib"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.ptex"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")