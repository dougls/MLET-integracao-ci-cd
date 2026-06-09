import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

def enviar_webhook_para_github():
    logging.info("Preparando envio de Webhook para o GitHub Actions...")
    
    # Para interagir com a API do GitHub como uma automação externa (não como um usuário UI),
    # o padrão corporativo exige um Personal Access Token (PAT) com permissões de 'repo'.
    token = os.environ.get("GITHUB_PAT")
    owner = "dougls" 
    repo = "MLET-integracao-ci-cd"
    
    # Endpoint oficial do GitHub para disparos de repositório
    url = f"https://api.github.com/repos/{owner}/{repo}/dispatches"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # O "event_type" é a senha exata que o YAML está esperando
    payload = {
        "event_type": "anomalia-detectada-retreinar",
        "client_payload": {
            "motivo": "Concept Drift crítico identificado na última hora.",
            "acuracia": "72%"
        }
    }
    
    resposta = requests.post(url, json=payload, headers=headers)
    
    if resposta.status_code == 204:
        logging.info("✅ WEBHOOK ENVIADO: A requisição foi autenticada e a esteira de treinamento foi acordada!")
    else:
        logging.error(f"❌ FALHA DE AUTENTICAÇÃO: HTTP {resposta.status_code} - {resposta.text}")

if __name__ == "__main__":
    enviar_webhook_para_github()