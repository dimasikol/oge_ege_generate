from . import task1
import random
def context(count_elements):
    if count_elements:
        context1 = [random.choice([task1.Task1().write1(), task1.Task1().write2(), task1.Task1().write3()]) for _ in range(int(count_elements["quiz1"]))]
        #context2 = [task1.Task2().write() for _ in range(int(count_elements["quiz2"]))]
        #context3 = [task1.Task3().write() for _ in range(int(count_elements["quiz3"]))]
        context4 = [task1.Task4().write() for _ in range(int(count_elements["quiz4"]))]
        context5 = [task1.Task5().write() for _ in range(int(count_elements["quiz5"]))]
        context6 = [task1.Task6().write() for _ in range(int(count_elements["quiz6"]))]
        context7 = [task1.Task7().write() for _ in range(int(count_elements["quiz7"]))]
        context8 = [task1.Task8().write() for _ in range(int(count_elements["quiz8"]))]
        #context9 = [task1.Task9().write() for _ in range(int(count_elements["quiz9"]))]
        context10 = [random.choice([task1.Task10().write1()]) for _ in range(int(count_elements["quiz10"]))]
        context = {"answer1": context1,"answer4":context4,"answer5": context5,"answer6":context6, "answer7": context7, "answer8": context8,"answer10": context10} #,"timer":[end1,end4,end5,end6,end7,end8,end10]
    else:
        return ''
    return context
