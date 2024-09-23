import streamlit as st

# Informations de Sasha
nom = "Sasha Le BG"
poste = "Ingénieur Data Science"
description = """
Sasha est un ingénieur talentueux et charismatique avec une passion pour la Data Science et l'intelligence artificielle.
Il possède une solide expérience dans la gestion de projets complexes et l'analyse de données massives.
"""

# Compétences
competences = {
    "Python": "⭐⭐⭐⭐⭐",
    "Machine Learning": "⭐⭐⭐⭐",
    "Deep Learning": "⭐⭐⭐⭐",
    "SQL": "⭐⭐⭐",
    "Gestion de projets": "⭐⭐⭐⭐",
    "Communication": "⭐⭐⭐⭐⭐"
}

# Expériences
experiences = [
    {"poste": "Data Scientist", "entreprise": "Google", "annees": "2021-2024", "description": "Développement de modèles prédictifs."},
    {"poste": "Stagiaire IA", "entreprise": "Thales", "annees": "2020-2021", "description": "Création d'applications d'IA en temps réel."},
]

# Diplômes
diplomes = [
    {"titre": "Master en Intelligence Artificielle", "ecole": "École Polytechnique", "annees": "2018-2020"},
    {"titre": "Licence en Informatique", "ecole": "Université Paris-Saclay", "annees": "2015-2018"},
]

# Contact
email = "sasha.lebg@example.com"
linkedin = "linkedin.com/in/sasha-lebg"
github = "github.com/sasha-lebg"

# Application Streamlit
st.title(f"CV de {nom}")
st.header(poste)
st.write(description)

# Compétences
st.subheader("Compétences")
for skill, niveau in competences.items():
    st.write(f"{skill} : {niveau}")

# Expériences professionnelles
st.subheader("Expériences professionnelles")
for experience in experiences:
    st.write(f"**{experience['poste']}** chez *{experience['entreprise']}* ({experience['annees']})")
    st.write(experience['description'])

# Diplômes
st.subheader("Diplômes")
for diplome in diplomes:
    st.write(f"**{diplome['titre']}** - {diplome['ecole']} ({diplome['annees']})")

# Contact
st.subheader("Contact")
st.write(f"Email : {email}")
st.write(f"[LinkedIn]({linkedin})")
st.write(f"[GitHub]({github})")

st.write("Merci de votre visite !")
