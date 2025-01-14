import pip


def install_packages():
    print('starting to install packages')

    def install_package(package):
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])

    install_package('pyttsx3')
    print("Installed 'pyttsx3'")
    f = open('initial.vira', 'w')
    f.write('initisalised')
    f.close()
    f = open('users.vira', 'w')
    f.write("admin-1234")
    f.close()
    print("added file 'initial.vira'")


if __name__ == "__main__":
    install_packages()
