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
    .translation-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    .translation-text {
        font-size: 1.5rem;
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
    .example-box {
        background-color: #e3f2fd;
        border: 1px solid #90caf9;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: black;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def get_verb_list():
    """Retorna a lista completa de verbos"""
    return ['Être', 'Avoir', 'Faire', 'Dire', 'Pouvoir', 'Aller', 'Voir', 'Savoir', 
            'Falloir', 'Vouloir', 'Venir', 'Devoir', 'Prendre', 'Trouver', 'Donner', 
            'Parler', 'Mettre', 'Penser', 'Passer', 'Comprendre', 'Rester', 'Vivre', 
            'Revenir', 'Sortir', 'Arriver', 'Connaître', 'Devenir', 'Sentir', 'Partir', 
            'Laisser', 'Demander', 'Répondre', 'Entendre', 'Regarder', 'Aimer', 'Jouer', 
            'Reconnaître', 'Choisir', 'Toucher', 'Retrouver', 'Appeler', 'Permettre', 
            'Continuer', 'Apprendre', 'Compter', 'Écouter', 'Attendre', 'Réussir', 
            'Créer', 'Montrer', 'Ouvrir', 'Lire', 'Écrire', 'Courir', 'Expliquer', 
            'Conduire', 'Manger', 'Boire', 'Changer', 'Travailler', 'Essayer', 
            'Appartenir', 'Utiliser', 'Atteindre', 'Finir', 'Décider', 'Construire', 
            'Offrir', 'Exister', 'Accepter', 'Agir', 'Poser', 'Supposer', 'Obtenir', 
            'Perdre', 'Douter', 'Former', 'Détruire', 'Rappeler', 'Sourire', 'Installer', 
            'Exprimer', 'Développer', 'Éviter', 'Améliorer', 'Convaincre', 'Prétendre', 
            'Apporter', 'Investir', 'Apprécier', 'Réfléchir', 'Désirer']


@st.cache_data
def get_conjugations():
    """Retorna as conjugações dos verbos principais"""
    return {
        'Être': {
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
        'Avoir': {
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
        'Aller': {
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
        'Faire': {
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
        'Dire': {
            'présent': {'je': 'dis', 'tu': 'dis', 'il': 'dit', 'elle': 'dit', 'on': 'dit',
                       'nous': 'disons', 'vous': 'dites', 'ils': 'disent', 'elles': 'disent'},
            'passé composé': {'je': 'ai dit', 'tu': 'as dit', 'il': 'a dit', 'elle': 'a dit', 'on': 'a dit',
                             'nous': 'avons dit', 'vous': 'avez dit', 'ils': 'ont dit', 'elles': 'ont dit'},
            'imparfait': {'je': 'disais', 'tu': 'disais', 'il': 'disait', 'elle': 'disait', 'on': 'disait',
                         'nous': 'disions', 'vous': 'disiez', 'ils': 'disaient', 'elles': 'disaient'},
            'futur simple': {'je': 'dirai', 'tu': 'diras', 'il': 'dira', 'elle': 'dira', 'on': 'dira',
                           'nous': 'dirons', 'vous': 'direz', 'ils': 'diront', 'elles': 'diront'},
            'futur proche': {'je': 'vais dire', 'tu': 'vas dire', 'il': 'va dire', 'elle': 'va dire', 'on': 'va dire',
                           'nous': 'allons dire', 'vous': 'allez dire', 'ils': 'vont dire', 'elles': 'vont dire'}
        },
        'Pouvoir': {
            'présent': {'je': 'peux', 'tu': 'peux', 'il': 'peut', 'elle': 'peut', 'on': 'peut',
                       'nous': 'pouvons', 'vous': 'pouvez', 'ils': 'peuvent', 'elles': 'peuvent'},
            'passé composé': {'je': 'ai pu', 'tu': 'as pu', 'il': 'a pu', 'elle': 'a pu', 'on': 'a pu',
                             'nous': 'avons pu', 'vous': 'avez pu', 'ils': 'ont pu', 'elles': 'ont pu'},
            'imparfait': {'je': 'pouvais', 'tu': 'pouvais', 'il': 'pouvait', 'elle': 'pouvait', 'on': 'pouvait',
                         'nous': 'pouvions', 'vous': 'pouviez', 'ils': 'pouvaient', 'elles': 'pouvaient'},
            'futur simple': {'je': 'pourrai', 'tu': 'pourras', 'il': 'pourra', 'elle': 'pourra', 'on': 'pourra',
                           'nous': 'pourrons', 'vous': 'pourrez', 'ils': 'pourront', 'elles': 'pourront'},
            'futur proche': {'je': 'vais pouvoir', 'tu': 'vas pouvoir', 'il': 'va pouvoir', 'elle': 'va pouvoir', 'on': 'va pouvoir',
                           'nous': 'allons pouvoir', 'vous': 'allez pouvoir', 'ils': 'vont pouvoir', 'elles': 'vont pouvoir'}
        },
        'Voir': {
            'présent': {'je': 'vois', 'tu': 'vois', 'il': 'voit', 'elle': 'voit', 'on': 'voit',
                       'nous': 'voyons', 'vous': 'voyez', 'ils': 'voient', 'elles': 'voient'},
            'passé composé': {'je': 'ai vu', 'tu': 'as vu', 'il': 'a vu', 'elle': 'a vu', 'on': 'a vu',
                             'nous': 'avons vu', 'vous': 'avez vu', 'ils': 'ont vu', 'elles': 'ont vu'},
            'imparfait': {'je': 'voyais', 'tu': 'voyais', 'il': 'voyait', 'elle': 'voyait', 'on': 'voyait',
                         'nous': 'voyions', 'vous': 'voyiez', 'ils': 'voyaient', 'elles': 'voyaient'},
            'futur simple': {'je': 'verrai', 'tu': 'verras', 'il': 'verra', 'elle': 'verra', 'on': 'verra',
                           'nous': 'verrons', 'vous': 'verrez', 'ils': 'verront', 'elles': 'verront'},
            'futur proche': {'je': 'vais voir', 'tu': 'vas voir', 'il': 'va voir', 'elle': 'va voir', 'on': 'va voir',
                           'nous': 'allons voir', 'vous': 'allez voir', 'ils': 'vont voir', 'elles': 'vont voir'}
        },
        'Savoir': {
            'présent': {'je': 'sais', 'tu': 'sais', 'il': 'sait', 'elle': 'sait', 'on': 'sait',
                       'nous': 'savons', 'vous': 'savez', 'ils': 'savent', 'elles': 'savent'},
            'passé composé': {'je': 'ai su', 'tu': 'as su', 'il': 'a su', 'elle': 'a su', 'on': 'a su',
                             'nous': 'avons su', 'vous': 'avez su', 'ils': 'ont su', 'elles': 'ont su'},
            'imparfait': {'je': 'savais', 'tu': 'savais', 'il': 'savait', 'elle': 'savait', 'on': 'savait',
                         'nous': 'savions', 'vous': 'saviez', 'ils': 'savaient', 'elles': 'savaient'},
            'futur simple': {'je': 'saurai', 'tu': 'sauras', 'il': 'saura', 'elle': 'saura', 'on': 'saura',
                           'nous': 'saurons', 'vous': 'saurez', 'ils': 'sauront', 'elles': 'sauront'},
            'futur proche': {'je': 'vais savoir', 'tu': 'vas savoir', 'il': 'va savoir', 'elle': 'va savoir', 'on': 'va savoir',
                           'nous': 'allons savoir', 'vous': 'allez savoir', 'ils': 'vont savoir', 'elles': 'vont savoir'}
        },
        'Vouloir': {
            'présent': {'je': 'veux', 'tu': 'veux', 'il': 'veut', 'elle': 'veut', 'on': 'veut',
                       'nous': 'voulons', 'vous': 'voulez', 'ils': 'veulent', 'elles': 'veulent'},
            'passé composé': {'je': 'ai voulu', 'tu': 'as voulu', 'il': 'a voulu', 'elle': 'a voulu', 'on': 'a voulu',
                             'nous': 'avons voulu', 'vous': 'avez voulu', 'ils': 'ont voulu', 'elles': 'ont voulu'},
            'imparfait': {'je': 'voulais', 'tu': 'voulais', 'il': 'voulait', 'elle': 'voulait', 'on': 'voulait',
                         'nous': 'voulions', 'vous': 'vouliez', 'ils': 'voulaient', 'elles': 'voulaient'},
            'futur simple': {'je': 'voudrai', 'tu': 'voudras', 'il': 'voudra', 'elle': 'voudra', 'on': 'voudra',
                           'nous': 'voudrons', 'vous': 'voudrez', 'ils': 'voudront', 'elles': 'voudront'},
            'futur proche': {'je': 'vais vouloir', 'tu': 'vas vouloir', 'il': 'va vouloir', 'elle': 'va vouloir', 'on': 'va vouloir',
                           'nous': 'allons vouloir', 'vous': 'allez vouloir', 'ils': 'vont vouloir', 'elles': 'vont vouloir'}
        },
        'Venir': {
            'présent': {'je': 'viens', 'tu': 'viens', 'il': 'vient', 'elle': 'vient', 'on': 'vient',
                       'nous': 'venons', 'vous': 'venez', 'ils': 'viennent', 'elles': 'viennent'},
            'passé composé': {'je': 'suis venu(e)', 'tu': 'es venu(e)', 'il': 'est venu', 'elle': 'est venue', 'on': 'est venu',
                             'nous': 'sommes venu(e)s', 'vous': 'êtes venu(e)(s)', 'ils': 'sont venus', 'elles': 'sont venues'},
            'imparfait': {'je': 'venais', 'tu': 'venais', 'il': 'venait', 'elle': 'venait', 'on': 'venait',
                         'nous': 'venions', 'vous': 'veniez', 'ils': 'venaient', 'elles': 'venaient'},
            'futur simple': {'je': 'viendrai', 'tu': 'viendras', 'il': 'viendra', 'elle': 'viendra', 'on': 'viendra',
                           'nous': 'viendrons', 'vous': 'viendrez', 'ils': 'viendront', 'elles': 'viendront'},
            'futur proche': {'je': 'vais venir', 'tu': 'vas venir', 'il': 'va venir', 'elle': 'va venir', 'on': 'va venir',
                           'nous': 'allons venir', 'vous': 'allez venir', 'ils': 'vont venir', 'elles': 'vont venir'}
        },
        'Prendre': {
            'présent': {'je': 'prends', 'tu': 'prends', 'il': 'prend', 'elle': 'prend', 'on': 'prend',
                       'nous': 'prenons', 'vous': 'prenez', 'ils': 'prennent', 'elles': 'prennent'},
            'passé composé': {'je': 'ai pris', 'tu': 'as pris', 'il': 'a pris', 'elle': 'a pris', 'on': 'a pris',
                             'nous': 'avons pris', 'vous': 'avez pris', 'ils': 'ont pris', 'elles': 'ont pris'},
            'imparfait': {'je': 'prenais', 'tu': 'prenais', 'il': 'prenait', 'elle': 'prenait', 'on': 'prenait',
                         'nous': 'prenions', 'vous': 'preniez', 'ils': 'prenaient', 'elles': 'prenaient'},
            'futur simple': {'je': 'prendrai', 'tu': 'prendras', 'il': 'prendra', 'elle': 'prendra', 'on': 'prendra',
                           'nous': 'prendrons', 'vous': 'prendrez', 'ils': 'prendront', 'elles': 'prendront'},
            'futur proche': {'je': 'vais prendre', 'tu': 'vas prendre', 'il': 'va prendre', 'elle': 'va prendre', 'on': 'va prendre',
                           'nous': 'allons prendre', 'vous': 'allez prendre', 'ils': 'vont prendre', 'elles': 'vont prendre'}
        },
        'Parler': {
            'présent': {'je': 'parle', 'tu': 'parles', 'il': 'parle', 'elle': 'parle', 'on': 'parle',
                       'nous': 'parlons', 'vous': 'parlez', 'ils': 'parlent', 'elles': 'parlent'},
            'passé composé': {'je': 'ai parlé', 'tu': 'as parlé', 'il': 'a parlé', 'elle': 'a parlé', 'on': 'a parlé',
                             'nous': 'avons parlé', 'vous': 'avez parlé', 'ils': 'ont parlé', 'elles': 'ont parlé'},
            'imparfait': {'je': 'parlais', 'tu': 'parlais', 'il': 'parlait', 'elle': 'parlait', 'on': 'parlait',
                         'nous': 'parlions', 'vous': 'parliez', 'ils': 'parlaient', 'elles': 'parlaient'},
            'futur simple': {'je': 'parlerai', 'tu': 'parleras', 'il': 'parlera', 'elle': 'parlera', 'on': 'parlera',
                           'nous': 'parlerons', 'vous': 'parlerez', 'ils': 'parleront', 'elles': 'parleront'},
            'futur proche': {'je': 'vais parler', 'tu': 'vas parler', 'il': 'va parler', 'elle': 'va parler', 'on': 'va parler',
                           'nous': 'allons parler', 'vous': 'allez parler', 'ils': 'vont parler', 'elles': 'vont parler'}
        },
        'Aimer': {
            'présent': {'je': 'aime', 'tu': 'aimes', 'il': 'aime', 'elle': 'aime', 'on': 'aime',
                       'nous': 'aimons', 'vous': 'aimez', 'ils': 'aiment', 'elles': 'aiment'},
            'passé composé': {'je': 'ai aimé', 'tu': 'as aimé', 'il': 'a aimé', 'elle': 'a aimé', 'on': 'a aimé',
                             'nous': 'avons aimé', 'vous': 'avez aimé', 'ils': 'ont aimé', 'elles': 'ont aimé'},
            'imparfait': {'je': 'aimais', 'tu': 'aimais', 'il': 'aimait', 'elle': 'aimait', 'on': 'aimait',
                         'nous': 'aimions', 'vous': 'aimiez', 'ils': 'aimaient', 'elles': 'aimaient'},
            'futur simple': {'je': 'aimerai', 'tu': 'aimeras', 'il': 'aimera', 'elle': 'aimera', 'on': 'aimera',
                           'nous': 'aimerons', 'vous': 'aimerez', 'ils': 'aimeront', 'elles': 'aimeront'},
            'futur proche': {'je': 'vais aimer', 'tu': 'vas aimer', 'il': 'va aimer', 'elle': 'va aimer', 'on': 'va aimer',
                           'nous': 'allons aimer', 'vous': 'allez aimer', 'ils': 'vont aimer', 'elles': 'vont aimer'}
        }
    }


@st.cache_data
def get_complements_with_grammar():
    """Retorna complementos enriquecidos com artigos, pronomes e outros elementos gramaticais"""
    return {
        'Être': [
            'le médecin', 'la professeure', 'un étudiant', 'une étudiante',
            'ce professeur', 'cette femme', 'cet homme', 'ces enfants',
            'content(e)', 'fatigué(e)', 'en retard', 'à la maison',
            'celui qui parle', 'celle que tu connais', 'quelqu\'un de bien',
            'très intelligent(e)', 'vraiment heureux(se)', 'toujours prêt(e)'
        ],
        'Avoir': [
            'le temps', 'la voiture', 'un chien', 'une maison',
            'ce livre', 'cette idée', 'cet objet', 'ces documents',
            'quelque chose à dire', 'plusieurs amis', 'beaucoup d\'argent',
            'du courage', 'de la patience', 'des nouvelles',
            'vraiment faim', 'très soif', 'trop chaud'
        ],
        'Aller': [
            'au cinéma', 'à l\'école', 'chez le médecin', 'en France',
            'à la plage', 'au supermarché', 'chez mes parents',
            'dans ce restaurant', 'vers cette direction', 'là-bas',
            'y aller souvent', 'quelque part', 'nulle part',
            'très loin', 'tout droit', 'toujours ensemble'
        ],
        'Faire': [
            'le travail', 'la cuisine', 'un gâteau', 'une erreur',
            'ce devoir', 'cette tâche', 'cet exercice', 'ces courses',
            'du sport', 'de la natation', 'des efforts',
            'quelque chose d\'important', 'beaucoup de progrès',
            'vraiment attention', 'toujours de son mieux', 'très bien'
        ],
        'Dire': [
            'la vérité', 'la réponse', 'un secret', 'une phrase',
            'ce mot', 'cette histoire', 'cet argument', 'ces choses',
            'quelque chose', 'n\'importe quoi', 'tout',
            'vraiment bonjour', 'toujours merci', 'souvent non'
        ],
        'Pouvoir': [
            'le faire', 'la comprendre', 'y arriver', 'en parler',
            'tout expliquer', 'quelque chose', 'beaucoup',
            'vraiment réussir', 'toujours essayer', 'facilement partir'
        ],
        'Voir': [
            'le film', 'la mer', 'un ami', 'une solution',
            'ce spectacle', 'cette personne', 'cet endroit', 'ces images',
            'quelqu\'un', 'quelque chose', 'tout le monde',
            'très bien', 'clairement', 'souvent'
        ],
        'Savoir': [
            'la réponse', 'la vérité', 'un secret', 'une histoire',
            'ce fait', 'cette information', 'cet événement', 'ces détails',
            'quelque chose', 'tout', 'beaucoup de choses',
            'vraiment nager', 'bien conduire', 'parfaitement parler'
        ],
        'Vouloir': [
            'le bonheur', 'la paix', 'un café', 'une réponse',
            'ce livre', 'cette voiture', 'cet emploi', 'ces résultats',
            'quelque chose', 'tout', 'rien',
            'vraiment partir', 'absolument réussir', 'toujours gagner'
        ],
        'Venir': [
            'demain', 'ce soir', 'la semaine prochaine', 'tout de suite',
            'chez moi', 'à la fête', 'avec nous', 'de Paris',
            'y venir', 'en venir', 'souvent', 'rarement'
        ],
        'Prendre': [
            'le train', 'la voiture', 'un café', 'une décision',
            'ce chemin', 'cette route', 'cet itinéraire', 'ces documents',
            'quelque chose', 'tout', 'du temps',
            'vraiment soin', 'toujours garde', 'souvent l\'avion'
        ],
        'Parler': [
            'le français', 'la langue', 'un dialecte', 'une histoire',
            'de ce sujet', 'de cette affaire', 'de cet incident',
            'à quelqu\'un', 'avec tout le monde', 'en public',
            'très fort', 'doucement', 'toujours clairement'
        ],
        'Aimer': [
            'le chocolat', 'la musique', 'un film', 'une chanson',
            'ce style', 'cette couleur', 'cet artiste', 'ces moments',
            'quelqu\'un', 'tout le monde', 'beaucoup de choses',
            'vraiment danser', 'énormément lire', 'passionnément'
        ]
    }


@st.cache_data
def get_translations():
    """Retorna traduções de frases comuns"""
    translations = {
        'présent': {
            'je suis': 'eu sou/estou',
            'tu es': 'tu és/estás',
            'il est': 'ele é/está',
            'elle est': 'ela é/está',
            'nous sommes': 'nós somos/estamos',
            'vous êtes': 'vós sois/estais',
            'ils sont': 'eles são/estão',
            'elles sont': 'elas são/estão',
            'je ai': 'eu tenho',
            'tu as': 'tu tens',
            'il a': 'ele tem',
            'nous avons': 'nós temos',
            'vous avez': 'vós tendes',
            'ils ont': 'eles têm',
            'je vais': 'eu vou',
            'je fais': 'eu faço',
            'je dis': 'eu digo',
            'je peux': 'eu posso',
            'je vois': 'eu vejo',
            'je sais': 'eu sei',
            'je veux': 'eu quero',
            'je viens': 'eu venho',
            'je prends': 'eu pego/tomo',
            'je parle': 'eu falo',
            'je aime': 'eu amo/gosto'
        },
        'complements': {
            'le médecin': 'o médico',
            'la professeure': 'a professora',
            'un étudiant': 'um estudante',
            'une étudiante': 'uma estudante',
            'content(e)': 'contente',
            'fatigué(e)': 'cansado(a)',
            'en retard': 'atrasado',
            'à la maison': 'em casa',
            'le temps': 'o tempo',
            'la voiture': 'o carro',
            'un chien': 'um cachorro',
            'une maison': 'uma casa',
            'au cinéma': 'ao cinema',
            'à l\'école': 'à escola',
            'chez le médecin': 'no médico',
            'en France': 'na França',
            'le travail': 'o trabalho',
            'la cuisine': 'a cozinha',
            'du sport': 'esporte',
            'la vérité': 'a verdade',
            'le film': 'o filme',
            'la mer': 'o mar',
            'le bonheur': 'a felicidade',
            'le train': 'o trem',
            'le français': 'o francês',
            'le chocolat': 'o chocolate',
            'la musique': 'a música'
        }
    }
    return translations


@st.cache_data
def get_example_sentences():
    """Retorna frases de exemplo por verbo"""
    return {
        'Être': [
            'Je suis content de te voir.',
            'Elle est médecin depuis 10 ans.',
            'Nous sommes en retard pour la réunion.',
            'Ils sont très intelligents.',
            'Tu es celle que je cherchais.'
        ],
        'Avoir': [
            'J\'ai beaucoup de travail aujourd\'hui.',
            'Elle a une belle voiture rouge.',
            'Nous avons trois enfants.',
            'Ils ont du courage.',
            'Tu as vraiment de la chance.'
        ],
        'Aller': [
            'Je vais au cinéma ce soir.',
            'Elle va chez le médecin demain.',
            'Nous allons en France cet été.',
            'Ils vont souvent à la plage.',
            'Tu vas y aller avec nous?'
        ],
        'Faire': [
            'Je fais du sport tous les jours.',
            'Elle fait la cuisine pour sa famille.',
            'Nous faisons de notre mieux.',
            'Ils font beaucoup de progrès.',
            'Tu fais vraiment attention.'
        ],
        'Dire': [
            'Je dis toujours la vérité.',
            'Elle dit bonjour à tout le monde.',
            'Nous disons merci souvent.',
            'Ils disent quelque chose d\'important.',
            'Tu dis ce que tu penses.'
        ],
        'Pouvoir': [
            'Je peux le faire facilement.',
            'Elle peut tout comprendre.',
            'Nous pouvons y arriver ensemble.',
            'Ils peuvent réussir.',
            'Tu peux toujours essayer.'
        ],
        'Voir': [
            'Je vois la mer de ma fenêtre.',
            'Elle voit ses amis régulièrement.',
            'Nous voyons tout clairement.',
            'Ils voient ce spectacle ce soir.',
            'Tu vois quelqu\'un?'
        ],
        'Savoir': [
            'Je sais nager depuis l\'enfance.',
            'Elle sait parler trois langues.',
            'Nous savons la réponse.',
            'Ils savent tout sur ce sujet.',
            'Tu sais conduire?'
        ],
        'Vouloir': [
            'Je veux un café, s\'il vous plaît.',
            'Elle veut réussir son examen.',
            'Nous voulons la paix.',
            'Ils veulent partir demain.',
            'Tu veux quelque chose?'
        ],
        'Venir': [
            'Je viens de Paris.',
            'Elle vient ce soir à la fête.',
            'Nous venons souvent ici.',
            'Ils viennent avec nous.',
            'Tu viens demain?'
        ],
        'Prendre': [
            'Je prends le train tous les jours.',
            'Elle prend un café le matin.',
            'Nous prenons une décision importante.',
            'Ils prennent leur temps.',
            'Tu prends ce chemin?'
        ],
        'Parler': [
            'Je parle français couramment.',
            'Elle parle très fort.',
            'Nous parlons de ce sujet.',
            'Ils parlent en public.',
            'Tu parles avec qui?'
        ],
        'Aimer': [
            'J\'aime le chocolat noir.',
            'Elle aime beaucoup la musique.',
            'Nous aimons voyager.',
            'Ils aiment ce style.',
            'Tu aimes danser?'
        ]
    }


def translate_sentence(sentence, pronoun, verb, tense, complement, translations):
    """Traduz a frase para português"""
    trans = translations
    
    # Tradução básica do pronome + verbo
    verb_key = f"{pronoun} {verb.split()[0]}"
    verb_trans = trans['présent'].get(verb_key, verb)
    
    # Tradução do complemento
    comp_trans = trans['complements'].get(complement, complement)
    
    # Estrutura básica da tradução
    if 'ne' in sentence and 'pas' in sentence:
        # Negativa
        translation = f"{verb_trans.split()[0].capitalize()} não {' '.join(verb_trans.split()[1:])} {comp_trans}."
    elif '?' in sentence:
        # Interrogativa
        translation = f"{verb_trans.capitalize()} {comp_trans}?"
    else:
        # Afirmativa
        translation = f"{verb_trans.capitalize()} {comp_trans}."
    
    return translation


def build_sentence(pronome, verbo, tempo, estrutura, complemento, conjugacoes):
    """Constrói a frase baseada nos parâmetros selecionados"""
    if verbo not in conjugacoes:
        verbo_conjugado = f"[{verbo} - conjugação não disponível]"
    else:
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


def initialize_random_values():
    """Inicializa valores aleatórios na primeira execução"""
    if 'initialized' not in st.session_state:
        pronouns = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles']
        verbs = list(get_conjugations().keys())
        tenses = ['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche']
        structures = ['Affirmative', 'Négative', 'Interrogative']
        
        st.session_state.pronome = random.choice(pronouns)
        st.session_state.verbo = random.choice(verbs)
        st.session_state.tempo = random.choice(tenses)
        st.session_state.estrutura = random.choice(structures)
        
        complements = get_complements_with_grammar()
        st.session_state.complemento = random.choice(complements[st.session_state.verbo])
        
        st.session_state.initialized = True


def main():
    # Inicializar valores aleatórios
    initialize_random_values()
    
    # Cabeçalho
    st.markdown('<h1 class="main-header">🇫🇷 Constructeur de phrases françaises</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # Obter dados
    conjugacoes = get_conjugations()
    complementos = get_complements_with_grammar()
    translations = get_translations()
    examples = get_example_sentences()

    # Layout em colunas
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("🎯 Sélectionnez vos éléments")

        # Seletores com valores iniciais do session_state
        pronome = st.selectbox(
            "1️⃣ Pronom personnel:",
            ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'],
            key="pronome"
        )

        verbo = st.selectbox(
            "2️⃣ Verbe:",
            list(conjugacoes.keys()),
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
            complementos.get(verbo, ['[aucun]']),
            key="complemento"
        )

        # Botões
        st.markdown("---")
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🎲 Phrase aléatoire", type="secondary", use_container_width=True):
                st.session_state.random_pronome = random.choice(['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'])
                st.session_state.random_verbo = random.choice(list(conjugacoes.keys()))
                st.session_state.random_tempo = random.choice(['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'])
                st.session_state.random_estrutura = random.choice(['Affirmative', 'Négative', 'Interrogative'])
                st.session_state.random_complemento = random.choice(complementos[st.session_state.random_verbo])
                st.rerun()
        
        with col_btn2:
            if st.button("🔄 Nouvelle combinaison", type="primary", use_container_width=True):
                st.session_state.pronome = random.choice(['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles'])
                st.session_state.verbo = random.choice(list(conjugacoes.keys()))
                st.session_state.tempo = random.choice(['présent', 'passé composé', 'imparfait', 'futur simple', 'futur proche'])
                st.session_state.estrutura = random.choice(['Affirmative', 'Négative', 'Interrogative'])
                st.session_state.complemento = random.choice(complementos[st.session_state.verbo])
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

        # Botão de tradução
        if st.button("🇧🇷 Voir la traduction en portugais", use_container_width=True):
            st.session_state.show_translation = True
        
        # Exibir tradução se solicitado
        if st.session_state.get('show_translation', False):
            translation = translate_sentence(frase, pronome, verbo, tempo, complemento, translations)
            st.markdown(f"""
            <div class="translation-box">
                <div class="translation-text">📖 {translation}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("❌ Masquer la traduction"):
                st.session_state.show_translation = False
                st.rerun()

        # Informações gramaticais
        if verbo in conjugacoes:
            grammar_html = f"""
            <div class="grammar-info">
                <h4>📚 Informations grammaticales:</h4>
                <ul>
                    <li><strong>Pronom:</strong> {pronome}</li>
                    <li><strong>Verbe:</strong> {verbo} ({tempo})</li>
                    <li><strong>Structure:</strong> {estrutura}</li>
                    <li><strong>Conjugaison:</strong> {conjugacoes[verbo][tempo][pronome]}</li>
                    {f"<li><strong>Complément:</strong> {complemento}</li>" if complemento else ""}
                </ul>
            </div>
            """
            st.markdown(grammar_html, unsafe_allow_html=True)

    # Seção de exemplo do verbo selecionado
    st.markdown("---")
    st.header("💡 Exemple avec ce verbe")
    
    if verbo in examples:
        example = random.choice(examples[verbo])
        st.markdown(f"""
        <div class="example-box">
            <h4>📖 Phrase d'exemple avec "{verbo}":</h4>
            <p style="font-size: 1.3rem; text-align: center; margin: 1rem 0;">
                <strong>{example}</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

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
                    <li><strong>Pronom:</strong> {st.session_state.get('random_pronome', '')}</li>
                    <li><strong>Verbe:</strong> {st.session_state.get('random_verbo', '')}</li>
                    <li><strong>Temps:</strong> {st.session_state.get('random_tempo', '')}</li>
                    <li><strong>Structure:</strong> {st.session_state.get('random_estrutura', '')}</li>
                    <li><strong>Complément:</strong> {st.session_state.get('random_complemento', '')}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            if st.button("🔍 Voir la solution"):
                random_verb = st.session_state.get('random_verbo', 'Être')
                if random_verb in conjugacoes:
                    solution = build_sentence(
                        st.session_state.get('random_pronome', 'je'),
                        random_verb,
                        st.session_state.get('random_tempo', 'présent'),
                        st.session_state.get('random_estrutura', 'Affirmative'),
                        st.session_state.get('random_complemento', ''),
                        conjugacoes
                    )
                    st.success(f"**Solution:** {solution}")
                else:
                    st.warning(f"Conjugaison non disponible pour {random_verb}")

    # Sidebar com informações adicionais
    with st.sidebar:
        st.header("ℹ️ À propos")
        st.markdown(f"""
        Cette application vous aide à construire des phrases en français 
        en combinant différents éléments grammaticaux.
        
        **Fonctionnalités:**
        - ✅ {len(conjugacoes)} verbes avec conjugaisons
        - ✅ 5 temps verbaux
        - ✅ 3 structures de phrase
        - ✅ Conjugaisons automatiques
        - ✅ Compléments enrichis (articles, pronoms, etc.)
        - ✅ Traduction en portugais
        - ✅ Exemples aléatoires
        - ✅ Défis aléatoires
        - ✅ Valeurs initiales aléatoires
        """)

        st.markdown("---")
        st.header("📖 Liste des verbes")
        all_verbs = get_verb_list()
        verbs_with_conj = list(conjugacoes.keys())
        st.markdown(f"**Verbes avec conjugaisons complètes:** {len(verbs_with_conj)}")
        st.markdown(f"**Verbes disponibles:** {len(all_verbs)}")
        
        with st.expander("Voir tous les verbes"):
            st.write(", ".join(all_verbs))

        st.markdown("---")
        st.header("🎓 Conseils d'utilisation")
        st.markdown("""
        1. **Commencez simple:** Utilisez le présent avec des phrases affirmatives
        2. **Pratiquez la négation:** Observez la position de 'ne...pas'
        3. **Maîtrisez l'interrogation:** Notez les différentes formes
        4. **Utilisez les défis:** Cliquez sur 'Phrase aléatoire' pour vous entraîner
        5. **Étudiez les exemples:** Chaque verbe a des phrases d'exemple
        6. **Vérifiez les traductions:** Comprenez le sens en portugais
        """)

        st.markdown("---")
        st.info("💡 **Astuce:** Essayez de construire 10 phrases différentes pour bien maîtriser chaque structure !")


if __name__ == "__main__":
    main()
