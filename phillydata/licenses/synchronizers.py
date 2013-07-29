import logging

import external_data_sync
from external_data_sync.synchronizers import Synchronizer

from .adapter import find_licenses


logger = logging.getLogger(__name__)


class LILicensesSynchronizer(Synchronizer):
    """
    A Synchronizer that updates L&I license data.

    """
    codes = (
        '3219', # residential vacancy license
        '3634', # commercial vacancy license
    )

    def sync(self, data_source):
        logger.info('Starting to synchronize L&I license data.')
        self.update_license_data()
        logger.info('Finished synchronizing L&I license data.')

    def update_license_data(self):
        for code in self.codes:
            find_licenses(code, self.data_source.last_synchronized)


external_data_sync.register(LILicensesSynchronizer)
