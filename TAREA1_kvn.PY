def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Argumentoss:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.
    
    Return:
    float: El área del rectángulo.
    """
    area = base * altura  # Calcula el área
    return area

    
def main():
    base = 5.0
    altura = 10.0
    area = calcular_area_rectangulo(base, altura)
    
    # Muestra el resultado al usuario
    print(f"El área del rectángulo es: {area}")


if __name__ == "__main__":
    main()
