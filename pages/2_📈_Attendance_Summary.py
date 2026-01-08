import streamlit as st
# from src.data import load_data, build_monthly
from src.filters import sidebar_filters
from src.charts import ca_month_chart, ca_freq_chart
from src.common import mois_fr, COLUMN_RENAME_MAP, month_en, format_euro
import pandas as pd
import io

st.title("Attendance Summary")

df_grp = pd.read_csv("data/fake_checkout_reports.csv", encoding="utf-8")
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
c1.metric("Guest Count", f"{total_cvts:,}".replace(",", " "))
c2.metric("Adm Revenue excl. VAT", format_euro(total_ca_adm))
c3.metric("Food Revenue excl. VAT", format_euro(total_ca_alim))


buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    df_view.to_excel(writer, index=False)
    

st.download_button(
    "📥 Download Excel",
    data=buffer.getvalue(),
    file_name="analyse_2025.xlsx",
    mime="application/vnd.ms-excel"
)

st.plotly_chart(ca_freq_chart(df_view, month_en))

df_view = df_view.rename(columns=COLUMN_RENAME_MAP)
df_view.drop(columns=["month_id"], axis=1, inplace=True)
# render df 
st.dataframe(df_view.style.format({
        "guest_count": "{:,.0f}",
        "adm_revenue_excl.VAT": "{:,.2f} €",
        "food_revenue_excl.VAT": "{:,.2f} €",
    }), width="stretch")




