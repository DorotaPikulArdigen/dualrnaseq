process COMBINE_QUANT_ANNOTATIONS {
   	    label 'process_high'

	    storeDir "${params.outdir}/salmon"
	    tag "comb_annots_quant_host_salmon"

	    input:
	    file quantification_table
	    file annotation_table
	    val attribute

	    output:
	    file "host_combined_quant_annotations.tsv"

	    script:
	    template 'combine_quant_annotations.py'
	}
