"""Provides extraction functions.

Currently only supports GET from URL or local file.
"""

import io
import logging
from google.cloud import bigquery
from google.oauth2 import service_account
from google.auth.transport import requests
import pandas as pd
import requests
path = 'pragmatic-port-344220-4fde2f3d1f5e.json'
credentials = service_account.Credentials.from_service_account_file(path)
project_id = 'pragmatic-port-344220'
client = bigquery.Client(credentials= credentials,project=project_id)
logger = logging.getLogger(__name__)


def csv_from_get_request(url):
    """Extracts a data text string accessible with a GET request.

    Parameters
    ----------
    url : str
        URL for the extraction endpoint, including any query string

    Returns
    ----------
    DataFrame
    """
    r = requests.get(url, timeout=5)
    data = r.content.decode('utf-8')
    df =  pd.read_csv(io.StringIO(data), low_memory=False)
    return df


def csv_from_local(path):
    """Extracts a csv from local filesystem.

    Parameters
    ----------
    path : str

    Returns
    ----------
    DataFrame
    """
    return pd.read_csv(path, low_memory=False)

def from_big_query(table_path):
    sql = "SELECT * FROM " + table_path + " LIMIT 1000"
    df = client.query(sql).to_dataframe()
    return df 