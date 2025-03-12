def arithmetic_arranger(problems, show_answers=False):
    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        num1, operator, num2 = problem.split()

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if num1.isdigit() and num2.isdigit():
            pass

        else:
            return 'Error: Numbers must only contain digits.'

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        max_length = max(len(num1), len(num2))
        score = max_length + 2

        first_line += f"{' ' * abs(score - len(num1))}{num1}    "
        second_line += f"{operator}{' ' * abs(score - len(num2)-1)}{num2}    "
        dashes_line += '-' * score + "    "

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            elif operator == '-':
                answer = str(int(num1) - int(num2))
            answers_line += f"{' ' * abs(score - len(answer))}{answer}    "
        
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip()

    if show_answers:
        arranged_problems += '\n' + answers_line.rstrip()
    return arranged_problems
