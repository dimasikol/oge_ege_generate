import os,json,random
from apps.settings import BASE_DIR
from ..models.quiz_create import QuizCreate
with open(os.path.join(BASE_DIR, r'quiz/logicquiz/scratch_2_ege.json'), 'r', encoding='UTF-8') as file2,open(os.path.join(BASE_DIR, r'quiz/logicquiz/scratch_1.json'), 'r', encoding='UTF-8') as file:
    date = json.load(file)
    date2 = json.load(file2)




class Task7:
    def __init__(self):
        self.date = date2['seven']['text'][0]#random.choice(date2['seven']['text'])
        self.answer = random.randint(4, 100000,4)

    def write(self):
        match self.date[-1]:
            case 'type1':
                self.format = [('моно',1),('стерео',2),('квадро',4)]
                self.format_choice = random.choice(self.format)
                self.format.pop(self.format_choice)
                self.format_choice2 = random.choice(self.format_choice2)
                self.size = self.answer
                self.discret = random.choice([2,3,4,5,6,8,10])
                self.chast = random.choice([2,3,4,5,6,8,10])
                self.data = self.date[0]+self.format[0]+self.date[1]+str(self.size)+self.date[2]
            case 'type2':
                self.data = self.date
            case 'type3':
                self.data = self.date
            case 'type4':
                self.data = self.date
            case 'type5':
                self.data = self.date
            case _:
                self.data = self.date
        return {'quiz':self.data, 'answer':self.answer}