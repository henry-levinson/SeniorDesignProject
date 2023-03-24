import requests
import pandas as pd

def get_protein_info(protein_id):
    endpoint = "https://www.uniprot.org/uniprot/"
    url = endpoint + protein_id + ".json"
    response = requests.get(url)
    if response.ok:
        protein_info = response.json()
        ac = protein_info["primaryAccession"]
        uniprot_id = protein_info["uniProtkbId"]
        gene_name = protein_info["genes"][0]["geneName"]["value"]
        description = protein_info["proteinDescription"]["recommendedName"]["fullName"]["value"]
        ensembl = None
        hgnc = None
        pdb_info = "False"
        pdb_id = "NA"
        gtex = "https://gtexportal.org/home/gene/"
        for dbReference in protein_info["uniProtKBCrossReferences"]:
            if dbReference["database"] == "OpenTargets":
                ensembl = dbReference["id"]
                gtex += ensembl

            elif dbReference["database"] == "HGNC":
                hgnc = dbReference["id"].split(":")[1]
            elif dbReference["database"] == "PDB" in protein_info["uniProtKBCrossReferences"]:
                pdb_info == "Y"
                pdb_id = dbReference["id"]
            
        return {"UniProtKB AC": ac, 
                "UniProtKB ID": uniprot_id, 
                "Gene Name": gene_name,
                "Description": description, 
                "Ensembl": ensembl, 
                "HGNC": hgnc,
                "PDB": pdb_info,
                "PDB ID": pdb_id,
                "GTEx": gtex
                }
    else:
        raise Exception(f"Failed to retrieve protein information for {protein_id}")

def protein_info_to_dataframe(protein_info):
    return pd.DataFrame([protein_info])

# Example usage:
protein_id = "Q9Y2J0"
protein_info = get_protein_info(protein_id)
df = protein_info_to_dataframe(protein_info)
print(df)