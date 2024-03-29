Ce fichier `README.md` décrit brièvement le projet, ses fonctionnalités, la façon de l'utiliser et les auteurs. Il fournit également des conseils sur la manière d'étendre le projet.

# Chatbot LD

Ce projet contient un chatbot simple nommé LD. Le chatbot répond à diverses entrées de l'utilisateur en utilisant des règles prédéfinies.

## Fonctionnalités

- **Salutations:** LD peut saluer l'utilisateur et répondre à des salutations courantes.
- **Réponses spécifiques:** Il peut répondre à des questions spécifiques sur ses préférences, ses activités et ses opinions.
- **Enregistrement des données:** LD peut enregistrer des informations telles que le nom de l'utilisateur.
- **Reconnaissance de motifs:** Il reconnaît les schémas dans les entrées de l'utilisateur pour sélectionner la réponse appropriée.
- **Gestion des erreurs:** Le chatbot gère les erreurs en fournissant une réponse par défaut lorsque la requête de l'utilisateur ne correspond à aucune règle prédéfinie.

## Règles de conversation

Les règles de conversation sont définies dans le fichier Python `LD_chatbot.py`. Elles sont organisées en deux versions, `regles_V1` et `regles_V2`, chacune décrivant les motifs de saisie de l'utilisateur et les réponses correspondantes.

## Utilisation

Pour utiliser le chatbot LD, exécutez le fichier Python `LD_chatbot.py`. Il vous invitera à poser des questions ou à engager une conversation.

```bash
python LD_chatbot.py
```
