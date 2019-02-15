Blanks = ["__1__", "__2__", "__3__", "__4__"]
OPENING = "Welcome to simple coding quiz to enhance your Understanding of Code!"

easy_question = '''"__1__" is the most basic building block of the Web. It describes
and defines the content of a webpage along with the basic layout of the webpage. Other technologies besides HTML
are generally used to describe a web page's appearance/presentation is "__2__" or functionality/behavior would be "__3__".
"__4__" refers to links that connect web pages to one another, either within a single website or between websites.'''
easy_answers = ["html", "hypertext", "css", "javascript"]

medium_question = '''Python is a general-purpose high-level programming language. Python is both __1__ oriented and
__2__ and it can be even used in a functional style as well. Python is very fast. The source code is compiled
into __3__, so that executing the same file will be faster, if the script will be executed again.The bytecode is an
"__4__ language", which is said to run on a virtual machine that executes the machine code corresponding to each bytecode.'''
medium_answers = ["object", "imperative", "bytecode", "intermediate"]

hard_question = '''There is actually a poem written by __1__ Peters named as THE __2__ OF PYTHON which can be read by just writing
import __3__ in the interpreter. Final fun fact: Function Argument __4__ is another awesome feature of Python.'''
hard_answers = ["tim", "zen", "this", "unpacking"]


def welcome():
    '''
    Behavior: Greeting + Opening
    '''
    print(OPENING)
    name = raw_input("What is your name: ")
    print("Hello %s nice to meet you!\n" % name)


def start_game():
    """
    Behavior:
        Check to make sure user input match answers and return current question with blank filled in.
    """
    welcome()
    level_difficulty = choose_difficulty()
    problem, answers = get_problem(level_difficulty)
    current_question = 0
    while current_question < len(answers):
        print("\n" + problem + "\n")
        answered_correctly = get_user_answer(answers[current_question], current_question + 1)
        if answered_correctly:
            problem = problem.replace('__' + str(current_question + 1) + '__', answers[current_question])
            current_question += 1
            if current_question == len(answers):
                print("\n" + problem + "\n")

def get_user_answer(correct_answer, index):
    '''
    Input:
        User input for answer
    Behavior:
        Takes user input for answer and checks to make sure it's correct.
    Output:
        If user input is correct or wrong.
    '''
    answer = raw_input("Please give answer for %i\n" % index)
    if answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print("Wrong :( ")
        return False

def choose_difficulty():
    '''
    Input:
        Level Difficulty
    Behavior:
        Prompt user to choose level of game.
    output:
        None
    '''
    level_difficulty = raw_input("Choose level of difficulty? easy | medium | hard: ").lower()
    return level_difficulty

def get_problem(difficulty):
    '''
    Input:
        None
    Behavior:
        If Statement that prints short greeting and return questions based off of difficulty choice.
    Output:
        Questions & Anwers based off of difficulty choice.
    '''
    if difficulty == "easy":
        print("Great!, Easy is a great place to start.\n")
        return easy_question, easy_answers
    elif difficulty == "medium":
        print("Great!, Middle of the road")
        return medium_question, medium_answers
    elif difficulty == "hard":
        print("Great!, Let's test your knowledge")
        return hard_question, hard_answers
    else:
        print("Wrong choice. Choices are easy, medium, hard.")
        return None, None
start_game()
