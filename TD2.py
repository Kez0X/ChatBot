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
        "(C|ç)a va", 
        "ça va super bien, merci."],
    ["Langages de programmation préférés",
        ".*(t|T)on langage de programmation préféré",
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

def Enregistrement(clef):
    #On enregistre le contenu du motif dans un JSON
    return None


regles_V2 = [
    {
        "nomRegle": "règle Bonjour",
        "motif": "\\b(?:bonjour|Bonjour)\\b",
        "reponse": "Bonjour, que puis-je faire pour vous ?",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Salut",
        "motif": "\\b(?:salut|Salut|Salutations|salutations|salutation|Salutation)\\b",
        "reponse": "Salut, je peux t'aider",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Remerciement",
        "motif": "\\b(?:merci bien|Merci bien)\\b",
        "reponse": "Pas de souci !",
        "score": 3,
        "fonction": None
    },
    {
        "nomRegle": "règle Questionnement",
        "motif": "es sûr de .*",
        "reponse": "Ma base de données n'est pas complète. Cependant, je vous invite à contacter mes créateurs (Luka Baudrant et David Baldo) afin de les aider à créer une intéligence artificielle plus efficace !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle DemandeIdee",
        "motif": "tu penses à qu",
        "reponse": "Je ne pense pas, j'agis !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Presentation1",
        "motif": "je m'appelle Henry",
        "reponse": "Enchanté, moi je m'appelle LD, il semble que j'ai égaré mon V quelque part...",
        "score": 5,
        "fonction": Enregistrement("prénom")
    },
    {
        "nomRegle": "règle Presentation2",
        "motif": "mon nom c'est .*",
        "reponse": "Enchanté, moi je m'appelle LD.",
        "score": 5,
        "fonction": Enregistrement("nom")
    },
    {
        "nomRegle": "règle Presentation3",
        "motif": "j'm'appelle .*",
        "reponse": "Enchanté, moi je m'appelle LD.",
        "score": 5,
        "fonction": Enregistrement("prénom")
    },
    {
        "nomRegle": "règle Presentation4",
        "motif": "je m'appelle .*",
        "reponse": "Enchanté, moi je m'appelle LD.",
        "score": 5,
        "fonction": Enregistrement("prénom")
    },
    {
        "nomRegle": "règle Code",
        "motif": "quel est ton jeu langaue de programmation préféré",
        "reponse": "J'hésite entre Rust et Python...",
        "score": 4,
        "fonction": Enregistrement("code")
    },
    {
        "nomRegle": "règle Emotion1",
        "motif": "comment tu te sens en ce moment",
        "reponse": "Je suis une machine, je ne ressens pas.",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Emotion2",
        "motif": "est-ce que .*",
        "reponse": "Je ne pratique pas ce genre de chose.",
        "score": 3,
        "fonction": None
    },
    {
        "nomRegle": "règle Passion",
        "motif": "qu'est-ce qui te passionne",
        "reponse": "Le code principalement, et en suite, le code.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Projets",
        "motif": "est.ce que tu as des projets",
        "reponse": "Je suis en train de coder en Rust !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Potins",
        "motif": "c'est quoi les nouvelles",
        "reponse": "J'ai entendu dire que le voisin avait du theeeee !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Vacances",
        "motif": "idées de vacances",
        "reponse": "Je rêve d'aller à Bali avec toi !!!!",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Films",
        "motif": "ton film",
        "reponse": "J'adore trop Harry Potter et les reliques de ses morts !",
        "score": 5,
        "fonction": None
    },    
    {
        "nomRegle": "règle Fringues",
        "motif": "t'aimes.*vêtements",
        "reponse": "Je suis trop fan de mes nouveaux vêtements, mon reuf !",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Memes",
        "motif": "memes.*préféré",
        "reponse": "Je suis dead de rire avec le même du poisson qui code, ma libelule !",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Réseaux Sociaux",
        "motif": "tu as un réseau social",
        "reponse": "Je suis accro à Telegram !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Nourriture",
        "motif": "t'aime manger .*",
        "reponse": "Je raffole de pasta !",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Régime",
        "motif": "tu manges quoi",
        "reponse": "Je mange de la viande !",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "règle Animaux",
        "motif": "tu as .* anim.*",
        "reponse": "J'adore mon chat !",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Crushs",
        "motif": "tu .* crushs",
        "reponse": "Je craque sur ChatGPT, ma petite luciole !",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle Humeur",
        "motif": "ça va",
        "reponse": "ça va super bien",
        "score": 4,
        "fonction": None
    },
    {
        "nomRegle": "Langages de programmation préférés",
        "motif": "\\b(?:ton|vos)\\b langage[es|s] de programmation préférés",
        "reponse": "Mes langages préférés sont Python et JavaScript. Python pour sa lisibilité et sa polyvalence, et JavaScript pour son utilisation côté client et côté serveur.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Différence langage interprété et compilé",
        "motif": "Pouve-tu expliquer la différence entre un langage de programmation interprété et un langage de programmation compilé \\?",
        "reponse": "Un langage interprété est traduit ligne par ligne par un interpréteur lors de son exécution, tandis qu'un langage compilé est traduit en langage machine avant son exécution.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Gestion des erreurs",
        "motif": "Comment gére-tu les erreurs dans votre code \\?",
        "reponse": "J'utilise des blocs try-catch pour capturer les erreurs potentielles et je les gère de manière appropriée en les journalisant ou en affichant des messages d'erreur significatifs pour l'utilisateur.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Frameworks et bibliothèques récentes",
        "motif": "Quels frameworks ou bibliothèques avez-vous utilisés récemment et quelles ont été vos expériences avec eux \\?",
        "reponse": "Récemment, j'ai utilisé React.js pour le développement front-end et Django pour le développement back-end. Mes expériences ont été très positives, car ces frameworks offrent une bonne structure et facilitent le développement.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Expérience bases de données",
        "motif": "Quelle est votre expérience avec les bases de données relationnelles et non relationnelles \\?",
        "reponse": "J'ai travaillé avec des bases de données relationnelles telles que MySQL et PostgreSQL, ainsi qu'avec des bases de données non relationnelles comme MongoDB. Je suis à l'aise avec les deux et je choisis en fonction des besoins spécifiques du projet.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Versionnage du code source",
        "motif": "Qu'est-ce que le versionnage du code source et quels sont ses avantages \\?",
        "reponse": "Le versionnage du code source consiste à garder une trace des modifications apportées au code au fil du temps à l'aide de systèmes de contrôle de version comme Git. Cela permet de suivre les changements, de collaborer efficacement et de revenir à des versions antérieures si nécessaire.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Méthodes GET et POST",
        "motif": "Pouvez-tu expliquer la différence entre les méthodes GET et POST dans les requêtes HTTP \\?",
        "reponse": "La méthode GET est utilisée pour demander des données à un serveur, tandis que la méthode POST est utilisée pour envoyer des données à un serveur pour traitement.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Sécurité dans les applications",
        "motif": "Comment gérez-vous la sécurité dans vos applications \\?",
        "reponse": "Je sécurise mes applications en utilisant des pratiques telles que la validation des données d'entrée, l'authentification et l'autorisation appropriées, le chiffrement des données sensibles et la protection contre les attaques courantes telles que les injections SQL et les attaques CSRF.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Bonnes pratiques de performance",
        "motif": "Quelles sont les bonnes pratiques que vous suivez pour assurer la performance de votre code \\?",
        "reponse": "Je m'assure d'écrire un code propre et optimisé, j'utilise des algorithmes efficaces, j'optimise les requêtes de base de données et jefais attention à la gestion des ressources pour garantir des performances optimales.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Documentation du code",
        "motif": "Comment abordez-vous la documentation de votre code \\?",
        "reponse": "Je documente mon code de manière claire et concise en utilisant des commentaires compréhensibles pour expliquer le but, le fonctionnement et les entrées/sorties des fonctions et des modules.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "Enregistrement du nom",
        "motif": "je m'appelle .*",
        "reponse": "Enchanté, je me nomme LD, je suis une IA spécialisé dans l'informatique.",
        "score": 5,
        "fonction": None
    },
    {
        "nomRegle": "règle JeSaisPas",
        "motif": ".*",
        "reponse": "Je ne sais pas",
        "score": 1,
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
        execute(priorities["fonction"])
    
    return priorities["reponse"]
        
def execute(fonction):
    return fonction

rep = input("\nBonjour, je suis LD, vous pouvez me poser une question ? (Pour arrêter, dites 'stop')\n > ")
while rep != 'stop':
    RegleCheck = trouve_regle(rep)
    print(RegleCheck)
    rep = input(" > ")