import pandas as pd

def name(x):
    cand_data = pd.read_csv("../OpenSecrets/CampaignFin16/cands16.txt", sep="\|,\|", names=['year', 'cand_id', 'com_id', 'name', 'party', 'state'], index_col=False)
    # Remove pipe from year field
    cand_data['year'] = cand_data['year'].apply(lambda x: x[1:])
    cand_data['name'] = cand_data['name'].apply(lambda x: x[:-3])
    cand_data['district'] = cand_data['state']
    cand_data['state'] = cand_data['state'].apply(lambda x: x[:2])
    cand_data = cand_data[cand_data['state'] != 'PR']
    rv = x.merge(cand_data, how='inner', left_on='CID', right_on='com_id')
    return rv
        

