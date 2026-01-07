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

