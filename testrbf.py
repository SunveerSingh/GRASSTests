"""
Name:       r.basins.fill
Purpose:    Tests r.basins.fill and its flags/options.
	
Author:     Sunveer Singh, Google Code-in 2017
Copyright:  (C) 2017 by Sunveer Singh and the GRASS Development Team
Licence:    This program is free software under the GNU General Public
	            License (>=v2). Read the file COPYING that comes with GRASS
	            for details.
"""
from grass.gunittest.case import TestCase

extract="""2  summit
3  ridge
4  shoulder
"""

class TestRasterbasin(TestCase):
    cnetwork='elevation'
    tnetwork='lakes'
    output='basinsoutput'

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster=cls.tnetwork, flags='p')
        cls.runModule('r.watershed', elevation='elevation', stream=cls.cnetwork, threshold='6', overwrite=True)
        cls.runModule('r.geomorphon', elevation=cls.tnetwork, forms=cls.tnetwork, overwrite=True)
        cls.runModule('r.category', map=cls.tnetwork, stdin=extract)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()
        
    def tearDown(cls):
        cls.runModule('g.remove', flags='f', type='raster', name=cls.output)

    def test_no1(self):
        lakes='lakes'
        self.assertModule('r.basins.fill', cnetwork=self.cnetwork, tnetwork=self.tnetwork, output=self.output, number='1')
        self.assertRasterMinMax(map=lakes, refmin=1, refmax=10,
	                        msg="lakes in degrees must be between 1 and 10")

    def test_no2(self):
        facility='facility'
        self.assertModule('r.basins.fill', cnetwork=self.cnetwork, tnetwork=self.tnetwork, output=self.output, number='4')
        self.assertRasterMinMax(map=facility, refmin=1, refmax=1,
	                        msg="facility in degrees must be between 1 and 1")

    def test_no3(self):
        slope='slope'
        self.assertModule('r.basins.fill', cnetwork=self.cnetwork, tnetwork=self.tnetwork, output=self.output, number='5')
        self.assertRasterMinMax(map=slope, refmin=0, refmax=38.68939,
	                        msg="slope in degrees must be between 0 and 38.68939")

if __name__ == '__main__':
    from grass.gunittest.main import test
    test()
