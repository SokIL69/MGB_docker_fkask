# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd
# import catboost
import os

dill._dill._reverse_typemap['ClassType'] = type
# import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import sklearn

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(model_path):
    # load the pre-trained model
    global model
    with open(model_path, 'rb') as f:
        model = dill.load(f)
    print(model)


# modelpath = "/home/sil/ML/Ml_in_bisiness/logreg_pipeline_v15.dill"
# modelpath = "/home/sil/ML/lesson_9/models/v_15/logreg_pipeline_v15.dill"
modelpath = "/app/app/models/logreg_pipeline_v15.dill"
load_model(modelpath)


@app.route("/", methods=["GET"])
def general():
    return """Welcome to fraudelent prediction process. Please use 'http://<address>/predict' to POST"""\



@app.route("/method1", methods=["GET"])
def method1():
    return """Test web-servis-a. Please use 'http://<address>/predict' to POST"""\



@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":

        Annual_Income, Number_of_Open_Accounts, Years_of_Credit_History, Maximum_Open_Credit, \
        Current_Loan_Amount, Current_Credit_Balance, Monthly_Debt, CreditScore_small, \
        CreditScore_large, Home_Ownership_int, Years_in_current_job_int, Purpose_int, \
        Term_int, Tax_Liens_int, Number_of_Credit_Problems_int \
            = "", "", "", "",\
              "", "", "", "",\
              "", "", "", "",\
              "", "", ""

        request_json = flask.request.get_json()

        # -------------------------------------------------------- #
        if request_json["Annual Income"]:  # 1
            Annual_Income = float(request_json['Annual Income'])

        if request_json["Number of Open Accounts"]:  # 2
            Number_of_Open_Accounts = float(request_json['Number of Open Accounts'])

        if request_json["Years of Credit History"]:  # 3
            Years_of_Credit_History = float(request_json['Years of Credit History'])

        if request_json["Maximum Open Credit"]:  # 4
            Maximum_Open_Credit = float(request_json['Maximum Open Credit'])

        if request_json["Current Loan Amount"]:  # 5
            Current_Loan_Amount = float(request_json['Current Loan Amount'])

        if request_json["Current Credit Balance"]:  # 6
            Current_Credit_Balance = float(request_json['Current Credit Balance'])

        if request_json["Monthly Debt"]:  # 7
            Monthly_Debt = float(request_json['Monthly Debt'])

        if request_json["CreditScore_small"]:  # 8
            CreditScore_small = float(request_json['CreditScore_small'])

        if request_json["CreditScore_large"]:  # 9
            CreditScore_large = float(request_json['CreditScore_large'])
        # ------------------------------------------------------- #

        if request_json["Home_Ownership_int"]:  # 10
            Home_Ownership_int = int(request_json['Home_Ownership_int'])

        if request_json["Years_in_current_job_int"]:  # 11
            Years_in_current_job_int = int(request_json['Years_in_current_job_int'])

        if request_json["Purpose_int"]:  # 12
            Purpose_int = int(request_json['Purpose_int'])

        if request_json["Term_int"]:  # 13
            Term_int = int(request_json['Term_int'])

        if request_json["Tax_Liens_int"]:  # 14
            Tax_Liens_int = int(request_json['Tax_Liens_int'])

        if request_json["Number_of_Credit_Problems_int"]:  # 15
            Number_of_Credit_Problems_int = int(request_json['Number_of_Credit_Problems_int'])

        # Purpose_int = "14"
        # Term_int = "1"
        # Tax_Liens_int = "0"
        # Number_of_Credit_Problems_int = "0"

        logger.info(f'{dt} Data:  ' +
                    f'Purpose_int={Annual_Income}, ' +
                    f'Number of Open Accounts={Number_of_Open_Accounts}, ' +
                    f'Years of Credit History={Years_of_Credit_History}, ' +
                    f'Maximum Open Credit={Maximum_Open_Credit},  Current Loan Amount={Current_Loan_Amount}, ' +
                    f'Current Credit Balance={Current_Credit_Balance}, Monthly Debt={Monthly_Debt}, ' +
                    f'CreditScore_small={CreditScore_small}, CreditScore_large={CreditScore_large}, ' +
                    f'Purpose_int={Home_Ownership_int}, Term_int={Years_in_current_job_int}, ' +
                    f'Purpose_int={Purpose_int}, Term_int={Term_int}, ' +
                    f'Tax_Liens_int={Home_Ownership_int}, Number_of_Credit_Problems_int={Years_in_current_job_int}')

        try:
            preds = model.predict_proba(pd.DataFrame({
                "Annual Income": [float(Annual_Income)],

                "Number of Open Accounts": [float(Number_of_Open_Accounts)],
                "Years of Credit History": [float(Years_of_Credit_History)],
                "Maximum Open Credit": [float(Maximum_Open_Credit)],
                "Current Loan Amount": [float(Current_Loan_Amount)],
                "Current Credit Balance": [float(Current_Credit_Balance)],
                "Monthly Debt": [float(Monthly_Debt)],
                "CreditScore_small": [float(CreditScore_small)],
                "CreditScore_large": [float(CreditScore_large)],

                "Home_Ownership_int": [int(Home_Ownership_int)],
                "Years_in_current_job_int": [int(Years_in_current_job_int)],
                "Purpose_int": [int(Purpose_int)],
                "Term_int": [int(Term_int)],
                "Tax_Liens_int": [int(Tax_Liens_int)],
                "Number_of_Credit_Problems_int": [int(Number_of_Credit_Problems_int)]}))

            # preds = model.predict_proba(pd.DataFrame({"Purpose_int": [Purpose_int],
            #                                           "Term_int": [Term_int],
            #                                           "Tax_Liens_int": [Tax_Liens_int],
            #                                           "Number_of_Credit_Problems_int": [Number_of_Credit_Problems_int]}))

        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)

        data["predictions"] = preds[:, 1][0]
        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    # port = int(os.environ.get('PORT', 8180))
    port = int(os.environ.get('PORT', 8182))
    app.run(host='0.0.0.0', debug=True, port=port)
