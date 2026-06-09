import os

def gerar_relatorio_luta():
    # Na vida real, carregaríamos o modelo da produção (V1) e o recém-treinado (V2) 
    # e calcularíamos a acurácia usando um dataset de validação dourado (Holdout).
    
    acuracia_champion = 0.82 # O modelo velho
    acuracia_challenger = 0.89 # O modelo novo treinado pelo bot
    
    # Decisão matemática
    vencedor = "CHALLENGER (Novo Modelo)" if acuracia_challenger > acuracia_champion else "CHAMPION (Modelo Atual)"
    
    # Criando um relatório Markdown maravilhoso para o humano ler
    relatorio_md = f"""
## 🥊 Relatório de Combate: Champion vs Challenger

O Sistema Imunológico detectou falhas e treinou um modelo novo. Aqui estão os resultados da validação cruzada:

| Modelo | Papel | Acurácia | F1-Score | Status |
| :--- | :--- | :---: | :---: | :---: |
| **V1 (Produção)** | Champion 🛡️ | 82.0% | 0.80 | ❌ Derrotado |
| **V2 (Recém Treinado)** | Challenger 🗡️ | **89.0%** | **0.88** | ✅ **Vencedor** |

**Veredito da Máquina:** O {vencedor} obteve performance superior.

⚠️ **Ação Humana Requerida:** Senhor(a) Tech Lead, por favor, revise os logs. Se concordar com a máquina, aprove este Pull Request para iniciar o *deploy* em produção.
"""
    
    # Salva o texto num arquivo que o GitHub Actions vai ler no próximo passo
    with open("relatorio_pr.md", "w", encoding="utf-8") as f:
        f.write(relatorio_md)
        
    print("Relatório Markdown gerado com sucesso!")

if __name__ == "__main__":
    gerar_relatorio_luta()