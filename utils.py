from flask import request, abort
import pandas as pd
import os
from functools import wraps

# Formats the incoming payload for the ml model
def format_data(data):
    df = pd.DataFrame(data, index=[0])
    df['status'] = df['status'].replace([20,10],[0,1])
    df['diff_experience'] = df['min_exp'] - df['experience']    
    df["skill_matching_score"] = df['score']
    return df

# Gets the stored secret from .env
def get_secret():
    return os.getenv("MY_SECRET_KEY")

# Checks the incoming secret with the stored secret in .env for authorization
def verify_secret(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        secret = request.headers['secret']
        stored_secret = os.getenv("MY_SECRET_KEY")
        if secret != stored_secret:
            abort(401)
        return func(*args, **kwargs)
    return wrapper
