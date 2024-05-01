# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20220273
# Date: 14.12.2022

#function to request marks
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

#function to categorize marks
def result(pass_marks, difer_marks, fail_marks):
    final = None
    if pass_marks == 120:
        final = 'Progress-'
        print('Progress')
    elif pass_marks == 100:
        final = 'module trailer-'
        print('Progress(module_trailer)')
    elif (pass_marks in [0, 20, 40]) and (difer_marks in [0, 20, 40]) and (fail_marks in [80, 100, 120]):
        final = 'Exclude-'
        print('Exclude')
    else:
        final = 'module retriever-'
        print('Do_not_progress(Module_retriever)')
    return [f'{final}{pass_marks},{differ_marks},{fail_marks}']


status = []
prog_count = 0
retr_count = 0
mod_tr_count = 0
exc_count = 0
total_outcomes = 0
x = True

while x:
    try:
        z = int(input('Enter 1 if you are  a student and 2 if you are a tutor:'))
        if z == 1:#student portal
            print('__________________welcome to student portal__________________')
            pass_marks = credit('pass')
            differ_marks = credit('difer')
            fail_marks = credit('fail')
            if pass_marks + differ_marks + fail_marks == 120:
                final_result = result(pass_marks, differ_marks, fail_marks)
                status.append(final_result)
                if pass_marks == 120:
                    prog_count += 1
                elif pass_marks == 100:
                    mod_tr_count += 1
                elif (120 >= fail_marks >= 80) and (0 <= pass_marks <= 40):
                    exc_count += 1
                else:
                    retr_count += 1
            else:
                print("Incorrect total")
            break
        elif z == 2:#staff portal
            print('__________________welcome to staff portal__________________')
            loop_1=True
            while loop_1:
                pass_marks = credit('pass')
                differ_marks = credit('difer')
                fail_marks = credit('fail')
                if pass_marks + differ_marks + fail_marks == 120:
                    final_result = result(pass_marks, differ_marks, fail_marks)
                    status.append(final_result)
                    if pass_marks == 120:
                        prog_count += 1
                    elif pass_marks == 100:
                        mod_tr_count += 1
                    elif (120 >= fail_marks >= 80) and (0 <= pass_marks <= 40):
                        exc_count += 1
                    else:
                        retr_count += 1
                else:
                    print("Incorrect total")
                    continue
                while True:#Considering user's choice tyo continue or not
                    user_dis = input("do u want to add another data set(y/q)").lower()
                    if user_dis == 'y':
                        break
                    elif user_dis == 'q':
                        #printing histogram
                        print('_________________________________________________________')
                        print('histogram')
                        print('Progress', prog_count, ':', '*' * prog_count)
                        print('Trailer', mod_tr_count, ':', '*' * mod_tr_count)
                        print('Retriever', retr_count, ':', '*' * retr_count)
                        print('Excluded', exc_count, ':', '*' * exc_count)
                        total_outcomes = prog_count + retr_count + mod_tr_count + exc_count
                        print(total_outcomes, "outcomes in total")
                        print('_________________________________________________________')
                        print("\n")
                        
                        x = False
                        loop_1=False
                        my_file = open('file_handling.txt', 'a')#file handling part
                        for m in status:
                            print(*m)#printing list
                            my_file.write(f'{m[0]}\n')
                    else:
                        print("Invalid input")
                        continue
                    break

        else:
            print("Enter a valid input")
    except ValueError:
        print("Integer required")
