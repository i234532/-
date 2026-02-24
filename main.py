questions = {
    'Сколько плнет в Солнечной системе ?': "8",
    'столица Франии?': "париж"
}
score = 8

for q, a in questions.items():
    user_answer = input(q + '')
    if user_answer.lower() == a.lower():
        print('правильно')
        score += 1
    else:
        print('Неверно!')
print(f'Ваш результат: {score} из {len(questions)}')