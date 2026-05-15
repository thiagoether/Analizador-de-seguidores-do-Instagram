import json

def carregar_usuarios(arquivo, chave=None):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        usuarios = set()

        # Se houver uma chave específica (caso de "relationships_following")
        if chave and chave in dados:
            dados = dados[chave]

        # Processar a lista de usuários
        if isinstance(dados, list):
            for item in dados:
                if "string_list_data" in item and item["string_list_data"]:
                    usuarios.add(item["string_list_data"][0]["value"])

        print(f"✅ {len(usuarios)} usuários carregados de {arquivo}")
        return usuarios

    except Exception as e:
        print(f"⚠️ Erro ao carregar {arquivo}: {e}")
        return set()

# Carregar as listas de seguidores
seguindo = carregar_usuarios('following.json', 'relationships_following')  # Quem você segue
seguidores = carregar_usuarios('followers.json')  # Quem te segue

# Verificar se as listas não estão vazias
if not seguindo:
    print("❌ A lista de pessoas que você segue está vazia ou com erro!")
if not seguidores:
    print("❌ A lista de seguidores está vazia!")

# Identificar quem não segue de volta
nao_seguem_de_volta = seguindo - seguidores

# Exibir o resultado
print("\n🚨 Pessoas que NÃO te seguem de volta:")
if nao_seguem_de_volta:
    for usuario in nao_seguem_de_volta:
        print(usuario)
else:
    print("🎉 Todos que você segue também te seguem de volta!")
