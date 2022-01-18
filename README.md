# DiscordOpenAI
Petite application permettant de déployer un bot discord utilisant l'API d'OpenAI

Lancer l'environnement (Script/activate.bat) 

Variables d'environnement : (conf.ini)
    openai_api_key (OpenAI API token)
    discord_token (Token du bot discord)

Dépendances : 
    pip install openai
    pip install discord

Notez que l'utilisation de données venant de l'API OpenAI est limitée.

Lancement : py bot.ini

Commandes: 
!help
!generate sujet nombre_de_tokens

![Apercu](/screenexample.png?raw=true "Apercu")