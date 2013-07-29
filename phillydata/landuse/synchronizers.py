import logging

import external_data_sync
from external_data_sync.synchronizers import Synchronizer

from .adapter import find_land_use_areas


logger = logging.getLogger(__name__)


class LandUseAreaSynchronizer(Synchronizer):
    """Synchronizes LandUseAreas."""

    def sync(self, data_source):
        logger.info('Synchronizing vacant land use area data.')
        find_land_use_areas()
        logger.info('Done synchronizing vacant land use area data.')


external_data_sync.register(LandUseAreaSynchronizer)
