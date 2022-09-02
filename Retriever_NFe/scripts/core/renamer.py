import os

def rename(path, file, info):
    dst = path+file
    src =f"{path}/{file}" #35220547411780000126550020001528301769037327.pdf / 35220547411780000126550020001528301769037327.xml
    dst =f"{path}/{info}" #DANFE152864.pdf / DANFE152864.xml
    os.rename(src, dst)

if __name__ == '__rename__':
    rename()