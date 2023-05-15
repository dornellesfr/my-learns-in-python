def zip_lists(cities, states):
    result = [(cities[i], states[i]) for i in range(len(cities))]
    return result


if __name__ == "__main__":
    a = zip_lists(['Salvador', 'Ubatuba', 'Belo Horizonte'],
                  ['BA', 'SP', 'MG', 'RJ'])
    print(a)
