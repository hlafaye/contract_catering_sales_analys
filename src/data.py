# import pandas as pd
# import numpy as np
# import calendar
# from .common import mois_fr


# def load_data():
#     df = pd.read_csv("data/patio_2025_monthly.csv", encoding="latin1", sep=';')

#     # Clean data and rename cols
#     df.columns = [c.lower().strip().split(':',1)[-1] for c in df.columns]
#     num_cols = df.select_dtypes(include=np.number).columns
#     df = df.loc[:, (df != 0).any(axis=0)]

#     # datetime 

#     # df['dateticket'] = pd.to_datetime(df['dateticket'], format="%d/%m/%Y")

#     # ca alim

#     catypeart_cols = [c for c in df.columns if "catypeart" in c]
#     tva_catypeart_cols = [c for c in df.columns if "catvatypeart" in c]
#     df["ca_alim_ttc"] = df[catypeart_cols].sum(axis=1)
#     df["ca_alim_ht"] =  df['ca_alim_ttc']- df[tva_catypeart_cols].sum(axis=1)
#     df["ca_adm_ht"] = df["caadmission1"] - df["catvaadm1"]

#     df["year"] = df["dateticket"].dt.year
#     df["month"] = df["dateticket"].dt.month
#     df["month_name"] = df["month"].apply(lambda m: calendar.month_name[m])
#     df["mois"] = df["month"].map(mois_fr)
    
#     return df




# def build_monthly(df):
#     df_grp = df.groupby(["mois", "month","departement"], as_index=False).agg(
#         nb_cvts=("quantiteadmission", "sum"),
#         ca_adm_ht=("ca_adm_ht", "sum"),
#         ca_alim_ht=("ca_alim_ht", "sum"),
        
        
#         )
#     df_grp.to_csv(
#     "data/patio_2025_monthly.csv",
#     index=False,
#     encoding="utf-8"
#     )

#     return df_grp