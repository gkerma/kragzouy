# app.py
# Jeu génératif "Cyber Opera Oracle"
# WebUI Streamlit

import random
import textwrap
import streamlit as st

# ---------- CONFIG STREAMLIT ----------

st.set_page_config(
    page_title="Cyber Opera Oracle",
    page_icon="🎭",
    layout="wide",
)

# ---------- DONNÉES : DECK 24 CARTES ----------

CARDS = [
    {
        "id": 1,
        "name": "Nombres + lettres + barres + soleil",
        "emoji": "⚡🛠️",
        "family": "Action",
        "keywords": ["mesurer", "régler", "analyser"],
        "role": "Régie technique",
        "short": "Régler les paramètres, comprendre ce qui se passe en coulisses.",
    },
    {
        "id": 2,
        "name": "Symboles + couleurs",
        "emoji": "⏸️🧘",
        "family": "Pause",
        "keywords": ["réfléchir", "coder", "associer"],
        "role": "Partition de code / langage symbolique",
        "short": "Prendre le temps de décoder et de faire des liens.",
    },
    {
        "id": 3,
        "name": "Ordinateur « HALO »",
        "emoji": "⚡",
        "family": "Action",
        "keywords": ["connecter", "dialoguer", "saisir"],
        "role": "Console principale",
        "short": "Se connecter au système, parler à la machine.",
    },
    {
        "id": 4,
        "name": "Calculatrice",
        "emoji": "⚡🧮",
        "family": "Action",
        "keywords": ["compter", "vérifier", "comparer"],
        "role": "Compte des coulisses",
        "short": "Faire les comptes, vérifier que tout tient debout.",
    },
    {
        "id": 5,
        "name": "Schéma « PREUVE / HALO »",
        "emoji": "⚔️",
        "family": "Combat",
        "keywords": ["argumenter", "démontrer", "défendre"],
        "role": "Tribunal / plaidoyer",
        "short": "On doit prouver quelque chose, défendre une position.",
    },
    {
        "id": 6,
        "name": "Entrées / sorties / calculateur / mémoire",
        "emoji": "⚡🛠️",
        "family": "Action",
        "keywords": ["traiter", "structurer", "organiser"],
        "role": "Moteur de l’Opéra",
        "short": "Le système tourne, absorbe, transforme, restitue.",
    },
    {
        "id": 7,
        "name": "Bocal-planète « VIRTUEL »",
        "emoji": "⏸️☁️",
        "family": "Pause",
        "keywords": ["imaginer", "simuler", "voyager"],
        "role": "Décor holographique",
        "short": "On observe un monde possible, un décor mental ou virtuel.",
    },
    {
        "id": 8,
        "name": "Deux visages « DISEMBLANCE »",
        "emoji": "⚔️🛡️",
        "family": "Combat",
        "keywords": ["contraste", "masque", "tension"],
        "role": "Duo / masque double",
        "short": "Deux versions, deux visages, une tension entre les deux.",
    },
    {
        "id": 9,
        "name": "Smiley « HUMOUR / GAG / JOUER »",
        "emoji": "⏸️☕",
        "family": "Pause",
        "keywords": ["détendre", "relativiser", "jouer"],
        "role": "Scène comique",
        "short": "Un moment de légèreté, de blague, de jeu.",
    },
    {
        "id": 10,
        "name": "9 = 9 « LOGIQUE »",
        "emoji": "⏸️🧠",
        "family": "Pause",
        "keywords": ["cohérence", "preuve", "raison"],
        "role": "Chœur des logiciens",
        "short": "On revient à la cohérence, aux faits, à la logique.",
    },
    {
        "id": 11,
        "name": "Coffre + bouteille « secret / love / bombe »",
        "emoji": "⚡",
        "family": "Action",
        "keywords": ["révéler", "envoyer", "oser"],
        "role": "Accessoire-clé",
        "short": "Un secret, un message, une bombe affective circule.",
    },
    {
        "id": 12,
        "name": "Maisons + bulles « monsters ? »",
        "emoji": "⚡🛠️",
        "family": "Action",
        "keywords": ["environnement", "contexte", "situer"],
        "role": "Décor de quartier / ville",
        "short": "Le cadre social, le voisinage, le contexte collectif.",
    },
    {
        "id": 13,
        "name": "Nuage + document + symboles",
        "emoji": "⏸️⏸️",
        "family": "Pause",
        "keywords": ["noter", "observer", "ressentir"],
        "role": "Storyboard / notes",
        "short": "On prend des notes, on réfléchit, on prépare.",
    },
    {
        "id": 14,
        "name": "Paysage + fleur « ARCHIVE »",
        "emoji": "⏸️🗂️",
        "family": "Pause",
        "keywords": ["souvenir", "trace", "classer"],
        "role": "Décor souvenir",
        "short": "Un souvenir, un paysage du passé, une archive affective.",
    },
    {
        "id": 15,
        "name": "Pyramide de personnages « ADD »",
        "emoji": "⚡⚡",
        "family": "Action",
        "keywords": ["rejoindre", "coopérer", "soutenir"],
        "role": "Chœur qui se forme",
        "short": "Le collectif se forme, on rejoint une troupe, un groupe.",
    },
    {
        "id": 16,
        "name": "Carte « LANGUES » + 2 personnes",
        "emoji": "⚡🧠",
        "family": "Action",
        "keywords": ["traduire", "apprendre", "relier"],
        "role": "Traduction / dialogue",
        "short": "On traduit, on négocie entre deux langues, deux mondes.",
    },
    {
        "id": 17,
        "name": "Fleurs + personnes « EXPAND / ÉTENDRE »",
        "emoji": "⚡✨",
        "family": "Action",
        "keywords": ["diffuser", "agrandir", "rayonner"],
        "role": "Final d’ensemble",
        "short": "L’énergie se répand, on touche plus large, on rayonne.",
    },
    {
        "id": 18,
        "name": "TV + film + casque « MEDIAS »",
        "emoji": "⚡🎬",
        "family": "Action",
        "keywords": ["communiquer", "diffuser", "écouter"],
        "role": "Diffusion hors-scène",
        "short": "Ce qui se passe est filmé, diffusé, médiatisé.",
    },
    {
        "id": 19,
        "name": "Smartphone + tablette",
        "emoji": "⚡📱",
        "family": "Action",
        "keywords": ["contacter", "envoyer", "recevoir"],
        "role": "Messages des coulisses",
        "short": "Messages, notifications, DM, échanges rapides.",
    },
    {
        "id": 20,
        "name": "Appareils audio / sons",
        "emoji": "⚡🎧",
        "family": "Action",
        "keywords": ["enregistrer", "mixer", "transmettre"],
        "role": "Cabine son / mixage",
        "short": "Le son est travaillé, remixé, réécouté.",
    },
    {
        "id": 21,
        "name": "Paysage / planète + personnage",
        "emoji": "⏸️🧘",
        "family": "Pause",
        "keywords": ["contemplation", "vision", "distance"],
        "role": "Solo contemplatif",
        "short": "Moment de recul, on regarde le monde depuis loin.",
    },
    {
        "id": 22,
        "name": "Ampoule + avions « CONNECT / HOW? »",
        "emoji": "⚡⚡",
        "family": "Action",
        "keywords": ["idée", "lien", "mise en réseau"],
        "role": "Idée de mise en scène",
        "short": "Une nouvelle idée de connexion ou de scénario surgit.",
    },
    {
        "id": 23,
        "name": "Avion + fusée « FABRIQUER / BUILD »",
        "emoji": "⚡🛠️",
        "family": "Action",
        "keywords": ["construire", "tester", "lancer"],
        "role": "Atelier / décollage",
        "short": "On fabrique, on teste, on prépare un lancement.",
    },
    {
        "id": 24,
        "name": "Voiture + carte « VOYAGE / GEOLOCAL »",
        "emoji": "⚡🚗",
        "family": "Action",
        "keywords": ["se déplacer", "explorer", "aller vers"],
        "role": "Transition de scène / voyage",
        "short": "On se met en mouvement, on change de lieu ou de phase.",
    },
]

