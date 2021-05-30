#This code is made by Ethan Levy and edited by Jinho Mo

#import sys method
import sys

#open class
class mathtest():

 #open method name YN
 def YN (self, answer):
   for yes in yesorno:
      if yes in answer:
         return True
      else:
         continue
   return False

 #open method name Level
 def Level (self):
    FR = [0, 0]
    num_a = 0; num_b = 0
    print('\n' +'=' * 20 +'level'+ '=' * 20)
    print('You have options of 1 to 5')
    level_str = input('Please chose your level : ')
    mathtest.stop(0, level_str)
    level_int = int(level_str)
    if level_int == 1:
       num_a = 9; num_b = 9
    elif level_int == 2:
       num_a = 99; num_b = 9
    elif level_int == 3:
       num_a = 99; num_b = 99
    elif level_int == 4:
       num_a = 999; num_b = 99
    else: num_a = 999; num_b = 999
    FR[0] = num_a
    FR[1] = num_b
    return FR

 ##open method name stop
 def stop (self, answer):
   for a in stop:
      if a in answer:
        sys.exit()
      else:
         continue
   return False

#explain the game
print('='*20 + 'Simple math test.' + '='*20)
print("This test is simple arithmetic test. The goal is get\nhighest score as you can. Good luck\n")
print('P.S. If the question comes with division, and if your\nanswer for the question is decimal; you should make your\nanswer as nearest tenth.\n')

#import random method
import random
#set score to 0
score = 0
retry = False
stop = ('STOP', 'STOp', 'STop', 'Stop', 'stop', 'stoP', 'stOP', 'sTOP', 'stOp', 'sTOp', 'sTop')
yesorno = ('yes', 'Yes', 'YEs', 'YES', 'yES', 'yeS', 'yEs', 'y', 'e', 's', 'Y', 'E', 'S')
please = "(please answer with yes or no)"
#variable for round the decimals
round_to = 1
mt = mathtest()
nums = []

#while loop for the continue the try
while(True):
   if retry == True :
      retry = False
      retry_answer = input('\nDo you want to change your level?%s\n' %please)
      mt.stop(retry_answer)
      if mt.YN(retry_answer):
         nums = mt.Level()
   else:
      nums = mt.Level()
      
   #open list name of questions
   questions = {}
   #for loop for the 10 questions
   for i in range(10):
       #while loop for the right question
       while(True):
           int_a = random.randint(0, nums[0])
           int_b = random.randint(0, nums[1])
           #if (int_a is smaller than int_b) or (int_a or int_b is 0) continue the loop.
           #else exit the loop
           if int_a < int_b or int_a == 0 or int_b == 0:
               continue
           else: break
           
       #options for the calculate question
       operators = ['+','-','*', '/']
       #randomly get a option
       operator_value = random.choice(operators)
       #make the formula
       question = str(int_a)+' '+str(operator_value)+' '+str(int_b)
       #calculate and get a answer
       answer = eval(question)
       question+=': '

       #if the calculate option is division
       if operator_value == '/':
           #make sure the answer is not decimal
           if (answer - int(answer)) != 0.0 :
               #but if the answer is decimal, get the length of digits
               length_answer = len(str(answer))
               #if answer is longer than established length change the answer to round to established length 
               if length_answer > round_to + 2 :
                   answer = round(answer, round_to)
           else :
               answer = int(answer)

        #set the list
       questions.update({question:str(answer)})

   #get the answers for user and correct tham
   for q in questions.keys():
       user_answer = input(q)
       mt.stop(user_answer)
       if questions.get(q) == str(user_answer):
           score+=1
           print('correct!')
       else:
           print('incorrect!')
           print("right answer is (%s)" %questions.get(q))
   #print final score
   print('you got '+str(score)+' correct!')
   #ask for continue to try
   user_input = input('do you want to play some more?%s\n' %please)
   mt.stop(user_input)
   if mt.YN(user_input) == True:
       retry = True
       continue
   else : break
