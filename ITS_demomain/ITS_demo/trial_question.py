from flask import Flask, render_template, request
from fractions import Fraction
import random
import os


app = Flask(__name__)

values = [Fraction('25/8'), Fraction('17/4'), Fraction('38/7'), Fraction('29/3'), Fraction('44/5')]
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')


@app.route("/")
def question():
    operand = random.choice(values)
    print(operand)
    que = 'Express as mixed fraction : '+str(operand)+'.'
    quo = operand.numerator // operand.denominator
    rem = operand.numerator % operand.denominator
    box_ans = [quo, rem, quo, rem, operand.denominator]
    answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    hint1 = 'Try dividing numerator by denominator'
    hint2 = 'After dividing N/D, quotient ='+str(quo)+' remainder = '+str(rem)
    hint3 = 'Mixed Fraction Answer :'+str(quo)+" ("+str(rem)+"/"+str(operand.denominator)+")"
    hints = {'h1': hint1, 'h2':hint2, 'h3': hint3}
    return render_template('display.html', answer=answer, hints=hints)


@app.route('/score/<counter>', methods=['POST'])
def score(counter):
    if request.method == 'POST':
        marks = 25-(int(counter)*5)
        print(marks)
        if marks==25:
            comment="Well Done"
        elif marks==20:
            comment="You have just about mastered it"
        elif marks==15:
            comment="Keep working on it you are improving"
        else:
            comment="That's not half bad"
    else:
        print("Pass")

    result={'marks':marks,'comment':comment}
    return render_template('card.html',result=result)


app.run(debug=True)
