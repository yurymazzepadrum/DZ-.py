#Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
# recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".

def send_email(message,recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient or not recipient.endswith(
            ('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адреса {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адреса {recipient}')
        if sender == recipient :
            print(f'Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        elif sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')









