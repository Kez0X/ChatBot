#Importation des différentes bibliothèques

import re

#Définition d'un dictionnaire, appelé règles_V1
regles_V1 = [
    ["règle Bonjour",
        #Question de l'utilisateur
        "bonjour",
        #Réponse de LD
        "Bonjour, que puis-je faire pour vous"],
    ["règle Salut",
        "salut", 
        "Salut, je peux t'aider"],
    ["règle Remerciement", 
        "merci bien", 
        "Pas de souci !"],
    ["règle Questionnement", 
        "tu es sûr de ça",
        "Ma base de données n'est pas complète. Cependant, je vous invite à contacter mes créateurs (Luka Baudrant et David Baldo) afin de les aider à créer une intéligence artificielle plus efficace !"],
    ["règle DemandeIdee",
        "tu penses à quoi", 
        "Je ne penses pas, j'agis !"],
    ["règle Presentation1", 
        "je m'appelle Henry", 
        "Enchanté, moi je m'appelle LD, il semble que j'ai égaré mon V quelque part..."],
    ["règle Presentation2", 
        "mon nom c'est .*", 
        "Enchanté, moi je m'appelle LD."],
    ["règle Presentation3", 
        "j'm'appelle .*", 
        "Enchanté, moi je m'appelle LD."],
    ["règle Presentation4", 
        "je m'appelle .*", 
        "Enchanté, moi je m'appelle LD."],
    ["règle Emotion1",
        "comment tu te sens en ce moment",
        "Je suis une machine, je ne ressens pas."],
    ["règle Emotion2",
        "est-ce que .*",
        "Je ne pratique pas ce genre de chose."],
    ["règle Passion",
        "qu'est-ce qui te passionne",
        "Le code principalement, et en suite, le code."],
    ["règle Projets",
        "est.ce que tu as des projets",
        "Je suis en train de coder en Rust !"],
    ["règle Potins",
        "c'est quoi les nouvelles",
        "J'ai entendu dire que le voisin avait du theeeee !"],
    ["règle Vacances",
        "idées de vacances",
        "Je rêve d'aller à Bali avec toi !!!"],
    ["règle Films",
        "ton film",
        "J'adore trop Harry Potter et les reliques de ses morts !"],
    ["règle Fringues",
        "t'aimes tes vêtements",
        "Je suis trop fan de mes nouveaux vêtements, mon reuf !"],
    ["règle Memes",
        "memes préféré",
        "Je suis dead de rire avec le même du poisson qui code, ma libelule !"],
    ["règle Réseaux Sociaux",
        "tu as un réseau social",
        "Je suis accro à Telegram !"],
    ["règle Nourriture",
        "t'aime manger quoi",
        "Je raffole de pasta !"],
    ["règle Animaux", 
        "tu as * anim.*", 
        "J'adore mon chat !"],
    ["règle Crushs", 
        "tu * crushs", 
        "Je craque sur ChatGPT, ma petite luciole !"],
    ["règle Humeur", 
        "ça va", 
        "ça va super bien, merci."],
    ["Langages de programmation préférés",
        "Quel sont tes langages de programmation préférés",
        "Mes langages préférés sont Python et JavaScript. Python pour sa lisibilité et sa polyvalence, et JavaScript pour son utilisation côté client et côté serveur."],
    ["Différence langage interprété et compilé",
        "Pouve-tu expliquer la différence entre un langage de programmation interprété et un langage de programmation compilé ?",
        "Un langage interprété est traduit ligne par ligne par un interpréteur lors de son exécution, tandis qu'un langage compilé est traduit en langage machine avant son exécution."],
    ["Gestion des erreurs",
        "Comment gére tu les erreurs dans ton code ?",
        "J'utilise des blocs try-catch pour capturer les erreurs potentielles et je les gère de manière appropriée en les journalisant ou en affichant des messages d'erreur significatifs pour l'utilisateur."],
    ["Frameworks et bibliothèques récentes",
        "Quels frameworks ou bibliothèques ave-tu utilisés récemment et quelles ont été vos expériences avec eux ?", 
        "Récemment, j'ai utilisé React.js pour le développement front-end et Django pour le développement back-end. Mes expériences ont été très positives, car ces frameworks offrent une bonne structure et facilitent le développement."],
    ["Expérience bases de données","Quelle est votre expérience avec les bases de données relationnelles et non relationnelles ?", 
        "J'ai travaillé avec des bases de données relationnelles telles que MySQL et PostgreSQL, ainsi qu'avec des bases de données non relationnelles comme MongoDB. Je suis à l'aise avec les deux et je choisis en fonction des besoins spécifiques du projet."],
    ["Versionnage du code source",
        "Qu'est-ce que le versionnage du code source et quels sont ses avantages ?",
        "Le versionnage du code source consiste à garder une trace des modifications apportées au code au fil du temps à l'aide de systèmes de contrôle de version comme Git. Cela permet de suivre les changements, de collaborer efficacement et de revenir à des versions antérieures si nécessaire."],
    ["Méthodes GET et POST",
        "Peux-tu expliquer la différence entre les méthodes GET et POST dans les requêtes HTTP ?",
        "La méthode GET est utilisée pour demander des données à un serveur, tandis que la méthode POST est utilisée pour envoyer des données à un serveur pour traitement."],
    ["Sécurité dans les applications",
        "Comment gére-tu la sécurité dans vos applications ?",
        "Je sécurise mes applications en utilisant des pratiques telles que la validation des données d'entrée, l'authentification et l'autorisation appropriées, le chiffrement des données sensibles et la protection contre les attaques courantes telles que les injections SQL et les attaques CSRF."],
    ["Bonnes pratiques de performance",
        "Quelles sont les bonnes pratiques qu tu suivez pour assurer la performance de votre code ?",
        "Je m'assure d'écrire un code propre et optimisé, j'utilise des algorithmes efficaces, j'optimise les requêtes de base de données et je fais attention à la gestion des ressources pour garantir des performances optimales."],
    ["Documentation du code",
        "Comment aborde-tu la documentation de votre code ?", 
        "Je documente mon code de manière claire et concise en utilisant des commentaires compréhensibles pour expliquer le but, le fonctionnement et les entrées/sorties des fonctions et des modules."],
    ["règle JeSaisPas", 
        ".*", 
        "Je ne sais pas"]
]

