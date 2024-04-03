'''
Utility functions for use by search resource objects
'''
from datetime import datetime, timedelta

def get_prior_and_current_date(num_days_prior) -> (int, int):
    current_date = datetime.now().strftime("%m/%d/%Y")
    return ((datetime.now() - timedelta(days=num_days_prior)).strftime("%m/%d/%Y"), current_date)