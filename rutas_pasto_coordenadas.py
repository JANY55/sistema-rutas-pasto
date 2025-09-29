import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# ======================================
# Coordenadas de inicio y destino
# Plaza de Nariño (Pasto, Colombia)
origen = (1.2149619545987047, -77.27620836592861)

# Barrio Tamasagra (Pasto, Colombia)
destino = (1.2105, -77.2855)
# ======================================

print("Descargando red de calles de Pasto...")
# Descargar red de calles de Pasto (solo para autos)
G = ox.graph_from_place("Pasto, Nariño, Colombia", network_type="drive")

# Encontrar nodos más cercanos al origen y destino
origen_nodo = ox.distance.nearest_nodes(G, X=origen[1], Y=origen[0])
destino_nodo = ox.distance.nearest_nodes(G, X=destino[1], Y=destino[0])

print("===================================")
print("Resultados de la búsqueda de rutas")
print("===================================")

# Ruta más corta en distancia
ruta_corta = nx.shortest_path(G, origen_nodo, destino_nodo, weight="length")
distancia = nx.shortest_path_length(G, origen_nodo, destino_nodo, weight="length")
print(f"Ruta más corta en distancia: {distancia/1000:.2f} km")

# Ruta más rápida (aprox. usando velocidad de OSM)
ruta_rapida = nx.shortest_path(G, origen_nodo, destino_nodo, weight="travel_time")
tiempo = nx.shortest_path_length(G, origen_nodo, destino_nodo, weight="travel_time")
print(f"Ruta más rápida en tiempo: {tiempo/60:.1f} minutos (aprox.)")

# Dibujar mapa con ambas rutas
fig, ax = ox.plot_graph_routes(
    G, [ruta_corta, ruta_rapida],
    route_colors=["red", "blue"],
    route_linewidth=3,
    node_size=0,
    bgcolor="white"
)
