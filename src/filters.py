import streamlit as st

def sidebar_filters(df_grp):
    st.sidebar.header("Filtres")
    

    clients = sorted(df_grp["departement"].dropna().unique())
    sel_clients = st.sidebar.multiselect(
        "Clients",
        clients,
        default=clients, width="stretch"
    )

    return sel_clients





