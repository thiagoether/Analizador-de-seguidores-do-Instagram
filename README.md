# 📊 Analisador de Seguidores do Instagram

Uma ferramenta simples e eficiente em Python para descobrir quem não te segue de volta no Instagram, utilizando os arquivos JSON exportados da própria plataforma.

⚠️ **Seguro e Privado:** Este script não pede sua senha e não faz login no Instagram. Ele analisa apenas os dados locais que você baixou.

## 🚀 Status do Projeto
✅ Concluído & Funcional

## ✨ Funcionalidades
O projeto possui duas versões para você escolher como quer ver o resultado:
1. **Exibição no Console:** Compara as listas e mostra os nomes diretamente na tela.
2. **Exportação para TXT:** Compara as listas e salva o resultado automaticamente em um arquivo de texto.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **JSON** (Biblioteca nativa)

## 📋 Pré-requisitos
Antes de começar, você vai precisar:
1. Ter o **Python 3** instalado na sua máquina.
2. Baixar seus dados do Instagram em formato **JSON** (Central de Contas > Baixar suas informações).

## 🔧 Instalação e Configuração

1. Clone este repositório:
```bash
git clone https://github.com
```

2. Entre na pasta do projeto:
```bash
cd nome-do-repositorio
```

3. Cole os arquivos JSON do seu Instagram (`followers_1.json` e `following.json`) dentro desta mesma pasta.

## 💻 Como Usar

### Opção 1: Ver o resultado apenas no terminal
Execute o script que exibe os dados diretamente no console:
```bash
python seguidores_console.py
```

### Opção 2: Salvar o resultado em um arquivo de texto
Execute o script que gera o relatório em formato `.txt`:
```bash
python seguidores_export.py
```
*Um arquivo chamado `user_list.txt` (ou o nome definido no seu script) será criado na mesma pasta.*

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

## 📝 Licença
Este projeto está sob a licença MIT.
