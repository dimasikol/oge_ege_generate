import json
import random
from . import generate_answer
import os
from apps.settings import BASE_DIR
with open(os.path.join(BASE_DIR, r'quiz/logicquiz/scratch_1.json'), 'r', encoding='UTF-8') as file:
    date = json.load(file)

class Task1:
    Task_num=0
    def __init__(self):
        Task1.Task_num+=1
        self.text = date['one']['text00']
        self.words_variable = random.choice(date['one']["text_quiz"])
        self.words_answer = random.choice(self.words_variable)  # ответ
        self.len_words = len(self.words_answer)
        self.bit = random.choice(date['one']["bits_num"])  # цифры
        self.type_bit = random.choice(date['one']["bits_type"])  # бит вопрос
        self.bit_answer = random.choice(date['one']["bits_type"])  # бит ответы
        self.sim_count = random.randint(0, 2)  # пробел и запятая
        self.new_text_bool = random.randint(0, 1)
        self.random_num = [random.randint(13, 100) for _ in range(5)]
        self.schet = date['one']['encoding_bit'][self.bit_answer + self.type_bit] if \
            isinstance(date['one']['encoding_bit'][self.bit_answer + self.type_bit], int)\
            else eval(date['one']['encoding_bit'][self.bit_answer + self.type_bit])
    def choice(self):
        if self.type_bit == self.bit_answer:
            self.result = (self.len_words + self.sim_count) * self.bit
        else:
            self.result = (self.len_words + self.sim_count) * (self.schet) * (self.bit)
        return self.result
    '''доделать и переписать функции write1,write2,write3, одну функцию с одной строкой'''

    def write(self, type):
        self.write_answer = f"{self.text[type]['1']} {self.bit} {self.type_bit}{self.text[type]['2']}"

    def write1(self):  # записываем вопрос
        self.write_answer = date['one']['text']
        if self.new_text_bool:
            self.write_answer3 = self.write_answer[:54] + str(self.bit) + ' ' + self.type_bit + self.write_answer[54:104] + '" ' + ', '.join(self.words_variable) + ' "\n ' + self.write_answer[104:136] + '. ' + date['one']['text' + str(self.sim_count)] + self.write_answer[136:204] + str(self.choice()) + ' ' + self.bit_answer + self.write_answer[204:]
        else:
            self.words_variable2 = self.words_variable.copy()
            self.words_variable2.pop(self.words_variable.index(self.words_answer))
            self.write_answer3 = self.write_answer[:54] + str(self.bit) + ' ' + self.type_bit + self.write_answer[54:104] + '" ' + ', '.join(self.words_variable2) + date['one']['2text'][:25] + self.words_answer + date['one']['2text' + str(self.sim_count)] + date['one']['2text'][26:44] + self.bit_answer + date['one']['2text'][44:] + '.'
            self.words_answer= self.choice()
            if isinstance(self.words_answer,float):
                self.words_answer=round(self.words_answer,2)
        return {'quiz': self.write_answer3, 'answer': str(self.words_answer), "type_quiz": f"{Task1.Task_num}.Задание №1(1)"}

    def write2(self):
        self.write_answer = date['one']['3text']
        self.write_answer3 = f'{self.write_answer[:44]} {self.random_num[0]}{self.write_answer[45:79]} {self.random_num[1]} {self.write_answer[80:108]} {self.random_num[2]} {self.write_answer[109:182]} {self.bit} {self.type_bit} {self.write_answer[182:188]}\n{self.write_answer[189:232]} {self.bit_answer}.\n{self.write_answer[236:]}'
        self.answer_2 = self.schet * self.bit * self.random_num[0] * self.random_num[1] * self.random_num[2]
        if isinstance(self.answer_2,float):
            self.answer_2 = round(self.answer_2, 2)
        return {'quiz': self.write_answer3, "answer": str(self.answer_2), "type_quiz": f"{Task1.Task_num}.Задание №1(2)"}

    def write3(self):
        """импортировать текст с интернета рандомный"""
        self.write_answer = random.choice(date['one']['4text'])
        self.write_answer3 = f'{date["one"]["4text0"][:54]} {self.bit} {self.type_bit}{date["one"]["4text0"][60:81]} {self.bit_answer} {date["one"]["4text0"][84:]}\n"{self.write_answer}"'
        self.answer_3 = len(self.write_answer) * self.bit * self.schet
        if isinstance(self.answer_3,float):
            self.answer_3 = round(self.answer_3, 2)
        return {"quiz": self.write_answer3, "answer": str(self.answer_3), "type_quiz": f"{Task1.Task_num}.Задание №1(3)"}

    def __str__(self):
        return f'биты {self.bit} {self.type_bit} правильный ответ {self.words_answer}'

