import platform

name = "usd"

version = "23.08"

authors = [
    "Pixar Studio"
]

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for
    authoring, reading, and streaming time-sampled scene description for
    interchange between graphics applications.
    """

build_requires = [
    "cmake",
    "gcc",
]

requires = [
    "boost-1.80",
    "tbb-2020.3",
    "opensubdiv-3",
    "openexr",
    "oiio-2.4",
    "ocio-2.2",
    "osl-1.12",
    "ptex-2",
    "embree",
    "zlib",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.usd"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.PYTHONPATH.append("{root}/lib/python")
    env.PATH.append("{root}/bin")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")