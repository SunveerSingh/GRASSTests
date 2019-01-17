"""
Name:       r.random test
Purpose:    Tests r.to.vect and its flags/options.
	
Author:     Sunveer Singh, Google Code-in 2018
Copyright:  (C) 2017 by Sunveer Singh and the GRASS Development Team
Licence:    This program is free software under the GNU General Public
	            License (>=v2). Read the file COPYING that comes with GRASS
	            for details.
"""
from grass.gunittest.case import TestCase
from grass.gunittest.main import test

class Testrr(TestCase):
    input='lakes'
    cover="elevation"
    raster="routfile"
    vector="voutfile"

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster=cls.input)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()


    def test_flag_z(self):
        """Testing flag z"""
        lakes="lakes"
        self.assertModule('r.random', input=self.input, cover=self.cover, raster=self.raster, vector=self.vector, npoints=100, flags='z', overwrite=True) 
        self.assertRasterMinMax(map=lakes, refmin=18683, refmax=46555,
	                                msg="lakes in degrees must be between 18683 and 46555")

    def test_flag_i(self):
        """Testing flag i"""
        self.assertModule('r.random', input=self.input, cover=self.cover, npoints=100, flags='i')

    def test_flag_d(self):
        """Testing flag d"""
        elevation="elevation"
        self.assertModule('r.random', input=self.input, cover=self.cover, npoints=100, vector=self.vector, flags='d', overwrite=True)
        self.assertRasterMinMax(map=elevation, refmin=55.57879, refmax=156.3299,
	                                msg="elevation in degrees must be between 55.57879 and 156.3299") 

    def test_flag_b(self):
        """Testing flag b"""
        self.assertModule('r.random', input=self.input, cover=self.cover, npoints=100, vector=self.vector, flags='b', overwrite=True) 


if __name__ == '__main__':
    from grass.gunittest.main import test
    test()
