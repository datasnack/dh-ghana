import re
import os
import datetime as dt

import numpy as np

from datalayers.datasources.tiff_layer import TiffLayer
from datalayers.datasources.base_layer import LayerTimeResolution

class ChirtsMaxt(TiffLayer):

    def __init__(self):
        super().__init__()
        self.time_col = LayerTimeResolution.DAY
        self.manual_nodata = -9999

    def download(self):
        start_date = dt.date(2015, 1, 1)
        end_date = dt.date(2016, 12, 31) # last date available for data source

        base_url = 'http://data.chc.ucsb.edu/products/CHIRTSdaily/v1.0/global_tifs_p05/Tmax/{year}/Tmax.{year}.{month:02d}.{day:02d}.tif'

        # download all required files
        for date in self.date_range(start_date, end_date):
            url = base_url.format(year=date.year, month=date.month, day=date.day)
            self._save_url_to_file(url)

    def date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)+1):
            yield start_date + dt.timedelta(n)

    def consume(self, file, band, shape):
        x = re.search(r'([0-9]{4})\.([0-9]{2})\.([0-9]{2})\.tif', os.path.basename(file))
        date = dt.date(int(x[1]), int(x[2]), int(x[3]))

        self.rows.append({
            'date': date,
            'shape_id':      shape.id,
            'value':         np.nanmean(band),
            'value_min':     np.nanmin(band),
            'value_max':     np.nanmax(band),
            'value_std_dev': np.nanstd(band),
        })
