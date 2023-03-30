import platform
import subprocess


PYTHON_DEPENDENCIES = "tk Pillow "

OS_TYPE = platform.system()
PROGNAME = "Chess Royal"
RELEASE = "Revision 1.0"
AUTHOR= "(c) On mettra nos nom plus tard"

def pip_dep():
    pip_install = "pip3 install " + PYTHON_DEPENDENCIES
    process = subprocess.Popen(pip_install.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if(error):
        print("PIP INSTALL FAILED. You may install depedencies yourself. See error :")
        print(error)

def install_mac():
     print("No extra dep for the moment")

def install_win():
     print("No extra dep for the moment")

print(RELEASE + " | " + AUTHOR)
pip_dep() # pip3 install of all python lib
if(OS_TYPE == 'Darwin'):
    print("Mac OS detected")
    install_mac()
elif(OS_TYPE == 'Windows'):
    print("Windows detected")
    install_win()


