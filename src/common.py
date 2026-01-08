mois_fr = {
    1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril",
    5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août",
    9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
}


def format_euro(v):
    if v >= 1_000_000:
        return f"{v/1_000_000:.1f} M€"
    if v >= 1_000:
        return f"{v/1_000:.1f} K€"
    return f"{v:.0f} €"

COLUMN_RENAME_MAP = {
    "mois": "month",
    "month": "month_id",
    "departement": "site_name",
    "nb_cvts": "guest_count",
    "ca_adm_ht": "adm_revenue_excl.VAT",
    "ca_alim_ht": "food_revenue_excl.VAT",
}

month_en = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
