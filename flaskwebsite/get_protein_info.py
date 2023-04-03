import requests
import pandas as pd

def get_value(key, protein_info):
    if key in protein_info:
        return protein_info[key]
    else:
        return None
    
def get_gene_name(protein_info):
    genes = get_value("genes", protein_info)
    if len(genes) > 0:
        gene_name = get_value("geneName", genes[0])
        if gene_name:
            value = get_value("value", gene_name)
            if value:
                return value
            else:
                return None
    return None

def get_description(protein_info):
    protein_description = get_value("proteinDescription", protein_info)
    if protein_description:
        recommended_name = get_value("recommendedName", protein_description)
        if recommended_name:
            full_name = get_value("fullName", recommended_name)
            if full_name:
                value = get_value("value", full_name)
                if value:
                    return value
    return None

def get_protein_info(protein_id):
    endpoint = "https://rest.uniprot.org/uniprotkb/"
    url = endpoint + protein_id + ".json"
    response = requests.get(url)
    if response.ok:
        protein_info = response.json()
        ac = get_value("primaryAccession", protein_info)
        # ac = protein_info["primaryAccession"]
        uniprot_id = get_value("uniProtkbId", protein_info)
        # protein_info["uniProtkbId"]

        gene_name = get_gene_name(protein_info)
        # gene_name = protein_info["genes"][0]["geneName"]["value"]

        description = get_description(protein_info)
        # description = protein_info["proteinDescription"]["recommendedName"]["fullName"]["value"]

        ensembl = "None"
        hgnc = "None"
        pdb_info = "False"
        pdb_id = "NA"
        gtex = "None"
        ExpresionAltas = "NA"
        
        if "uniProtKBCrossReferences" in protein_info:
            for dbReference in protein_info["uniProtKBCrossReferences"]:
                if get_value("database", dbReference) == "OpenTargets":
                    ensembl = get_value("id", dbReference)
                    gtex ="https://gtexportal.org/home/gene/"+ensembl
                elif get_value("database", dbReference) == "HGNC":
                    hgnc = get_value("id", dbReference).split(":")[1]
                elif get_value("database", dbReference) == "PDB" in protein_info["uniProtKBCrossReferences"]:
                    pdb_info = "Y"
                    pdb_id = get_value("id", dbReference)
         
        return protein_info_to_dataframe({
            "UNIPROTKB_AC": ac, 
            "UNIPROTKB_ID": uniprot_id, 
            "Gene Name": gene_name,
            "Description": description, 
            "Ensembl": ensembl, 
            "HGNC": hgnc,
            "PDB": pdb_info,
            "PDB ID": pdb_id,
            "GTEx": gtex,
            "ExpresionAltas": ExpresionAltas
            }), []
    else:
        raise Exception(f"Failed to retrieve protein information for {protein_id}")


def protein_info_to_dataframe(protein_info):
    return pd.DataFrame([protein_info])


if __name__ == "__main__":
    # Example usage:
    protein_id = "Q9Y2J0"
    # protein_id = "123"
    protein_info = get_protein_info(protein_id)
    df = protein_info_to_dataframe(protein_info)
    print(df)
