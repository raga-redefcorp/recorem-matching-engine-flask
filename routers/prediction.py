import pickle
from flask import jsonify, make_response, request, Blueprint
from utils import format_data, verify_secret

router = Blueprint('router', __name__)

# home router
@router.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

# Sample router
@router.route("/hello", methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    secret = request.headers['secret']
    return jsonify(message='Hello from path!')

# returns a prediction percentage
@router.route("/prediction", methods=['POST'])    
@verify_secret
def get_resume_score():
    data = request.get_json()
    df = format_data(data)
    model = pickle.load(open('artifacts/rf_model.pkl', 'rb'))
    y_pred = model.predict(df[["diff_experience","skill_matching_score"]])
    y_pred_proba = model.predict_proba(df[["diff_experience","skill_matching_score"]])
    y_pred = y_pred.reshape(-1)[0]
    y_pred_proba = y_pred_proba.reshape(-1)[y_pred]
    return {'matching_percentage': y_pred_proba}

# page not found route
@router.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)