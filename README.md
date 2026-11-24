# LAB9 – CI/CD: Pipeline com Ambientes de Homologação e Produção

API em **Python (FastAPI)** com pipeline completo no **GitHub Actions** ([`python-app.yml`](.github/workflows/python-app.yml)), separando os ambientes de **Homologação** (deploy automático na branch `develop`) e **Produção** (deploy controlado com aprovação manual na branch `main`).

## Fluxo do Pipeline

- **`push` → `develop`**: `Build e Testes` → `Imagem Docker` → `Deploy Homologação` (automático na porta `8080`)
- **`push` → `main`**: `Build e Testes` → `Imagem Docker` → **Aprovação Manual (GitHub Environment)** → `Deploy_Producao` (porta `80`)

## Estrutura do Projeto

- `app/main.py`: API FastAPI com endpoints `/` e `/health`
- `tests/test_main.py`: Testes automatizados com `pytest`
- `Dockerfile`: Empacotamento da API na porta `8000`
- `.github/workflows/python-app.yml`: Workflow de CI/CD

## Configuração Necessária no GitHub e AWS

### 1. Branches
Garanta a existência das branches:
- `develop` (ambiente de homologação)
- `main` (ambiente de produção)

### 2. GitHub Environments (Settings → Environments)
Crie dois environments no repositório:
- **`homologacao`**: sem exigência de aprovação manual (deploy automático).
- **`producao`**: marque **Required reviewers** e adicione os aprovadores obrigatórios antes do deploy em produção.

### 3. Secrets do Repositório / Environments (Settings → Secrets and variables → Actions)

**Homologação:**
- `HOMOL_EC2_HOST`: IP ou DNS público da instância EC2 de homologação (porta `8080` liberada no Security Group)
- `HOMOL_EC2_USERNAME`: usuário SSH da instância (ex.: `ubuntu` ou `ec2-user`)
- `HOMOL_EC2_SSH_KEY`: chave privada SSH (`.pem`)

**Produção:**
- `EC2_HOST`: IP ou DNS público da instância EC2 de produção (porta `80` liberada no Security Group)
- `EC2_USERNAME`: usuário SSH da instância (ex.: `ubuntu` ou `ec2-user`)
- `EC2_SSH_KEY`: chave privada SSH (`.pem`)

> **Observação:** Ambas as instâncias EC2 devem ter o **Docker** instalado e em execução, com o usuário SSH pertencente ao grupo `docker`.

## Execução Local

```bash
pip install -r requirements.txt
pytest -v
uvicorn app.main:app --reload
```
