# Класс для узла
class Node:
    def __init__(self, description, choices=None):
        self.description = description
        self.choices = choices if choices else {}

# Класс для квеста
class QuestGraph:
    def __init__(self):
        self.nodes = {}
        self.create_graph()

    def add_node(self, node_key, description, choices=None):
        self.nodes[node_key] = Node(description, choices)

    def create_graph(self):
        self.add_node(
            "start",
            "Алексей выходит из дома и видит два возможных пути в библиотеку: короткий через площадь и длинный через тихие улочки.",
            {"A": "short_path", "B": "long_path"}
        )
        self.add_node(
            "short_path",
            "На площади происходит стычка между демонстрантами и полицией. Алексей может помочь раненому демонстранту или уйти, чтобы не попасть в беду.",
            {"A": "help_protester", "B": "leave_square"}
        )
        self.add_node("help_protester", "Помощь демонстранту приводит к новым знакомствам среди студентов, но также привлекает внимание полиции.")
        self.add_node("leave_square", "Алексей сохраняет нейтралитет, но упускает шанс узнать важные новости от демонстрантов.")
        self.add_node(
            "long_path",
            "По дороге Алексей находит странную записку, которая приводит его к загадочному дневнику.",
            {"A": "explore_diary", "B": "ignore_find"}
        )
        self.add_node("explore_diary", "Изучение дневника открывает новую сюжетную ветвь о тайном обществе и дает подсказки о местоположении важных документов.")
        self.add_node("ignore_find", "Алексей продолжает свой путь в библиотеку, но упускает шанс погрузиться в загадочное приключение.")

    def get_node(self, node_key):
        return self.nodes[node_key]

    def show_path(self, node_key):
        node = self.get_node(node_key)
        print(f"Описание: {node.description}\n")
        if node.choices:
            for key, value in node.choices.items():
                print(f"Выбор {key}: Ведет к узлу '{value}'")

# Дополнение квеста функционалом для интерактивного выбора пути пользователем
class InteractiveQuestGraph(QuestGraph):
    def start_quest(self):
        current_node_key = "start"
        while True:
            self.show_path(current_node_key)
            current_node = self.get_node(current_node_key)
            
            if not current_node.choices:
                print("Этот путь завершен. Спасибо за участие в квесте!")
                break
            
            choice = input("Введите ваш выбор (например, A или B): ").strip().upper()
            
            
            if choice in current_node.choices:
                
                current_node_key = current_node.choices[choice]
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")

# Создание объекта интерактивного квеста
interactive_quest = InteractiveQuestGraph()

# Запуск квеста
interactive_quest.start_quest()

