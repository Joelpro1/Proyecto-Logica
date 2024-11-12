import networkx as nx
import matplotlib.pyplot as plt
import sys

# Crear un grafo no dirigido y ponderado w
G = nx.Graph()

# Lista de nodos basada en el listado que proporcionaste
nodes = [
    "N01", "N02", "N03", "K2", "N05", "N06", "N07", "Edificio K1", "N09", "N10", "Facultad Ingenieria", "N12",
    "N13", "N14", "N15", "Casa de Gobierno", "N17", "Capilla", "N19", "N20", "Living", "Ad4", "N23", "Ad3",
    "N25", "Ad2", "N27", "Edificio Ad1", "N29", "Cafeteria AdPortas", "K3", "N32", "N33", "N34", "N35", "N37",
    "N38", "Edificio G(1)", "N40", "N41", "G2", "Embarcadero", "N44", "N45", "N46", "N47", "Cafeteria Embarcadero", "N49",
    "Edificio E1(1)", "N51", "N52", "Edificio E2", "N54", "N55", "N56", "N57", "Edificio E1(2)", "N59", "N60", "N61",
    "Puente Madera", "N63", "N64", "N65", "N66", "N67", "N68", "N69", "N70", "N71", "N72", "N73", "Bienestar", "N75", "Meson", "N77", "N78",
    "N79", "N80", "N81", "N82", "N83", "Cafeteria Atelier", "Edificio F", "Edificio H", "N87", "N88", "N89", "N90", "N91",
    "N92", "N93", "N94", "N95", "Punto Wok", "Punto Verde", "N98", "N99", "N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107",
    "N108", "Punto Sandwich", "Edificio B", "N111", "Edificio C", "Puesto HotDog", "N114", "N115", "N116", "N117", "Kioskos(2)", "N119", "Kioskos(1)",
    "N121", "N122", "N123", "N124", "N125", "N126", "Edificio A", "N128", "N129", "N130", "N131", "Biblioteca", "Edificio D2", "Edificio O", "Edificio D1"
]

# Añadir nodos al grafo
G.add_nodes_from(nodes)

