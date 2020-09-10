# FSL to Philips DTI

[![DOI](https://zenodo.org/badge/171647493.svg)](https://zenodo.org/badge/latestdoi/171647493)

A utility that allows you to generate spherical DTI vectors that can be read into a Philips MRI scanner.

The advantages of collecting DTI data sampling a whole sphere rather than the traditional hemisphere are outlined [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/eddy). [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL) provides a useful tool for generating these spherical vectors however this isn't ideal as a. the output from this function can't be read by a Philips MRI scanner as it's in the wrong orientation and doesn't include a b-value and b. FSL can't be run on the scanner meaning you need to pre-plan your scanning sessions and can't change the number of directions on the fly. 

To solve these issues this command line utility is designed to sit in the `E:\ftp\export` directory on the scanner. When executed it asks the user how many directions they want and what b-value, it then asks if you would like to overwrite the existing `dti_vectors_input.txt` file. This may be desired as this is the file that the scanner reads new vectors in from or may be undesired if you want to keep the files for easier switching in the future. If the user decides not to overwrite the file then the file name will be unique to the number of vectors and b-value e.g. `dti_vectors_input-fsl_128_directions_bval_800.txt`. To make keeping track of potentially overwritten files, a log file is produced in the same directory to keep track of the date, time, number of directions and b-values that were generated.

Once the desired vectors are in `dti_vectors_input.txt` simply `read new file` from the directions resolution drop-down in the Philips software.

![Scanner Interface](http://alexdaniel.info/images/read_new_file.png "Scanner Interface")

A `.exe` file that can be run on the scanner can be downloaded from the [latest realase page](https://github.com/alexdaniel654/FSL_to_Philips_DTI/releases/latest).
