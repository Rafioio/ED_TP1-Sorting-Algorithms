from src.sorts.bubblesort import Bubblesort
from src.sorts.insertionsort import Insertionsort
from src.sorts.selectionsort import Selectionsort
from src.sorts.shellsort import Shellsort
from src.sorts.mergesort import MergeSort
from src.sorts.quicksort import Quicksort
from src.sorts.countingsort import CountingSort
from src.sorts.radixsort import RadixSort
from src.sorts.bucketsort import BucketSort
from functools import partial

ALGORITMOS = {
    "bubble":          dict(fabrica=Bubblesort,                    grupo="quadratico", dominio="int"),
    "insertion":       dict(fabrica=Insertionsort,                 grupo="quadratico", dominio="int"),
    "selection":       dict(fabrica=Selectionsort,                 grupo="quadratico", dominio="int"),
    "shell_ciura":     dict(fabrica=partial(Shellsort, "ciura"),   grupo="nlogn",      dominio="int"),
    "shell_knuth":     dict(fabrica=partial(Shellsort, "knuth"),   grupo="nlogn",      dominio="int"),
    "shell_shell":     dict(fabrica=partial(Shellsort, "shell"),   grupo="nlogn",      dominio="int"),
    "merge":           dict(fabrica=MergeSort,                     grupo="nlogn",      dominio="int"),
    "quick_aleatorio": dict(fabrica=partial(Quicksort, "aleatorio"), grupo="nlogn",    dominio="int"),
    "quick_mediana3":  dict(fabrica=partial(Quicksort, "mediana3"),  grupo="nlogn",    dominio="int"),
    "quick_ultimo":    dict(fabrica=partial(Quicksort, "ultimo"),    grupo="nlogn",    dominio="int"),
    "counting":        dict(fabrica=CountingSort,                  grupo="linear",     dominio="int"),
    "radix":           dict(fabrica=RadixSort,                     grupo="linear",     dominio="int"),
    "radix_b10":       dict(fabrica=partial(RadixSort, 10),        grupo="linear",     dominio="int"),
    "bucket":          dict(fabrica=BucketSort,                    grupo="linear",     dominio="float01"),
}

TIPOS = ["aleatoria", "ordenada", "inversa", "quase_ordenada"]