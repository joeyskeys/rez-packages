import os
import sys
import requests
import tarfile
import subprocess
import signal
import traceback
import functools


def build(source_path, build_path, install_path, targets):
    package_url = 'https://ftp.gnu.org/gnu/binutils/binutils-2.31.1.tar.xz'
    package_name = os.path.basename(package_url)
    # extension name .tar.xz is kinda special, the following logic is specific
    # to this downloading url
    extension_idx = package_name.find('.tar.xz')
    folder_name = package_name[:extension_idx]
    build_folder = "build"
    build_folder_path = os.path.join(build_path, build_folder)

    def terminate_proc(proc, sig, frame):
        try:
            if proc:
                proc.terminate()
                proc.wait()
        except:
            traceback.print_exc()
        finally:
            sys.exit()

    def _build():
        os.chdir(build_path)
        if not os.path.exists(package_name):
            print("package doesn't exist, start downloading...")
            response = requests.get(package_url)
            open(package_name, 'wb').write(response.content)

        if not os.path.exists(folder_name):
            print('extracting package...')
            f = tarfile.open(package_name)
            f.extractall(build_path)

        if not os.path.exists(build_folder_path):
            os.makedirs(build_folder_path)
        os.chdir(build_folder_path)

        makefile_path = os.path.join(build_path, build_folder, 'Makefile')
        if not os.path.exists(makefile_path):
            print('package not configured, configure now...')
            configure_proc = subprocess.Popen('../{}/configure --prefix=$REZ_BUILD_INSTALL_PATH'.format(folder_name), shell=True)
            handler = functools.partial(terminate_proc, configure_proc)
            signal.signal(signal.SIGINT, handler)
            signal.signal(signal.SIGTERM, handler)
            configure_proc.wait()
            print('configure return code', configure_proc.returncode)
            if (configure_proc.returncode != 0):
                print('configure failed, terminating...')
                return

        built_path = os.path.join(build_path, build_folder, 'built')
        if not os.path.exists(built_path):
            print('package not built, build now...')
            make_proc = subprocess.Popen('make -j{}'.format(os.cpu_count()), shell=True)
            handler = functools.partial(terminate_proc, make_proc)
            signal.signal(signal.SIGINT, handler)
            signal.signal(signal.SIGTERM, handler)
            make_proc.wait()
            if (make_proc.returncode != 0):
                print('make failed, terminating...')
                return
            f = open('built', 'w')
            f.write('0')
            f.close()

        print('build done')

    def _install():
        print('installing package...')
        os.chdir(build_folder_path)
        install_proc = subprocess.Popen('make install', shell=True)
        handler = functools.partial(terminate_proc, install_proc)
        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)
        install_proc.wait()
        print('install done')

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )