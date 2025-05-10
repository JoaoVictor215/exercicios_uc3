praias = []

n=int(input("Quantas praias deseja adicionar? "))

for i in range(n):
    print(f"Praia {i+1}")
    nome = input("Nome da Praia: ")
    distancia =  float(input("Distancia do centro da cidade (km): " ))
    veranistas = int(input("Número médio de veranistas na última temporada: "))
    acesso = int(input("Tipo de acesso (0 - não asfaltado, 1 - asfaltado): "))

    praias.append({
        "nome":nome,
        "distancia":distancia,
        "veranistas":veranistas,
        "acesso":acesso,
    })

praias_mais_15km = [praia for praia in praias if praia["distancia"]>15]
num_praias_mais_15km = len(praias_mais_15km)

praias_nao_asfaltadas = [praia for praia in praias if praia["acesso"] ==0]
if praias_nao_asfaltadas:
    media_veranistas_nao_asfaltadas = sum(p["veranistas"] for p in praias_nao_asfaltadas) / len(praias_nao_asfaltadas)
else:
    media_veranistas_nao_asfaltadas = 0

praias_asfaltadas_com_poucos = [(p["nome"], p["distancia"])for p in [praias] if p["acesso"] == 1 and p["veranistas"]<1000]

print("Resultados:")
print("a) Número de praias a mais de 15km do centro:", num_praias_mais_15km)
print("b) Média de veranistas nas praias com acesso não asfaltado:", round(media_veranistas_nao_asfaltadas,2))
print("c) Praias asfaltadas com menos de 1000 veranistas:")
if praias_asfaltadas_com_poucos:
    for nome, distancia in praias_asfaltadas_com_poucos:
        print(f"  - {nome},{distancia}km")
else:
    print("Nenhuma praia atende a esse critério.")
        