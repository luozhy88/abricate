## get the contig fasta path
files_to_read = list.files(
  path = "/data_bk/zhiyu/pipeline_data/shotgun/sixhop_621samples", # directory to search within
  pattern = "*_final_contigs.fasta", # regex pattern, some explanation below
  recursive = TRUE,          # search subdirectories
  full.names = TRUE          # return the full path
)

## get the samples names
##
filesNames.1 <- sub(pattern = "/data_bk/zhiyu/pipeline_data/shotgun/sixhop_621samples/","",files_to_read)
filesNames.2 <- sub(pattern = "/assembly.*","",filesNames.1)



## make the sample sheet for nf-core/funcscan
contigs.samples <- data.frame( sample = filesNames.2, fasta = files_to_read) 

##
write.csv(contigs.samples, file = "samplesheet_621samples_funcscan.csv",row.names = F)