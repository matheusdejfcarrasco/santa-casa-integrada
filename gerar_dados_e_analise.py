import csv
import random
from pathlib import Path

MESES = [
    ("01", "Jan", "Q1", "S1", 0.94),
    ("02", "Fev", "Q1", "S1", 0.90),
    ("03", "Mar", "Q1", "S1", 1.04),
    ("04", "Abr", "Q2", "S1", 1.08),
    ("05", "Mai", "Q2", "S1", 1.16),
    ("06", "Jun", "Q2", "S1", 1.22),
    ("07", "Jul", "Q3", "S2", 1.19),
    ("08", "Ago", "Q3", "S2", 1.10),
    ("09", "Set", "Q3", "S2", 1.03),
    ("10", "Out", "Q4", "S2", 1.07),
    ("11", "Nov", "Q4", "S2", 1.01),
    ("12", "Dez", "Q4", "S2", 0.92),
]

CIDADES_BAIRROS = {
    "Pompéia": [
        ("Centro", 24),
        ("Flândria", 16),
        ("Jardim JK", 14),
        ("Primavera", 13),
        ("Lacombe", 11),
        ("Bandeirantes", 10),
        ("Paulópolis (Distrito)", 7),
        ("Novo Mundo (Distrito)", 5),
    ],
    "Quintana": [
        ("Centro (Quintana)", 55),
        ("Jardim Paulista (Quintana)", 28),
        ("Portal do Sol (Quintana)", 17),
    ],
    "Herculândia": [
        ("Centro (Herculândia)", 62),
        ("Vila Nova (Herculândia)", 38),
    ],
    "Oriente": [
        ("Centro (Oriente)", 68),
        ("Jardim Morada do Sol (Oriente)", 32),
    ],
    "Marília": [
        ("Zona Oeste (Marília)", 54),
        ("Centro (Marília)", 46),
    ],
    "Tupã": [
        ("Centro (Tupã)", 60),
        ("Parque Universitário (Tupã)", 40),
    ],
}


def pick_weighted(rng: random.Random, options):
    items, weights = zip(*options)
    return rng.choices(items, weights=weights, k=1)[0]


def gerar_csv(caminho_saida: Path):
    rng = random.Random(20260419)
    cidades_pesos = [
        ("Pompéia", 64),
        ("Quintana", 13),
        ("Herculândia", 9),
        ("Oriente", 6),
        ("Marília", 5),
        ("Tupã", 3),
    ]

    registros = []
    id_counter = 1

    for mes_id, mes_nome, trim, sem, sazon in MESES:
        qtd = round(390 * sazon)
        for _ in range(qtd):
            cidade = pick_weighted(rng, cidades_pesos)
            bairro = pick_weighted(rng, CIDADES_BAIRROS[cidade])
            faixa = pick_weighted(
                rng,
                [
                    ("0 a 12 anos", 16 if mes_id in ("05", "06", "07") else 12),
                    ("13 a 17 anos", 7),
                    ("18 a 29 anos", 15),
                    ("30 a 44 anos", 21),
                    ("45 a 59 anos", 22),
                    ("60+ anos", 27),
                ],
            )
            sexo = pick_weighted(rng, [("Feminino", 56), ("Masculino", 44)])

            if faixa == "0 a 12 anos":
                serv_pesos = [
                    ("Pediatria", 46),
                    ("Pronto Atendimento / Urgência", 26),
                    ("Exames Laboratoriais", 16),
                    ("Diagnóstico por Imagem", 7),
                    ("Ortopedia e Traumatologia", 5),
                ]
            elif faixa == "60+ anos":
                serv_pesos = [
                    ("Consulta Clínica Geral", 26),
                    ("Cardiologia", 22),
                    ("Exames Laboratoriais", 22),
                    ("Diagnóstico por Imagem", 13),
                    ("Ortopedia e Traumatologia", 10),
                    ("Pronto Atendimento / Urgência", 7),
                ]
            else:
                serv_pesos = [
                    ("Consulta Clínica Geral", 27),
                    ("Exames Laboratoriais", 23),
                    ("Pronto Atendimento / Urgência", 22 if mes_id in ("05", "06") else 16),
                    ("Diagnóstico por Imagem", 12),
                    ("Ortopedia e Traumatologia", 9),
                    ("Ginecologia e Obstetrícia", 14 if sexo == "Feminino" else 1),
                    ("Cardiologia", 6),
                ]

            servico = pick_weighted(rng, serv_pesos)
            if servico == "Ginecologia e Obstetrícia":
                sexo = "Feminino"

            registros.append(
                {
                    "id": id_counter,
                    "mes": mes_id,
                    "mes_nome": mes_nome,
                    "trimestre": trim,
                    "semestre": sem,
                    "tipo_servico": servico,
                    "cidade": cidade,
                    "bairro": bairro,
                    "sexo": sexo,
                    "faixa_etaria": faixa,
                }
            )
            id_counter += 1

    with caminho_saida.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "mes",
                "mes_nome",
                "trimestre",
                "semestre",
                "tipo_servico",
                "cidade",
                "bairro",
                "sexo",
                "faixa_etaria",
            ],
            delimiter=";",
        )
        writer.writeheader()
        writer.writerows(registros)

    print(f"Base gerada com sucesso: {caminho_saida} ({len(registros)} atendimentos)")


if __name__ == "__main__":
    out_file = Path(__file__).parent / "atendimentos_santa_casa_2026.csv"
    gerar_csv(out_file)
