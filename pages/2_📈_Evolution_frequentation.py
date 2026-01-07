import streamlit as st
# from src.data import load_data, build_monthly
from src.filters import sidebar_filters
from src.charts import ca_month_chart, ca_freq_chart
from src.common import mois_fr
import pandas as pd
import io

st.title("Statistiques de frequentation")

df_grp = pd.read_csv("data/patio_2025_monthly.csv", encoding="utf-8")
print(df_grp.head())
sel_clients = sidebar_filters(df_grp)

print(df_grp.columns.to_list())
# data treatment
df_view = df_grp[
    df_grp["departement"].isin(sel_clients)
]



# calculate total metrics
total_cvts = int(df_view["nb_cvts"].sum())
total_ca_adm = df_view["ca_adm_ht"].sum()
total_ca_alim = df_view["ca_alim_ht"].sum()

c1, c2, c3 = st.columns(3)


# display metrics
c1.metric("Couverts", f"{total_cvts:,}".replace(",", " "))
c2.metric("CA admission HT", f"{total_ca_adm:,.2f} €".replace(",", " "))
c3.metric("CA alim HT", f"{total_ca_alim:,.2f} €".replace(",", " "))


buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    df_view.to_excel(writer, index=False)

st.download_button(
    "📥 Télécharger Excel",
    data=buffer.getvalue(),
    file_name="analyse_2025.xlsx",
    mime="application/vnd.ms-excel"
)

st.plotly_chart(ca_freq_chart(df_view, mois_fr))

# render df 
st.dataframe(df_view.style.format({
        "nb_cvts": "{:,.0f}",
        "ca_adm_ht": "{:,.2f} €",
        "ca_alim_ht": "{:,.2f} €",
    }), width="stretch")




