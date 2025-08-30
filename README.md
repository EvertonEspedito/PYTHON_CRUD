# PYTHON CRUD

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Um sistema CRUD (Create, Read, Update, Delete) completo desenvolvido em Python com interface gráfica usando Tkinter e banco de dados SQLite.

## 📋 Descrição

Sistema de gerenciamento com funcionalidades completas de CRUD para demonstração e aprendizado. Desenvolvido para estudos de programação Python com banco de dados.

## ✨ Funcionalidades

- ✅ **Create** - Adicionar novos registros
- 📖 **Read** - Visualizar e listar registros
- ✏️ **Update** - Editar registros existentes
- ❌ **Delete** - Excluir registros
- 🔍 **Busca** - Pesquisar registros específicos
- 💾 **Persistência** - Armazenamento em banco de dados SQLite

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **SQLite** - Banco de dados embutido

## 📦 Instalação

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Clonar o repositório
```bash
git clone https://github.com/EvertonEspedito/PYTHON_CRUD.git
cd PYTHON_CRUD
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

Execute o arquivo principal do sistema:

```bash
python main.py
```

Ou:

```bash
python3 main.py
```

## 📖 Como Usar

1. **Adicionar Registro**: Preencha os campos do formulário e clique em "Adicionar"
2. **Visualizar Registros**: Os registros aparecerão na lista/tabela principal
3. **Editar Registro**: Selecione um registro da lista e clique em "Editar"
4. **Excluir Registro**: Selecione um registro e clique em "Excluir"
5. **Buscar**: Use o campo de busca para filtrar registros

## 🗃️ Estrutura do Banco de Dados

O sistema utiliza SQLite com uma estrutura similar a:

```sql
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);
```

## 📁 Estrutura do Projeto

```
PYTHON_CRUD/
│
├── main.py                 # Arquivo principal da aplicação
├── utils.py                # Configuração e operações do banco de dados
├── minha_db.sqlite3        # Banco de Dados
└── README.md               # Este arquivo
```

## 🎯 Funcionalidades Técnicas

- **Validação de dados** - Campos validados antes da inserção
- **Confirmação de exclusão** - Prevenção contra exclusões acidentais

## 🔧 Personalização

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estos passos:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/NovaFuncionalidade`)
3. Adicione suas mudanças (`git add .`)
4. Comite suas mudanças (`git commit -m 'Adiciona NovaFuncionalidade'`)
5. Faça o Push da Branch (`git push origin feature/NovaFuncionalidade`)
6. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Everton Espedito**

- GitHub: [@EvertonEspedito](https://github.com/EvertonEspedito)
- LinkedIn: [Everton Espedito](https://www.linkedin.com/in/everton-espedito-3062071a3/)

## 🙌 Agradecimentos

- À comunidade Python por recursos incríveis
- A todos os contribuidores que ajudam a melhorar este projeto

---

⭐️ Se este projeto foi útil para você, deixe uma estrela no repositório!