import platform

name = "embree"

version = "4.2.0"

authors = [
    "Intel Corporation"
]

description = \
    """
    Intel® Embree is a collection of high-performance ray tracing kernels, developed at Intel.
    """

build_requires = [
    "cmake",
    "gcc"
]

requires = [
    "tbb-2020.3",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "embree-4.2.0"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/embree-4.2.0")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")