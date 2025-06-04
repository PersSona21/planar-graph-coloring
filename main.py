import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def read_adjacency_matrix():
    """Считывает матрицу смежности из ввода пользователя."""
    print("Введите размер матрицы (число вершин):")
    n = int(input())
    matrix = []
    print("Введите матрицу смежности построчно (0 или 1, разделённые пробелами):")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return np.array(matrix)

def greedy_coloring(graph):
    """Реализует жадную раскраску графа."""
    colors = {}  # Словарь для хранения цвета каждой вершины
    available_colors = set()  # Множество доступных цветов

    # Проходим по всем вершинам
    for vertex in graph.nodes():
        # Получаем соседей текущей вершины
        neighbors = set(graph.neighbors(vertex))
        # Узнаём цвета соседей
        neighbor_colors = {colors.get(neighbor) for neighbor in neighbors if neighbor in colors}
        
        # Находим наименьший доступный цвет
        color = 0
        while color in neighbor_colors:
            color += 1
        colors[vertex] = color

    return colors

def visualize_graph(matrix, colors):
    """Визуализирует граф с раскраской."""
    # Создаём граф на основе матрицы смежности
    G = nx.Graph(matrix)
    pos = nx.spring_layout(G)  # Расположение вершин

    # Определяем цвета для вершин (RGB)
    color_map = ['#FF9999', '#99FF99', '#9999FF', '#FFFF99', '#FF99FF']  # Различные цвета
    vertex_colors = [color_map[colors[i] % len(color_map)] for i in range(len(colors))]

    # Рисуем граф
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_color=vertex_colors, with_labels=True, node_size=500, font_size=12, font_weight='bold')
    plt.title("Раскраска планарного графа (жадный алгоритм)")
    plt.show()

def main():
    # Считываем матрицу смежности
    matrix = read_adjacency_matrix()
    
    # Создаём граф
    G = nx.Graph(matrix)
    
    # Применяем жадную раскраску
    colors = greedy_coloring(G)
    
    # Выводим результаты
    print("Раскраска вершин (индекс: цвет):")
    for vertex, color in colors.items():
        print(f"Вершина {vertex}: цвет {color}")
    
    # Визуализация
    visualize_graph(matrix, colors)

if __name__ == "__main__":
    main()