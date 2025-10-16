# LinkedIn-like Backend API

Un backend complet type LinkedIn construit avec Flask, SQLAlchemy et PostgreSQL.

## 🚀 Fonctionnalités

### Authentification
- ✅ Inscription d'utilisateurs
- ✅ Connexion avec JWT
- ✅ Protection des routes avec middleware

### Profils Utilisateurs
- ✅ Profils professionnels complets
- ✅ Photo de profil et bannière
- ✅ Headline et bio
- ✅ Localisation et industrie
- ✅ Recherche d'utilisateurs

### Expérience Professionnelle
- ✅ Historique de travail
- ✅ Postes actuels et passés
- ✅ Descriptions de rôles

### Éducation
- ✅ Historique académique
- ✅ Diplômes et formations

### Posts/Feed
- ✅ Création de posts (texte, image, vidéo, articles)
- ✅ Feed personnalisé
- ✅ Likes et commentaires
- ✅ Partages et statistiques

### Connexions
- ✅ Demandes de connexion
- ✅ Accepter/Rejeter connexions
- ✅ Gestion du réseau professionnel

### Messages
- ✅ Messagerie directe entre utilisateurs
- ✅ Pièces jointes
- ✅ Statut de lecture

### Offres d'Emploi
- ✅ Publication d'offres
- ✅ Recherche d'emplois
- ✅ Candidatures

### Compétences
- ✅ Ajout de compétences
- ✅ Endorsements

## 📋 Prérequis

- Python 3.8+
- PostgreSQL (Neon ou local)
- pip

## 🔧 Installation

1. **Cloner le projet** (si applicable)
```bash
cd backend
```

2. **Créer un environnement virtuel**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. **Installer les dépendances**
```powershell
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Modifiez le fichier `.env` avec vos informations de base de données.

5. **Initialiser la base de données**
```powershell
python application.py
```

Les tables seront créées automatiquement au premier lancement.

## 🏃 Démarrage

```powershell
python application.py
```

Le serveur démarrera sur `http://localhost:5000`

## 📚 API Endpoints

### Authentication
```
POST /api/auth/register    - Inscription
POST /api/auth/login       - Connexion
```

### Users
```
GET  /api/users/me         - Mon profil
PUT  /api/users/me         - Modifier mon profil
GET  /api/users/search     - Rechercher utilisateurs
GET  /api/users/:id        - Voir un profil
```

### Posts
```
POST   /api/posts/              - Créer un post
GET    /api/posts/:id           - Voir un post
DELETE /api/posts/:id           - Supprimer un post
POST   /api/posts/:id/like      - Liker un post
GET    /api/posts/feed          - Mon feed
GET    /api/posts/user/:id      - Posts d'un utilisateur
```

### Connections
```
POST /api/connections/request        - Envoyer une demande
POST /api/connections/:id/accept     - Accepter
POST /api/connections/:id/reject     - Rejeter
GET  /api/connections/my-connections - Mes connexions
GET  /api/connections/pending        - Demandes en attente
```

### Health Check
```
GET /health     - Statut du serveur
GET /api        - Info API
```

## 🔐 Authentification

Toutes les routes (sauf `/auth/register` et `/auth/login`) nécessitent un token JWT dans le header:

```
Authorization: Bearer <votre_token>
```

## 📝 Exemples d'utilisation

### 1. Inscription
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePassword123",
    "first_name": "John",
    "last_name": "Doe",
    "headline": "Software Engineer",
    "location": "Paris, France"
  }'
```

### 2. Connexion
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePassword123"
  }'
```

### 3. Créer un post
```bash
curl -X POST http://localhost:5000/api/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "content": "Excited to announce my new position!",
    "post_type": "TEXT"
  }'
```

## 🗄️ Structure de la Base de Données

### Tables principales:
- **users** - Profils utilisateurs
- **experiences** - Historique professionnel
- **education** - Formations académiques
- **skills** - Compétences
- **posts** - Publications
- **comments** - Commentaires
- **connections** - Connexions réseau
- **messages** - Messages directs
- **jobs** - Offres d'emploi

## 📁 Structure du Projet

```
backend/
├── application.py              # Point d'entrée
├── requirements.txt            # Dépendances
├── .env                        # Variables d'environnement
├── config/
│   └── database_config.py     # Configuration DB
├── model/
│   ├── base.py                # Modèle de base
│   ├── users.model.py         # Modèle utilisateur
│   ├── posts.model.py         # Modèle posts
│   ├── connections.model.py   # Modèle connexions
│   ├── experience.model.py    # Modèle expérience
│   ├── education.model.py     # Modèle éducation
│   ├── skills.model.py        # Modèle compétences
│   ├── comments.model.py      # Modèle commentaires
│   ├── jobs.model.py          # Modèle emplois
│   └── messages.model.py      # Modèle messages
├── services/
│   ├── auth.service.py        # Service authentification
│   ├── user.service.py        # Service utilisateur
│   ├── post.service.py        # Service posts
│   └── connection.service.py  # Service connexions
├── controller/
│   ├── auth.controller.py     # Contrôleur auth
│   ├── user.controller.py     # Contrôleur utilisateur
│   ├── post.controller.py     # Contrôleur posts
│   └── connection.controller.py # Contrôleur connexions
└── routes/
    ├── __init__.py            # Enregistrement des routes
    ├── middleware.py          # Middleware auth
    ├── auth.routes.py         # Routes auth
    ├── user.routes.py         # Routes utilisateur
    ├── post.routes.py         # Routes posts
    └── connection.routes.py   # Routes connexions
```

## 🛡️ Sécurité

- ✅ Mots de passe hashés avec bcrypt
- ✅ Authentication JWT
- ✅ Protection CORS configurée
- ✅ Validation des entrées
- ✅ SSL/TLS pour la base de données

## 🚧 Améliorations Futures

- [ ] Système de notifications en temps réel
- [ ] Upload de fichiers (images, vidéos)
- [ ] Système de recommandations
- [ ] Analytics et statistiques
- [ ] Système de messagerie en temps réel (WebSockets)
- [ ] Recherche avancée avec filtres
- [ ] Système de reporting
- [ ] API rate limiting

## 📄 Licence

Ce projet est à usage éducatif.

## 👨‍💻 Développement

Pour contribuer au projet:

1. Créer une branche pour votre fonctionnalité
2. Faire vos modifications
3. Tester localement
4. Soumettre une pull request

---

**Fait avec ❤️ pour apprendre le développement backend**
