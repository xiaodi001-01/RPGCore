Auther = "xiaodi001"
Version="1.0.0"
CmdTrans={
    "prn":{
        "PythonCmd":"print(",
        "IsFunction":True,
        "ArgCount":1
    },
    "imprt":{
        "PythonCmd":"print(",
        "IsPythonCmd":False,
        "IsFunction":True,
        "ArgCount":1
    } # type: ignore
}
def init():
    return Auther, Version, CmdTrans