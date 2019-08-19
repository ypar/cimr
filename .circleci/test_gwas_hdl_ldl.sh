#!/bin/bash

set -ex

cd ~/cimr/examples/gwas-tar-gz/
cimr processor -process -yaml-file hdl_ldl_cholesterol_tar_gz.yml

# Decompress the output files ("-k" option keeps the original gz file).
# Note that WE CAN NOT COMPARE TWO GZ FILES DIRECTLY, because by default a gz file
# includes the original file's name and timestamp in the header when it is generated.
# See more details at: https://github.com/greenelab/cimr-d/issues/14
gunzip -k processed_data/gwas/*.gz

# Verify de-compressed files' md5sum.
# (To disable the output message, use "--status" option.)
# If this command's return status is not zero, CircleCI will quit immediately.
md5sum --check md5.txt
