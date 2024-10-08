CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/OpenImageIO/oiio/archive/refs/tags/v2.4.6.0.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if($ENV{REZ_BUILD_INSTALL})
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
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
        -DCMAKE_FIND_USE_CMAKE_PATH=FALSE
        -DCMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY=FALSE
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=17
        -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
        -DPython_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python3
        -Dpybind11_ROOT=$ENV{REZ_PYBIND11_ROOT}
        -DTBB_ROOT=$ENV{REZ_TBB_ROOT}
        -DOpenEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
        -DOpenColorIO_ROOT=$ENV{REZ_OCIO_ROOT}
        #-DLibRaw_ROOT=$ENV{REZ_RAW_ROOT}
        -DOpenJPEG_ROOT=$ENV{REZ_OPENJPEG_ROOT}
        -DTIFF_ROOT=$ENV{REZ_TIFF_ROOT}
        -DPNG_ROOT=$ENV{REZ_PNG_ROOT}
        -DOPENVDB_ROOT=$ENV{REZ_OPENVDB_ROOT}
        -DJPEGTurbo_ROOT=$ENV{REZ_JPEG_ROOT}
        -DGIF_ROOT=$ENV{REZ_GIF_ROOT}
        -DHEIF_ROOT=$ENV{REZ_HEIF_ROOT}
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        -DUSE_SIMD=sse2,sse3,ssse3,sse4.1,sse4.2,avx,avx2
        -DOIIO_BUILD_TESTS=OFF
        -DOIIO_BUILD_TOOLS=ON
        #-DUSE_QT=OFF
        #-DUSE_OPENGL=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
