import platform

name = "srt"

version = "1.5.3"

authors = [
    "Haivision stuffs",
]

description = \
    """
    Secure Reliable Transport (SRT) is a transport protocol for ultra low
    (sub-second) latency live video and audio streaming, as well as for
    generic bulk data transfer.
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

uuid = "libs.srt"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
