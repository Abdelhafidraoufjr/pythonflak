# Guide de Démarrage Rapide

## Étapes pour lancer l'application

### 1. Activer l'environnement virtuel
```powershell
.\venv\Scripts\activate
```

### 2. Installer les dépendances
```powershell
pip install -r requirements.txt
```

### 3. Lancer l'application
```powershell
python application.py
```

Vous devriez voir:
```
==============================================================
Starting LinkedIn-like Backend Server
==============================================================

✓ Database connection successful!
✓ Connected to: intelli_backend_db at ep-patient-lake-a816cbtn-pooler.eastus2.azure.neon.tech:5432
✓ Database tables created/verified successfully!
✓ All routes registered successfully
```

### 4. Tester l'API

Ouvrez votre navigateur et allez sur:
- http://localhost:5000/health
- http://localhost:5000/api

Ou utilisez Postman/curl pour tester les endpoints.

## Test avec curl

### Inscription
```bash
curl -X POST http://localhost:5000/api/auth/register -H "Content-Type: application/json" -d "{\"email\":\"test@example.com\",\"password\":\"password123\",\"first_name\":\"John\",\"last_name\":\"Doe\"}"
```

### Connexion
```bash
curl -X POST http://localhost:5000/api/auth/login -H "Content-Type: application/json" -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

Récupérez le token et utilisez-le pour les autres requêtes:

```bash
curl -X GET http://localhost:5000/api/users/me -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Structure des Modèles

Votre base de données contient maintenant:

1. **users** - Profils utilisateurs avec toutes les informations professionnelles
2. **experiences** - Historique de travail
3. **education** - Formations académiques
4. **skills** - Compétences professionnelles
5. **posts** - Publications type LinkedIn feed
6. **comments** - Commentaires sur les posts
7. **connections** - Réseau professionnel (connexions)
8. **messages** - Messagerie directe
9. **jobs** - Offres d'emploi

Toutes les tables sont créées automatiquement au premier lancement!

## Bon développement! 🚀