# ---------- DONNÉES : GLYPHES ----------

GLYPHS = [
    {
        "name": "TRIΔ",
        "emoji": "🔺⚡",
        "role": "Prototype vivant, bug sacré, étincelle de nouveau",
        "style": "chaotique, joueur, explosif",
        "special": "Quand je casse une règle ou un cadre figé, alors je peux ouvrir une possibilité totalement nouvelle.",
    },
    {
        "name": "ORBITA",
        "emoji": "👁️⭕",
        "role": "Caméra vivante, regard qui révèle",
        "style": "calme, précis, observateur",
        "special": "Quand je fixe un détail ou une scène, alors je peux la montrer à tout le monde comme une vérité évidente.",
    },
    {
        "name": "CANTORA",
        "emoji": "🌪️🎙️",
        "role": "Voix, chant, incantation",
        "style": "dramatique, intense, émotionnel",
        "special": "Quand je chante ce que tout le monde retient, alors je peux libérer une émotion bloquée.",
    },
    {
        "name": "SHARP-4",
        "emoji": "✴️💥",
        "role": "Silhouette de diva, icône visuelle",
        "style": "flamboyant, théâtral",
        "special": "Quand j’entre en scène comme si tout tournait autour de moi, alors je peux provoquer un tournant dramatique.",
    },
    {
        "name": "LINKHEART",
        "emoji": "❤️🔗",
        "role": "Lien affectif, relations profondes",
        "style": "tendre, intense",
        "special": "Quand je relie deux personnages par un sentiment, alors je peux changer la direction de l’histoire.",
    },
    {
        "name": "MIRRA",
        "emoji": "🎭🌀",
        "role": "Métamorphe, imposteur, acteur multiple",
        "style": "joueur, ambigu",
        "special": "Quand je prends le visage ou la voix de quelqu’un, alors je peux révéler ce que cette personne n’oserait jamais dire.",
    },
    {
        "name": "ARCH-7",
        "emoji": "🧱📐",
        "role": "Architecte, designer de systèmes",
        "style": "posé, analytique, perfectionniste",
        "special": "Quand je redessine la structure d’une scène, alors je peux transformer un chaos en architecture vivante.",
    },
    {
        "name": "CHORUS-LOOP",
        "emoji": "✨💫",
        "role": "Chœur, foule, communauté",
        "style": "collectif, mouvant, amplificateur",
        "special": "Quand nous choisissons qui soutenir ou qui attaquer, alors nous pouvons faire monter ou tomber n’importe qui.",
    },
    {
        "name": "BLOOM",
        "emoji": "🌸🎟️",
        "role": "Poète, détail inoubliable",
        "style": "discret, sensible, subtil",
        "special": "Quand j’ajoute un petit geste ou une image, alors je peux graver cette scène dans la mémoire de tous.",
    },
    {
        "name": "PACTUM",
        "emoji": "✒️📜",
        "role": "Contrat, loi, engagement",
        "style": "sérieux, solennel",
        "special": "Quand je scelle un pacte ou le brise, alors je peux redéfinir les règles du jeu entre les personnages.",
    },
    {
        "name": "RUMOR",
        "emoji": "☁️💬",
        "role": "Rumeur, mémoire diffuse, réseau",
        "style": "bavard, changeant",
        "special": "Quand je laisse circuler ce qui se dit déjà, alors je peux faire remonter des vérités et des mensonges.",
    },
    {
        "name": "SENSEÏ-0",
        "emoji": "🧘‍♀️⏸️",
        "role": "Maître immobile, gardien du temps lent",
        "style": "minimal, silencieux, tranchant",
        "special": "Quand je m’assois et que j’impose le silence, alors je peux forcer tout le monde à ressentir ce qui est vraiment là.",
    },
]

