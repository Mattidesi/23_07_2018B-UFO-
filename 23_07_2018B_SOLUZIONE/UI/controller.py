import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choise_anno=None

    def handle_graph(self, e):
        strGiorni = self._view.txt_giorni.value
        if strGiorni == "":
            self._view.create_alert("Inserire un valore per il giorno")
            self._view.update_page()
            return
        try:
            self._choise_giorni = int(strGiorni)
        except ValueError:
            self._view.create_alert("Inserire un numero intero")
            self._view.update_page()
            return
        if self._choise_giorni < 1 or self._choise_giorni > 180:
            self._view.create_alert("Inserire un valore compreso tra 1 e 180")
            self._view.update_page()
            return
        self._model.buildGraph(self._choise_giorni, self._choise_anno)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di archi: {self._model.getNumEdges()}"))
        self._view.update_page()

    def handle_countedges(self, e):
        pass

    def handle_search(self, e):
        pass

    def readddAnno(self, e):
        print("read dd anno called")
        if e.control.data==None:
            self._choise_anno=None
            return
        self._choise_anno=e.control.data