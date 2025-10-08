# 📘 Algoritmos de Ordenamiento y Búsqueda en Python

Este repositorio contiene implementaciones en **Python** de los algoritmos de ordenamiento y búsqueda más utilizados en programación.  
El objetivo es que los estudiantes puedan **comprender, practicar y comparar** cada técnica.

---

## 🚀 Algoritmos Incluidos

### 🔄 Ordenamiento
1. **Bubble Sort** 🫧  
   - Compara pares de elementos adyacentes y los intercambia si están en desorden.  
   - Simple de entender, poco eficiente en listas grandes.  

2. **Selection Sort** ✅  
   - Selecciona el elemento más pequeño y lo coloca en su posición correcta.  
   - Fácil de implementar, pero no muy rápido.  

3. **Insertion Sort** 🃏  
   - Inserta cada elemento en su posición dentro de la parte ordenada.  
   - Muy eficiente en listas pequeñas o casi ordenadas.  

4. **Merge Sort** ⚡  
   - Aplica la técnica de *divide y vencerás*: divide la lista y luego mezcla ordenadamente.  
   - Muy eficiente con listas grandes y garantiza buen rendimiento.  

---

### 🔍 Búsqueda
1. **Búsqueda Lineal** 🔎  
   - Recorre la lista elemento por elemento.  
   - No requiere lista ordenada.  

2. **Búsqueda Binaria** ⏩  
   - Divide la lista a la mitad en cada paso.  
   - Requiere lista **ordenada**. Muy rápida en listas grandes.  

---

## 📊 Complejidad Algorítmica

| Algoritmo           | Mejor Caso | Peor Caso | Requiere lista ordenada |
|---------------------|------------|-----------|--------------------------|
| Bubble Sort         | O(n)       | O(n²)     | ❌ |
| Selection Sort      | O(n²)      | O(n²)     | ❌ |
| Insertion Sort      | O(n)       | O(n²)     | ❌ |
| Merge Sort          | O(n log n) | O(n log n)| ❌ |
| Búsqueda Lineal     | O(1)       | O(n)      | ❌ |
| Búsqueda Binaria    | O(1)       | O(log n)  | ✅ |

---

## 🛠 Ejemplo de Uso

```python
from algoritmos import (
    bubble_sort, selection_sort, insertion_sort, merge_sort,
    busqueda_lineal, busqueda_binaria
)

# Lista de prueba
datos = [64, 34, 25, 12, 22, 11, 90]

# Ordenamiento
print("Bubble Sort:", bubble_sort(datos.copy()))
print("Selection Sort:", selection_sort(datos.copy()))
print("Insertion Sort:", insertion_sort(datos.copy()))
print("Merge Sort:", merge_sort(datos.copy()))

# Búsquedas
ordenado = merge_sort(datos.copy())
print("Búsqueda Lineal (22):", busqueda_lineal(ordenado, 22))
print("Búsqueda Binaria (22):", busqueda_binaria(ordenado, 22))
```
