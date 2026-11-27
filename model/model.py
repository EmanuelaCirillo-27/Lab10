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
        self._dizionario_filiali={}

    def get_filiali(self):
        if self._lista_filiali is None:
            self._lista_filiali=DAO.read_all_filiali()

        for filiale in self._lista_filiali:
            self._dizionario_filiali[filiale.id]=filiale

        return self._lista_filiali

    def get_collegamenti(self):
        if self._lista_collegamenti is None:
            self._lista_collegamenti=DAO.read_all_collegamenti()

        #for collegamento in self._lista_collegamenti:
            #self._dizionario_collegamenti[collegamento.id]=collegamento


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

        for collegamento in collegamenti:
            origine_id = collegamento["origine"]
            arrivo_id = collegamento["arrivo"]
            somma = collegamento["somma"]
            conteggio = collegamento["conteggio"]

            if origine_id not in self._dizionario_filiali or arrivo_id not in self._dizionario_filiali:
                continue

            if somma is None or not conteggio:
                continue

            media = float(somma) / conteggio

            u = self._dizionario_filiali[origine_id]
            v = self._dizionario_filiali[arrivo_id]
            if media>=threshold:
                #peso_calcolato=float(collegamento["media"])

                self.G.add_edge(u, v, peso=media)


    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        result=[]
        for u, v, data in self.G.edges(data=True):
            result.append(f"{u} - {v} - {data['peso']:.2f}")

        return result
