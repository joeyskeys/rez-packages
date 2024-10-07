import platform

name = "binutils"

version = "2.31.1"

authors = [
    "Michael Larabel and others"
]

description = \
    """
    Collection of tools for operating on object files.
    """

build_requires = [
    "gcc"
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.binutils"

build_command = 'python {root}/build.py {install}'


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")