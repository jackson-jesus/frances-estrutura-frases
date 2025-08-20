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
    }
    .random-challenge {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: black;
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
        }
    }

@st.cache_data
def get_complements():
    """Retorna os complementos por verbo em cache"""
    return {
        'être': ['content(e)', 'fatigué(e)', 'en retard', 'à la maison', 'médecin', 'étudiant(e)', 'français(e)', 'intelligent(e)'],
        'avoir': ['faim', 'soif', 'froid', 'chaud', '20 ans', 'une voiture', 'un chien', 'des amis', 'du temps', 'de la chance'],
        'aller': ['au cinéma', 'à l\'école', 'chez le médecin', 'en France', 'au travail', 'à la plage', 'au supermarché', 'voir des amis'],
        'faire': ['du sport', 'les courses', 'la cuisine', 'ses devoirs', 'du vélo', 'une promenade', 'attention', 'du bruit']
    }

def build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes):
    """Constrói a frase baseada nos parâmetros selecionados"""
    verbo_conjugado = conjugacoes[verbo][tempo][pronome]
    
    if estrutura == 'Affirmative':
        frase = f"{pronome.capitalize()} {verbo_conjugado}"
        if complemento:
            frase += f" {complemento}"
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
        
        if complemento:
            frase += f" {complemento}"
        frase += "."
        
    elif estrutura == 'Interrogative':
        if pronome in ['je', 'tu', 'il', 'elle', 'on']:
            frase = f"Est-ce que {pronome} {verbo_conjugado}"
            if complemento:
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
            
            if complemento:
                frase += f" {complemento}"
            frase += " ?"
    
    return frase

def main():
    # Cabeçalho
    st.markdown('<h1 class="main-header">🇫🇷 Constructeur de phrases françaises</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Obter dados
    conjugacoes = get_conjugations()
    complementos = get_complements()
    
    # Layout em colunas
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("🎯 Sélectionnez vos éléments")
        
        # Seletores
        pronome = st.selectbox(
            "1️⃣ Pronome personnel:",
            ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'],
            key="pronome"
        )
        
        verbo = st.selectbox(
            "2️⃣ Verbe:",
            ['être', 'avoir', 'aller', 'faire'],
            key="verbo"
        )
        
        tempo = st.selectbox(
            "3️⃣ Temps verbal:",
            ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'],
            key="tempo"
        )
        
        estrutura = st.selectbox(
            "4️⃣ Structure de phrase:",
            ['Affirmative', 'Négative', 'Interrogative'],
            key="estrutura"
        )
        
        complemento = st.selectbox(
            "5️⃣ Complément:",
            [''] + complementos[verbo],
            key="complemento",
            index=random.randint(0, len(complementos[verbo]) - 1)
        )
        
        # Botão para frase aleatória
        st.markdown("---")
        if st.button("🎲 Phrase aléatoire", type="secondary"):
            st.session_state.random_pronome = random.choice(['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'])
            st.session_state.random_verbo = random.choice(['être', 'avoir', 'aller', 'faire'])
            st.session_state.random_tempo = random.choice(['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'])
            st.session_state.random_estrutura = random.choice(['Affirmative', 'Négative', 'Interrogative'])
            st.session_state.random_complemento = random.choice(complementos[st.session_state.random_verbo])
            st.rerun()
    
    with col2:
        st.header("📝 Phrase construite")
        
        # Construir e exibir a frase
        frase = build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes)
        
        st.markdown(f"""
        <div class="sentence-box">
            <div class="sentence-text">{frase}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Informações gramaticais
        complement_line = f'<li><strong>Complément:</strong> {complemento}</li>' if complemento else ''
        
        grammar_html = f"""
        <div class="grammar-info">
            <h4>📚 Informations grammaticales:</h4>
            <ul>
                <li><strong>Pronome:</strong> {pronome}</li>
                <li><strong>Verbe:</strong> {verbo} ({tempo})</li>
                <li><strong>Structure:</strong> {estrutura}</li>
                <li><strong>Conjugaison:</strong> {conjugacoes[verbo][tempo][pronome]}</li>
                {"<li><strong>Complément:</strong> {complemento}</li>" if complemento else ""}
            </ul>
        </div>
        """

        st.markdown(grammar_html, unsafe_allow_html=True)
    
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
                random_complemento = random.choice(complementos[st.session_state.get('random_verbo', 'être')])
                solution = build_sentence(
                    st.session_state.get('random_pronome', 'je'),
                    st.session_state.get('random_verbo', 'être'),
                    st.session_state.get('random_tempo', 'présent'),
                    st.session_state.get('random_estrutura', 'Affirmative'),
                    st.session_state.get('random_complemento', ''),
                    conjugacoes
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
        """)
        
        st.markdown("---")
        st.header("🎓 Conseils d'utilisation")
        st.markdown("""
        1. **Commencez simple:** Utilisez le présent avec des phrases affirmatives
        2. **Pratiquez la négation:** Observez la position de 'ne...pas'
        3. **Maîtrisez l'interrogation:** Notez les différentes formes
        4. **Utilisez les défis:** Cliquez sur 'Phrase aléatoire' pour vous entraîner
        """)
        
        st.markdown("---")
        st.info("💡 **Astuce:** Essayez de construire 10 phrases différentes pour bien maîtriser chaque structure !")

if __name__ == "__main__":
    main()
