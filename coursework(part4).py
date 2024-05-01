# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20220273
# Date: 14.12.2022

#function for requesting marks
def credit(credit_type):
    while True:
        try:
            marks = int(input(f'enter your {credit_type} credits:'))
            if marks in range(0, 121, 20):
                return marks
            else:
                print('out of range')
        except ValueError:
            print('Integer required')

#Function for categorize marks
def result(pass_marks,difer_marks,fail_marks):
    final=None
    if pass_marks == 120 :
        final='Progress-'
    elif pass_marks == 100 :
        final='module trailer-'
    elif (pass_marks in [0, 20, 40])  and (difer_marks in [0,20,40]) and (fail_marks in [80,100,120]):
        final = 'Exclude-'
    else:
        final = 'module retriever-'
    return f'{final}{pass_marks},{differ_marks},{fail_marks}'

#Function to check student id
def id():
    while x:
        st_id = input('Input your student ID:')
        if not (st_id[1:].isdigit()):
            print("Invalid student ID")
            continue
        if len(str(st_id[1:]))==7 and st_id==("w"+str(st_id[1:]))and len(st_id)==8:
            return st_id
        else:
            print("Invalid student ID")
while True:
    x = True
    status_dict = {}#opening dictionary 
    try:
        z = int(input('Enter 1 if you are  a student and 2 if you are a tutor:'))
        if z == 1:
            print('\n')
            print('__________________welcome to student portal__________________')
            print('\n')
            while True:
                student_id=id()
                pass_marks = credit('pass')
                differ_marks = credit('difer')
                fail_marks = credit('fail')
                if pass_marks + differ_marks + fail_marks == 120:
                    final_mark=result(pass_marks, differ_marks, fail_marks)
                    print('\n')
                    print(f'{student_id}:{final_mark}')
                    print('\n')
                    break
                else:
                    print("Incorrect total")
        elif z == 2:
            print('\n')
            print('__________________welcome to staff portal__________________')
            print('\n')
            while x:
                student_id=id()
                pass_marks = credit('pass')
                differ_marks = credit('difer')
                fail_marks = credit('fail')

                if pass_marks + differ_marks + fail_marks == 120:
                    final_result=result(pass_marks,differ_marks,fail_marks)
                    status_dict[student_id] = final_result
                    print(f'{student_id}:{final_result}')
                    print('\n')
                else:
                    print("Incorrect total")
                    continue
                while True:
                    user_decision = input("do u want to add another data set(y/q)").lower()
                    print('\n')
                    if user_decision == 'y':
                        break
                    elif user_decision == 'q':
                        for key in status_dict:
                            print(f'{key}:{status_dict[key]}')#printing dictionary
                            print('\n')
                        x=False
                        break
                    else:
                        print("Invalid input")
        else:
            print('Enter a valid number')
    except ValueError:
        print('please enter 1 or 2')

