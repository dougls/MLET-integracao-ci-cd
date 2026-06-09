import os
import pickle

# 1. Finge que treinou uma rede neural complexa...
print("Treinando modelo de fraude (Dummy)...")

# 2. Cria a pasta 'outputs' se ela não existir
os.makedirs('outputs', exist_ok=True)

# 3. Salva um arquivo .pkl falso para a esteira ter o que auditar
with open('outputs/modelo_fraude.pkl', 'wb') as f:
    pickle.dump({"modelo_falso": "apenas para enganar o pipeline"}, f)

print("✅ Modelo salvo com sucesso em outputs/modelo_fraude.pkl")