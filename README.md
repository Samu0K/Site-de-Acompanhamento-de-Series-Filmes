# 🎬 Site de Acompanhamento de Séries e Filmes

Um site para acompanhar lançamentos, categorias e conteúdos salvos de séries e filmes, com sistema de rastreamento de episódios e banco de dados de usuário.

---

## 📋 Sobre o Projeto

Este projeto é uma aplicação web que permite ao usuário acompanhar séries e filmes, organizar conteúdos por categorias, salvar títulos favoritos e monitorar o progresso de episódios assistidos. O sistema conta com um backend em Python e armazenamento local via SQLite.

---

## 🚀 Funcionalidades

- 📺 **Acompanhamento de episódios** — marque episódios como assistidos e acompanhe seu progresso
- 🆕 **Lançamentos** — visualize os novos lançamentos de séries e filmes
- 🗂️ **Categorias** — navegue por categorias para encontrar conteúdos do seu interesse
- 🔖 **Salvos** — salve títulos para assistir mais tarde
- 👤 **Banco de dados de usuário** — preferências e histórico armazenados localmente

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| HTML | Estrutura das páginas |
| CSS | Estilização e layout |
| JavaScript | Interatividade no frontend |
| Python | Scripts de backend / processamento |
| SQLite | Banco de dados local |

---

## 📁 Estrutura do Projeto
Site-de-Acompanhamento-de-Series-Filmes/
│
├── Home/                                             # Arquivos da página inicial
├── Site com Sistema de Acompanhamento de episodios/  # Módulo de rastreamento de episódios
├── Banco de Dados/                                   # Scripts e configurações do banco de dados
│
├── index.html                                        # Página principal
├── home.css                                          # Estilos globais
├── script.js                                         # Lógica do frontend
├── scrip.py                                          # Script Python de apoio
│
├── banco_de_dados.db                                 # Banco de dados de conteúdos
├── banco_de_dados_de_usuario.db                      # Banco de dados de usuários
│
└── README.md

---

## ⚙️ Como Executar

### Pré-requisitos

- Navegador web moderno (Chrome, Firefox, Edge...)
- Python 3.x instalado (para os scripts de backend)

### Passos

1. **Clone o repositório:**
```bash
   git clone https://github.com/Samu0K/Site-de-Acompanhamento-de-Series-Filmes.git
```

2. **Acesse a pasta do projeto:**
```bash
   cd Site-de-Acompanhamento-de-Series-Filmes
```

3. **Abra o arquivo principal no navegador:**
```bash
   # Basta abrir o index.html diretamente no navegador, ou usar uma extensão como Live Server no VS Code
```

4. **(Opcional) Execute o script Python se necessário:**
```bash
   python scrip.py
```

---

## 🗄️ Banco de Dados

O projeto utiliza dois bancos de dados SQLite:

- **`banco_de_dados.db`** — armazena informações sobre séries, filmes e episódios
- **`banco_de_dados_de_usuario.db`** — armazena dados do usuário, como histórico e conteúdos salvos

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um **fork** do projeto
2. Crie uma branch para sua feature:
```bash
   git checkout -b feature/minha-feature
```
3. Faça o commit das suas alterações:
```bash
   git commit -m "feat: adiciona minha feature"
```
4. Envie para o repositório remoto:
```bash
   git push origin feature/minha-feature
```
5. Abra um **Pull Request**

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## 👤 Autor

Desenvolvido por **[Samu0K](https://github.com/Samu0K)**
