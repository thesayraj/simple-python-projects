import ast

# questions = [
#     "Full form of DHCP is : ", "Who created C language? ",
#     "Who owns Java?"
# ]

# answers = ["a","b","b"]


# options = {1:" A) Dynamic Host Control Protocol\n B) Dynamic Host Configuration Protocol",
# 2:" A) Robert Steve\n B) Dennis Ritchie\n C) Robert Smallshare", 3:" A) Sys \n B) Oracle"
# }

# score = 0
# for i in range(len(questions)):
#     print(questions[i])
#     print(options[i+1])
#     choice = input(":")
#     if choice.lower() == answers[i]:
#         print("correct")
#         score += 1
#     else:
#         print("wrong")
#     print("\n")



# print("\n\n Final Score is "+str(score))


# r = input("Reveal ansewers ? (y or n) : ")
# if r == 'n' or r == 'N':
#     print("okay")
# else:
#     print("Answers are \n")
#     for index,answer in enumerate(answers):
#         print(str(index+1)+'.'+answer)



"""
{
    '1' : {
        'options':['a','b','c','d'],
        'answer':'a'
    },
    '2':{
        'a','b','c','d'
    },
    '3':{
        'a','b','c','d'
    }
}
"""

def add_questions():
    questions = []
    option_sol = dict()


    for i in range(1,4):   
        q = input(f"q:{i} ")
        questions.append(q)

        options = list()
        for j in range(1,4):
            option = input(f"option {j} ")
            options.append(option)
        ans = input("correct option: ")
     
        option_sol[i] = dict({'options':options, 'answer':ans})



    # print("\n")
    # print(questions)
    # print("\n")
    # print(option_sol)

    with open("quiz.txt", 'a+') as file:
        file.write("\n")
        file.write(str(questions))
        file.write(" ;9; ")
        file.write(str(option_sol))



#add_questions()


def fetch_quiz():

    with open("quiz.txt",'r') as file:
        line = file.readlines()[-1]
        #print(lines[4])
        separator_index = line.find(';9;')
        ques_list = line[:separator_index]
        #ques_list = ques_list.strip('][ ')
        #print(ques_list.split(','))
        questions = ast.literal_eval(ques_list)

        option_sol_dict = line[separator_index+4:]
        #print(option_sol_dict)
        option_sol = ast.literal_eval(option_sol_dict)
    

    return questions,option_sol



def start_quiz():
    questions,option_sol = fetch_quiz()

    for i in range(len(questions)):
        print(questions[i])
        options = option_sol[i+1]['options']
        answer = option_sol[i+1]['answer']
        for index,option in enumerate(options):
            print(f"{index+1}) {option}")

        choice = input(": ")
        if choice == answer:
            print("correct")
        else:
            print("incorrect")
        print("\n")


#start_quiz()




if __name__ == "__main__":
    print("Welcome")
    print("""
    1) Play Quiz
    2) Add Questions
    """)
    c = input(':')
    if c == '1':
        start_quiz()
    elif c == '2':
        add_questions()
    else:
        quit