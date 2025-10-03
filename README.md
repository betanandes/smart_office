🎮 GameX Backend

Backend em Flask (Python 3.13.7) que simula uma plataforma de jogos digitais (GameX).
Ele fornece APIs para monitoramento de acessos, vendas e inserção de jogos por devs, além de métricas, insights e relatórios inteligentes.

📂 Estrutura do Projeto
gamex_backend/
 ├── app.py              # Servidor Flask (API principal)
 ├── gamex_data.json     # Base de dados simulada (acessos, vendas, jogos)
 └── README.md           # Documentação do projeto

⚙️ Pré-requisitos

Python 3.13.7 (Windows 11)

Pip atualizado

Ambiente virtual (venv) recomendado

🚀 Como rodar o projeto

Criar pasta e clonar/copiar os arquivos

mkdir gamex_backend
cd gamex_backend


Criar ambiente virtual

python -m venv venv
venv\Scripts\activate


Instalar dependências

pip install flask flask-cors


Rodar servidor

python app.py


Acessar endpoints no navegador ou Postman

O servidor roda em: http://127.0.0.1:5000/

📌 Endpoints da API
🔹 Módulo 1 — Métricas básicas

1. Acessos

GET /api/gamex/access


📤 Exemplo:

[{ "date": "2025-09-01", "users": 120 }]


2. Vendas

GET /api/gamex/sales


📤 Exemplo:

[{ "date": "2025-09-01", "amount": 500.0 }]


3. Jogos adicionados

GET /api/gamex/games


📤 Exemplo:

[{ "date": "2025-09-01", "dev": "Dev1", "title": "Game Alpha" }]


4. Métricas consolidadas

GET /api/gamex/metrics


📤 Exemplo:

{
  "avg_daily_users": 250.5,
  "total_sales": 32000.0,
  "avg_daily_sales": 1066.67,
  "games_added": 10
}

🔹 Módulo 2 — Monitoramento em tempo real

5. Stream de eventos

GET /api/gamex/stream


📤 Exemplo (em tempo real):

data: {"event": "new_access", "timestamp": "...", "users": 7}
data: {"event": "new_sale", "timestamp": "...", "amount": 120.0}

🔹 Módulo 3 — Análise e Insights

6. Insights

GET /api/gamex/insights


📤 Exemplo:

{
  "top_dev": { "name": "Dev1", "games_published": 3 },
  "highest_sales_day": { "date": "2025-09-30", "amount": 3500.0 },
  "access_sales_correlation": [
    { "date": "2025-09-01", "users": 120, "sales": 500.0 }
  ]
}

🔹 Módulo 4 — Relatórios Inteligentes

7. Relatório

GET /api/gamex/report


📤 Exemplo:

{
  "report": "
    📊 Relatório Inteligente da Plataforma GameX (2025-09-23)

    👥 Usuários totais no período: 8900
    👥 Média de acessos por dia: 296.67

    💰 Faturamento total: R$ 32000.0
    💵 Faturamento médio por dia: R$ 1066.67
    📈 Melhor dia de vendas: 2025-09-30 (R$ 3500.0)

    🎮 Jogos adicionados no período: 10
    🏆 Dev mais ativo: Dev1 (3 jogos publicados)

    🔎 Insights:
    - Crescimento consistente em acessos e vendas.
    - Forte correlação entre aumento de acessos e faturamento.
    - Devs ativos impulsionam diretamente as vendas.
  "
}

🧪 Roteiro rápido de testes

Abra http://127.0.0.1:5000/api/gamex/access → deve listar acessos.

Abra http://127.0.0.1:5000/api/gamex/sales → deve listar faturamento.

Abra http://127.0.0.1:5000/api/gamex/metrics → deve trazer métricas gerais.

Abra http://127.0.0.1:5000/api/gamex/insights → deve trazer dev top, dia de maior venda, correlação.

Abra http://127.0.0.1:5000/api/gamex/report → relatório completo.

Abra http://127.0.0.1:5000/api/gamex/lessons → lições aprendidas.


Teste http://127.0.0.1:5000/api/gamex/stream → verá eventos sendo emitidos a cada 5s.

📌 Próximos passos

Criar frontend (React/Angular) para consumir esses endpoints.

Integrar com Notebook Python (pandas) para análises avançadas.

Conectar com banco real (MySQL/Postgres) em vez de JSON.

Integrar IA generativa para relatórios mais inteligentes.
