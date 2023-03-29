#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:07:56 2020
@author: B.Mika-Gospdoorz
Input files: .tsv quantification table with combined results from all samples
            .tsv file with annotations extracted from gff using extract_annotations_from_gff.py
Output file: *combined_quant_gene_level_annotations.tsv with gene annotations and quantification results
Description: Used to combine annotations with quantification results
"""


import pandas as pd


# function to combine annotations with quantification results
def combine_annotations_quant():
    # read quantification results
    col_names = pd.read_csv("$quantification_table", sep="\t", nrows=0).columns
    types_dict = {"$gene_attribute": str}
    types_dict.update({col: float for col in col_names if col not in types_dict})
    quantification = pd.read_csv("$quantification_table", sep="\t", index_col=0, dtype=types_dict)
    # read annotations
    annotations = pd.read_csv("$annotations_table", sep="\t", index_col=0, dtype="str")
    # combine annotations and quantification results
    quant_merged_table = pd.concat([annotations, quantification], axis=1, join="inner").sort_index()
    quant_merged_table.index.names = ["$gene_attribute"]
    # save results
    if "$organism" == "pathogen":
        quant_merged_table.to_csv("pathogen_combined_quant_annotations.tsv", sep="\t")
    elif "$organism" == "host":
        quant_merged_table.to_csv("host_combined_quant_annotations.tsv", sep="\t")


if __name__ == "__main__":
    # combine annotations with quantification results
    combine_annotations_quant()
