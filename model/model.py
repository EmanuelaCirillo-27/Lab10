from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self._lista_filiali=None
        self._lista_collegamenti=None
        self._dizionario_collegamenti={}

    def get_filiali(self):
        if self._lista_filiali is None:
            self._lista_filiali=DAO.read_all_filiali()

        for collegamento in self._dizionario_collegamenti:
            self._dizionario_collegamenti[collegamento.id]=collegamento

        return self._lista_filiali

    def get_collegamenti(self):
        if self._lista_collegamenti is None:
            self._lista_collegamenti=DAO.read_all_collegamenti()

        return self._lista_collegamenti


    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        self.G.clear()

        nodi=self.get_filiali()

        self.G.add_nodes_from(nodi)



        collegamenti=self.get_collegamenti()

        for c in collegamenti:
            u=self.
            v=

        for collegamento in collegamenti:
            if collegamento['media']>=threshold:
                self.G.add_edge(f_orig, f_dest, weight=collegamento["media"])


    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
