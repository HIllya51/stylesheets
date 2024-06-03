import os, sys, json

sys.path.append(os.path.dirname(__file__))
from qtsymbols import *
from gui.inputdialog import autoinitdialog
from qt_material import build_stylesheet


def tryloadconfig():
    try:
        with open(__file__ + ".json", "r", encoding="utf8") as ff:
            return json.loads(ff.read())
    except:
        return {}


def get_setting_window(parent, callback):

    config = tryloadconfig()

    def callback1():
        with open(__file__ + ".json", "w", encoding="utf8") as ff:
            ff.write(json.dumps(config))
        callback()

    autoinitdialog(
        parent,
        "qt material",
        600,
        [
            {
                "type": "combo",
                "name": "Theme name",
                "d": config,
                "k": "theme",
                "list": [
                    "amber",
                    "blue",
                    "cyan",
                    "cyan_500",
                    "lightgreen",
                    "pink",
                    "purple",
                    "red",
                    "teal",
                    "yellow",
                ],
            },
            {"type": "okcancel", "callback": callback1},
        ],
    )


def stylesheet():
    config = tryloadconfig().get("theme", 0)
    return build_stylesheet(
        [
            "light_amber.xml",
            "light_blue.xml",
            "light_cyan.xml",
            "light_cyan_500.xml",
            "light_lightgreen.xml",
            "light_pink.xml",
            "light_purple.xml",
            "light_red.xml",
            "light_teal.xml",
            "light_yellow.xml",
        ][config],
        False,
        {},
    )
