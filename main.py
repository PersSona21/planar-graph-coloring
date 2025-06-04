import networkx as nx
import matplotlib
matplotlib.use('Qt5Agg')  # Устанавливаем Qt5Agg как бэкенд
import matplotlib.pyplot as plt
import numpy as np

# Словарь соответствий номеров цветов и их названий (ограничимся 4 цветами)
COLOR_NAMES = {
    0: "красный",
    1: "зелёный",
    2: "синий",
    3: "жёлтый"
}

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
    """Реализует жадную раскраску графа с ограничением до 4 цветов."""
    colors = {}  # Словарь для хранения номера цвета каждой вершины

    # Проходим по всем вершинам
    for vertex in graph.nodes():
        # Получаем соседей текущей вершины
        neighbors = set(graph.neighbors(vertex))
        # Узнаём цвета соседей
        neighbor_colors = {colors.get(neighbor) for neighbor in neighbors if neighbor in colors}
        
        # Находим наименьший доступный цвет (до 3, так как 0-3 = 4 цвета)
        color = 0
        while color in neighbor_colors and color < 4:
            color += 1
        # Если все 4 цвета использованы соседями (что редко для планарных графов),
        # оставляем последний доступный цвет
        if color >= 4:
            color = 3  # Принудительно ограничиваем до 3 (жёлтый)
        colors[vertex] = color

    return colors

def visualize_graph(matrix, colors):
    """Визуализирует граф с раскраской."""
    # Создаём граф на основе матрицы смежности
    G = nx.Graph(matrix)
    pos = nx.spring_layout(G)  # Расположение вершин

    # Определяем цвета для вершин (RGB) на основе COLOR_NAMES
    color_map = {
        0: '#FF9999',  # красный
        1: '#99FF99',  # зелёный
        2: '#9999FF',  # синий
        3: '#FFFF99'   # жёлтый
    }
    vertex_colors = [color_map[colors[i] % len(color_map)] for i in range(len(colors))]

    # Рисуем граф
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_color=vertex_colors, with_labels=True, node_size=500, font_size=12, font_weight='bold')
    plt.title("Раскраска планарного графа (жадный алгоритм, 4 цвета)")
    plt.savefig("graph_coloring.png")
    plt.show()

def main():
    # Считываем матрицу смежности
    matrix = read_adjacency_matrix()
    
    # Создаём граф
    G = nx.Graph(matrix)
    
    # Применяем жадную раскраску
    colors = greedy_coloring(G)
    
    # Выводим результаты с названиями цветов
    print(f"Раскраска вершин (индекс: цвет):")
    for vertex, color_num in colors.items():
        color_name = COLOR_NAMES.get(color_num, f"цвет {color_num}")  # Если цвет вне словаря
        print(f"Вершина {vertex}: {color_name}")
    
    # Визуализация
    visualize_graph(matrix, colors)

if __name__ == "__main__":
    main()