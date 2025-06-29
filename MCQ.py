print("Enter your answers, do not include anything except the answers in a long string: ABCD \n")
answers = (input())
print("Enter the mark scheme, do not include anything except the answers in a long string: ABCD \n")
markscheme = (input())

answers = list(answers.replace(" ", ""))
markscheme = (markscheme.replace(" ",""))



correct = 0
list_of_wrong = []

for i in range(len(markscheme)):
    
    if len(markscheme) != len(answers):
        print(f"Invalid answers.. Numbers of answers/ms do not add up. \n MS: {len(markscheme)} Ans: {len(answers)} ")
        break
    else:
        if markscheme[i] == answers[i]:
            print(f"Q{i+1} ✅")
            correct += 1
        else:
            print(f"Q{i+1} ❌") 
            list_of_wrong.append(f"Q{(i+1)}")
        
print(f"\n Your final mark: {correct}/{len(markscheme)}.")
print(f"Incorrect questions: {list_of_wrong}")



"""


AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA - This is 40 letters.


"""