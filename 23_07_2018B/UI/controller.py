import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDYear(self):
        years = self._model.getYears()
        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(year))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()

        ggStr = self._view.txt_giorni.value
        try:
            gg = int(ggStr)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("il valore inserito non è un intero"))
            self._view.update_page()
            return

        if gg < 1 or gg > 180:
            self._view.txt_result.controls.append(
                ft.Text("inserire un valore tra 1 e 180 inclusi",color='red'))
            self._view.update_page()
            return

        if self._view._ddAnno.value is None:
            self._view.txt_result.controls.append(ft.Text("Inserisci un anno!", color='red'))
            self._view.update_page()
            return

        self._model.buildGraph(self._view._ddAnno.value,int(self._view.txt_giorni.value))

        nNodes, nEdges = self._model.getGraphDetails()

        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nEdges}"))
        self._view.update_page()

        sumWeight = self._model.getSumWeightNeighbor()

        for e in sumWeight:
            self._view.txt_result.controls.append(ft.Text(f"arco: {e[0]} - somma pesi archi adiacenti: {e[1]}"))
            self._view.update_page()


    def handle_countedges(self, e):
        pass

    def handle_search(self, e):
        pass

    def readddAnno(self, e):
        pass