CMAKE_MINIMUM_REQUIRED(VERSION 3.12)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/PixarAnimationStudios/OpenSubdiv/archive/refs/tags/v3_5_0.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
        "-DOSD_CUDA_NVCC_FLAGS=--gpu-architecture compute_50"
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
