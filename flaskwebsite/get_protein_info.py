import requests
import pandas as pd

def get_value(key, protein_info):
    if key in protein_info:
        return protein_info[key]
    else:
        return None
    
def get_gene_name(protein_info):
    genes = get_value("genes", protein_info)
    if genes and len(genes) > 0:
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

        prot_dict = {}
        ac = get_value("primaryAccession", protein_info)
        prot_dict["UNIPROTKB_AC"] = ac
        # ac = protein_info["primaryAccession"]
        prot_dict["UNIPROTKB_ID"] = get_value("uniProtkbId", protein_info)
        # protein_info["uniProtkbId"]

        prot_dict["GENE_NAME"] = get_gene_name(protein_info)
        # gene_name = protein_info["genes"][0]["geneName"]["value"]

        prot_dict["DESCRIPTION"] = get_description(protein_info)
        # description = protein_info["proteinDescription"]["recommendedName"]["fullName"]["value"]

        prot_dict["ENSEMBL"] = "None"
        prot_dict["HGNC"] = "None"
        prot_dict["PDB"] = "False"
        prot_dict["PDB_ID"] = "NA"
        prot_dict["GTEX"] = "None"
        prot_dict["EXPRESSION_ATLAS"] = "NA"
        hpa_val = None
        
        if "uniProtKBCrossReferences" in protein_info:
            for dbReference in protein_info["uniProtKBCrossReferences"]:
                if get_value("database", dbReference) == "OpenTargets":
                    prot_dict["ENSEMBL"] = get_value("id", dbReference)
                    prot_dict["GTEX"] ="https://gtexportal.org/home/gene/"+prot_dict["ENSEMBL"]
                elif get_value("database", dbReference) == "HGNC":
                    prot_dict["HGNC"] = get_value("id", dbReference).split(":")[1]
                elif get_value("database", dbReference) == "PDB":
                    prot_dict["PDB"] = "True"
                    prot_dict["PDB_ID"] = get_value("id", dbReference)
                elif get_value("database", dbReference) == "HPA":
                    for item in get_value("properties", dbReference):
                        if get_value("key", item) == "ExpressionPatterns":
                            hpa_val = get_value("value", item)

        if hpa_val and prot_dict["ENSEMBL"] != "None" and prot_dict['GENE_NAME']: 
            prot_dict["EXPRESSION_ATLAS"] = f"https://www.proteinatlas.org/{prot_dict['ENSEMBL']}-{prot_dict['GENE_NAME']}/tissue"
        

        # protein_df = info_to_dataframe({
        #     "UNIPROTKB_AC": ac, 
        #     "UNIPROTKB_ID": uniprot_id, 
        #     "Gene Name": gene_name,
        #     "Description": description, 
        #     "Ensembl": ensembl, 
        #     "HGNC": hgnc,
        #     "PDB": pdb_info,
        #     "PDB ID": pdb_id,
        #     "GTEx": gtex,
        #     "ExpresionAltas": ExpresionAltas
        #     })
        protein_df = info_to_dataframe(prot_dict)
         
        pubs_df_list = []
        for pub in protein_info["references"]:
            citation = get_value("citation", pub)
            if citation:
                pub_name = get_value("title", citation)
                pub_id = get_value("id", citation)

                author_l = get_value("authors", citation)
                if author_l:
                    authors = ', '.join(author_l)
                else:
                    authors = ', '.join(get_value("authoringGroup", citation))

                pub_df = info_to_dataframe({
                    "UNIPROTKB_AC": ac, 
                    "PUBLICATION_NAME": pub_name,
                    "PUBLICATION_ID": pub_id,
                    "AUTHORS": authors,
                    "SCORE": -1
                })
                pubs_df_list.append(pub_df)


        return protein_df, pubs_df_list
    else:
        raise Exception(f"Failed to retrieve protein information for {protein_id}")


def info_to_dataframe(protein_info):
    return pd.DataFrame([protein_info])


if __name__ == "__main__":
    # Example usage:
    protein_id = "Q9Y2J0"
    # protein_id = "123"
    protein_info = get_protein_info(protein_id)
    df = info_to_dataframe(protein_info)
    print(protein_info[0])
