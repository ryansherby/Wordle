def installDependencies(listObj):
    import sys
    import subprocess

    package_list = listObj

    for package in package_list:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    package])


if __name__ == '__main__':
    installDependencies()


