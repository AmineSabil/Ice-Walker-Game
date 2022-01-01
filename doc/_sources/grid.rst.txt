=========================
:mod:`grid` module
=========================

Ce module définit une classe et des fonctions auxiliaires pour gérer le plateau du jeu de Ice Walker.


Class description
=================

Une classe pour définir la grille du jeu.


La classe :class:`Grid`
------------------------------

.. autoclass:: grid.Grid

Méthodes
~~~~~~~~

.. automethod:: grid.Grid.from_file

.. automethod:: grid.Grid.get_dim

.. automethod:: grid.Grid.get_number_of_players

.. automethod:: grid.Grid.get_final_cell_coord

.. automethod:: grid.Grid.get_player_coord

.. automethod:: grid.Grid.get_all_players_coord

.. automethod:: grid.Grid.get_final_cell_coord

.. automethod:: grid.Grid.get_walls_coord

.. automethod:: grid.Grid.get_grille

.. automethod:: grid.Grid.modif_coord_player

Fonction auxiliaire
===================

.. autofunction:: grid.ajout_plus

.. autofunction:: grid.intialiser_grille


