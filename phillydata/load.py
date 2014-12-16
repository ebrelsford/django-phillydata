import os

from django.conf import settings


def get_processed_data_dir():
    """
    Get the processed data directory, which can be configured by setting
    PHILLYDATA_PROCESSED_DATA_DIR in your settings. Defaults to './processed/'.
    """
    processed_data_dir = None
    try:
        processed_data_dir = settings.PHILLYDATA_PROCESSED_DATA_DIR
    except AttributeError:
        pass
    if not processed_data_dir:
        processed_data_dir = os.path.join(os.path.dirname(__file__), 'processed')
    return processed_data_dir


def get_processed_data_file(name):
    """
    Get the processed data file with the given name.
    """
    return os.path.join(get_processed_data_dir(), name)
