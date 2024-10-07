import platform

name = "make"

version = "4.3"

authors = [
    "Stuart Feldman"
]

description = \
    """
    GNU Make is a tool which controls the generation of executables
    and other non-source files of a program from the program's
    source files.
    """

build_requires = []

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "softwares.make"


def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")