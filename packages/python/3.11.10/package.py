import platform

name = "python"

version = "3.11.10"

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

build_command = 'python {root}/build.py {install}'


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")