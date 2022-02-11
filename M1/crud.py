"""
 * Copyright 2022, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Santiago Arteaga
 """


#  LIB IMPORTS
import config as cf
import csv
import os
import random
from DISClib.ADT import list as lt
assert cf


"""
Este codigo contiene un ejemplo de como configurar e inicializar
un ADT Lista con DISClib y las operaciones basicas CRUD (CREATE,
READ, UPDATE, DELETE)
"""


def load_data(catalog):
    """
    load_data loads all the CSV data into the catalog and returns the size
    of the structures.

    Args:
        catalog ([dict]): dictionary with the ADTs loaded from the CSV files

    Returns:
        [list]: list with the size ot the laded structure
    """

    grossers = load_grossers(catalog)
    ans = (grossers,)
    return ans


def load_grossers(catalog):
    """
    load_grossers loads the HighestGrossers.csv into the ADT list.

    Args:
        catalog ([dict]): dictionary with the ADTs loaded from the CSV files

    Returns:
        [int]: the size ot the loaded structure
    """

    mf = "Movies"
    gf = "HighestGrossers.csv"
    grosser_lt = catalog["grossers"]
    grossers_file = os.path.join(cf.data_dir, mf, gf)
    wfile = open(grossers_file, encoding="utf-8")
    input_file = csv.DictReader(wfile)
    for gr in input_file:
        lt.addLast(grosser_lt, gr)
    ans = grossers_size(catalog)
    return ans


def compare_years(y1, y2):
    """
    compare_years between the inmemory element and the incoming one

    Args:
        y1 ([int]): incoming year of the element
        y2 ([dict]): inmemory element dict

    Returns:
        [int]: -1 if is lesser, 0 if is equal and 1 if is greater
    """
    if (y1 == y2["YEAR"]):
        return 0
    elif (y1 > y2["YEAR"]):
        return 1
    return -1


def grossers_size(catalog):
    """
    grossers_size calculate the ADT list size

    Args:
        catalog ([dict]): dictionary with the ADTs loaded from the CSV files

    Returns:
        [int]: the size ot the loaded structure
    """

    grossers_lt = catalog["grossers"]
    ans = lt.size(grossers_lt)
    return ans


def print_grossers(catalog):
    """
    print_grossers prints each element's fields (key-value dicts) in the
    ADT list

    Args:
        catalog ([dict]): dictionary with the ADTs loaded from the CSV files
    """

    grossers_lt = catalog["grossers"]
    msg = str()
    for gr in lt.iterator(grossers_lt):
        tmsg = str()
        keys = list(gr.keys())
        # keys.remove("TICKETS SOLD")
        for k in keys:
            v = gr.get(k)
            fmsg = str(k) + ": " + str(v) + "|"
            tmsg = tmsg + fmsg
        msg = msg + tmsg + "\n"
    print(msg)


def print_element(element):
    """
    print_element prints the keys & values of one element of the ADT list

    Args:
        element ([dict]): element of the list
    """
    msg = str()
    keys = list(element.keys())
    for k in keys:
        v = element.get(k)
        fmsg = str(k) + ": " + str(v) + "\n"
        msg = msg + fmsg
    print(msg)


def clean_element(element, key):
    """
    clean_element clean data from one specified key in the element's dict

    Args:
        element ([dict]): element of the list
        key ([str]): key to clean in the element

    Returns:
        [dict]: clean element of the list
    """
    value = element.get(key)
    value = str(value).replace(",", "")
    value = eval(value)
    ans = {key: value}
    element.update(ans)
    return element


# main exe
if __name__ == "__main__":
    """
    print_grossers main exec script
    """

    # catalog definition
    catalog = {
        "grossers": None,
    }

    """
    CREATE
    """
    # highest grossers linked list creation
    catalog["grossers"] = lt.newList("SINGLE_LINKED",
                                     cmpfunction=compare_years)

    # loading data from file
    print("Grossers number:", lt.size(catalog["grossers"]))
    ans = load_data(catalog)
    print("Grossers number:", ans[0])
    print_grossers(catalog)

    # working variable
    grossers = catalog["grossers"]

    """
    UPDATE
    """
    # updating one random element in list
    rand_idx = random.randrange(1, lt.size(grossers))
    print("Element index to update", rand_idx)
    rand_elm = lt.getElement(catalog["grossers"], rand_idx)
    print_element(rand_elm)
    clean_elm = clean_element(rand_elm, "TICKETS SOLD")
    lt.insertElement(grossers, clean_elm, rand_idx)
    clean_elm = lt.getElement(grossers, rand_idx)
    print_element(clean_elm)

    """
    READ
    """
    # reading one random element in list
    rand_idx = random.randrange(1, ans[0])
    print("Element index to read", rand_idx)
    rand_elm = lt.getElement(catalog["grossers"], rand_idx)
    print_element(rand_elm)

    """
    DELETE
    """
    # deleting one random element in list
    rand_idx = random.randrange(1, lt.size(catalog["grossers"]))
    print("Element index to delete", rand_idx)
    rand_elm = lt.getElement(grossers, rand_idx)
    print_element(rand_elm)
    lt.deleteElement(grossers, rand_idx)
    print_grossers(catalog)
    ng = lt.size(catalog["grossers"])
    print("NEW Grossers number:", ng)
