# this script is used to format the VFDB format into Abricate format
# (https://github.com/tseemann/abricate#making-your-own-database) download the lasted vfdb nt
# sequences http://www.mgc.ac.cn/VFs/download.htm only need to change the
# fasta_file and output_file according to your preference

# then run this script "python vfdb_names_2_abricate_format.py"

import re

fasta_file = 'VFDB_names_matched_for_downstream_analysis/VFDB_setB_nt.fas'
output_file = 'db/VFDB_output.fasta'
prefix = 'vfdb~~~'
suffix = '~~~'

with open(fasta_file, 'r') as input_file, open(output_file, 'w') as output:
    for line in input_file:
        if line.startswith('>'):
            line = line.strip()
            header = line[1:]  # Remove the ">" symbol
            match = re.search(r'\((.*?)\)', header)  # Extract string within the first parenthesis
            if match:
                extracted_string = match.group(1)
                new_header = f'>{prefix}{extracted_string}{suffix}{header}'
                output.write(new_header + '\n')
        else:
            output.write(line)
