# KO_extract
The script facilitates the retrieval and processing of KEGG orthology (KO IDs) data from the Kyoto Encyclopedia of Genes and Genomes (KEGG) database. It specifically targets data related to organism codes, which are unique identifiers for various organisms in the KEGG database. 

# Use
1-Prepare a text file with a list of organism codes in the first column. Organism codes can be obtained from [here](https://www.genome.jp/kegg/catalog/org_list.html).  
2-Run the tool and provide the full path to the input file when prompted.  
3-The tool fetches and processes data for each code.  
4-Enter the desired path and the output file name.     

# Output
The output file includes a list of fetched "KOs" corresponding to the input organisms and can be used for downstream analysis. 
