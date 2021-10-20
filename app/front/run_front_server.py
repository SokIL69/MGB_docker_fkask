import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField, FloatField
from wtforms.validators import DataRequired

import urllib.request
import json


class ClientDataForm(FlaskForm):
    # annual_income = StringField('Annual Income', validators=[DataRequired()])
    # number_of_open_accounts = StringField('Number of Open Accounts', validators=[DataRequired()])
    # years_of_credit_history = StringField('Years of Credit History', validators=[DataRequired()])
    # maximum_open_credit = StringField('Maximum Open Credit', validators=[DataRequired()])
    # current_loan_amount = StringField('Current Loan Amount', validators=[DataRequired()])
    # current_credit_balance = StringField('Current Credit Balance', validators=[DataRequired()])
    # monthly_debt = StringField('Monthly Debt', validators=[DataRequired()])
    # credit_score_small = StringField('CreditScore small', validators=[DataRequired()])
    # credit_score_large = StringField('CreditScore large', validators=[DataRequired()])
    # home_ownership_int = StringField('Home Ownership (int)', validators=[DataRequired()])
    # years_in_current_job_int = StringField('Years in current job (int)', validators=[DataRequired()])
    # purpose_int = StringField('Purpose (int)', validators=[DataRequired()])
    # term_int = StringField('Term (int)', validators=[DataRequired()])
    # tax_liens_int = StringField('Tax Liens (int)', validators=[DataRequired()])
    # number_of_credit_problems_int = StringField('Number of Credit Problems (int)', validators=[DataRequired()])

    annual_income = FloatField('Annual Income', validators=[DataRequired()])
    number_of_open_accounts = FloatField('Number of Open Accounts', validators=[DataRequired()])
    years_of_credit_history = FloatField('Years of Credit History', validators=[DataRequired()])
    maximum_open_credit = FloatField('Maximum Open Credit', validators=[DataRequired()])
    current_loan_amount = FloatField('Current Loan Amount', validators=[DataRequired()])
    current_credit_balance = FloatField('Current Credit Balance', validators=[DataRequired()])
    monthly_debt = FloatField('Monthly Debt', validators=[DataRequired()])
    credit_score_small = FloatField('CreditScore small', validators=[DataRequired()])
    credit_score_large = FloatField('CreditScore large', validators=[DataRequired()])
    home_ownership_int = IntegerField('Home Ownership (int)', validators=[DataRequired()])
    years_in_current_job_int = IntegerField('Years in current job (int)', validators=[DataRequired()])
    purpose_int = IntegerField('Purpose (int)', validators=[DataRequired()])
    term_int = IntegerField('Term (int)', validators=[DataRequired()])
    tax_liens_int = IntegerField('Tax Liens (int)', validators=[DataRequired()])
    number_of_credit_problems_int = IntegerField('Number of Credit Problems (int)', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


def get_prediction(annual_income,
                   number_of_open_accounts,
                   years_of_credit_history,
                   maximum_open_credit,
                   current_loan_amount,
                   current_credit_balance,
                   monthly_debt,
                   credit_score_small,
                   credit_score_large,
                   home_ownership_int,
                   years_in_current_job_int,
                   purpose_int,
                   term_int,
                   tax_liens_int,
                   number_of_credit_problems_int):

    body = {'Annual Income': str(annual_income),

            'Number of Open Accounts': str(number_of_open_accounts),
            'Years of Credit History': str(years_of_credit_history),
            'Maximum Open Credit': str(maximum_open_credit),
            'Current Loan Amount': str(current_loan_amount),
            'Current Credit Balance': str(current_credit_balance),

            'Monthly Debt': str(monthly_debt),
            'CreditScore_small': str(credit_score_small),
            'CreditScore_large': str(credit_score_large),

            'Home_Ownership_int': str(home_ownership_int),
            'Years_in_current_job_int': str(years_in_current_job_int),
            'Purpose_int': str(purpose_int),
            'Term_int': str(term_int),
            'Tax_Liens_int': str(tax_liens_int),
            'Number_of_Credit_Problems_int': str(number_of_credit_problems_int)
            }


    # myurl = "http://0.0.0.0:8180/predict"
    myurl = "http://0.0.0.0:8182/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    # print(jsondataasbytes)

    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['annual_income'] = request.form.get('annual_income')
        data['number_of_open_accounts'] = request.form.get('number_of_open_accounts')
        data['years_of_credit_history'] = request.form.get('years_of_credit_history')

        data['maximum_open_credit'] = request.form.get('maximum_open_credit')
        data['current_loan_amount'] = request.form.get('current_loan_amount')
        data['current_credit_balance'] = request.form.get('current_credit_balance')
        data['monthly_debt'] = request.form.get('monthly_debt')
        data['credit_score_small'] = request.form.get('credit_score_small')
        data['credit_score_large'] = request.form.get('credit_score_large')

        data['home_ownership_int'] = request.form.get('home_ownership_int')
        data['years_in_current_job_int'] = request.form.get('years_in_current_job_int')
        data['purpose_int'] = request.form.get('purpose_int')
        data['term_int'] = request.form.get('term_int')
        data['tax_liens_int'] = request.form.get('tax_liens_int')
        data['number_of_credit_problems_int'] = request.form.get('number_of_credit_problems_int')


        try:
            response = str(get_prediction(data['annual_income'],
                                          data['number_of_open_accounts'],
                                          data['years_of_credit_history'],
                                          data['maximum_open_credit'],
                                          data['current_loan_amount'],
                                          data['current_credit_balance'],
                                          data['monthly_debt'],
                                          data['credit_score_small'],
                                          data['credit_score_large'],
                                          data['home_ownership_int'],
                                          data['years_in_current_job_int'],
                                          data['purpose_int'],
                                          data['term_int'],
                                          data['tax_liens_int'],
                                          data['number_of_credit_problems_int']))

            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
    # app.run(host='0.0.0.0', port=9181, debug=True)
