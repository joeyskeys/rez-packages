import platform

name = "glibc"

version = "2.28"

authors = [
    "Roland McGrath, Ulrich Drepper and others"
]

description = \
    """
    The GNU C Library, commonly known as glibc, is the GNU Project
    implementation of the C standard library. It is a wrapper
    around the system calls of the Linux kernel for application
    use.
    """

build_requires = [
    "make",
]

requires = []

variants = []

if platform.system() == "Darwin":
    variants.append(["platform-osx", "arch-x86_64"])
elif platform.system() == "Linux":
    variants.append(["platform-linux", "arch-x86_64"])

uuid = "libs.glibc"

build_command = 'python {root}/build.py {install}'


def commands():
    env.CPLUS_INCLUDE_PATH.append("{root}/include")
    env.LD_LIBRARY_PATH.append("{root}/lib")