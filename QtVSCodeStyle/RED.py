import os,sys
sys.path.append(os.path.dirname(__file__))
import qtvscodestyle as qtvsc

def stylesheet():
    return qtvsc.load_stylesheet(qtvsc.Theme.RED)