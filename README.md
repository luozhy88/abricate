# abricate
1. run docker version of abricate  
2. download the docker version from https://quay.io/repository/biocontainers/abricate  
3. docker pull quay.io/biocontainers/abricate:1.0.1--ha8f3691_1  
4. mount the local folder to the container folder following the commands below  

docker run -it -v /data/zhiyu/software/abricate/test:/mnt/Desktop 83bf731c4d47  

5. now you can do anything with abricate, including make custom database and running files  
5a. vfdb_names_2_abricate_format.py  
5b. https://github.com/tseemann/abricate#making-your-own-database  
5c. Run the "atlas_output_2_funcscan_samplesheet.R" to get all contigs names and paths in the css file.  
5d. All contigs output from atlas can be copied to the same folder for step 6, and the script is placed in the current folder as well, please check and run.  
6. abricate --db VFDB --datadir /mnt/Desktop/db --threads 160 ./samples_contings/*.fasta > results.tab  
7. abricate --summary results.tab > summary.tab  
8. run "03_extract_names...py" script to get names-matched table for downstream analysis, e.g. category  
