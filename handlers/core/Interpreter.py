Auther = "xiaodi001"
Version="1.0.0"
CmdTrans={
    "prn":{
        "PythonCmd":"print(",
        "IsFunction":True,
        "ArgCount":1
    },
    "imprtImgRes()":{
        "PythonCmd":"pygame.image.load(",
        "IsPythonCmd":True,
        "IsFunction":True,
        "ArgCount":1
    }
}
def init():
    return Auther, Version, CmdTrans