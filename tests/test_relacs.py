import unittest
import os
from relacs import relacs as rl

class testInitRelacs(unittest.TestCase):

    def setUp(self):
        self.relObj_custom = rl.makeRelacsObject("tests/test_data/chip_seq_sample_config.custom.yaml",
                                                experiment_name="test_relacs_custom")
        self.relObj_snakepipes = rl.makeRelacsObject("tests/test_data/chip_seq_sample_config.snakePipes.yaml",
                                                experiment_name="test_relacs_snakepipes",
                                                snakePipes_config="tests/test_data/ChIP-seq.config.yaml")
    def test_get_all_bams(self):
        self.assertEqual(sorted(rl.get_all_bams(self.relObj_custom.config_yml)),
                         sorted([".".join(f_.split(".")[:-1]) for f_ in os.listdir("tests/test_data/filtered_bam/") if f_.endswith(".bam")]))
        self.assertEqual(sorted(rl.get_all_bams(self.relObj_snakepipes.config_yml)),
                         sorted([".".join(f_.split(".")[:-2]) for f_ in os.listdir("tests/test_data/filtered_bam/") if f_.endswith(".bam")]))

    def test_initAttributes(self):
        # test experiment_name attribute
        self.assertEqual(self.relObj_custom.experiment_name, "test_relacs_custom")
        self.assertEqual(self.relObj_snakepipes.experiment_name, "test_relacs_snakepipes")
        # test base_dir attribute
        self.assertEqual(self.relObj_custom.base_dir, "tests/test_data/filtered_bam")
        self.assertEqual(self.relObj_snakepipes.base_dir, "tests/test_data/")




# class testCalc(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEqual(rl.add_nums(10,5),15.0)
#         self.assertEqual(rl.add_nums(-1,1),0.0)
#         self.assertEqual(rl.add_nums(-1,-1),-2.0)
#
#     def test_divide(self):
#         self.assertEqual(rl.divide_nums(10,5),2)
#         self.assertEqual(rl.divide_nums(-1,1),-1)
#         self.assertEqual(rl.divide_nums(-1,-1),1)
#         self.assertEqual(rl.divide_nums(5,2),2.5)
#
# # test for errors to be correctly raised
#         self.assertRaises(ValueError, rl.divide_nums, 5, 0)
#         with self.assertRaises(ValueError):
#             rl.divide_nums(5, 0)
#
# class testEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.emp1 = rl.Employees("Francesco","Ferrari",1000)
#         self.emp2 = rl.Employees("ANGELICA","gRAY",1000)
#
#     def tearDown(self):
#         pass
#
#     def test_email(self):
#         self.assertEqual(self.emp1.email, "ferrari@ie-freiburg.mpg.de")
#         self.assertEqual(self.emp2.email, "gray@ie-freiburg.mpg.de")
#

if __name__ == "__main__":
    unittest.main()
