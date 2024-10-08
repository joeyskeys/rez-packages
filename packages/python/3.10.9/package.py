import platform

name = "python"

version = "3.10.9"

authors = [
    "Guido van Rossum"
]

description = \
    """
    Python is an interpreted high-level general-purpose programming 
    language.
    """

build_requires = [
    "gcc",
    "glibc"
]

requires = [
    "zlib",
    "openssl",
]

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.python"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")