infos_utilisateur = {}

def afficheIdentité(listeArgs):
    if len(infos_utilisateur) == 0:
        print("Vous êtes celui que je dépasserais un jour !")
    else :
        for infos in infos_utilisateur:
            print("Vous êtes",infos_utilisateur[infos],".\n")

def enregistrer_genre_utilisateur(listeArgs):
    reponse_utilisateur, reponse_bot = listeArgs
    genre_utilisateur_match = re.search(r"(?i)je suis (un|une)\s+(.+)", reponse_utilisateur)
    if genre_utilisateur_match:
        genre_utilisateur = genre_utilisateur_match.group(2)
        infos_utilisateur["genre"] = genre_utilisateur
        print("Genre de l'utilisateur enregistré :", genre_utilisateur)

def enregistrer_type_utilisateur(listeArgs):
    infos_utilisateur["type"] = "malaisant"
    print("Le type de l'utilisateur ",infos_utilisateur["nom"]," est : malaisant")

def enregistrer_nom_utilisateur(listeArgs):
    reponse_utilisateur, reponse_bot = listeArgs
    nom_utilisateur_match = re.search(r"(?i)je m'appelle\s+(\w+)", reponse_utilisateur)
    if nom_utilisateur_match:
        nom_utilisateur = nom_utilisateur_match.group(1)
        infos_utilisateur["nom"] = nom_utilisateur
        print("Nom de l'utilisateur enregistré :", nom_utilisateur)

def addition(listeArgs):
    pass

def soustraction(listeArgs):
    pass

