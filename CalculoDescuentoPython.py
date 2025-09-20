def calcular_descuento(monto_compra: float, porcentaje: float = 10) -> float:
    """
    Calcula el descuento de una compra.

    :param monto_compra: Monto total de la compra.
    :param porcentaje: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = monto_compra * (porcentaje / 100)
    return descuento


if __name__ == "__main__":
    # Ejemplo 1: usando el descuento por defecto (10%)
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    final1 = monto1 - descuento1
    print(f"Compra 1: Monto = ${monto1:.2f}, Descuento = ${descuento1:.2f}, Total a pagar = ${final1:.2f}")

    # Ejemplo 2: usando un descuento diferente (15%)
    monto2 = 200.0
    descuento2 = calcular_descuento(monto2, 15)
    final2 = monto2 - descuento2
    print(f"Compra 2: Monto = ${monto2:.2f}, Descuento = ${descuento2:.2f}, Total a pagar = ${final2:.2f}")