# Diccionario con las posiciones personalizadas en el plano cartesiano de (-50,50)
nuevas_posiciones = {
    "N01": (-27.59, 34.4), "N02": (-21.21, 33.19), "N03": (-17.31, 34.96), "K2": (-12.37, 38.39),
    "N05": (-17.18, 26.2), "N06": (-20.56, 23.43), "N07": (-13.11, 26.85), "Edificio K1": (-11.07, 29.33),
    "N09": (-11.46, 25.55), "N10": (-13.28, 17.14), "Facultad Ingenieria": (-18.74, 14.32), "N12": (-11.85, 14.76),
    "N13": (-8.99, 14.58), "N14": (-10.37, 12.02), "N15": (-6.56, 17.18), "Casa de Gobierno": (-2.39, 19.61),
    "N17": (0, 17.23), "Capilla": (2.42, 17.27), "N19": (8.92, 20.44), "N20": (16.82, 26.68),
    "Living": (22.45, 32.49), "Ad4": (16.12, 35.74), "N23": (13.48, 29.28), "Ad3": (11.18, 37.26),
    "N25": (10.05, 31.23), "Ad2": (7.06, 38.26), "N27": (6.15, 31.67), "Edificio Ad1": (1.12, 39.04),
    "N29": (1.29, 31.93), "Cafeteria AdPortas": (-6.25, 39.43), "K3": (-8.73, 37.31), "N32": (20.16, 23.13),
    "N33": (24.54, 31.36), "N34": (22.5, 22.82), "N35": (23.41, 21.61), "N37": (23.78, 19.18),
    "N38": (26.66, 20.46), "Edificio G(1)": (29.76, 19.55), "N40": (27.94, 15.39), "N41": (30.64, 11.67),
    "G2": (34.36, 13.56), "Embarcadero": (33.45, 10.24), "N44": (30.89, 6.41), "N45": (32.35, 6.3),
    "N46": (33.7, 5.87), "N47": (34.8, 5.61), "Cafeteria Embarcadero": (36.88, 7.65), "N49": (30, 4),
    "Edificio E1(1)": (33.01, 3.13), "N51": (34.14, 2.87), "N52": (33.63, 0.69), "Edificio E2": (35.97, 0.54),
    "N54": (33.29, -0.86), "N55": (31.76, -4.71), "N56": (30.05, -6.65), "N57": (35.55, -12.88),
    "Edificio E1(2)": (36.67, -5.56), "N59": (36.52, -14.47), "N60": (36.87, -16.29), "N61": (34.08, -20.9),
    "Puente Madera": (22.47, -27.89), "N63": (21.09, -27.07), "N64": (5.81, -32.51), "N65": (2.84, -35.27),
    "N66": (1.49, -33.27), "N67": (6.52, -28.07), "N68": (3.64, -29.19), "N69": (2.43, -27.25),
    "N70": (1.67, -26.16), "N71": (3.34, -24.96), "N72": (-0.21, -22.93), "N73": (5.61, -26.31),
    "Bienestar": (6.28, -25.48), "N75": (-2.27, -35.5), "Meson": (-4.8, -36.86), "N77": (-9.97,-39.41), "N78": (-9.5, -41.65),
    "N79": (-2.42, -30.66), "N80": (-5.5, -28.42), "N81": (13.25, -21.46), "N82": (10.78, -19.7),
    "N83": (7.69, -17.29), "Cafeteria Atelier": (8.63, -16.14), "Edificio F": (4.93, -15.14), "Edificio H": (6, -14),
    "N87": (2.64, -13.73),"N88": (3.81,-10.29), "N89": (1.79, -9.32), "N90": (19.59, -15.26), "N91": (13.45, -5.39),
    "N92": (23.35, -2.12), "N93": (-1.24, -3.45), "N94": (-0.89, -1.62), "N95": (0.55, -0.89),
    "Punto Wok": (3.99, 0.49), "Punto Verde": (-0.68, 1.37), "N98": (-2.5, 3.96), "N99": (-4.09, 1.31),
    "N100": (-6, 4), "N101": (-7.47, 2.4), "N102": (-7, 7.46), "N103": (-8.59, 10.51),
    "N104": (-9.2, 9.89), "N105": (-9.56, 7.34), "N106": (-12.7, 5.07), "N107": (-10.67, 5.96),
    "N108": (-10, 4), "Punto Sandwich": (-12, 4), "Edificio B": (-16, 4), "N111": (-20.52, 1.93), "Edificio C": (-27.57, -0.77),
    "Puesto HotDog": (-25.36, 3.81), "N114": (-24.48, 5.22), "N115": (-30.45, 6.22), "N116": (-30.77, 8.84),
    "N117": (-31.57, 10.83), "Kioskos(2)": (-33.71, 10.95), "N119": (-38, 10), "Kioskos(1)": (-40.53, 10.22),
    "N121": (-45.38, 13.83), "N122": (-42.17, 9.72), "N123": (-26.78, 10.8), "N124": (-25.89, 12.39),
    "N125": (-21.84, 9.1), "N126": (-22.07, 10.6), "Edificio A": (-20.43, 10.01), "N128": (-16.9, 8.42),
    "N129": (-17.23, 7.4), "N130": (13.64, -0.44), "N131": (17.97, 2.57), "Biblioteca": (17.31, 11.35),
    "Edificio D2": (13.83, 12.51), "Edificio O": (8.46, 6.4), "Edificio D1": (4.16, 13.71)
}


