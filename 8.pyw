# coding=UTF-8
# script create by Konstantyn Davidenko
# mail: kostya_ya@it-transit.com
#

"""
Magic 8 ball — шар, внешне напоминающий бильярдный шар №8, но большего размера — обычно диаметром 10-11 см,
внутри которого есть емкость с тёмной жидкостью, например, чернилами. В жидкости плавает фигура с 20 поверхностями —
икосаэдр, на каждой из которых нанесено по одному ответу.
"""
import random
import Tkinter


def choice():
    answers = {
        1: 'Бесспорно', 2: 'Предрешено', 3: 'Никаких сомнений', 4: 'Определённо да', 5: 'Можешь быть уверен в этом',
        6: 'Мне кажется — «да»', 7: 'Вероятнее всего', 8: 'Хорошие перспективы', 9: 'Да', 10: 'Знаки говорят — «да»',
        11: 'Пока не ясно, попробуй снова', 12: 'Спроси позже', 13: 'Лучше не рассказывать', 14: 'Сконцентрируйся и спроси опять', 15: 'Сейчас нельзя предсказать',
        16: 'Даже не думай', 17: 'Мой ответ — «нет»', 18: 'По моим данным — «нет»', 19: 'Перспективы не очень хорошие', 20: 'Весьма сомнительно',
    }
    return random.choice(answers)


class Eight:

    def __init__(self, root=None):
        answer_frame = Tkinter.Frame(master=root)
        answer_frame.pack()
        self.answer_label = Tkinter.Label(master=answer_frame, text='Нажмите кнопку.')
        self.answer_label.pack()
        buttons_frame = Tkinter.Frame(master=root)
        buttons_frame.pack()
        generate_button = Tkinter.Button(master=buttons_frame, text='Узнать ответ', command=self.answer)
        generate_button.pack()

    def answer(self):
        self.answer_label.config(text=choice())

if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry('200x50')
    root.title('Magic 8 ball')
    app = Eight(root)
    root.mainloop()
