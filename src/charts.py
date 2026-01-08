import plotly.express as px

def ca_month_chart(df_view, mois_fr):
    # create plotly chart
    df_curve = df_view.groupby("month", as_index=False)[["ca_adm_ht", "ca_alim_ht"]].sum()
    df_curve["ca_total_ht"] = df_curve["ca_adm_ht"] + df_curve["ca_alim_ht"]
    df_curve = df_curve.sort_values("month")
    df_curve["food_incomes"] = df_curve["ca_alim_ht"]
    df_curve["adm_incomes"] = df_curve["ca_adm_ht"]


    # version "long" pour 3 lignes sur le même graphe
    df_long = df_curve.melt(
        id_vars="month",
        value_vars=["adm_incomes", "food_incomes"],
        var_name="type",
        value_name="amount"
    )

    fig = px.line(df_long, x="month", y="amount", color="type", markers=True)
    fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(1, 13)),
        ticktext=[mois_fr[m] for m in range(1, 13)]
    )
    return fig


def ca_freq_chart(df_view, mois_fr):
    # create plotly chart
    df_curve = df_view.groupby("month", as_index=False)[["nb_cvts"]].sum()
    df_curve = df_curve.sort_values("month")
    df_curve["Guest_Count"] = df_curve["nb_cvts"] 


    # version "long" 
    df_long = df_curve.melt(
        id_vars="month",
        value_vars=["Guest_Count"],
        var_name="type",
        value_name="guest count"
    )

    fig = px.line(df_long, x="month", y="guest count", color="type", markers=True)
    fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(1, 13)),
        ticktext=[mois_fr[m] for m in range(1, 13)]
    )
    return fig