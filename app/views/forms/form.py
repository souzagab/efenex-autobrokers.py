from PyInquirer import style_from_dict, Token, prompt


class FormBase:
    questions = []

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    def __init__(self):
        self.answers = None

    def render(self):
        self.answers = prompt(self.questions)

        return self.answers