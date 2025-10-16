import streamlit as st
import random

# Configuração da página
st.set_page_config(
    page_title="Constructeur de phrases françaises",
    page_icon="🇫🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sentence-box {
        background-color: #f0f8ff;
        border-left: 5px solid #1f4e79;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    .sentence-text {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .grammar-info {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        color: black;
    }
    .random-challenge {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: black;
    }
    .translation-box {
        background-color: #e8f5e8;
        border-left: 5px solid #2e7d32;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_conjugations():
    """Retorna as conjugações dos verbos em cache"""
    return {
        'être': {
            'présent': {'je': 'suis', 'tu': 'es', 'il': 'est', 'elle': 'est', 'on': 'est',
                       'nous': 'sommes', 'vous': 'êtes', 'ils': 'sont', 'elles': 'sont'},
            'passé composé': {'je': 'ai été', 'tu': 'as été', 'il': 'a été', 'elle': 'a été', 'on': 'a été',
                             'nous': 'avons été', 'vous': 'avez été', 'ils': 'ont été', 'elles': 'ont été'},
            'imparfait': {'je': 'étais', 'tu': 'étais', 'il': 'était', 'elle': 'était', 'on': 'était',
                         'nous': 'étions', 'vous': 'étiez', 'ils': 'étaient', 'elles': 'étaient'},
            'futur simple': {'je': 'serai', 'tu': 'seras', 'il': 'sera', 'elle': 'sera', 'on': 'sera',
                           'nous': 'serons', 'vous': 'serez', 'ils': 'seront', 'elles': 'seront'},
            'futur proche': {'je': 'vais être', 'tu': 'vas être', 'il': 'va être', 'elle': 'va être', 'on': 'va être',
                           'nous': 'allons être', 'vous': 'allez être', 'ils': 'vont être', 'elles': 'vont être'}
        },
        'avoir': {
            'présent': {'je': 'ai', 'tu': 'as', 'il': 'a', 'elle': 'a', 'on': 'a',
                       'nous': 'avons', 'vous': 'avez', 'ils': 'ont', 'elles': 'ont'},
            'passé composé': {'je': 'ai eu', 'tu': 'as eu', 'il': 'a eu', 'elle': 'a eu', 'on': 'a eu',
                             'nous': 'avons eu', 'vous': 'avez eu', 'ils': 'ont eu', 'elles': 'ont eu'},
            'imparfait': {'je': 'avais', 'tu': 'avais', 'il': 'avait', 'elle': 'avait', 'on': 'avait',
                         'nous': 'avions', 'vous': 'aviez', 'ils': 'avaient', 'elles': 'avaient'},
            'futur simple': {'je': 'aurai', 'tu': 'auras', 'il': 'aura', 'elle': 'aura', 'on': 'aura',
                           'nous': 'aurons', 'vous': 'aurez', 'ils': 'auront', 'elles': 'auront'},
            'futur proche': {'je': 'vais avoir', 'tu': 'vas avoir', 'il': 'va avoir', 'elle': 'va avoir', 'on': 'va avoir',
                           'nous': 'allons avoir', 'vous': 'allez avoir', 'ils': 'vont avoir', 'elles': 'vont avoir'}
        },
        'aller': {
            'présent': {'je': 'vais', 'tu': 'vas', 'il': 'va', 'elle': 'va', 'on': 'va',
                       'nous': 'allons', 'vous': 'allez', 'ils': 'vont', 'elles': 'vont'},
            'passé composé': {'je': 'suis allé(e)', 'tu': 'es allé(e)', 'il': 'est allé', 'elle': 'est allée', 'on': 'est allé',
                             'nous': 'sommes allé(e)s', 'vous': 'êtes allé(e)(s)', 'ils': 'sont allés', 'elles': 'sont allées'},
            'imparfait': {'je': 'allais', 'tu': 'allais', 'il': 'allait', 'elle': 'allait', 'on': 'allait',
                         'nous': 'allions', 'vous': 'alliez', 'ils': 'allaient', 'elles': 'allaient'},
            'futur simple': {'je': 'irai', 'tu': 'iras', 'il': 'ira', 'elle': 'ira', 'on': 'ira',
                           'nous': 'irons', 'vous': 'irez', 'ils': 'iront', 'elles': 'iront'},
            'futur proche': {'je': 'vais aller', 'tu': 'vas aller', 'il': 'va aller', 'elle': 'va aller', 'on': 'va aller',
                           'nous': 'allons aller', 'vous': 'allez aller', 'ils': 'vont aller', 'elles': 'vont aller'}
        },
        'faire': {
            'présent': {'je': 'fais', 'tu': 'fais', 'il': 'fait', 'elle': 'fait', 'on': 'fait',
                       'nous': 'faisons', 'vous': 'faites', 'ils': 'font', 'elles': 'font'},
            'passé composé': {'je': 'ai fait', 'tu': 'as fait', 'il': 'a fait', 'elle': 'a fait', 'on': 'a fait',
                             'nous': 'avons fait', 'vous': 'avez fait', 'ils': 'ont fait', 'elles': 'ont fait'},
            'imparfait': {'je': 'faisais', 'tu': 'faisais', 'il': 'faisait', 'elle': 'faisait', 'on': 'faisait',
                         'nous': 'faisions', 'vous': 'faisiez', 'ils': 'faisaient', 'elles': 'faisaient'},
            'futur simple': {'je': 'ferai', 'tu': 'feras', 'il': 'fera', 'elle': 'fera', 'on': 'fera',
                           'nous': 'ferons', 'vous': 'ferez', 'ils': 'feront', 'elles': 'feront'},
            'futur proche': {'je': 'vais faire', 'tu': 'vas faire', 'il': 'va faire', 'elle': 'va faire', 'on': 'va faire',
                           'nous': 'allons faire', 'vous': 'allez faire', 'ils': 'vont faire', 'elles': 'vont faire'}
        },
        # Adicione mais conjugações para os outros verbos aqui
    }

@st.cache_data
def get_complements():
    """Retorna os complementos por verbo em cache"""
    return {
        'être': ['content(e)', 'fatigué(e)', 'en retard', 'à la maison', 'médecin', 'étudiant(e)', 'français(e)', 'intelligent(e)'],
        'avoir': ['faim', 'soif', 'froid', 'chaud', '20 ans', 'une voiture', 'un chien', 'des amis', 'du temps', 'de la chance'],
        'aller': ['au cinéma', "à l'école", 'chez le médecin', 'en France', 'au travail', 'à la plage', 'au supermarché', 'voir des amis'],
        'faire': ['du sport', 'les courses', 'la cuisine', 'ses devoirs', 'du vélo', 'une promenade', 'attention', 'du bruit']
    }

@st.cache_data
def get_grammar_elements():
    """Retorna elementos gramaticais adicionais"""
    return {
        'articles_definis': ['le', 'la', 'les', "l'"],
        'articles_indefinis': ['un', 'une', 'des'],
        'adverbes': ['souvent', 'toujours', 'rarement', 'vite', 'lentement', 'bien', 'mal', 'beaucoup', 'peu', 'trop'],
        'adjectifs_demonstratifs': ['ce', 'cet', 'cette', 'ces'],
        'adjectifs_indefinis': ['quelque', 'chaque', 'plusieurs', 'certain(e)s', 'aucun(e)', 'tout(e)'],
        'pronoms_indefinis': ['quelqu\'un', 'quelque chose', 'personne', 'rien', 'chacun(e)', 'tout le monde'],
        'pronoms_complements': ['me', 'te', 'le', 'la', 'lui', 'nous', 'vous', 'les', 'leur'],
        'pronoms_adjectifs': ['mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ma', 'ta', 'sa', 'mes', 'tes', 'ses', 'nos', 'vos', 'leurs'],
        'pronoms_demonstratifs': ['celui', 'celle', 'ceux', 'celles'],
        'pronoms_possessifs': ['le mien', 'la mienne', 'les miens', 'les miennes', 'le tien', 'la tienne', 'les tiens', 'les tiennes'],
        'pronoms_relatifs': ['qui', 'que', 'dont', 'où', 'lequel', 'laquelle', 'lesquels', 'lesquelles'],
        'partitifs': ['du', 'de la', "de l'", 'des'],
        'pronoms_en_y': ['en', 'y']
    }

@st.cache_data
def get_verb_list():
    """Retorna a lista completa de verbos"""
    return [
        'Être', 'Avoir', 'Faire', 'Dire', 'Pouvoir', 'Aller', 'Voir', 'Savoir', 'Falloir', 'Vouloir', 
        'Venir', 'Devoir', 'Prendre', 'Trouver', 'Donner', 'Parler', 'Mettre', 'Penser', 'Passer', 
        'Comprendre', 'Rester', 'Vivre', 'Revenir', 'Sortir', 'Arriver', 'Connaître', 'Devenir', 
        'Sentir', 'Partir', 'Laisser', 'Demander', 'Répondre', 'Entendre', 'Regarder', 'Aimer', 
        'Jouer', 'Reconnaître', 'Choisir', 'Toucher', 'Retrouver', 'Appeler', 'Permettre', 'Continuer', 
        'Apprendre', 'Compter', 'Écouter', 'Attendre', 'Réussir', 'Créer', 'Montrer', 'Ouvrir', 
        'Lire', 'Écrire', 'Courir', 'Expliquer', 'Conduire', 'Manger', 'Boire', 'Changer', 
        'Travailler', 'Essayer', 'Appartenir', 'Utiliser', 'Atteindre', 'Finir', 'Décider', 
        'Construire', 'Offrir', 'Exister', 'Accepter', 'Agir', 'Poser', 'Supposer', 'Obtenir', 
        'Perdre', 'Douter', 'Former', 'Détruire', 'Rappeler', 'Sourire', 'Installer', 'Exprimer', 
        'Développer', 'Éviter', 'Améliorer', 'Convaincre', 'Prétendre', 'Apporter', 'Investir', 
        'Apprécier', 'Réfléchir', 'Désirer'
    ]

@st.cache_data
def get_translations():
    """Retorna traduções para português"""
    return {
        'être': 'ser/estar',
        'avoir': 'ter',
        'faire': 'fazer',
        'aller': 'ir',
        'content(e)': 'contente',
        'fatigué(e)': 'cansado(a)',
        'en retard': 'atrasado(a)',
        'à la maison': 'em casa',
        'médecin': 'médico(a)',
        'étudiant(e)': 'estudante',
        'français(e)': 'francês(a)',
        'intelligent(e)': 'inteligente',
        'faim': 'fome',
        'soif': 'sede',
        'froid': 'frio',
        'chaud': 'calor',
        '20 ans': '20 anos',
        'une voiture': 'um carro',
        'un chien': 'um cachorro',
        'des amis': 'amigos',
        'du temps': 'tempo',
        'de la chance': 'sorte',
        'au cinéma': 'ao cinema',
        "à l'école": 'à escola',
        'chez le médecin': 'no médico',
        'en France': 'na França',
        'au travail': 'no trabalho',
        'à la plage': 'na praia',
        'au supermarché': 'no supermercado',
        'voir des amis': 'ver amigos',
        'du sport': 'esporte',
        'les courses': 'compras',
        'la cuisine': 'a cozinha/cozinhar',
        'ses devoirs': 'seus deveres',
        'du vélo': 'andar de bicicleta',
        'une promenade': 'um passeio',
        'attention': 'atenção',
        'du bruit': 'barulho'
    }

def get_random_values(conjugacoes, complementos):
    """Retorna valores aleatórios para inicializar os campos"""
    pronomes = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles']
    verbos = list(conjugacoes.keys())
    tempos = ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche']
    estruturas = ['Affirmative', 'Négative', 'Interrogative']
    
    pronome = random.choice(pronomes)
    verbo = random.choice(verbos)
    tempo = random.choice(tempos)
    estrutura = random.choice(estruturas)
    complemento = random.choice(complementos[verbo])
    
    return pronome, verbo, tempo, estrutura, complemento

def build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes, grammar_elements):
    """Constrói a frase baseada nos parâmetros selecionados"""
    verbo_conjugado = conjugacoes[verbo][tempo][pronome]
    
    # Adiciona elementos gramaticais aleatórios
    artigo = random.choice(grammar_elements['articles_definis'] + grammar_elements['articles_indefinis'])
    adjetivo_demonstrativo = random.choice(grammar_elements['adjectifs_demonstratifs'])
    adjetivo_indefinido = random.choice(grammar_elements['adjectifs_indefinis'])
    pronome_complemento = random.choice(grammar_elements['pronoms_complements'])
    pronome_en_y = random.choice(grammar_elements['pronoms_en_y'])
    adverbe = random.choice(grammar_elements['adverbes'])

    if estrutura == 'Affirmative':
        frase = f"{pronome.capitalize()} {verbo_conjugado}"
        
        # Adiciona elementos gramaticais com certa probabilidade
        if random.random() < 0.3:
            frase += f" {adverbe}"
        
        if complemento:
            # Adiciona artigo/pronome antes do complemento com certa probabilidade
            if random.random() < 0.4:
                if random.random() < 0.5:
                    frase += f" {artigo} {complemento}"
                else:
                    frase += f" {adjetivo_demonstrativo} {complemento}"
            else:
                frase += f" {complemento}"
        
        # Adiciona pronome complemento com certa probabilidade
        if random.random() < 0.2:
            frase = f"{pronome.capitalize()} {pronome_complemento} {verbo_conjugado}" + frase.split(verbo_conjugado)[1]
        
        frase += "."

    elif estrutura == 'Négative':
        if tempo in ['passé composé', 'futur proche']:
            if ' ' in verbo_conjugado:
                aux, part = verbo_conjugado.split(' ', 1)
                frase = f"{pronome.capitalize()} ne {aux} pas {part}"
            else:
                frase = f"{pronome.capitalize()} ne {verbo_conjugado} pas"
        else:
            frase = f"{pronome.capitalize()} ne {verbo_conjugado} pas"

        # Adiciona adverbe com certa probabilidade
        if random.random() < 0.3:
            frase = frase.replace(' pas', f' {adverbe} pas')

        if complemento:
            # Adiciona artigo/pronome antes do complemento com certa probabilidade
            if random.random() < 0.4:
                if random.random() < 0.5:
                    frase += f" {artigo} {complemento}"
                else:
                    frase += f" {adjetivo_demonstrativo} {complemento}"
            else:
                frase += f" {complemento}"
        
        frase += "."

    elif estrutura == 'Interrogative':
        if pronome in ['je', 'tu', 'il', 'elle', 'on']:
            frase = f"Est-ce que {pronome} {verbo_conjugado}"
            
            # Adiciona adverbe com certa probabilidade
            if random.random() < 0.3:
                frase += f" {adverbe}"
                
            if complemento:
                # Adiciona artigo/pronome antes do complemento com certa probabilidade
                if random.random() < 0.4:
                    if random.random() < 0.5:
                        frase += f" {artigo} {complemento}"
                    else:
                        frase += f" {adjetivo_demonstrativo} {complemento}"
                else:
                    frase += f" {complemento}"
            frase += " ?"
        else:
            if tempo in ['passé composé', 'futur proche']:
                if ' ' in verbo_conjugado:
                    aux, part = verbo_conjugado.split(' ', 1)
                    frase = f"{aux.capitalize()}-{pronome} {part}"
                else:
                    frase = f"{verbo_conjugado.capitalize()}-{pronome}"
            else:
                frase = f"{verbo_conjugado.capitalize()}-{pronome}"

            # Adiciona adverbe com certa probabilidade
            if random.random() < 0.3:
                frase += f" {adverbe}"
                
            if complemento:
                # Adiciona artigo/pronome antes do complemento com certa probabilidade
                if random.random() < 0.4:
                    if random.random() < 0.5:
                        frase += f" {artigo} {complemento}"
                    else:
                        frase += f" {adjetivo_demonstrativo} {complemento}"
                else:
                    frase += f" {complemento}"
            frase += " ?"

    return frase

