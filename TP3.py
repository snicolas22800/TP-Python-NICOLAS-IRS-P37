import pandas as pd
import re
import matplotlib.pyplot as plt

def parse_line(line):
    pattern = r'^(\S+) - - \[(.*?)\] "(\S+) (.*?) HTTP/[\d.]+" (404) "(.*?)"$'
    match = re.match(pattern, line)
    if match:
        ip = match.group(1)
        datetime = match.group(2)
        method = match.group(3)
        url = match.group(4)
        status = int(match.group(5))
        user_agent = match.group(6)
        return [ip, datetime, method, url, status, user_agent]

parsed_data = []
with open("C:/Users/snicolas/Downloads/access.log", "r") as f:
    for line in f:
        result = parse_line(line)
        if result:
            parsed_data.append(result)

df = pd.DataFrame(parsed_data, columns=["ip", "datetime", "method", "url", "status", "user_agent"])

df_404 = df[df["status"] == 404]
print(f"Nombre total d'erreurs 404 : {len(df_404)}")

print("\nLignes contenant des erreurs 404 :")
print(df_404.to_string(index=False))

top_ips = df_404["ip"].value_counts().head(5)
print("Top 5 des IPs générant le plus d'erreurs 404 :")
print(top_ips)

if top_ips.empty:
    print("Aucune erreur 404 détectée")
else:
    plt.figure(figsize=(10,6))
    top_ips.plot(kind="bar", color="tomato")
    plt.title("Top 5 des IPs responsables d'erreurs 404")
    plt.xlabel("IP")
    plt.ylabel("Nombre d'erreurs 404")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()