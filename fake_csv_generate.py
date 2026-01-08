import random
import csv

random.seed(42)

MONTHS = [
    ("January", 1), ("February", 2), ("March", 3), ("April", 4),
    ("May", 5), ("June", 6), ("July", 7), ("August", 8),
    ("September", 9), ("October", 10), ("November", 11), ("December", 12),
]

DEPARTEMENTS = [
    "DPT-01", "DPT-02", "DPT-03", "DPT-04", "DPT-05",
    "DPT-06", "DPT-07", "DPT-08", "DPT-09", "DPT-10",
]

# name gen
PREFIX = ["Nova", "Astra", "Orion", "Helio", "Vertex", "Zenith", "Kairo", "Lumen", "Vanta", "Nexa", "Altair", "Cobalt"]
SUFFIX = ["Systems", "Group", "Industries", "Labs", "Partners", "Holdings", "Consulting", "Solutions", "Logistics", "Foods", "Services", "Digital"]

def fake_company():
    return f"{random.choice(PREFIX)} {random.choice(SUFFIX)}"

def gen_row(month_name, month_num, dept):
    nb_cvts = random.randint(90, 800)  # volume
    
    base_admin = random.uniform(3.0, 7.5)     # € / cvt
    base_alim = random.uniform(4.0, 9.5)      # € / cvt
    noise_admin = random.uniform(0.85, 1.20)
    noise_alim = random.uniform(0.85, 1.20)

    ca_adm_ht = round(nb_cvts * base_admin * noise_admin, 2)
    ca_alim_ht = round(nb_cvts * base_alim * noise_alim, 2)
    return [month_name, month_num, dept, nb_cvts, ca_adm_ht, ca_alim_ht]

def generate_csv(path="portfolio_dataset_fictif.csv", companies_per_month=25):
    # pool create
    companies = [fake_company() for _ in range(max(60, companies_per_month * 2))]


    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["mois", "month", "departement", "nb_cvts", "ca_adm_ht", "ca_alim_ht"])

        for month_name, month_num in MONTHS:
            sample = random.sample(companies, companies_per_month)
            for comp in sample:
                row = gen_row(month_name, month_num, comp)  # on met l'entreprise dans "departement"
                writer.writerow(row)

    print(f"✅ CSV generated : {path}")

if __name__ == "__main__":
    generate_csv("data/fake_checkout_reports.csv", companies_per_month=35)
