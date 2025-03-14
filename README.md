# QC-tips-and-tricks

This repo contains a couple of very simple scripts for establishing quality control (QC'ing) over datasets. I've included two scripts, one in R tidyverse and the other in Python pandas.  These scripts are based on the following five steps to quickly locate problems in datasets: (1) load data, (2) select columns, (3) create unique lists for text data, (4) create group by counts for categorical data and (5) create bar charts for date, integer and continuous numeric data. The bar charts for date and integer are counts histograms while the bar chart for continuous data is a binned continuous histogram. Everything else I do for QCind data is just an extension of these five steps.

The example data is an ecological monitoring dataset containing bird point counts by David Peitz and coworkers. It is available here: https://doi.org/10.57830/2300777









