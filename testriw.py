"""
Name:       r.in.wms test
Purpose:    Tests r.in.wms and its flags/options.
	
Author:     Sunveer Singh, Google Code-in 2018
Copyright:  (C) 2018 by Sunveer Singh and the GRASS Development Team
Licence:    This program is free software under the GNU General Public
	            License (>=v2). Read the file COPYING that comes with GRASS
	            for details.
"""
from grass.gunittest.case import TestCase
from grass.gunittest.main import test


class Testrr(TestCase):
    output='outriw'

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    def test_flag_c(self):
        """Running a basic test with flag c"""
        self.assertModule('r.in.wms', url="http://wms.cuzk.cz/wms.asp", flags='c', output=self.output)

    def test_osm(self):
        """Testing OSM Data"""
        self.assertModule('r.in.wms', url="http://watzmann-geog.urz.uni-heidelberg.de/cached/osm", layers='osm_auto:all', flags='c',            			  output=self.output)

    def test_osm_overlay_wms(self):
        """Testing OSM Data"""
        self.assertModule('r.in.wms', url="http://ows.mundialis.de/services/service?", layers='OSM-Overlay-WMS', flags='c',            			          output=self.output)

    def test_cc(self):
        """Testing Countries and coastlines"""
        self.assertModule('r.in.wms', url="http://www2.demis.nl/WMS/wms.asp", layers="Countries,Borders,Coastline", flags='c',  		 	  output=self.output)



if __name__ == '__main__':
    from grass.gunittest.main import test
    test()

