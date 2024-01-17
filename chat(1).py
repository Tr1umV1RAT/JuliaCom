#!/usr/bin/env python
# coding: utf-8




import openai

openai.api_key = ""  # Remplacez ceci par votre clé API
openai.api_base = "http://192.168.1.30:1234/v1"  # Adresse du serveur local

def send_message(role, content):
    return {"role": role, "content": content}

# Fonction pour envoyer une requête au modèle d'IA et recevoir une réponse
def chat_with_model(messages):
    completion = openai.ChatCompletion.create(
        model="votre-modele-choisi",  # Remplacez 'votre-modele-choisi' par le nom de votre modèle
        messages=messages
    )
    return completion.choices[0].message['content']

# Exemple de discussion ininterrompue
conversation = [
    send_message("system", "Bonjour, commençons la conversation."),
]

while True:
    user_input = input("Vous: ")  # Attend l'entrée de l'utilisateur
    conversation.append(send_message("user", user_input))  # Ajoute l'entrée utilisateur à la conversation

    response = chat_with_model(conversation)  # Envoie la conversation au modèle et reçoit la réponse
    print(f"Modèle: {response}")  # Affiche la réponse du modèle

    conversation.append(send_message("system", response))




