# Programme principal pour jouer au jeu Quixo
import argparse
from quixo_ia import QuixoIA

def main():
    parser = argparse.ArgumentParser(description="Quixo")
    parser.add_argument("idul", help="IDUL du joueur")
    parser.add_argument("-p", "--parties", action="store_true", help="Lister les parties existences")
    parser.add_argument("-a", "--automatique", action="store_true", help="Jouer automatiquement")
    args = parser.parse_args()

    game = QuixoIA()
    
    if args.automatique:
        # Implémentation du jeu automatique contre l'ordinateur
        pass

if __name__ == "__main__":
    main()
