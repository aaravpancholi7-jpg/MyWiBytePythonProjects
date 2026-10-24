import turtle
import random
import math



t=turtle.Turtle()

#Points
pts = 0

class WrongCommandError(Exception):
    pass

l_list = [125*(2**n) for n in range(0, -6, -1)]
clr_list = ['red', 'blue', 'green', 'magenta', 'teal', 'purple']


def square(x, y, level):

  l = l_list[level]

  t.color(clr_list[level])



  t.penup()
  t.goto(x,y)

  t.pendown()

  t.setheading(random.randint(-20,20))

 
  t.begin_fill()
  for _ in range(4):
    t.forward(l)
    t.left(90)


  #t.goto(x+l, y)
  #t.goto(x+l, y+l)
  #t.goto(x, y+l)
  #t.goto(x,y)

  t.end_fill()

  if level < 5:
    #square(x+l*3/4, y+l/4, level + 1)
    #square(x-l*1/4, y+l/4, level + 1)
    
    square(x+ 9/8*l, y - 3/4*l, level +1)
    square(x - 5/8*l, y - 3/4*l, level+1)
    #square(x+1/4*l, y -3/4*l, level + 1)

def branch(sz, level):

  if level > 0:

    if level == 1:
      t.color('green')
    else:
      t.color('brown')
    
    t.pensize(level)
    t.forward(sz)

    if level == 1:
      t.color('red')
      t.dot(5)

    t.right(30)
    branch(0.8*sz, level -1)
    t.right(-60)
    branch(0.8*sz, level -1)
    t.right(30)
    t.penup()
    t.forward(-sz)
    t.pendown()

def fibonacci(n):
  if n==0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)


#Drawing Commands
def drawing_commands_fractals(command):
    global pts
    try:
        if command == square:
            pts = pts + 1
            square(0,0,0)
        elif command == branch:
            t.setheading(90)
            pts = pts +1
            branch(100, 8)
        elif command == fibonacci:
            pts = pts +1
            print("This is a random fibonacci number: ", fibonacci(random.randint(1,20)))
        else:    
            raise WrongCommandError()
    except WrongCommandError:
        print("Something went wrong.")
        pts = pts - 1
    finally:
        print("I hope you passed this part of the test.")

def math_quiz(*nums):
    global pts
    if sum(nums) > math.prod(nums):
      pts = pts + 1
    else:
        material = {"allnums": list(nums), "sum": sum(nums), "product": math.prod(nums), "average": sum(nums) / len(nums) if nums else 0}
 
    

        questions = {
            "sum": "What is the sum of all these numbers? ",
            "product": "What is the product value? ",
            "average": "What is the average of these numbers in the list? "
        }

        for category, question_text in questions.items():
            correct_answer = material[category]
            
            while True:
                inpt = input(question_text).strip()
                try:
        
                    user_answer =float(inpt)
                    break
                except ValueError:
                    print("Invalid input. Please type a valid number.")
            
            #Find answer
            if user_answer == correct_answer:
                print("Correct!")
                pts += 1
            else:
                print(f" Incorrect. The correct answer was {correct_answer}.\n")
                

        print(f"You scored {pts}/{len(questions)}.")
        
        return material  

def evaluate():
    global pts
    if pts >2:
        print("You passed! You get an A!")
        print("")
    else:
        print("You failded! You get an F!")
        print("")

print("Welcome to your Python and Math skills test!")
print("I am Dr. Joe, and you will be taking this test for a summative grade.")
print("There are more instructions on the README1 file. May luck be on your side!")


      
 

