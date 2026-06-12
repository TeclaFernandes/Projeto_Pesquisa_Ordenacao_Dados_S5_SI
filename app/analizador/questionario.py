def obter_requisitos():

    estabilidade = input(
        "Precisa de estabilidade? (s/n): "
    ).lower()

    memoria = input(
        "Memória limitada? (s/n): "
    ).lower()

    return {
        "estabilidade": estabilidade == "s",
        "memoria_limitada": memoria == "s"
    }