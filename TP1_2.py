import re
from collections import Counter
import matplotlib.pyplot as plt

with open("C:/Users/snicolas/Downloads/auth.log", "r") as fichier:
    lignes = fichier.readlines()

lignes_echecs = [ligne for ligne in lignes if "failed password" in ligne.lower()]

ips = []
for ligne in lignes_echecs:
    match = re.search(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", ligne)
    if match:
        ips.append(match.group(0))
for ligne in lignes:
    if "failed password" in ligne.lower():
        print(ligne.strip())

compteur_ips = Counter(ips)

top_ips = compteur_ips.most_common(5)
print("Top 5 des IPs avec le plus d’échecs de connexion :")
for ip, count in top_ips:
    print(f"{ip} : {count} tentatives échouées")

ips_labels = [ip for ip, _ in top_ips]
tentatives = [count for _, count in top_ips]

plt.figure(figsize=(10, 6))
plt.bar(ips_labels, tentatives, color='red', label="Échecs de connexion")

plt.xlabel("IP")
plt.ylabel("Nombre d’échecs")
plt.title("Top 5 des IPs avec le plus d’échecs de connexion")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
