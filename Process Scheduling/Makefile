# Nom du programme
PROGRAM = rr.py

# Commande Python
PYTHON = python3

# Règle par défaut pour exécuter le programme
run:
    $(PYTHON) $(PROGRAM)

# Règle pour nettoyer les fichiers temporaires
clean:
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete

# Règle pour installer les dépendances depuis requirements.txt
install:
    pip install -r requirements.txt

# Règle pour vérifier la syntaxe avec pylint
lint:
    pylint $(PROGRAM)

# Règle pour tester le code avec pytest
test:
    pytest
