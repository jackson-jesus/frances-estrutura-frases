import streamlit as st
import random
import requests

st.set_page_config(page_title="Constructeur de phrases françaises", page_icon="🇫🇷", layout="wide")

# ==========================
# CACHE LOCAL
# ==========================
if "cache_conjug" not in st.session_state:
    st.session_state.cache_conjug = {}
if "cache_trad" not in st.session_state:
    st.session_state.cache_trad = {}

# ==========================
# FUNÇÕES DE API
# ==========================

def google_translate(text, target_lang="pt", source_lang="fr"):
    """
    Usa a API pública do Google Translate (sem necessidade de chave)
    """
    try:
        key = (text, target_lang, source_lang)
        if key in st.session_state.cache_trad:
            return st.session_state.cache_trad[key]

        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": source_lang, "tl": target_lang, "dt": "t", "q": text}
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            data = r.json()[0]
            translation = "".join([seg[0] for seg in data])
            st.session_state.cache_trad[key] = translation
            return translation
        else:
            return text
    except Exception as e:
        st.warning(f"Falha na tradução: {e}")
        return text


def conjugate_verb(verb, pronoun, tense):
    """
    Gera conjugação do verbo usando tradução reversa como proxy.
    Usa cache local para evitar requisições repetidas.
    """
    key = (verb, pronoun, tense)
    if key in st.session_state.cache_conjug:
        return st.session_state.cache_conjug[key]

    try:
        # Frase em francês pedindo a conjugação
        prompt = f"Conjugue le verbe '{verb}' avec '{pronoun}' au {tense}."
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": "fr", "tl": "en", "dt": "t", "q": prompt}
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            text = r.json()[0][0][0]
            # Tenta extrair o verbo conjugado
            tokens = text.replace(".", "").split()
            conj = tokens[-1] if tokens else verb
            st.session_state.cache_conjug[key] = conj
            return conj
    except Exception:
        pass

    # fallback
    st.session_state.cache_conjug[key] = verb
    return verb


# ==========================
# GERAÇÃO DE FRASES
# ==========================

def build_sentence(pronoun, verb, tense, structure):
    """Gera frase em francês com elementos variados"""
    conj = conjugate_verb(verb, pronoun, tense)
    phrase = f"{pronoun.capitalize()} {conj}"

    extras = [
        "souvent", "toujours", "rarement", "vite", "bien",
        "à la maison", "au travail", "avec mes amis", "dans le parc",
        "aujourd’hui", "demain", "en ce moment"
    ]
    if random.random() < 0.6:
        phrase += " " + random.choice(extras)

    if structure == "Négative":
        phrase = phrase.replace("Je ", "Je ne ").replace("Tu ", "Tu ne ") + " pas"
    elif structure == "Interrogative":
        phrase = f"Est-ce que {phrase.lower()} ?"
    else:
        phrase += "."

    return phrase


# ==========================
# INTERFACE STREAMLIT
# ==========================

st.markdown("<h1 style='text-align:center;color:#1f4e79;'>🇫🇷 Constructeur de phrases françaises</h1>", unsafe_allow_html=True)
st.markdown("---")

pronouns = ['je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles']
tenses = ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche']
structures = ['Affirmative', 'Négative', 'Interrogative']
verbs = [
    'être', 'avoir', 'faire', 'aller', 'dire', 'pouvoir', 'voir', 'savoir', 'venir',
    'devoir', 'parler', 'mettre', 'trouver', 'donner', 'comprendre', 'vivre', 'aimer', 'jouer'
]

# Valores aleatórios iniciais
pronoun = st.selectbox("👤 Pronome", pronouns, index=random.randint(0, len(pronouns)-1))
verb = st.selectbox("🔤 Verbe", verbs, index=random.randint(0, len(verbs)-1))
tense = st.selectbox("⏳ Temps verbal", tenses, index=random.randint(0, len(tenses)-1))
structure = st.selectbox("🧩 Structure de phrase", structures, index=random.randint(0, len(structures)-1))

# Geração da frase
phrase = build_sentence(pronoun, verb, tense, structure)
st.markdown(f"""
<div style="background:#f0f8ff;border-left:5px solid #1f4e79;padding:1rem;margin:1rem 0;border-radius:0.5rem;">
<p style="font-size:1.6rem;text-align:center;color:#2c3e50;"><b>{phrase}</b></p>
</div>
""", unsafe_allow_html=True)

# Tradução
if st.button("🇧🇷 Exibir tradução em português"):
    with st.spinner("Traduzindo..."):
        translated = google_translate(phrase, "pt", "fr")
        st.markdown(f"""
        <div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:1rem;margin:1rem 0;border-radius:0.5rem;">
        <p style="font-size:1.4rem;text-align:center;color:#1b5e20;">{translated}</p>
        </div>
        """, unsafe_allow_html=True)

# Exemplo
if st.button("💡 Exemplo com este verbo"):
    with st.spinner("Gerando exemplo..."):
        ex_pronoun = random.choice(pronouns)
        ex_tense = random.choice(tenses)
        ex_structure = random.choice(structures)
        example = build_sentence(ex_pronoun, verb, ex_tense, ex_structure)
        st.success(f"**Exemple:** {example}")

        if st.button("🇧🇷 Traduzir exemplo"):
            translated_ex = google_translate(example, "pt", "fr")
            st.info(f"**Tradução:** {translated_ex}")

# Mostrar cache
with st.expander("🧠 Cache local"):
    st.write(f"Conjugações armazenadas: {len(st.session_state.cache_conjug)}")
    st.write(f"Traduções armazenadas: {len(st.session_state.cache_trad)}")
    if st.button("🗑️ Limpar cache"):
        st.session_state.cache_conjug.clear()
        st.session_state.cache_trad.clear()
        st.rerun()

