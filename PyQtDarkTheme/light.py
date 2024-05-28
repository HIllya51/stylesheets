import os


def stylesheet():

    with open(
        os.path.join(os.path.dirname(__file__), "light.qss"),
        "r",
        encoding="utf8",
    ) as ff:
        s = ff.read()
    return s.replace(
        "___PATH___",
        os.path.join(os.path.dirname(__file__), "light").replace("\\", "/"),
    )