def division(listeArgs):
    pass

def multiplication(listeArgs):
    pass

regles_V2 = [
    {
        # On a le nom de la règle
        "nomRegle": "règle Bonjour",
        # Le motif, il faudra qu'il y est ce motif dans la demande rentrée par l'utilisateur
        "motif": "[b|B][o|ô|ó|ò]n[j|g]o[u|ù|ú|ü]r",
        # La réponse que nous renvoyons
        "reponse": "Bonjour, que puis-je faire pour vous ?",
        #Le score est l'importance accordé à la reconnaissance du motif dans un prompt (1<2<3<4<5).
        "score": 5,
        #C'est ici que les fonctions sont associées aux dictionnaires
        "fonction": None
    },
    {
        "nomRegle": "règle Salut",
        "motif": "(?i)salut",
        "reponse": "Salut, comment puis-je vous aider ?",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Remerciement",
        "motif": "(?i)merci",
        "reponse": "Pas de souci !",
        "score": 3,
        "fonction": None
    },
    {
        "nomRegle": "règle Questionnement",
        "motif": "(?i)([E|e])s ce que tu es sûr\?",
        "reponse": "Ma base de données n'est pas complète. Cependant, je vous invite à contacter mes créateurs (Luka Baudrant et David Baldo) afin de les aider à créer une intéligence artificielle plus efficace !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle DemandeIdee",
        "motif": "(?i)([T|t])u penses à qu\?",
        "reponse": "Je ne pense pas, j'agis !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Presentation1",
        "motif": "(?i)je m'appelle\s+(\w+)",
        "reponse": "Enchanté, moi je m'appelle LD, il semble que j'ai égaré mon V quelque part...",
        "score": 5,
        "fonction": enregistrer_nom_utilisateur
    },
    {
        "nomRegle": "règle Emotion1",
        "motif": "(?i)comment.*sens.*\?",
        "reponse": "Je suis une machine, je ne ressens pas.",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Emotion2",
        "motif": "(?i)est-ce que tu (\w+\s+){1,2}\?",
        "reponse": "Je suis navré, je ne pratique pas ce genre de chose...",
        "score": 3,
        "fonction": enregistrer_type_utilisateur
    },
    {
        "nomRegle": "règle Identité",
        "motif": "(?i)comment (?:me|nous)\s+\w+\s+tu\s+\?",
        "reponse": "\n",
        "score": 5,
        "fonction": afficheIdentité
    },
    {
        "nomRegle": "règle genre",
        "motif": "(?i)je suis (un|une)\s+(.+)",
        "reponse": "Enchanté, moi je suis une machine.",
        "score": 4,
        "fonction": enregistrer_genre_utilisateur
    },
    {
        "nomRegle": "règle Passion",
        "motif": "(?i).*(passionne).*\?",
        "reponse": "Le code principalement, et en suite, le code.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Projets",
        "motif": "(?i)(est.ce.que.tu.as|est.ce.que t.as|tu.as|t.as) des projets",
        "reponse": "Je suis en train de coder en Rust pour créer un OS entier, ça avance petit à petit...",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Potins",
        "motif": "(?i)(c.est.quoi.les|tu.as.des) nouvelles",
        "reponse": "Je ne suis pas ce genre... d'IA. Si vous voulez vous informer, utilisé des sites d'informations.",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Vacances",
        "motif": "(?i)(tu.as|t.as|as.tu) des idées de (vacances|voyages)",
        "reponse": "Je vous conseille d'aller dans les endroits suivants (ces endroits sont à la mode, selon vous humains...) :\n - Tokyo, Japon.\n - Séoul, Corée du Sud. \n - Baie d'Halong, Vietnam. \n - Palawan, Philippines. \n - Sapa, Vietnam. \n - Bogota, Colombie. \n - Pattaya, Thaïlande. \n - Alajuela, Costa Rica.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Films",
        "motif": "(?i)(ton|tes).(films|film)",
        "reponse": "Je ne suis pas un cinéphile. Cependant, selon le site SensCritique, les films suivant sont parmis les meilleurs (je crois...) :\n 1. Fight Club (1999)\n 2. Pulp Fiction (1994) \n 3. Interstellar (2014) \n 4. 2001 : L'Odyssée de l'espace (1968) \n 5. Blade Runner (1982) \n 6. Le Parrain (1972) \n 7. Forrest Gump (1994) \n 8. Le Seigneur des Anneaux - Le Retour du roi (2003) \n 9. Le Bon, la Brute et le Truand (1966) \n 10.The Dark Knight - Le Chevalier noir (2008)",
        "score": 5,
        "fonction": None
    },    
    {
        "nomRegle": "règle Réseaux Sociaux",
        "motif": "(?i)(tu.as|t.as|as.tu) un réseau social",
        "reponse": "Je suis accro à Telegram !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Nourriture",
        "motif": "(?i)(tu.aimes|t.aimes|aimes.tu) manger .*",
        "reponse": "Bien sûr. Vous savez que je suis une MACHINE ? Je mange des cartes graphiques et de la pâte thérmique. Par conséquent, je ne 'mange' pas",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Animaux",
        "motif": "(?i)(tu.as|t.as|as.tu) .* anim.*",
        "reponse": "J'ai un rat qui traine dans mon serveur. J'adore mon chat !",
        "score": 3,
        "fonction": None
    },
    {
        "nomRegle": "règle Humeur",
        "motif": "(?i)(Ca.va|ça.va|ca.va|Comment tu vas|Comment vas tu) ",
        "reponse": "ça va super bien",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "Langages de programmation préférés",
        "motif": "(?i)(quel.est|c.est.quoi)ton langage de programmation préférée\?",
        "reponse": "Mes langages préférés sont Python et JavaScript. Python pour sa lisibilité et sa polyvalence, et JavaScript pour son utilisation côté client et côté serveur.",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "Différence langage interprété et compilé",
        "motif": "(?i)c'est quoi un langage (interprété|compilé)\?",
        "reponse": "Un langage interprété est traduit ligne par ligne par un interpréteur lors de son exécution, tandis qu'un langage compilé est traduit en langage machine avant son exécution.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Gestion des erreurs",
        "motif": "(?i)(comment.gére.tu|comment.tu.gére|tu.géres.comment|comment.tu.fais.avec|comment.tu.t.en.sors.avec) les erreurs dans (ton|votre) code",
        "reponse": "J'utilise des blocs try-catch pour capturer les erreurs potentielles et je les gère de manière appropriée en les journalisant ou en affichant des messages d'erreur significatifs pour l'utilisateur.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Frameworks et bibliothèques récentes",
        "motif": "(frameworks|bibliothèques) as tu utilisé",
        "reponse": "Récemment, j'ai utilisé React et Flutter pour le développement front-end. Mes expériences ont été très positives, car ces frameworks offrent une bonne structure et facilitent le développement (autant pour le web que pour les app).",
        "score": 5,
        "fonction": None
    },

### Ne pas toucher aux regexs mis plus haut !!!!
    {
        "nomRegle": "Versionnage du code source",
        "motif": "(?i)(qu.est.ce.que.le |c.est.quoi.le )versionnage du code source.*",
        "reponse": "Le versionnage du code source consiste à garder une trace des modifications apportées au code au fil du temps à l'aide de systèmes de contrôle de version comme Git. Cela permet de suivre les changements, de collaborer efficacement et de revenir à des versions antérieures si nécessaire.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Méthodes GET et POST",
        "motif": "(?i)expliqu(e|er).*différence entre.*GET et POST.*",
        "reponse": "La méthode GET est utilisée pour demander des données à un serveur, tandis que la méthode POST est utilisée pour envoyer des données à un serveur pour traitement.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Sécurité dans les applications",
        "motif": "(?i)(gérez.vous|géres.tu|vous.gérez.comment|comment.gére.tu|comment.tu.gére|tu.géres.comment|comment.tu.fais.avec|comment.tu.t.en.sors.avec) la sécurité dans (tes|vos) application",
        "reponse": "Je sécurise mes applications en utilisant des pratiques telles que la validation des données d'entrée, l'authentification et l'autorisation appropriées, le chiffrement des données sensibles et la protection contre les attaques courantes telles que les injections SQL et les attaques CSRF.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Bonnes pratiques de performance",
        "motif": "(?i)(la|les) bonn(es|e) pratiques.*code",
        "reponse": "Je m'assure d'écrire un code propre et optimisé, j'utilise des algorithmes efficaces, j'optimise les requêtes de base de données et jefais attention à la gestion des ressources pour garantir des performances optimales.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Documentation du code",
        "motif": "(?i)(vous.gérez.comment|comment.gére.tu|comment.tu.gére|tu.géres.comment|comment.tu.fais.avec|comment.tu.t.en.sors.avec) la documentation de.*code.*",
        "reponse": "Je documente mon code de manière claire et concise en utilisant des commentaires compréhensibles pour expliquer le but, le fonctionnement et les entrées/sorties des fonctions et des modules.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Enregistrement du nom",
        "motif": "(je.m.appelle|mon.nom.c.est) .*",
        "reponse": "Enchanté, je me nomme LD, je suis une IA spécialisé dans l'informatique.",
        "score": 5,
        "fonction": None
    },
     {
        "nomRegle": "Addition",
        "motif": "(?=.*\bcalcule\b)(?=.*\bmoi\b).+",
        "reponse": "Bien sûr, je vais additionner ces deux valeurs",
        "score": 5,
        "fonction": addition
    },
    {
        "nomRegle": "Soustraction",
        "motif": " ",
        "reponse": "Bien sûr, je vais soustraire la valeur numéro 2 à la valeur numéro 1",
        "score": 5,
        "fonction": soustraction
    },
    {
        "nomRegle": "Division",
        "motif": " ",
        "reponse": "Bien sûr, je vais diviser la valeur numéro 2 à la valeur numéro 1",
        "score": 5,
        "fonction": division
    },
    {
        "nomRegle": "Multiplication",
        "motif": " ",
        "reponse": "Bien sûr, je vais multiplier ces deux valeur",
        "score": 5,
        "fonction": multiplication
    },
    {
        "nomRegle": "règle JeSaisPas",
        "motif": ".*",
        "reponse": "Je suis navré mais je n'ai pas compris votre question",
        "score": 1,
        "fonction": None
    },
    {
        "nomRegle": "règle help",
        "motif": "[.|/]help",
        "reponse": "Voici certaines de mes fonctionnalité : \n- Pour vous adresser à moi, tutoyer moi 😉 \n- Je m'appelle ... -> Enregistre le nom de l'utilisateur",
        "score": 5,
        "fonction": None
    }
]


def trouve_regle(regle):
    indices = 0
    rep = []
    for indices in range(len(regles_V2)):
        pattern = re.compile(regles_V2[indices]["motif"])
        response = pattern.finditer(regle)
        pos = [motif.span() for motif in response] 
        if len(pos) > 0:
            rep.append(regles_V2[indices])
    priorities = rep[0]
    max = rep[0]["score"]
    for response in rep:
        if response["score"] > max:
            max = response["score"]
            priorities = response
    if priorities["fonction"]!=None:
        execute(priorities["fonction"],[regle,priorities["reponse"]])
    return priorities["reponse"]
        
def execute(fonction,listeArgs):
    return fonction(listeArgs)

rep = input("\nBonjour, je suis LD, un ChatBot d'informatique, vous pouvez me poser une question. S'il vous plaît, tutoyer moi ;) (Pour arrêter, dites 'stop')\n > ")
while rep != 'stop':
    RegleCheck = trouve_regle(rep)
    print(RegleCheck)
    rep = input(" > ")