# ---------- FONCTIONS UTILITAIRES ----------


def draw_cards(n: int, seed: int | None = None):
    rng = random.Random(seed)
    return rng.sample(CARDS, k=n)


def draw_glyphs(n: int, seed: int | None = None):
    rng = random.Random(seed)
    return rng.sample(GLYPHS, k=n)


def wrap(text: str, width: int = 80) -> str:
    return "\n".join(textwrap.wrap(text, width=width))


# Génération de texte de scène simple (pas d'API, juste combinatoire)


def generate_scene_summary(mode: str, cards: list[dict], glyphs: list[dict]) -> str:
    """Crée une mini proposition de scène en français."""

    lines = []

    if mode == "Scène en 3 actes" and len(cards) >= 3:
        c1, c2, c3 = cards[:3]
        lines.append("🎬 **Proposition de scène en 3 actes**")
        lines.append(
            f"- **Acte I** ({c1['emoji']} *{c1['name']}*) : {c1['short']}"
        )
        lines.append(
            f"- **Acte II** ({c2['emoji']} *{c2['name']}*) : {c2['short']}"
        )
        lines.append(
            f"- **Acte III** ({c3['emoji']} *{c3['name']}*) : {c3['short']}"
        )

    elif mode == "Coup de projecteur" and cards:
        c = cards[0]
        lines.append("🔦 **Énergie du moment**")
        lines.append(
            f"Cette scène tourne autour de **{c['name']}** ({c['emoji']}), "
            f"avec {', '.join(c['keywords'])} comme thèmes principaux."
        )

    elif mode == "Duo de personnages" and len(cards) >= 2 and glyphs:
        c1, c2 = cards[:2]
        g = glyphs[0]
        lines.append("👥 **Duo + Glyphe**")
        lines.append(
            f"- {g['emoji']} **{g['name']}** arrive sur un décor inspiré de "
            f"*{c1['name']}*."
        )
        lines.append(
            f"- La tension ou la dynamique entre les personnes est colorée par "
            f"*{c2['name']}* ({c2['emoji']})."
        )

    elif mode == "Hack en direct" and len(cards) >= 4:
        s, bug, hack, res = cards[:4]
        lines.append("🎧💥 **Hack en direct**")
        lines.append(f"- Système actuel : *{s['name']}* ({s['emoji']}).")
        lines.append(f"- Bug / tension : *{bug['name']}* ({bug['emoji']}).")
        lines.append(f"- Hack proposé : *{hack['name']}* ({hack['emoji']}).")
        lines.append(
            f"- Résultat possible : *{res['name']}* ({res['emoji']})."
        )

    elif mode == "Voyage initiatique" and len(cards) >= 5:
        p0, bag, defy, ally, dest = cards[:5]
        lines.append("🚗🌙 **Voyage initiatique**")
        lines.append(f"- Point de départ : *{p0['name']}* ({p0['emoji']}).")
        lines.append(f"- Bagage : *{bag['name']}* ({bag['emoji']}).")
        lines.append(f"- Défi : *{defy['name']}* ({defy['emoji']}).")
        lines.append(f"- Alliée·e : *{ally['name']}* ({ally['emoji']}).")
        lines.append(f"- Paysage d’arrivée : *{dest['name']}* ({dest['emoji']}).")

    elif mode == "Diva & Coulisses" and len(cards) >= 3:
        diva, coulisses, reg = cards[:3]
        lines.append("👑🎭 **Diva & Coulisses**")
        lines.append(f"- Diva (façade) : *{diva['name']}* ({diva['emoji']}).")
        lines.append(
            f"- Coulisses (ce qui se passe derrière) : *{coulisses['name']}* ({coulisses['emoji']})."
        )
        lines.append(
            f"- Régisseur (ajustement possible) : *{reg['name']}* ({reg['emoji']})."
        )

    elif mode == "Scène-éclair" and len(cards) >= 2 and glyphs:
        c1, c2 = cards[:2]
        g = glyphs[0]
        lines.append("⚡ **Scène-éclair**")
        lines.append(
            f"{g['emoji']} **{g['name']}** entre dans une situation inspirée de "
            f"*{c1['name']}* ({c1['emoji']})."
        )
        lines.append(
            f"L’issue ou le twist est coloré par *{c2['name']}* ({c2['emoji']})."
        )

    # Ajout d'une phrase bonus avec les glyphes
    if glyphs:
        g_names = ", ".join([f"{g['emoji']} {g['name']}" for g in glyphs])
        lines.append("")
        lines.append(f"🌀 **Glyphes en jeu :** {g_names}")

    return "\n".join(lines)


