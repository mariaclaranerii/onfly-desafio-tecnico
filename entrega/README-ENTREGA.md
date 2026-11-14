# Entrega — Desafio Técnico Onfly

## Investigação e correções

A análise partiu das regras do `README.md` e das falhas nos testes fornecidos. As correções foram realizadas nos módulos responsáveis pelas regras de negócio e pela leitura do CSV. Também comparei a quantidade de registros da base principal com o total informado pelo relatório, identificando uma limitação que não era detectada pelos testes originais. O uso de IA como apoio à investigação e à implementação está documentado em `entrega/uso-de-ia/`.

| Arquivo | Causa raiz | Correção |
|---|---|---|
| `status_policy.py` | `NO_SHOW` era considerado faturável. | Restringir o faturamento a `CONFIRMED`. |
| `stay_calculator.py` | O cálculo considerava apenas o dia do mês. | Calcular a diferença entre datas completas e multiplicar pelo número de quartos. |
| `currency_converter.py` | A taxa era dividida e havia uso de `float`. | Multiplicar pela taxa e manter os cálculos em `Decimal`. |
| `report_builder.py` | O ranking não priorizava o maior faturamento. | Ordenar por valor decrescente e desempatar por `hotel_id` ascendente. |
| `csv_reservation_repository.py` | A leitura era interrompida após 200 registros. | Percorrer todo o CSV sem limite artificial. |

As alterações preservaram os testes originais, o contrato do CLI e o formato JSON solicitado.

## Testes adicionais

Foram criados cinco testes: leitura de mais de 200 reservas (`test_large_csv.py`), agrupamento mensal (`test_monthly_aggregation.py`), precisão monetária (`test_money_precision.py`), acumulação e desempate de hotéis (`test_hotel_aggregation.py`) e ausência de reservas confirmadas (`test_no_confirmed.py`).

## Como executar e validar

Requisitos: Python 3.11 ou superior. No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m ruff check .
$env:PYTHONPATH = "src"
python -m onfly_report --input data/exemplo-validacao.csv --rates data/taxas_cambio.csv --output output/exemplo.json
python -m onfly_report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json --top 5
```

## Resultados obtidos

- **pytest:** `10 passed in 4.45s` (cinco testes originais e cinco adicionais).
- **Ruff:** `All checks passed!`.
- **Amostra oficial:** 12 reservas, 9 confirmadas, 28 noites, total de `7566.00` BRL e diária média de `270.21` BRL; resumo em conformidade com o README original.
- **Base principal:** 300 reservas, 235 confirmadas, 1.347 noites e total de `396170.00` BRL. A execução confirmou a leitura integral dos registros.

## Uso de IA

Foi utilizado o ChatGPT como apoio técnico durante o desafio. Os registros das conversas e a declaração das atividades realizadas com e sem assistência da ferramenta estão em `entrega/uso-de-ia/`.
