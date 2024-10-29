# coding: utf-8
import sys
import io

# Configurar la codificación de salida a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from tabulate import tabulate

result_product = [
    [1, "Categoría A"],
    [2, "Categoría B"],
    [3, "¡Categoría Especial!"]
]

print(tabulate(result_product, headers=['ID', 'Category'], tablefmt="fancy_grid"))
