import streamlit as st
# from src.data import load_data, build_monthly
from src.filters import sidebar_filters
from src.charts import ca_month_chart# titel select filter
from src.common import mois_fr, format_euro
import pandas as pd
import io


st.title("Analyse financiere")


df_grp =pd.read_csv("data/patio_2025_monthly.csv", encoding="utf-8")
sel_clients = sidebar_filters(df_grp)


# data treatment
df_view = df_grp[
    df_grp["departement"].isin(sel_clients)
]


# calculate total metrics
total_cvts = int(df_view["nb_cvts"].sum())
total_ca_adm = df_view["ca_adm_ht"].sum()
total_ca_alim = df_view["ca_alim_ht"].sum()
ticket_moyen =  df_view["ca_alim_ht"].sum() / int(df_view["nb_cvts"].sum()) 
c1, c2, c3, c4 = st.columns(4)



# display metrics
c1.metric("Couverts", f"{total_cvts:,}".replace(",", " "))
c2.metric("CA admission HT", format_euro(total_ca_adm))
c3.metric("CA alim HT", format_euro(total_ca_alim))
c4.metric("TM", f"{ticket_moyen:,.2f} €".replace(",", " "))

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    df_view.to_excel(writer, index=False)

st.download_button(
    "📥 Télécharger Excel",
    data=buffer.getvalue(),
    file_name="analyse_2025.xlsx",
    mime="application/vnd.ms-excel"
)


st.plotly_chart(ca_month_chart(df_view, mois_fr))

# render df 
st.dataframe(df_view.style.format({
        "nb_cvts": "{:,.0f}",
        "ca_adm_ht": "{:,.2f} €",
        "ca_alim_ht": "{:,.2f} €",
    }), width="stretch")




