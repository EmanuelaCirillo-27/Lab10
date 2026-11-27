import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        valore = self._view.importo_medio_minimo.value
        try:
            valore=float(valore)
        except ValueError:
            self._view.show_alert("Inserire un valore numerico")
            return

        self._model.costruisci_grafo(valore)

        nodi=self._model.get_num_nodes()
        collegamenti=self._model.get_num_edges()

        self._view.lista_visualizzazione.controls.clear()
        # self._view._lst_results.controls.append(ft.Text(f"{self._model.grafo}"))
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Filiali: {nodi}\nNumero di collegamenti {collegamenti}"))


        for arco in self._model.get_all_edges():
            arco_in_testo=ft.Text(arco)
            self._view.lista_visualizzazione.controls.append(arco_in_testo)

        self._view.update()