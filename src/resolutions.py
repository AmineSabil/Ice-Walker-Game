from grid import Grid
from cell import Cell
from queue import Queue
from projet import *
import sys


def moves(grille,tup_config):
    """
    Cette fonction permet de générer toutes les configurations possibles des joueurs en faisant tous les mouvements possibles

    :param grille: la grille du jeu
    :type grille: Grid
    :param tup_config: une configuration données des joueurs
    :type tup_config: tuple
    :return: une liste de toutes les configurations des joueurs avec tous les mouvements possibles
    :rtype: list
    :CU: None
    """
    n = grille.get_number_of_players()
    tup_joueurs,t2=tup_config
    n = grille.get_number_of_players()
    dico=dict(grille.get_all_players_coord())
    l = list()
    for t in tup_joueurs:
        grille.modif_coord_player(tup_joueurs.index(t),t[0],t[1])
    for joueur in range(n):
        coord_ancienne=grille.get_player_coord(joueur)
        for c in ['N','S','O','E']:
            if c=='N':
                move_to_nord(grille,joueur)
            elif c=='S':
                move_to_sud(grille,joueur)
            elif c=='O':
                move_to_ouest(grille,joueur)
            elif c=='E':
                move_to_est(grille,joueur)
            ti=tuple()
            if coord_ancienne != grille.get_player_coord(joueur):
                for i in range(n):
                    ti+=(grille.get_all_players_coord()[i],)
                res=(ti,t2+((joueur,c),))
                l.append(res)
            grille.modif_coord_player(joueur,coord_ancienne[0],coord_ancienne[1])
    return l


def is_solved(grille,tup_config):
    """
     Cette fonction indique est-ce-que le joueur principal est bien arrivé à la case finale dans grille
    :param grille: la grille du jeu
    :type grille: Grid
    :param tup_config: une configuration données des joueurs
    :type tup_config: tuple
    :return: True si le joueur principal est bien arrivé à la case finale ,False sinon
    :rtype: bool
    :CU: None
    :Exemples:
    >>> g=Grid.from_file('grid02.txt')
    >>> is_solved(g,(((2,7),),()))
    True
    >>> is_solved(g,(((1,3),),()))
    False
    """
    xf,yf=grille.get_final_cell_coord()
    tup_coord,ti_mouv=tup_config
    x,y=tup_coord[0]
    return x==xf and y==yf
  

def fonction_resolution(grille):
    """
     Cette fonction permet de savoir tous les coordonnées par lesquelles le joueur principal va passer pour arriver à la case finale.
    :param grille: la grille du jeu
    :type grille: Grid
    :CU: None
    :Exemple:
    >>> g=Grid.from_file('grid06.txt')
    >>> fonction_resolution(g)
    ((0, 'S'), (0, 'O'), (0, 'N'), (0, 'E'), (0, 'S'), (0, 'O'), (0, 'N'), (0, 'E'))
    """
    
    n=grille.get_number_of_players()
    ti=tuple()
    for i in range(n):
        ti+=(grille.get_all_players_coord()[i],)
    config=(ti,())
    if is_solved(grille,config):
        return config[1]
    queue = Queue()
    visited = dict()
    queue.put(config)
    visited[config] = None
    solved = False
    while not queue.empty() and not solved:
        s = queue.get()
        for sp in moves(grille,s):
            if not sp in visited:
                if is_solved(grille,sp):
                    solved = True
                    solution = sp
                visited[sp] = s
                queue.put(sp)
    return solution[1]
 
def main():
    """
    main function for game's resolution 
    """
    g=Grid.from_file(sys.argv[1])
    print(fonction_resolution(g))

if __name__ == '__main__':
    main()
