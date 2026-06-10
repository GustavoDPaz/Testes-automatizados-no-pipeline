# Testes Automatizados no Pipeline de CI

Este repositório contém uma aplicação Python simples com testes unitários automatizados e cobertura de código integrada a um workflow de Integração Contínua (CI) com GitHub Actions.

## Estrutura do Projeto

* `src/calculator.py`: Funções matemáticas de soma e subtração.
* `tests/test_calculator.py`: Quatro testes unitários testando as funções com números positivos e negativos.
* `requirements.txt`: Dependências necessárias (pytest e pytest-cov).
* `.github/workflows/tests.yml`: Configuração do pipeline do GitHub Actions.

## Como Instalar as Dependências

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   * Windows:
     ```bash
     venv\Scripts\activate
     ```
   * Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências listadas no requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar os Testes Localmente

Com o ambiente virtual ativo, execute o comando abaixo para rodar os testes e gerar o relatório de cobertura:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=70
```

## Como Interpretar os Resultados da Aba Actions

Ao abrir a aba **Actions** no repositório do GitHub e selecionar uma execução do workflow, você verá:
1. O status geral do pipeline (verde para sucesso, vermelho para falha).
2. O passo `Run tests with coverage validation` detalhado nos logs do job `build-and-test`.
3. Uma tabela no terminal mostrando o percentual de cobertura de cada arquivo dentro da pasta `src/`. Se alguma linha não tiver sido testada, ela será listada sob a coluna `Missing`.

## Cobertura Atingida pelo Projeto

O projeto atingiu **100% de cobertura** de código nas funções da pasta `src/`, atendendo com folga a meta mínima de 70% estabelecida no pipeline.
