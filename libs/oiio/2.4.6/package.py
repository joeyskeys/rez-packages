import platform

name = "oiio"

version = "2.4.6"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and 
    a bunch of related classes, utilities, and applications.
    """

build_requires = [
    "cmake"
]

requires = [
    "boost-1.80",
    "python-3.10",
    "tbb-2020.3",
    "imath-3.1",
    "openexr-3.1",
    "ocio-2.2",
    "openjpeg-2.4.0",
    "jpeg-2.1.0",
    "tiff-4.3.0",
    "gif-5.2",
    "png-1.6.37",
    "zlib-1.2.11",
    "fmt-8.0.1",
    "pybind11-2.10"
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.oiio"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/OpenImageIO")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