# Lista completa de aristas con distancias
edges = [
    ("N01", "N02", 38.4), ("N02", "N03", 26.5), ("N03", "K2", 35.5), ("K2", "K3", 22.2), ("K3", "Cafeteria AdPortas", 21.8),
    ("Cafeteria AdPortas", "Edificio Ad1", 40), ("Edificio Ad1", "N29", 42.87), ("Edificio Ad1", "Ad2", 34.17), ("N29", "N27", 28), ("Ad2", "N27", 39.34),
    ("N27", "N25", 22.66), ("Ad2", "Ad3", 25.55), ("Ad3", "N25", 38.24), ("N25", "N23", 23.13), ("Ad3", "Ad4", 29),
    ("Ad4", "N23", 40), ("Ad4", "Living", 42.05), ("N23", "N20", 25.24), ("Living", "N20", 46.57), ("Living", "N33", 14),
    ("N33", "N38", 63.55), ("N38", "Edificio G(1)", 17.22), ("N38", "N35", 18.07), ("N35", "N34", 7.8), ("N32", "N34", 15.11),
    ("N32", "N20", 26.57), ("N35", "N37", 11.68), ("N37", "N40", 33.43), ("N38", "N40", 31.26), ("N40", "N41", 27.57),
    ("N41", "G2", 23.32), ("G2", "Embarcadero", 23.62), ("N41", "N44", 30.45), ("N44", "N45", 7.53), ("Embarcadero", "N45", 15.37),
    ("N45", "N46", 9.39), ("N46", "N47", 5.51), ("N47", "Cafeteria Embarcadero", 20.65), ("N44", "N49", 15.92), ("N46", "Edificio E1(1)", 16.98),
    ("N49", "Edificio E1(1)", 17.09), ("N47", "N51", 17.34), ("Edificio E1(1)", "N51", 6.3), ("N51", "N52", 12.29), ("N52", "Edificio E2", 12.55),
    ("N52", "N54", 9.74), ("N55", "N54", 22.07), ("N55", "N56", 16.33), ("N49", "N92", 52), ("N92", "N56", 46.37),
    ("N56", "N57", 47.65), ("N57", "Edificio E1(2)", 44.29), ("N57", "N59", 11.71), ("N59", "N60", 9.79), ("N60", "N61", 31.13),
    ("N61", "Puente Madera", 78.86), ("Puente Madera", "N63", 9.02), ("N63", "N64", 92.9), ("N64", "N65", 24.55), ("N65", "N66", 13.57),
    ("N66", "N75", 26.25), ("N75", "Meson", 14.32), ("Meson", "N77", 34.96), ("N77", "N78", 14.69), ("Meson", "N79", 37.59),
    ("N79", "N80", 24.11), ("N79", "N70", 35.52), ("N70", "N71", 9.24), ("N70", "N72", 24.34), ("N70", "N69", 6.58),
    ("N68", "N69", 14.32), ("N69", "N73", 19.8), ("N68", "N67", 19.05), ("N73", "Bienestar", 5.68), ("N64", "N67", 27.15),
    ("N67", "Bienestar", 14), ("Bienestar", "N82", 42.11), ("N82", "N81", 17.91), ("N82", "N83", 22.42), ("N83", "Cafeteria Atelier", 8.39),
    ("N83", "Edificio F", 19.91), ("Edificio F", "Edificio H", 8.76), ("Edificio F", "N87", 15.78), ("N87", "N88", 22.32), ("N81", "N90", 54.25),
    ("N81", "N63", 54.99), ("N90", "N91", 66), ("N91", "N92", 60.78), ("N90", "N56", 76.43), ("N89", "N93", 39.38),
    ("N93", "N94", 12.89), ("N94", "N95", 6.68), ("N93", "N99", 33.26), ("N95", "Punto Verde", 14.9), ("N95", "Punto Wok", 21.39),
    ("Punto Verde", "Edificio O", 62.21), ("Punto Verde", "N98", 18.55), ("Punto Verde", "N99", 18.91), ("N99", "N100", 21.84), ("N99", "N101", 20.88),
    ("N101", "Punto Sandwich", 18.89), ("Punto Sandwich", "N108", 11.24), ("N100", "N108", 21.03), ("N108", "N107", 11.54), ("N106", "N105", 13.85),
    ("N106", "Punto Sandwich", 6.76), ("N106", "Edificio B", 18.61), ("Edificio B", "N129", 21.87), ("N129", "N128", 5.97), ("N102", "Edificio B", 18.15),
    ("N106", "N105", 8.97), ("N105", "N102", 18.12), ("N105", "N104", 16.29), ("N104", "N103", 4.87), ("N102", "N103", 22.8),
    ("N104", "N14", 16.26), ("N12", "N14", 17.62), ("N103", "N15", 42.79), ("N13", "N15", 19.9), ("N15", "Casa de Gobierno", 27.69),
    ("N12", "N13", 17.53), ("Edificio O", "Edificio D1", 50.2), ("Edificio O", "Biblioteca", 56.83), ("Biblioteca", "Edificio D2", 19.57), ("N19", "Edificio D2", 52.62),
    ("N19", "N20", 58.04), ("N19", "Capilla", 41.33), ("N17", "Capilla", 13.78), ("Casa de Gobierno", "N17", 20.48), ("Biblioteca", "N131", 60.04),
    ("N131", "N130", 32.55), ("N12", "N10", 17.31), ("N10", "Facultad Ingenieria", 40.78), ("N05", "N10", 57.14), ("N05", "N06", 25.04),
    ("N05", "N07", 22.94), ("N07", "N09", 12.08), ("N07", "Edificio K1", 18.78), ("N05", "N02", 47.14), ("N09", "N29", 84.29),
    ("N129", "N128", 6.13), ("N128", "Edificio A", 23.27), ("Edificio A", "N125", 8.38), ("Edificio A", "N126", 7.81), ("N126", "N125", 8.21),
    ("N126", "N124", 24.4), ("N124", "N123", 8.04), ("N123", "N116", 26.31), ("N116", "N117", 13.55), ("N117", "Kioskos(2)", 10.51),
    ("N116", "N115", 14.79), ("N115", "N119", 49.3), ("N119", "Kioskos(1)", 13.97), ("Kioskos(1)", "N122", 9.32), ("Kioskos(1)", "N121", 38),
    ("N115", "Edificio C", 42.27), ("Edificio C", "N111", 39.78), ("Edificio C", "Puesto HotDog", 29.52), ("N111", "Puesto HotDog", 25.85), ("Puesto HotDog", "N115", 31.7),
    ("Puesto HotDog", "N114", 8.34), ("N111", "Edificio B", 32.12), ("N114", "N125", 28.45), ("Edificio D1", "Capilla", 15.6)
]

