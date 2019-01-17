"""
Name:       r.clip
Purpose:    Tests r.clip and its flags/options.
	
Author:     Sunveer Singh
Copyright:  (C) 2017 by Sunveer Singh and the GRASS Development Team
Licence:    This program is free software under the GNU General Public
	            License (>=v2). Read the file COPYING that comes with GRASS
	            for details.
"""
from grass.gunittest.case import TestCase

class Testrclip(TestCase):
    input='elevation'
    output='zipcodes'
    vector='lakes'

    @classmethod
    def setUpClass(cls):
        seed = 500
        cls.use_temp_region()
        cls.runModule('g.region', raster=cls.input, flags='g')
        cls.runModule('r.to.vect', input=cls.vector, output=cls.output, type="area", overwrite=True)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()


    def test_soils(self):
        soils="soils"
        self.assertModule('r.clip', input=self.input, output=self.output, overwrite=True)
        self.assertRasterMinMax(map=soils, refmin=18683, refmax=46555,
	                        msg="soils in degrees must be between 18683 and 46555")

    def test_flag(self):
        """Testing Flag"""
        self.assertModule('r.clip', input=self.input, output=self.output, flags="r", overwrite=True)

    def test_vector(self):
        """Testing With Vector Map"""
        self.assertModule('r.clip', input=self.vector, output=self.output, flags="r", overwrite=True)

    def test_where(self):
        self.assertModule('v.to.rast', layer=1,  type='line', use='val', input='zipcodes', flags='d', output=self.output, where="ZIPCODE_ID =='2'", overwrite=True)
        self.assertModule('r.mask', vector=self.output, where="ZIPCODE_ID == '2'")
        self.assertModule('r.clip', input=self.input, vector=self.output, where="ZIPCODE_ID == '2'", output='test_zipcode2')



if __name__ == '__main__':
    from grass.gunittest.main import test
    test()

