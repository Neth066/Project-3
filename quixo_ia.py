# quixo_ia.py
from quixo import Quixo, QuixoError
import random

class QuixoIA(Quixo):
    def valider_diagonale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        # Exemple simplifié de validation pour diagonale principale
        joueur = None
        count = 0
        for i in range(len(plateau)):
            if plateau[i][i] != ' ' and (joueur is None or plateau[i][i] == joueur):
                joueur = plateau[i][i]
                count += 1
            else:
                break
        if count == nb_pions:
            return {joueur: [[[1, 1], [5, 5]]]}
        return {}

    def valider_horizontale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        # Exemple simplifié
        results = {}
        for i, row in enumerate(plateau):
            count = 0
            joueur = None
            for j, cell in enumerate(row):
                if cell != ' ' and (joueur is None or cell == joueur):
                    joueur = cell
                    count += 1
                else:
                    count = 0
                    joueur = None
                if count == nb_pions:
                    if joueur not in results:
                        results[joueur] = []
                    results[joueur].append([[i + 1, j - nb_pions + 2], [i + 1, j + 1]])
        return results

    def valider_verticale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        # Exemple simplifié
        results = {}
        for j in range(len(plateau[0])):
            count = 0
            joueur = None
            for i in range(len(plateau)):
                if plateau[i][j] != ' ' and (joueur is None or plateau[i][j] == joueur):
                    joueur = plateau[i][j]
                    count += 1
                else:
                    count = 0
                    joueur = None
                if count == nb_pions:
                    if joueur not in results:
                        results[joueur] = []
                    results[joueur].append([[i - nb_pions + 2, j + 1], [i + 1, j + 1]])
        return results

    def partie_terminée(self):
        # Vérifier toutes les lignes, colonnes, et diagonales
        for check in [self.valider_diagonale, self.valider_horizontale, self.valider_verticale]:
            results = check(self.plateau)
            if results:
                return list(results.keys())[0]
        return None

    def jouer_le_coup(self, pion):
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        # Choix de coup simple: choisir aléatoirement un coup valide
        coups_possibles = self.obtenir_coups_valides(pion)
        if not coups_possibles:
            raise QuixoError("Aucun coup possible.")
        coup_choisi = random.choice(coups_possibles)
        self.deplacer_pion(*coup_choisi)
        return coup_choisi
