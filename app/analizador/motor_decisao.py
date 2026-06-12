class MotorDecisao:

    def recomendar(
        self,
        caracteristicas,
        requisitos
    ):

        scores = {
            "Bubble Sort": 50,
            "Selection Sort": 50,
            "Insertion Sort": 50,
            "Merge Sort": 50,
            "Quick Sort": 50,
            "Heap Sort": 50
        }

        tamanho = caracteristicas["tamanho"]

        if tamanho > 10000:

            scores["Bubble Sort"] -= 100
            scores["Selection Sort"] -= 100

            scores["Merge Sort"] += 40
            scores["Quick Sort"] += 40
            scores["Heap Sort"] += 40

        if caracteristicas["grau_ordenacao"] > 85:

            scores["Insertion Sort"] += 50

        if requisitos["estabilidade"]:

            scores["Merge Sort"] += 20

            scores["Quick Sort"] -= 20
            scores["Heap Sort"] -= 20

        melhor = max(
            scores,
            key=scores.get
        )

        return melhor, scores