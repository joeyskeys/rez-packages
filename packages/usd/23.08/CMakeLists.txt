CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v23.08.tar.gz)
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
        -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
        -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
        -DOPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}
        -DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
        -DOIIO_LOCATION=$ENV{REZ_OIIO_ROOT}
        -DOCIO_LOCATION=$ENV{REZ_OCIO_ROOT}
        -DOSL_LOCATION=$ENV{REZ_OSL_ROOT}
        -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
        -DEMBREEE_LOCATION=$ENV{REZ_EMBREE_ROOT}
        -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
