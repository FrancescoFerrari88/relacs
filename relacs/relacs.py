"""

logic of relacs module:

tasks to perform:

1. compute RELACS scaling factors (either from total number of reads or from a set of bed regions)
 - compute various kinds of scaling factors (RLE (deseq2), and other deeptools SF)
2. plot scalign factor heatmap for a given mark
3. plot locus specific MA plots between two conditions

How to implement this:

1. Create a RELACS object (class). The object is initialized using the yml config file for the ChIP-seq snakePipe.
2. method get_relacs_scaling_factors(bed_file=None, **kwargs) --> compute relacs scaling factors. By default, sf
are computed using the total number of reads mapped to each sample according to specific constraints
(see deeptools.countReadsPerBin). If a bed file is specified, the sf are computed based on the number of reads
mapping to the bed regions.

"""

import os
import yaml
import logging
from deeptools.countReadsPerBin import CountReadsPerBin as crpb


def process_yaml(config_yml, key_name=None):
    """
    Import yaml file. If key_name is provided, return value associated with key_name
    otherwise, return the whole file content.
    """
    try :
        with open(config_yml, 'r') as config:
            dict_config = yaml.safe_load(config)
        if key_name:
            return dict_config[key_name]
        else:
            return dict_config
    except Exception as exe:
        print("Something is wrong with your config file: {}".format(exe))

def get_all_bams(config_dict):
    all_bams = list(set([sample for sample in config_dict.keys()])) + \
                list(set(config_dict[sample]["control"] for sample in config_dict.keys()))
    return all_bams


def check_format_yaml():
    # TODO: check that config_yml provided is in in the correct format
    pass


class makeRelacsObject:

    def __init__(self, config_yml, experiment_name="GenericRelacsObject", snakePipes_config=None):
        """ initializer of relacs object """
        # 2. check that bam files exist and are indexed
        self.experiment_name = experiment_name
        self.config_yml = process_yaml(config_yml,"chip_dict")
        self.snakePipes_config = snakePipes_config
        if snakePipes_config:
            self.base_dir = process_yaml(snakePipes_config, "outdir")
            self.check_paths()
        else:
            self.base_dir = process_yaml(config_yml,"base_dir")
            self.check_paths()

    def check_paths(self):

        all_bam_files = get_all_bams(self.config_yml)

        if self.snakePipes_config:
            file_list = [os.path.join(self.base_dir, "filtered_bam/{}.filtered.bam".format(sample)) for sample in all_bam_files]
        else:
            file_list = [os.path.join(self.base_dir, "{}.bam".format(sample)) for sample in all_bam_files]

        ### check that bam files are present
        check_file_path = [os.path.isfile(f_) for f_ in file_list]
        if all(check_file_path):
            # make logging info
            print("all bam files are present")
        else:
            print("some files are not present: {}".format([file_list[i] for i, val in enumerate(check_file_path) if not val]))

        ### check that indices are present
        check_presence_indices = [os.path.isfile("{}.bai".format(f_)) for f_ in file_list]
        if all(check_file_path):
            # TODO: substitute print statments with proper logging
            print("all indexes are present")
        else:
            print("some files indexes are not present: {}".format(["{}.bai".format(file_list[i]) for i, val in enumerate(check_file_path) if not val]))




        # make sure paths exist







    def __repr__(self):
        return self.experiment_name

    def __str__(self):
        return self.experiment_name

    def as_dataFrame(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
