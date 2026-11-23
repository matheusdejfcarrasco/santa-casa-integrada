# Santa Casa Integrada — Painel de Gestão e Análise de Demanda

> **Faculdade de Tecnologia de Pompéia (FATEC Pompéia — SP)**  
> **Curso Superior de Tecnologia em Sistemas Inteligentes (2026)**  
> **Grupo Preto:** Eddy Henrique de Freitas Arrais, Leandro Moura, Matheus Carrasco, Talita Sátiro Queiroz  
> **Disciplina:** Liderança e Empreendedorismo — Prof. Antônio Cesar Dall Evedove

[![Dashboard Online](https://img.shields.io/badge/Cloudflare_Workers-Dashboard_Online-0d7a6f?style=for-the-badge)](https://dashboard.santa-casa-pompeia.workers.dev)

---

## 1. Sobre o Projeto

A **Santa Casa Integrada** é uma proposta de plataforma digital inteligente voltada ao acesso e à gestão de serviços de saúde para instituições de pequeno e médio porte, tendo como referência a **Santa Casa de Pompéia (SP)** e municípios da região.

Este repositório reúne:
- **Painel de Gestão e Dados ([`index.html`](./index.html)):** Dashboard web responsivo e interativo para exploração multidimensional dos atendimentos, incluindo módulo preditivo de Inteligência Artificial para apoio à decisão.
- **Script de Tratamento e Geração de Dados ([`gerar_dados_e_analise.py`](./gerar_dados_e_analise.py)):** Script em Python para estruturação, limpeza e geração de base de atendimentos em formato CSV compatível com fluxos em Pandas.

---

## 2. Indicadores e Análises Disponíveis no Dashboard

1. **Distribuição dos atendimentos por tipo de serviço:** comparativo em barras horizontais com volume absoluto e participação percentual.
2. **Distribuição dos atendimentos por cidade e bairro:** visão territorial dupla (municípios da região e concentração por bairros/distritos).
3. **Distribuição dos atendimentos por sexo:** gráfico de rosca (*donut*) interativo com proporção categórica.
4. **Distribuição dos atendimentos por faixa etária:** distribuição demográfica de `0 a 12 anos` até `60+ anos`.
5. **Volume de atendimentos ao longo do período analisado:** série histórica mensal com linha de tendência e projeção gerada pelo módulo de IA.
6. **Cruzamento entre dimensões (Mapa de Calor):** matriz de contingência dinâmica permitindo cruzar quaisquer dimensões em linhas e colunas (Volume, `% na Linha` e `% do Total`).

---

## 3. Lógica de Navegação e Filtros

- **Filtros Globais Combinados:** seleção por **Período** (ano completo, semestre, trimestre ou mês específico), **Tipo de Serviço**, **Cidade**, **Bairro** (com filtro em cascata conforme a cidade selecionada), **Sexo** e **Faixa Etária**.
- **Cross-filtering (Clique nos Gráficos):** clicar em qualquer barra de mês, serviço, cidade, bairro, faixa etária ou legenda de sexo aplica o filtro imediatamente a todo o painel.
- **Importação e Exportação CSV:** permite carregar uma base `.csv` própria diretamente pelo navegador (sem envio de dados sensíveis a servidores externos, em conformidade com a LGPD) e exportar o recorte filtrado.

---

## 4. Como Executar Localmente

1. Clone este repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd santa-casa-dashboard
   ```
2. Abra o arquivo [`index.html`](./index.html) diretamente em qualquer navegador web moderno.
3. *(Opcional)* Para gerar uma nova planilha `.csv` de testes com Python:
   ```bash
   python gerar_dados_e_analise.py
   ```

---

## 5. Demonstração Publicada

O painel está publicado e acessível em:  
👉 **https://dashboard.santa-casa-pompeia.workers.dev**
