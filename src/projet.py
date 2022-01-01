
from cell import Cell
from grid import Grid
import sys

def choix_direction(g):
    """
     Permettre au joueur de saisir la direction où il veut se déplacer et son numéro
     
    :param grille: la grille où se déroule le jeu
    :type grille: Grid
    :CU: Aucune
    """
    fini=False
    while fini==False:
        m= input("Entrez votre mouvement 'num,direction' : ou 'q' (quit)")
        if len(m)==1 and m in {'q','Q'}:
            fini=True
            return m
        elif len(m)==3:
            try:
                t=m.split(',')
                assert len(t)==2 and (0<=int(t[0])<g.get_number_of_players()) and (t[1] in {'e','E','s','S','n','N','O','o'})
                fini=True
                return (int(t[0]),t[1])
            except AssertionError:
                print('Veuillez saisir un numéro de joueur valide et une direction valide séparé par une virgule svp')
            except ValueError:
                print('le numero du joueur en chiffre et la direction doivent etre séparé par une virgule svp !')
        else:
            print("veuillez ecrire un mouvement 'num,direction' ou 'q' pour quitter")
        
def move_to_est(g,player):
    """
     cette fonction permet au joueur player de se déplacer vers l'est dans la grille g
     
    :param g: La grille qui représente le jeu
    :type g: Grid
    :param player: un joueur
    :type player: str
    :return: tuple des nouvelles coordonnees du player
    :rtype: tuple
    :CU: player in g.get_all_players_coord()
    :Exemple:
    
    >>> g = Grid.from_file('grid03.txt')
    >>> move_to_est(g,0)
    >>> g.get_player_coord(0)
    (4,1)
    """
    assert player in g.get_all_players_coord()
    xf,yf=g.get_final_cell_coord()
    x,y = g.get_all_players_coord()[int(player)]
    while not(g.get_grille()[y][x].get_est()) and  g.get_grille()[y][x+1].get_contenu() == ' ' and x<g.get_dim()[0]:
        x+=1
    if x+1==xf and y==yf and player==0 and not g.get_grille()[y][x].get_est():
        x=xf
    g.modif_coord_player(int(player),x,y)
    return (x,y)


def move_to_ouest(g,player):
    """
     Cette fonction permet au joueur player de se déplacer vers l'ouest dans la grille g
     
    :param g: La grille qui représente le jeu
    :type g: Grid
    :param player: un joueur
    :type player: str
    :return: tuple des nouvelles coordonnees du player
    :rtype: tuple
    :CU: player in g.get_all_players_coord()
    :Exemple:
    
    >>> g = Grid.from_file('grid03.txt')
    >>> move_to_ouest(g,1)
    >>> g.get_player_coord(1)
    (0,3)
    """
    assert player in g.get_all_players_coord()
    xf,yf=g.get_final_cell_coord()
    x,y= g.get_all_players_coord()[int(player)]
    while not(g.get_grille()[y][x-1].get_est()) and g.get_grille()[y][x-1].get_contenu() == ' ' and x>0:
        x-=1
    if x-1==xf and y==yf and player==0 and g.get_grille()[yf][xf].get_est():
        x=xf
    g.modif_coord_player(int(player),x,y)
    return (x,y)


def move_to_nord(g,player):
    """
    Cette fonction permet au joueur player de se déplacer vers le nord dans la grille g
    
    :param g: La grille qui représente le jeu
    :type g: Grid
    :param player: un joueur
    :type player: str
    :return: tuple des nouvelles coordonnees du player
    :rtype: tuple
    :CU: player in g.get_all_players_coord()
    :Exemple:
    
    >>> g = Grid.from_file('grid04.txt')
    >>> move_to_nord(g,1)
    >>> g.get_player_coord(1)
    (1,0)
    """
    assert player in g.get_all_players_coord()
    x,y = g.get_all_players_coord()[int(player)]
    xf,yf=g.get_final_cell_coord()
    while not(g.get_grille()[y-1][x].get_sud()) and g.get_grille()[y-1][x].get_contenu() == ' ' and y>0:
        y-=1
    if x==xf and y-1==yf and player==0 and not g.get_grille()[yf][xf].get_sud():
        y=yf
    g.modif_coord_player(int(player),x,y)
    return (x,y)

def move_to_sud(g,player):
    """
     Cette fonction permet au joueur player de se déplacer vers le sud dans la grille g
     
    :param g: La grille qui représente le jeu
    :type g: Grid
    :param player: un joueur
    :type player: str
    :return: tuple des nouvelles coordonnees du player
    :rtype: tuple
    :CU: player in g.get_all_players_coord()
    :Exemple:
    
    >>> g = Grid.from_file('grid04.txt')
    >>> move_to_sud(g,0)
    >>> g.get_player_coord(0)
    (0,14)
    """
    assert player in g.get_all_players_coord()
    x,y = g.get_all_players_coord()[int(player)]
    xf,yf=g.get_final_cell_coord()
    while not(g.get_grille()[y][x].get_sud()) and g.get_grille()[y+1][x].get_contenu() == ' ' and y<g.get_dim()[1]:
        y+=1
    if x==xf and y+1==yf and player==0 and not g.get_grille()[y][x].get_sud():
        y=yf
    g.modif_coord_player(int(player),x,y)
    return (x,y)
  
    
def repl_play(grille):
    """
    Dans cette fonction , on déplace les joueurs vers la direction qu'il ont choisie
    et si le joueur principal arrive vers la case finale alors on déclare sa victoire
    
    :param g: La grille qui représente le jeu
    :type g: Grid
    """
    xf,yf=grille.get_final_cell_coord()
    print(grille)
    fini=False
    while not fini:
        a=choix_direction(grille)
        if a in {'q','Q'}:
            fini=True
            print('Vous avez perdu !')
        else:
            num,direction=a
            if direction in {'e','E'} :
                x,y=move_to_est(grille,num)
                if x==xf and y==yf and num==0:
                    fini=True
                    print('Gagné !!')
                else:
                    print(grille)
            elif direction in {'O','o'}:
                x,y=move_to_ouest(grille,num)
                if x==xf and y==yf and num==0:
                    fini=True
                    print('Gagné !!')
                else:
                    print(grille)
            elif direction in {'n','N'}:
                x,y=move_to_nord(grille,num)
                if x==xf and y==yf and num==0:
                    fini=True
                    print('Gagné !!')
                else:
                    print(grille)
            elif direction in {'s','S'}:
                x,y=move_to_sud(grille,num)
                if x==xf and y==yf and num==0:
                    fini=True
                    print('Gagné !!')
                else:
                    print(grille)

def main():
    """
    main function for graphical ice walker game
    """
    g=Grid.from_file(sys.argv[1])
    repl_play(g)

if __name__ == '__main__':
    main()

   