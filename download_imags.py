#Write by jonathan brahmi

#Enter a images your want to download


import os

nginx = 0
adejonge_world = 0
jenkins = 0
dockerui = 0

def images_install():
    print(" + Select images\n")
    print(" - Jenkins\n")
    print(" - dockerui \n")
    print(" - nginx  \n")
    print(" - adejonge/helloworld\n")
    images_name = str(input("Which images you want to install>>"))
    os.system(f"docker pull {images_name}")
    os.system("docker images")
    os.system("pause")
images_install()