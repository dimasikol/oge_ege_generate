
def check_answer(answer_user,answer_true):
    if str(answer_user).replace(',','.',1).isdigit():
        try:
            if int(str(answer_user).strip().replace(',','.',1))==int(str(answer_true).strip().replace(',','.',1)):
                return 1
            else:
                return 0
        except:
            return 0
    else:
        if str(answer_true).strip().upper()==str(answer_user).strip().upper():
            return 1
        else:
            return 0

