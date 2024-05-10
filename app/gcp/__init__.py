import json
import os

from google.cloud import bigquery


def get_bigquery_client():
    credentials = json.loads(os.environ.get("GCP_BIGQUERY_CREDENTIALS", ""))
    return bigquery.Client.from_service_account_info(credentials)
