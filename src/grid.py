#AUTEURS: SABIL MOHAMED AMINE
from cell import Cell

def ajout_plus(grille):
    """
    :param grille: la liste qui represente la grille du jeu
    :type grille: (list)
    :CU: Aucune
    :effet de bord: ajout les plus dans la grille .
    """
    for l in grille: #ajout des plus dans la grille
        for i in range(len(l)):
            if  l[i].get_est() and grille[grille.index(l)-1][i].get_est():
                grille[grille.index(l)-1][i].set_plus()
            if l[i].get_sud() and l[i].get_est():
                l[i].set_plus()
            if l[i-1].get_est() and l[i].get_sud():
                l[i-1].set_plus()
            if l[i].get_est() and grille[grille.index(l)-1][i].get_sud():
                grille[grille.index(l)-1][i].set_plus()
            if l[i-1].get_est() and grille[grille.index(l)-1][i].get_sud():
                grille[grille.index(l)-1][i-1].set_plus()
            if l[i].get_sud() and l[i-1].get_sud():
                l[i-1].set_plus()
            
    
def intialiser_grille(dim,nbr_player,final_cell,players,walls):
    """
    :param dim: la dimension de la grille
    :type dim: tuple
    :param nbr_player: le nombre de joueur
    :type nbr_player: int
    :param final_cell: les coordonnées de la case finale
    :type final_cell: tuple
    :param players: un dictionnaire qui représente les joueurs et leurs coordonnées
    :type players: dict
    :param walls: une liste qui représente les coordonnées des murs
    :type walls: list
    :return: liste de la grille construite à partir de dim,nbr_player,final_cell,players et walls
    :rtype: list
    :UC: None 
    """
    grille=[]
    for i in range(dim[1]):
        temp=[]
        for j in range(dim[0]):
            temp.append(Cell())    
            if j==dim[0]-1:
                temp[dim[0]-1].set_walls('E')
        if i==dim[1]-1:
            for cel in temp:
                cel.set_sud()
        grille.append(temp)
    for t in players: #ajout des joueurs dans la grille
        grille[t[1]][t[0]].set_contenu(str(players.index(t)))
    for t in walls: #ajout des walls dans la grille
        grille[t[1]][t[0]].set_walls(t[2])
    grille[final_cell[1]][final_cell[0]].set_contenu('⬜')
    ajout_plus(grille) #ajout des plus dans la grille
    return grille

