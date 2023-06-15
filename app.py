from flask import Flask, render_template, request
import random

app = Flask(__name__)
answer = ""


def generate_answer():
    """生成四位數作為答案"""
    digits = list(range(10))
    random.shuffle(digits)
    # return 自動產生答案
    # return ''.join(str(d) for d in digits[:4])
    # return 手動設定答案
    return '1234'


def generate_random_number():
    digits = list(range(10))  # 創建包含0到9的列表
    random.shuffle(digits)  # 隨機打亂列表順序
    random_number = ''.join(str(d) for d in digits[:4])  # 取前四元素作為字串
    return random_number


def check_guess(guess):
    """判斷ＡＢ"""
    a = 0
    b = 0
    for i in range(4):
        if guess[i] == answer[i]:
            a += 1
        elif guess[i] in answer:
            b += 1
    return a, b


@app.route('/', methods=['GET', 'POST'])
def play_game():
    # guess_number = '1234'
    guess_number = generate_random_number()
    global answer
    if request.method == 'POST':
        guess = request.form['guess']
        a, b = check_guess(guess)
        if a == 4:
            message = "恭喜電腦猜對了！答案是：" + answer
            answer = ""  # 重置答案
        else:
            message = "上次猜猜結果：{}A{}B".format(a, b)
    else:
        answer = generate_answer()
        message = "輸入不重複四位數。"
    return render_template('game.html', message=message, guess_number=guess_number)


if __name__ == '__main__':
    app.run(debug=True)
