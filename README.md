# 🇫🇷 Constructeur de Phrases Françaises

Uma aplicação web interativa para aprender e praticar a construção de frases em francês, desenvolvida com Streamlit.

![French Flag](https://img.shields.io/badge/Français-🇫🇷-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)

## 🎯 Funcionalidades

- **Construção Interativa**: Combine pronomes, verbos, tempos verbais e estruturas
- **4 Verbos Essenciais**: être, avoir, aller, faire
- **5 Tempos Verbais**: présent, passé composé, imparfait, futur simple, futur proche
- **3 Estruturas**: afirmativa, negativa, interrogativa
- **Conjugação Automática**: Todas as conjugações são feitas automaticamente
- **Complementos Contextuais**: Sugestões de complementos baseadas no verbo escolhido
- **Desafios Aleatórios**: Pratique com combinações aleatórias
- **Interface Responsiva**: Funciona perfeitamente em desktop e mobile

## 🚀 Demo Online

[**Acesse a aplicação aqui**](https://frances-frases.streamlit.app)

## 🛠️ Instalação Local

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Passos para instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/frances-estrutura-frases.git
cd french-sentence-builder
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
streamlit run app.py
```

5. **Acesse no navegador**
```
http://localhost:8501
```

## 📦 Deploy no Streamlit Cloud

### Opção 1: Deploy Automático via GitHub

1. **Fork este repositório** no GitHub
2. **Acesse** [share.streamlit.io](https://share.streamlit.io)
3. **Conecte sua conta** do GitHub
4. **Selecione** seu repositório forkado
5. **Configure**:
   - **Main file path**: `app.py`
   - **Python version**: 3.9
6. **Deploy!** 🚀

### Opção 2: Deploy Manual

1. **Crie um novo repositório** no GitHub
2. **Faça upload dos arquivos**:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. **Siga os passos** da Opção 1

## 📚 Como Usar

### Interface Principal
1. **Selecione os elementos** na coluna esquerda:
   - Pronome pessoal (je, tu, il, elle, etc.)
   - Verbo (être, avoir, aller, faire)
   - Tempo verbal (présent, passé composé, etc.)
   - Estrutura da frase (afirmativa, negativa, interrogativa)
   - Complemento (opcional)

2. **Visualize a frase** construída na coluna direita
3. **Veja as informações gramaticais** detalhadas

### Desafio Aleatório
- Clique em **"🎲 Phrase aléatoire"** para gerar um desafio
- Tente construir a frase mentalmente
- Clique em **"🔍 Voir la solution"** para ver a resposta

## 🎓 Aspectos Educacionais

### Para Professores
- **Ferramenta de ensino** interativa para aulas de francês
- **Prática estruturada** de conjugação verbal
- **Exercícios variados** com diferentes estruturas

### Para Estudantes
- **Aprendizado progressivo** do básico ao avançado
- **Feedback imediato** na construção de frases
- **Prática autônoma** com desafios aleatórios

## 🔧 Estrutura do Projeto

```
french-sentence-builder/
│
├── app.py              # Aplicação principal Streamlit
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── .gitignore         # Arquivos ignorados pelo Git
```

## 🤝 Revisões futuras

### Melhorias:
- [ ] Adicionar mais verbos
- [ ] Criar sistema de pontuação
- [ ] Adicionar explicações gramaticais
- [ ] Implementar modo de quiz

## 📋 Changelog

### v1.0.0
- ✅ Implementação inicial
- ✅ Interface básica do Streamlit
- ✅ 4 verbos essenciais com conjugações
- ✅ 5 tempos verbais
- ✅ 3 estruturas de frase
- ✅ Sistema de desafios aleatórios

## 📄 Licença

Projeto licenciado sob a GPL-3.0 license, mais detalhes em [LICENSE](LICENSE).