def get_translation(frase, traducoes):
    """Traduz a frase para português (versão simplificada)"""
    # Esta é uma tradução básica, em uma aplicação real você usaria uma API de tradução
    traducoes_frases = {
        "Je suis": "Eu sou",
        "Tu es": "Tu és",
        "Il est": "Ele é",
        "Elle est": "Ela é",
        "Nous sommes": "Nós somos",
        "Vous êtes": "Vocês são",
        "Ils sont": "Eles são",
        "Elles sont": "Elas são",
        "J'ai": "Eu tenho",
        "Tu as": "Tu tens",
        "Il a": "Ele tem",
        "Elle a": "Ela tem",
        "Nous avons": "Nós temos",
        "Vous avez": "Vocês têm",
        "Ils ont": "Eles têm",
        "Elles ont": "Elas têm",
        "Je vais": "Eu vou",
        "Tu vas": "Tu vais",
        "Il va": "Ele vai",
        "Elle va": "Ela vai",
        "Nous allons": "Nós vamos",
        "Vous allez": "Vocês vão",
        "Ils vont": "Eles vão",
        "Elles vont": "Elas vão",
        "Je fais": "Eu faço",
        "Tu fais": "Tu fazes",
        "Il fait": "Ele faz",
        "Elle fait": "Ela faz",
        "Nous faisons": "Nós fazemos",
        "Vous faites": "Vocês fazem",
        "Ils font": "Eles fazem",
        "Elles font": "Elas fazem"
    }
    
    # Procura por padrões conhecidos na frase
    for padrao_fr, padrao_pt in traducoes_frases.items():
        if padrao_fr in frase:
            traducao = frase.replace(padrao_fr, padrao_pt)
            # Substitui palavras individuais
            for palavra_fr, palavra_pt in traducoes.items():
                traducao = traducao.replace(palavra_fr, palavra_pt)
            return traducao
    
    # Se não encontrar padrão, faz substituição básica
    traducao = frase
    for palavra_fr, palavra_pt in traducoes.items():
        traducao = traducao.replace(palavra_fr, palavra_pt)
    
    return traducao

