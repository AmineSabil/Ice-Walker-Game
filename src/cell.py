class Cell():
    """
    >>> cel = Cell()
    >>> cel.get_est()
    False
    >>> cel.get_sud()
    False
    >>> cel.set_walls('E')
    >>> cel.get_est()
    True
    >>> cel.set_contenu(1)
    >>> cel.get_contenu()
    1
    >>> cel.set_walls('s')
    >>> cel.get_sud()
    True
    """ 
    def __init__(self,est=False,sud=False,plus=False):
        """
        Construire la cellule et initialiser les valeurs des murs sud et est ainsi que les plus
    
        :param est: un booléen qui indique True s'il y a un mur est dans la cellule ,False sinon
        :type est: (bool)
        :param sud: un booléen qui indique True s'il y a un mur sud dans la cellule ,False sinon
        :type sud: (bool)
        :param plus: un booléen qui indique True s'il y a un plus dans la cellule ,False sinon
        :type plus: (bool)
        """
        self.__content = ' '
        self.__est = est
        self.__sud = sud
        self.__plus= plus
        
    def get_est(self):
        """
         Cette fonction nous informe de la présence d'un mur est dans self
         
         :return: True s'il y a mur est dans self, False sinon
         :rtype: (bool)
         :Exemples:

         >>> cel = Cell()
         >>> cel.get_est()
         False
        """ 
        return self.__est
    
    def get_sud(self):
        """
         Cette fonction nous informe de la présence d'un mur sud dans self
         
         :return: True s'il y a mur sud dans self, False sinon
         :rtype: (bool)
         :Exemples:

         >>> cel = Cell()
         >>> cel.get_sud()
         False
         >>> cel1 = Cell()
         >>> cel1.set_sud()
         >>> cel1.get_sud()
         True
        """  
        return self.__sud
    
    def get_plus(self):
        """
         Cette fonction nous informe de la présence d'un plus dans self
         
         :return: True s'il y a un plus dans self, False sinon
         :rtype: (bool)
         :Exemples:

         >>> cel = Cell()
         >>> cel.get_plus()
         False
         >>> cel1 = Cell()
         >>> cel1.set_plus()
         >>> cel1.get_plus()
         True
        """  
        return self.__plus
    
    def set_walls(self,direction):
        """
        Cette fonction permet de mettre un mur dans self selon direction
        
        :param direction: un caractère représentant le type du mur
    qu'on doit mettre dans self
        :type direction: (str)
        :CU: direction in {'S','E','s','e'}
        :Exemple:

        >>> cel = Cell()
        >>> cel.set_walls('E')
        >>> cel1 = Cell()
        >>> cel1.set_walls('S')
        """ 
        if direction == 'E':
            self.__est = True
        else:
            self.__sud = True
        
    def get_contenu(self):
        """
        Cette fonction permet de savoir le contenu dans self
         
        :return: le contenu dans self
        :rtype: (str)
        :Exemple:
        
        >>> cel = Cell()
        >>> cel.set_contenu(0)
        >>> cel.get_contenu()
        0
        """ 
        return self.__content
    
    def set_contenu(self,c):
        """
        Cette fonction permet de mettre c dans le contenu de self
         
        :param c: un caractère représentant le nouveau contenu de self
        :type c: (str)
        :sideeffect: change le contenu de la cellule
        :CU: None
        :Exemple:
        
        >>> cel = Cell()
        >>> cel.set_contenu(4)
        >>> cel.get_contenu()
        4
        """
        self.__content = c
    
    def set_sud(self):
        """
        Cette fonction permet de mettre un mur sud dans self
        
        :CU: None
        :sideeffect: met un mur sud dans la cellule
        :Exemple:

        >>> cel = Cell()
        >>> cel.set_sud()
        >>> cel.get_sud()
        True
        """
        self.__sud=True

    def set_est(self):
        """
        Cette fonction permet de mettre un mur est dans self
        
        :CU: None
        :sideeffect: met un mur est dans la cellule
        :Exemple:

        >>> cel = Cell()
        >>> cel.set_est()
        >>> cel.get_est()
        True
        """
        self.__est=True
  
        
    def set_plus(self):
        """
        Cette fonction permet de mettre un plus dans la cellule
         
        :CU: None
        :sideeffect: met un plus dans la cellule
        :Exemple:

        >>> cel = Cell()
        >>> cel.set_plus()
        >>> cel.get_plus()
        True
        """
        self.__plus= True
