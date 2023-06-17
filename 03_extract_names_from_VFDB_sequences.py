import re
import csv

fasta_file = "VFDB_names_matched_for_downstream_analysis/VFDB_setA_nt.fas"
csv_file = "protein_info.csv"

# Regular expression pattern to extract strings from parentheses
pattern = r"\((.*?)\)"

# Open the CSV file in write mode
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the CSV header
    writer.writerow(["Protein Name", "String 1", "String 2", "String 3"])

    # Open the fasta file and iterate over the lines
    with open(fasta_file, "r") as fastafile:
        for line in fastafile:
            if line.startswith(">"):
                # Extract the strings from parentheses
                matches = re.findall(pattern, line)
                protein_name = line.strip()[1:]  # Remove the ">" symbol and whitespace

                # Write the protein name and extracted strings to the CSV file
                writer.writerow([protein_name] + matches[:3])