# ---------- UI ----------

st.title("🎭 Cyber Opera Oracle – Jeu génératif")
st.markdown(
    "Un jeu de cartes et de glyphes pour composer des scènes, "
    "des oracles narratifs et des micro-opéras cyber."
)

with st.sidebar:
    st.header("🎛️ Paramètres")

    mode = st.selectbox(
        "Mode de tirage",
        [
            "Scène en 3 actes",
            "Coup de projecteur",
            "Duo de personnages",
            "Hack en direct",
            "Voyage initiatique",
            "Diva & Coulisses",
            "Scène-éclair",
            "Libre",
        ],
    )

    use_glyphs = st.checkbox("Inclure les glyphes-personnages", value=True)

    seed_input = st.text_input(
        "Seed aléatoire (optionnel, pour rejouer le même tirage)",
        value="",
        placeholder="laisser vide pour du pur hasard",
    )

    if seed_input.strip() == "":
        seed_value = None
    else:
        try:
            seed_value = int(seed_input)
        except ValueError:
            seed_value = sum(ord(c) for c in seed_input)

    st.markdown("---")
    st.markdown("**Nombre de glyphes max** (si activés)")
    max_glyphs = st.slider("Glyphes", min_value=1, max_value=3, value=1)

    st.markdown("---")
    st.caption("Made in Cyber Opera 🌀")