def get_example_sentence(verbo, conjugacoes, complementos, grammar_elements):
    """Gera uma frase de exemplo com o verbo selecionado"""
    pronomes = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles']
    tempos = ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche']
    estruturas = ['Affirmative', 'Négative', 'Interrogative']
    
    pronome = random.choice(pronomes)
    tempo = random.choice(tempos)
    estrutura = random.choice(estruturas)
    complemento = random.choice(complementos.get(verbo, ['']))
    
    return build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes, grammar_elements)

def main():
    # Cabeçalho
    st.markdown('<h1 class="main-header">🇫🇷 Constructeur de phrases françaises</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # Obter dados
    conjugacoes = get_conjugations()
    complementos = get_complements()
    grammar_elements = get_grammar_elements()
    verbos_lista = get_verb_list()
    traducoes = get_translations()

    # Inicializar valores aleatórios se não existirem na sessão
    if 'initialized' not in st.session_state:
        pronome, verbo, tempo, estrutura, complemento = get_random_values(conjugacoes, complementos)
        st.session_state.pronome = pronome
        st.session_state.verbo = verbo
        st.session_state.tempo = tempo
        st.session_state.estrutura = estrutura
        st.session_state.complemento = complemento
        st.session_state.initialized = True

    # Layout em colunas
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("🎯 Sélectionnez vos éléments")

        # Seletores com valores iniciais aleatórios
        pronome = st.selectbox(
            "1️⃣ Pronome personnel:",
            ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'],
            key="pronome",
            index=['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'].index(st.session_state.pronome)
        )

        verbo = st.selectbox(
            "2️⃣ Verbe:",
            list(conjugacoes.keys()),
            key="verbo",
            index=list(conjugacoes.keys()).index(st.session_state.verbo)
        )

        tempo = st.selectbox(
            "3️⃣ Temps verbal:",
            ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'],
            key="tempo",
            index=['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'].index(st.session_state.tempo)
        )

        estrutura = st.selectbox(
            "4️⃣ Structure de phrase:",
            ['Affirmative', 'Négative', 'Interrogative'],
            key="estrutura",
            index=['Affirmative', 'Négative', 'Interrogative'].index(st.session_state.estrutura)
        )

        complemento = st.selectbox(
            "5️⃣ Complément:",
            complementos[verbo],
            key="complemento",
            index=complementos[verbo].index(st.session_state.complemento)
        )

        # Botão para frase aleatória
        st.markdown("---")
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🎲 Phrase aléatoire", type="secondary", use_container_width=True):
                pronome, verbo, tempo, estrutura, complemento = get_random_values(conjugacoes, complementos)
                st.session_state.pronome = pronome
                st.session_state.verbo = verbo
                st.session_state.tempo = tempo
                st.session_state.estrutura = estrutura
                st.session_state.complemento = complemento
                st.rerun()
        
        with col_btn2:
            if st.button("📚 Exemple avec ce verbe", type="secondary", use_container_width=True):
                st.session_state.exemple_verbe = get_example_sentence(verbo, conjugacoes, complementos, grammar_elements)
                st.session_state.montrer_exemple = True

    with col2:
        st.header("📝 Phrase construite")

        # Construir e exibir a frase
        frase = build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes, grammar_elements)

        st.markdown(f"""
        <div class="sentence-box">
            <div class="sentence-text">{frase}</div>
        </div>
        """, unsafe_allow_html=True)

        # Botão para mostrar tradução
        if st.button("🇧🇷 Voir la traduction en portugais"):
            traducao = get_translation(frase, traducoes)
            st.markdown(f"""
            <div class="translation-box">
                <div class="sentence-text">{traducao}</div>
            </div>
            """, unsafe_allow_html=True)

        # Informações gramaticales
        grammar_html = f"""
        <div class="grammar-info">
            <h4>📚 Informations grammaticales:</h4>
            <ul>
                <li><strong>Pronome:</strong> {pronome}</li>
                <li><strong>Verbe:</strong> {verbo} ({tempo})</li>
                <li><strong>Structure:</strong> {estrutura}</li>
                <li><strong>Conjugaison:</strong> {conjugacoes[verbo][tempo][pronome]}</li>
                {f"<li><strong>Complément:</strong> {complemento}</li>" if complemento else ""}
            </ul>
        </div>
        """

        st.markdown(grammar_html, unsafe_allow_html=True)

    # Exemplo com o verbo selecionado
    if st.session_state.get('montrer_exemple', False):
        st.markdown("---")
        st.header("💡 Exemple avec ce verbe")
        
        col_ex1, col_ex2 = st.columns([1, 1])
        
        with col_ex1:
            st.markdown(f"""
            <div class="random-challenge">
                <h4>📚 Phrase d'exemple avec <strong>{verbo}</strong>:</h4>
                <div class="sentence-text">{st.session_state.exemple_verbe}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_ex2:
            if st.button("🔄 Nouvel exemple", type="secondary"):
                st.session_state.exemple_verbe = get_example_sentence(verbo, conjugacoes, complementos, grammar_elements)
                st.rerun()

    # Seção de desafio aleatório
    if any(key.startswith('random_') for key in st.session_state):
        st.markdown("---")
        st.header("🎯 Défi aléatoire")

        col3, col4 = st.columns([1, 1])

        with col3:
            st.markdown(f"""
            <div class="random-challenge">
                <h4>🎲 Construisez une phrase avec:</h4>
                <ul>
                    <li><strong>Pronome:</strong> {st.session_state.get('random_pronome', '')}</li>
                    <li><strong>Verbe:</strong> {st.session_state.get('random_verbo', '')}</li>
                    <li><strong>Temps:</strong> {st.session_state.get('random_tempo', '')}</li>
                    <li><strong>Structure:</strong> {st.session_state.get('random_estrutura', '')}</li>
                    <li><strong>Complément:</strong> {st.session_state.get('random_complemento', '')}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            if st.button("🔍 Voir la solution"):
                solution = build_sentence(
                    st.session_state.get('random_pronome', 'je'),
                    st.session_state.get('random_verbo', 'être'),
                    st.session_state.get('random_tempo', 'présent'),
                    st.session_state.get('random_estrutura', 'Affirmative'),
                    st.session_state.get('random_complemento', ''),
                    conjugacoes,
                    grammar_elements
                )
                st.success(f"**Solution:** {solution}")

    # Sidebar com informações adicionais
    with st.sidebar:
        st.header("ℹ️ À propos")
        st.markdown("""
        Cette application vous aide à construire des phrases en français 
        en combinant différents éléments grammaticaux.
        
        **Fonctionnalités:**
        - ✅ 4 verbes essentiels
        - ✅ 5 temps verbaux
        - ✅ 3 structures de phrase
        - ✅ Conjugaisons automatiques
        - ✅ Compléments contextuels
        - ✅ Défis aléatoires
        - ✅ Traductions en portugais
        - ✅ Exemples avec chaque verbe
        - ✅ Éléments grammaticaux variés
        """)

        st.markdown("---")
        st.header("🎓 Conseils d'utilisation")
        st.markdown("""
        1. **Commencez simple:** Utilisez le présent avec des phrases affirmatives
        2. **Pratiquez la négation:** Observez la position de 'ne...pas'
        3. **Maîtrisez l'interrogation:** Notez les différentes formes
        4. **Utilisez les défis:** Cliquez sur 'Phrase aléatoire' pour vous entraîner
        5. **Consultez les traductions:** Comprenez le sens en portugais
        """)

        st.markdown("---")
        st.info("💡 **Astuce:** Essayez de construire 10 phrases différentes pour bien maîtriser chaque structure !")


if __name__ == "__main__":
    main()
