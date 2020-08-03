iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {}
    iris[id_n]['species'] = species
    iris[id_n]['petal_length'] = petal_length
    iris[id_n]['petal_width'] = petal_width
    for key, value in kwargs.items():
        iris[id_n][key] = value
    return iris

print(add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac'))