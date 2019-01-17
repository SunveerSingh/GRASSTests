"""
Name:       v.generalize test
Purpose:    Tests v.generalize and its flags/options.
	
Author:     Sunveer Singh, Google Code-in 2018
Copyright:  (C) 2018 by Sunveer Singh and the GRASS Development Team
Licence:    This program is free software under the GNU General Public
	            License (>=v2). Read the file COPYING that comes with GRASS
	            for details.
"""
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.gunittest.gmodules import SimpleModule

class Testrr(TestCase):
    input='roadsmajor'
    output='testvg'

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster=cls.input)
	
    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    def tearDown(cls):
        cls.runModule('g.remove', type='vector', flags='f', name=cls.output)

    def test_flagt(self):
        """Testing flag t with method douglas"""
        self.assertModule('v.generalize', input=self.input, output=self.output, method='douglas', threshold=1500, flags='t') 
        topology = dict(points=0, lines=355, areas=0)
	self.assertVectorFitsTopoInfo(self.output, topology)

    def test_flagl(self):
        """Testing flag l with method boyle"""
        self.assertModule('v.generalize', input=self.input, output=self.output, method='boyle', threshold=1500, flags='l') 
        topology = dict(points=0, lines=355, areas=0)
	self.assertVectorFitsTopoInfo(self.output, topology)


    def test_where(self):
        """Testing where option with method snakes"""
        self.assertModule('v.generalize', input=self.input, output=self.output, method='snakes', threshold=1500, where='cat<=200')
        topology = dict(points=0, lines=355, areas=0)
	self.assertVectorFitsTopoInfo(self.output, topology)

if __name__ == '__main__':
    from grass.gunittest.main import test
    test()