class Grid():
    """
    >>> g = Grid.from_file('grid01.txt')
    >>> g.get_dim()
    (16,16)
    >>> g.get_number_of_players()
    4
    >>> g.get_final_cell_coord()
    (3, 14)
    >>> g.get_player_coord(1)
    (0, 0)
    >>> g.get_walls_coord()
      [(3, 0, 'E'), (9, 0, 'E'), (13, 1, 'E'), (13, 1, 'S'), (15, 1, 'S'),
      (5, 2, 'E'), (5, 2, 'S'), (9, 2, 'S'), (2, 3, 'S'), (8, 3, 'E'), (14, 3, 'S'),
      (0, 4, 'S'), (2, 4, 'E'), (14, 4, 'E'), (1, 5, 'S'), (6, 5, 'E'), (7, 5, 'S'),
      (0, 6, 'E'), (7, 6, 'S'), (8, 6, 'S'), (11, 6, 'E'), (12, 6, 'S'), (6, 7, 'E'),
      (8, 7, 'E'), (6, 8, 'E'), (7, 8, 'S'), (8, 8, 'S'), (8, 8, 'E'), (3, 9, 'E'),
      (4, 9, 'S'), (6, 9, 'S'), (12, 9, 'E'), (13, 9, 'S'), (0, 10, 'S'), (5, 10, 'E'),
      (7, 11, 'S'), (9, 11, 'S'), (9, 11, 'E'), (15, 11, 'S'), (1, 12, 'S'),(7, 12, 'E'), (14, 12, 'S'), (1, 13, 'E'), (10, 13, 'S'), (14, 13, 'E'), (3, 14, 'E'), (3, 14, 'S'), (9, 14, 'E'), (4, 15, 'E'), (11, 15, 'E')]
    """
    def __init__(self,dim,nbr_player,final_cell,players,walls):
        """
        construire la grille du jeu, de dimension dim , avec nbr_player joueurs et mettre en place les murs 

        :param dim: la dimension de la grille
        :type dim: tuple
        :param nbr_player: le nombre de joueur
        :type nbr_player: int
        :param final_cell: les coordonnées de la case finale
        :type final_cell: tuple
        :param players: les coordonnées des joueurs
        :type players: list
        :param walls: les coordonnées des murs
        :type walls: list
        :return: la grille
        :rtype: Grid
        :UC: dim[0]>1 and dim[1]>0 and dim[0]==dim[1] and nbr_player>1 and 0<final_cell[0]<dim[0] and 0<final_cell[1]<dim[1]
        """
        assert dim[0]>1 and dim[1]>0 
        assert nbr_player>=1
        assert 0<=final_cell[0]<dim[0] and 0<=final_cell[1]<dim[1]
        self.__dim=dim
        self.__nbr_player=nbr_player
        self.__final_cell=final_cell
        self.__players=dict()
        for i in range(len(players)):
            self.__players[i]=players[i] 
        self.__walls=walls
        self.__grille=intialiser_grille(dim,nbr_player,final_cell,players,walls)
        
        
    def from_file(file):
        """
        récupérer les informations nécessaires pour construire la grille , notamment sa dimension,les coordonnées de la case finale,le nombre de joueurs, les coordonnées des joueurs ainsi que
        les coordonnées des murs
        :param file: un fichier qui contient les details de la grille
        :type file: (file)
        :CU: None
        """
        canal=open(file,'rt')
        liste_fichier=[]
        i=0
        ligne= canal.readline() 
        while not ligne=='':
            if not ligne[0] == "#":
                liste_fichier.append(ligne.rstrip())
            ligne=canal.readline()
        dim=tuple(int(i) for i in liste_fichier[0].split(','))
        final_cell = tuple(int(i) for i in liste_fichier[1].split(','))
        nbr_player= int(liste_fichier[2])
        players = [tuple(int(i)for i in liste_fichier[i].split(',')) for i in range(3,3+nbr_player)]
        walls=[]
        for i in range(3+nbr_player,len(liste_fichier)):
            t=()
            for j in liste_fichier[i].split(','):
                if j in 'OESN':
                    t+=(j,)
                else:
                    t+=(int(j),)
            walls.append(t)
        canal.close()       
        return Grid(dim,nbr_player,final_cell,players,walls)
    
    def get_dim(self):
        """
        :return: la dimension de la grille
        :rtype: tuple
        :UC: none
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_dim()
        (10,10)
        """
        return self.__dim
    
    def get_number_of_players(self):
        """
        :return: le nombre de joueurs dans la partie
        :rtype: int
        :UC: none
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_final_cell_coord()
        (2, 7)
        """
        return self.__nbr_player
    
    def get_final_cell_coord(self):
        """
        :return: les coordonnées de la case finale
        :rtype: tuple
        :UC: none
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_final_cell_coord()
        (2,7)
        """
        return self.__final_cell

    def get_player_coord(self,i):
        """
        :param i: le numero du joueur
        :type i: (int)
        :return: tuple des coordonnées du joueur
        :rtype: (tuple)
        :UC: i<self.get_number_of_players()
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_player_coord(0)
        (0,0)
        """
        assert i<self.get_number_of_players()
        return self.__players[i]
    
    def get_all_players_coord(self):
        """
        :return: dictionnaire de tous les joueurs avec comme valeur leurs coordonnées
        :rtype: (dict)
        :UC: none
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_all_players_coord()
        {0: (0, 0)}
        """
        return self.__players
    
    def get_walls_coord(self):
        """
        :return: liste contenant les coordonnées de tout les murs de la partie.
        :rtype: (list)
        :UC: none
        :Exemple:

        >>> g = Grid.from_file('grid02.txt')
        >>> g.get_walls_coord()
        [(1, 9, 'E'), (4, 3, 'S'), (0, 2, 'S'), (9, 4, 'S'), (4, 9, 'E'), (3, 4, 'E')]
        """
        return self.__walls
    
    def get_grille(self):
        """
        :return: liste de la grille
        :rtype: (list)
        :UC: none
        :Exemple:
        
        >>> g = Grid.from_file('grid04.txt')
        >>> g.get_grille()
        [[<cell.Cell object at 0x03E418F0>, <cell.Cell object at 0x03E418B0>, <cell.Cell object at 0x03E41830>, <cell.Cell object at 0x03E41690>, <cell.Cell object at 0x03E416F0>, <cell.Cell object at 0x03E41710>, <cell.Cell object at 0x03E41750>, <cell.Cell object at 0x03E41770>], [<cell.Cell object at 0x03E41730>, <cell.Cell object at 0x03E416B0>, <cell.Cell object at 0x03E414F0>, <cell.Cell object at 0x03E41530>, <cell.Cell object at 0x03E41570>, <cell.Cell object at 0x03E41550>, <cell.Cell object at 0x03E41510>, <cell.Cell object at 0x03E414D0>], [<cell.Cell object at 0x03E41950>, <cell.Cell object at 0x03E41A70>, <cell.Cell object at 0x03E41AD0>, <cell.Cell object at 0x03E41AF0>, <cell.Cell object at 0x03E41B10>, <cell.Cell object at 0x03E41A90>, <cell.Cell object at 0x03E41AB0>, <cell.Cell object at 0x03E41970>], [<cell.Cell object at 0x03E41A50>, <cell.Cell object at 0x03E419B0>, <cell.Cell object at 0x03E419D0>, <cell.Cell object at 0x03E41A30>, <cell.Cell object at 0x03E41A10>, <cell.Cell object at 0x03E41990>, <cell.Cell object at 0x03E41B50>, <cell.Cell object at 0x03E412D0>], [<cell.Cell object at 0x03E41350>, <cell.Cell object at 0x03E412F0>, <cell.Cell object at 0x03E41310>, <cell.Cell object at 0x03E3F6D0>, <cell.Cell object at 0x03E3F770>, <cell.Cell object at 0x03E3F7B0>, <cell.Cell object at 0x03E3F7D0>, <cell.Cell object at 0x03E3F7F0>], [<cell.Cell object at 0x03E3F830>, <cell.Cell object at 0x03E3F850>, <cell.Cell object at 0x03E3F870>, <cell.Cell object at 0x03E3F890>, <cell.Cell object at 0x03E3F8B0>, <cell.Cell object at 0x03E3F8F0>, <cell.Cell object at 0x03E3F910>, <cell.Cell object at 0x03E3F930>], [<cell.Cell object at 0x03E3F950>, <cell.Cell object at 0x03E3F970>, <cell.Cell object at 0x03E3F990>, <cell.Cell object at 0x03E3F9B0>, <cell.Cell object at 0x03E3F9D0>, <cell.Cell object at 0x03E3FA10>, <cell.Cell object at 0x03E3FA30>, <cell.Cell object at 0x03E3FA50>], [<cell.Cell object at 0x03E3FA70>, <cell.Cell object at 0x03E3FA90>, <cell.Cell object at 0x03E3FAB0>, <cell.Cell object at 0x03E3FAD0>, <cell.Cell object at 0x03E3FAF0>, <cell.Cell object at 0x03E3FB30>, <cell.Cell object at 0x03E3FB50>, <cell.Cell object at 0x03E3FB70>]]
        """
        return self.__grille
    
    def modif_coord_player(self,num_player,x,y):
        """
        modifier la position de num_player en le mettant dans la position (x,y)
        
        :param num_player: le numéro du joueur
        :type num_player: (int)
        :param x: un nombre qui représente l'abscisse de la position du joueur
        :type x: (int)
        :param y: un nombre qui représente l'ordonnée de la position du joueur
        :type y: (int)
        :UC: 0<=x<self.get_dim()[0] and 0<=y<self.get_dim()[1] and num_player in self.__players
        :Exemple:
        
        >>> g = Grid.from_file('grid03.txt')
        >>> g.modif_coord_player(1,3,3)
        >>> g.get_player_coord(1)
        (3, 3)
        """
        assert 0<=x<self.get_dim()[0]
        assert 0<=y<self.get_dim()[1]
        assert num_player in self.__players
        x_ancien,y_ancien=self.__players[num_player]
        self.__players[num_player]=(x,y)
        self.__grille[y_ancien][x_ancien].set_contenu(' ')
        self.__grille[y][x].set_contenu(str(num_player))

    def set_coord_players(self,dico):
        """
         Cette fonction permet de modifier les coordonnées des joueurs par dico
         
        :param dico: un dictionnaire indiquant les coordonnées des joueurs
        :type dico: dict
        :CU: NONE
        :Exemple:
        
        >>> g = Grid.from_file('grid03.txt')
        >>> g.set_coord_players({0:(3,2),1:(3,3)})
        >>> g.get_all_players_coord()
        {0: (3, 2), 1: (3, 3)}
        """
        self.__players=dico
    
    def __str__(self):
        """
        :return: une chaine de caractères qui contient toute la grille
        :rtype: str
        :UC: none
        """
        res='+'+''.join(['-+'for i in range(self.get_dim()[0])])+'\n'
        for l in self.__grille:
            res1='|'
            res2='+'
            for cel in l:
                if cel.get_est() and cel.get_sud():
                    res1+=cel.get_contenu()+'|'
                    if cel.get_plus():
                        res2+='-+'
                    else:
                        res2+='- '
                elif cel.get_est() and  not cel.get_sud():
                    res1+=cel.get_contenu()+'|'
                    if l.index(cel)!=self.__dim[0]-1:
                        if (cel.get_plus() and l[l.index(cel)+1].get_sud()) or cel.get_plus():
                            res2+=' +'
                        else:
                            res2+='  '
                    else:
                        res2+='  '
                elif not cel.get_est() and  cel.get_sud():
                    res1+=cel.get_contenu()+' '
                    if cel.get_plus():
                        res2+='-+'
                    else:
                        res2+='- '
                else:
                    res1+=cel.get_contenu()+' '
                    if cel.get_plus():
                        res2+=' +'
                    else:
                        res2+='  '
            res2=list(res2)
            res2[-1]='+'
            res2=''.join(res2)
            res+=res1+'\n'+res2+'\n'   
        return res
    
    def __repr__(self):
        """
        :return: une chaine de caractères qui contient toute la grille
        :rtype: str
        :UC: none
        """
        return self.__str__()
        