class Task2:
    pass

class Task3:
    pass

class Task4:
    def __init__(self):
        self.word = ' ABCDEFGH'
        self.rand1=[(1,4),(2,8),(4,9),(1,4),(5,10),(7,14)]
    @property
    def show_table(self):
        random.shuffle(self.rand1)
        self.date = [[random.randint(*self.rand1[0]) if i==0 else random.randint(*self.rand1[1]) if i==1 else random.randint(*self.rand1[0]) if i==2 else random.randint(*self.rand1[0]) if i==3 else random.randint(*self.rand1[0]) if i==0 else random.randint(*self.rand1[0]) if i==4 else random.randint(*self.rand1[0]) if i==5 else random.randint(16,50) for i in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                if i == 0 or j == 0:
                    if i == 0:
                        self.date[i][j] = self.word[j]
                    else:
                        self.date[i][j] = self.word[i]
                else:
                    if i == j:
                        self.date[i][j] = 'Ø'
                    else:
                        self.date[j][i] = self.date[i][j]
        self.date[1][6] += 15
        self.answer_date = []
        for k in range(2,6):

            self.time_res=self.date[1][k]+self.date[k][len(self.date[0])-1]
            self.answer_date.append(self.time_res)
            try:
                if isinstance(self.date[k][k+1],int) and isinstance(self.date[k][2],int):
                    self.answer_date.append((self.time_res-self.date[1][k]+self.date[1][k-1]+self.date[k-1][k]))
            except ValueError:
                print('error Value')
            self.answer_min=min(self.answer_date)
        return self.date,self.answer_min


    def write(self):
        self.table,self.answer = self.show_table
        return {"quiz":self.table,"answer":self.answer}

class Task5:
    Task_num = Task1.Task_num
    def __init__(self):
        Task5.Task_num += 1
        self.date = date['five']
        self.text = self.date['text']
        self.random_type_choise=random.choice(self.date['random_type']['5'])
        self.start_num= random.randint(2,44)
        self.result = self.start_num
        self.nums=[random.randint(1,20),random.randint(2,60)]
        self.type_znaks = [random.choice(['*','+','-']),random.choice(['*','+','-'])]
        self.spisok=random.choice(self.date['random_type']['5'])
        self.answer = 'ответ'
        self.variant = 'вариант'
    def create_quiz(self):
        for item in self.spisok:
            self.result= eval(f'{self.result}{self.type_znaks[item-1]}{self.nums[item-1]}')

        return self.result

    def write(self):
        #self.quiz= self.text['text']+self.type_znaks[0]+" "+str(self.nums[0])+'<br>'+self.type_znaks[1]+str(self.nums[1])+self.text['text1']
        self.quiz= f'{self.text["text"]} {self.date["keys"][self.type_znaks[0]]}' \
                   f' {self.nums[0]}<br>{self.date["keys"][self.type_znaks[1]]} ' \
                   f'b {self.text["text1"]}{self.text["text2"]} {self.date["keys"][self.type_znaks[0]]} {self.nums[0]} ' \
                   f'{self.text["text3"]} {self.date["keys"][self.type_znaks[1]]} {self.nums[1]} {self.text["text4"]} {"".join(list(map(str,self.spisok)))}' \
                   f' {self.text["text5"]} {self.start_num} в {self.create_quiz()} {self.text["text6"]}'

        return {"quiz":self.quiz,"variant":self.variant,"answer":self.nums,"type_quiz":{Task5.Task_num}}


class Task6:
    Task_num = Task5.Task_num
    def __init__(self):
        Task6.Task_num += 1
        self.date = date['six']
        self.text = self.date['text']
        self.num = [random.randint(11,43),random.randint(11,43)]
        self.variant = [((random.randint(-45,45),random.randint(-45,45))) for _ in range(9)]
        self.choice_znak = random.choice([">", ">=", "<", "<=","=="]),
        self.choice_znak2 = random.choice([">", ">=", "<", "<=","=="]),
        self.logic = random.choice(['and','or'])
        self.count_YES=0
        self.YES_OR_NO = random.choice(['"YES"','"NO"'])
    def choice(self):
        for i in range(len(self.variant)):
            if self.logic=='and' and eval(f'{self.variant[i][0]} {self.choice_znak[0]} {self.num[0]} and {self.variant[i][1]} {self.choice_znak2[0]} {self.num[1]}'):
                self.count_YES+=1
            elif self.logic=='or' and eval(f'{self.variant[i][0]} {self.choice_znak[0]} {self.num[0]} or {self.variant[i][1]} {self.choice_znak2[0]} {self.num[1]}'):
                self.count_YES += 1
        if self.YES_OR_NO=='"NO"':
            self.count_YES=9-self.count_YES

        return self.count_YES
    def write(self):
        self.choice()
        self.quiz = f"<h6>{self.text['text1']}</h6> if s{self.choice_znak[0]}{self.num[0]} {self.logic} t{self.choice_znak2[0]}{self.num[1]}:<h6>&nbsp;&nbsp;&nbsp;&nbsp;print('YES')</h6><h6>else:</h6><h6>&nbsp;&nbsp;&nbsp;&nbsp;print('NO')</h6>"
        return {"quiz":self.quiz,"variant":self.variant,"answer":self.count_YES,"type_quiz":Task6.Task_num,"YES_OR_NO":self.YES_OR_NO}


class Task7:
    Task_num = Task6.Task_num
    def __init__(self):
        Task7.Task_num+=1
        self.date = date['seven']
        self.text = self.date['address']
        self.protokol = random.choice(self.text['protokol'])
        self.address = [random.choice(self.text['domain']),random.choice(self.text['second_level_domain']),random.choice(self.text['top_level_domain'])]
        self.path = random.choice(self.text['path'])
        self.file_type = random.choice(self.text['file_type'][random.choice(['photo','media','text','video'])])
        self.file_name = random.choice(self.text['file_name'])
        self.answer = f'{self.protokol}://{self.address[0]}.{self.address[1]}.{self.address[2]}/{self.path}/{self.file_name}.{self.file_type}'
        self.randomize_answer = (self.protokol,"://","/",'.',self.address[0],self.address[1],self.address[2],self.path,self.file_name,self.file_type)
        self.alf = list(date['alfa'])[:10]
        random.shuffle(self.alf)
        self.answer_tuple = sorted(list(zip(self.alf,self.randomize_answer)))
        self.answer_dict = {v:k for k, v in dict(self.answer_tuple).items()}
        self.answer1 = self.answer_dict[self.protokol]+self.answer_dict['://']+self.answer_dict[self.address[0]]+self.answer_dict["."]+self.answer_dict[self.address[1]]+self.answer_dict["."]+self.answer_dict[self.address[2]]+self.answer_dict["/"]+self.answer_dict[self.path]+self.answer_dict["/"]+self.answer_dict[self.file_name]+self.answer_dict["."]+self.answer_dict[self.file_type]
        self.answer_quiz = ''.join(list(map(lambda x:f'{x[0]}) {x[1]}<br>',self.answer_tuple)))

    def write(self):
        self.quiz=f"{self.date['text1']} {self.file_name}.{self.file_type} {self.date['text2']} {self.address[1]}.{self.address[2]} в директории {self.path} поддомена {self.address[0]} {self.date['text3']} {self.protokol} {self.date['text4']}"
        return {"quiz":self.quiz,'answer_quiz':self.answer_quiz,"answer":str(self.answer1),"type_quiz":f'{Task7.Task_num}.Задание № 7'}


class Task8:
    Task_num=Task7.Task_num
    def __init__(self):
        Task8.Task_num+=1
        self.date = date['eight']
        self.text = self.date['text']
        self.random = sorted([random.randint(11, 1000) * 10 for _ in range(3)])
        self.choice = random.choice(["|", "&","1"])
        self.words = random.choice(self.date["requests_word"]['2'])
    def func_random_choice(self,choice):
        if choice in "|&":
            self.answer = self.random[2] + self.random[1] - self.random[0]
            self.choice_words = {"&": (self.random[0],"|"), "|": (self.answer,"&")}
            self.quiz = [(self.words[0], self.random[2]),
                         (self.words[1], self.random[1]),
                         (f'{self.words[0]} {choice} {self.words[1]}',self.choice_words[choice[0]])]  # три элемента для вопроса
            return self.quiz,self.choice_words[self.choice_words[choice][1]][0],f'{self.words[0]} {self.choice_words[self.choice][1]} {self.words[1]}'
        else:
            self.random_1_0=random.randint(1,2)
            self.answer = self.random[self.random_1_0]
            self.quiz_reversed = 2 if self.random_1_0==1 else 1
            self.quiz= [(f'{self.words[0]} & {self.words[1]}', self.random[0]),
                        (f'{self.words[0]} | {self.words[1]}', self.random[2] + self.random[1] - self.random[0] ),
                        (self.words[1],(self.random[self.quiz_reversed],))]
            return self.quiz, self.answer,self.words[0]
    def write(self):
        self.write_quiz =f"{self.text['type1']}"
        self.quiz,self.answer_total,self.quiz3_anwer = self.func_random_choice(self.choice)
        self.write_quiz2 =f'{self.text["type2"]} "{self.quiz3_anwer}" {self.text["type3"]}'
        return {"quiz": self.write_quiz,"answer":self.answer_total,"quiz1":self.write_quiz2, "quiz_p": self.quiz, 'type_quiz': f'{Task8.Task_num}.Задание №8'}


class Task10:
    Task_num=Task8.Task_num
    def __init__(self):
        self.text = date['ten']
        self.num_random = random.randint(26, 999)  # минимум и максимум рандома
        self.list_random_num = sorted(
            list(set([self.num_random + random.randint(1, 10) for _ in range(1, 6)])))  # три числа
        if len(self.list_random_num) <= 3:
            self.list_random_num = [self.num_random - 1, self.num_random, self.num_random + 3]  # три числа
        self.variants = self.text['variable']  # всевозможные варианты
        self.variant_choice = random.choice(self.variants)  # выбранный вариант
        self.quiz_answer = generate_answer.choice_variant(self.list_random_num, self.variant_choice)
        self.cc = [random.randint(2, 36) for _ in range(len(self.quiz_answer[0]))]
        self.random_cc = 10  # random.randint(2,16)
        Task10.Task_num+=1
    def change_num(self, num, cc,
                   result=''):  # перевод из 10 сс в любую другую до 36 "num"=число которое перести "cc" в какую систему счисления
        if num < cc:
            return str(date["ten"]["translate"][str(num % cc)]) + result
        res = date["ten"]["translate"][str(num % cc)] + result
        return self.change_num(num=num // cc, cc=cc, result=res)

    def write1(self):
        self.list_change_num = [self.change_num(num, cc) for num, cc in zip(self.quiz_answer[0], self.cc)]
        self.question_list = [f'{v}<sub>({k})</sub>' for v, k in zip(self.list_change_num, self.cc)]
        random.shuffle(self.question_list)
        self.kratnost = ''
        if self.variant_choice == 'кратное' or self.variant_choice == 'количество чисел':
            self.kratnost = self.quiz_answer[2]
        self.write_answer2 = f"{self.text['text1']} <b>{len(self.list_change_num)}</b> {self.text['text2']} <p> <b>{self.variant_choice}</b> {self.kratnost}  <b>({', '.join(self.question_list)})</p></b>{self.text['text3']} {self.random_cc} {self.text['text4']} <p>{self.text['text5']}</p>"
        return {"quiz": self.write_answer2, 'answer': self.quiz_answer[1], 'parametrs': self.variant_choice,
                "type_quiz": f"{Task10.Task_num}.Задание №10(1)"}