# Nombre de cartes selon le mode
CARDS_PER_MODE = {
    "Scène en 3 actes": 3,
    "Coup de projecteur": 1,
    "Duo de personnages": 2,
    "Hack en direct": 4,
    "Voyage initiatique": 5,
    "Diva & Coulisses": 3,
    "Scène-éclair": 2,
    "Libre": 3,
}

n_cards = CARDS_PER_MODE.get(mode, 3)

col_left, col_right = st.columns([2, 3])

with col_left:
    st.subheader("🎲 Tirage")
    if st.button("Tirer les cartes et les glyphes", type="primary"):
        # Tirages
        drawn_cards = draw_cards(n_cards, seed=seed_value)
        drawn_glyphs = draw_glyphs(
            min(max_glyphs, len(GLYPHS)), seed=seed_value
        ) if use_glyphs else []

        st.session_state["drawn_cards"] = drawn_cards
        st.session_state["drawn_glyphs"] = drawn_glyphs

# Récupération des tirages
drawn_cards = st.session_state.get("drawn_cards", [])
drawn_glyphs = st.session_state.get("drawn_glyphs", [])

with col_left:
    if drawn_cards:
        st.markdown("### 🃏 Cartes tirées")
        for c in drawn_cards:
            st.markdown(
                f"**{c['emoji']} Carte {c['id']} – {c['name']}**  \n"
                f"*Famille : {c['family']} · Rôle : {c['role']}*  \n"
                f"_{', '.join(c['keywords'])}_"
            )
    else:
        st.info("Clique sur **« Tirer les cartes et les glyphes »** pour lancer une scène.")

    if drawn_glyphs:
        st.markdown("### 🌀 Glyphes en jeu")
        for g in drawn_glyphs:
            st.markdown(
                f"**{g['emoji']} {g['name']}** – {g['role']}  \n"
                f"_Style : {g['style']}_"
            )

with col_right:
    st.subheader("✨ Génération de scène")

    if drawn_cards:
        summary = generate_scene_summary(mode, drawn_cards, drawn_glyphs)
        st.markdown(summary)
    else:
        st.markdown(
            "Ici s’affichera une **proposition de scène**, un mini-synopsis ou un "
            "angle de lecture, généré à partir des cartes et des glyphes."
        )

    st.markdown("---")
    st.markdown("### 📝 Espace de notes")
    st.text_area(
        "Tu peux écrire ici ta version de la scène, des dialogues, ou ce que ça t’inspire :",
        height=200,
    )
