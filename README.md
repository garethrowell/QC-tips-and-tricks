# QC-tips-and-tricks

This repo contains a couple of scripts for establishing quality control (QC'ing) over datasets. There's one in R tidyverse and the other is in Python pandas.  I basically use five steps for most of my QC work: (1) load data, (2) select columns, (3) create unique lists for text data, (4) create group by counts for categorical data and (5) create histograms for numerical and dates. I re-use these basic operations over and over again.

The example data is an ecological monitoring dataset containing bird point counts by David Peitz and coworkers. It is available here: https://doi.org/10.57830/2300777