# Añadir aristas y pesos al grafo
G.add_weighted_edges_from(edges)

# Implementación del algoritmo de Dijkstra
def dijkstra_custom(grafo, inicio, fin):
    # Inicialización
    distancias = {nodo: sys.maxsize for nodo in grafo.nodes}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo.nodes}
    visitados = set()

    while True:
        # Seleccionar el nodo no visitado con la distancia mínima
        nodo_actual = None
        for nodo in grafo.nodes:
            if nodo not in visitados:
                if nodo_actual is None or distancias[nodo] < distancias[nodo_actual]:
                    nodo_actual = nodo

        if nodo_actual is None or distancias[nodo_actual] == sys.maxsize:
            # No quedan nodos accesibles o alcanzamos un nodo no accesible
            break

        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)

        # Actualizar las distancias de los vecinos
        for vecino in grafo.neighbors(nodo_actual):
            peso = grafo[nodo_actual][vecino]['weight']
            nueva_distancia = distancias[nodo_actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = nodo_actual

        # Parar si llegamos al destino
        if nodo_actual == fin:
            break

    # Reconstruir el camino más corto desde el nodo final al inicio
    camino = []
    nodo = fin
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padres[nodo]

    # Verificar si se alcanzó el destino
    if distancias[fin] == sys.maxsize:
        print("No hay camino disponible entre", inicio, "y", fin)
        return None

    # Imprimir la distancia total y el camino
    print(f"\nCamino más corto entre {inicio} y {fin}:")
    for i in range(len(camino) - 1):
        origen, destino = camino[i], camino[i + 1]
        distancia = grafo[origen][destino]['weight']
        print(f"   {origen} -> {destino}: {distancia} metros")
    print(f"\nDistancia total del camino más corto: {distancias[fin]} metros\n")

    return camino

# Función para visualizar el grafo y el camino más corto
def visualizar_camino():
    print("Principales referencias en la Universidad: \n1. Edificio K1 \n2. Facultad Ingenieria \n3. Casa de Gobierno \n4. Capilla \n5. Living \n6. Edificio Ad1 \n7. Cafeteria AdPortas \n8. Edificio G(1) \n9. Embarcadero \n10. Cafeteria Embarcadero \n11. Edificio E1(1) \n12. Edificio E2 \n13. Edificio E1(2) \n14. Puente Madera \n15. Bienestar \n16. Meson \n17. Cafeteria Atelier \n18. Edificio F \n19. Edificio H \n20. Punto Wok \n21. Punto Verde \n22. Punto Sandwich \n23. Edificio B \n24. Edificio C \n25. Puesto HotDog \n26. Kioskos(1) \n27. Edificio A \n28. Biblioteca \n29. Edificio D2 \n30. Edificio O \n31. Edificio D1")
    print("Cualquier otra ubicacion que no este en las referencias por favor marque el numero del nodo (Ej. N#) ")
    inicio = input("Ingrese su punto de partida: ")
    fin = input("Ingrese su destino: ")
    camino = dijkstra_custom(G, inicio, fin)
    
    if camino:
        plt.figure(figsize=(12, 12))
        nx.draw(G, nuevas_posiciones, with_labels=True, node_size=500, node_color="lightblue",
                font_size=8, font_weight="bold", edge_color="gray")
        camino_edges = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, nuevas_posiciones, edgelist=camino_edges, edge_color="red", width=3)
        plt.title(f"Camino más corto entre {inicio} y {fin}")
        plt.show()

# Ejecutar visualización con interacción de usuario
visualizar_camino()
