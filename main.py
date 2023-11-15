# Карта
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 3, 1, 1, 0, 3, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 3, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 3, 1, 1, 1, 1, 3, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Функция, которая возвращает в радиусе от игрока блоки
def get_field_around_player(player_symbol, radius):
    global map

    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == player_symbol:
                player_position = (i, j)
                break

    field_around_player = []
    for i in range(max(0, player_position[0] - radius), min(len(map), player_position[0] + radius + 1)):
        row = []
        for j in range(max(0, player_position[1] - radius), min(len(map[0]), player_position[1] + radius + 1)):
            row.append(map[i][j])
        field_around_player.append(row)
    
    return field_around_player
    
# Ваша функция,которая должна вернуть куда должен сходить персонаж
def movePlayer(map, store):
    # Вывод матрицы в консоли, разкомментировать для тестирования
    #for row in map:
        #for element in row:
            #print(element, end=' ')
        #print() 

    return 'bottom', store

# Количество еды на карте
amoutn_food = 5
player_moves = 0

def move(direction):
    global player_moves
    global map
    global amoutn_food

    player_moves += 1
    player_position = [(i, row.index(2)) for i, row in enumerate(map) if 2 in row][0]

    new_position = None

    # Поиск позиции куда нужно пойти
    if direction == 'left':
        new_position = (player_position[0], player_position[1] - 1)
    elif direction == 'right':
        new_position = (player_position[0], player_position[1] + 1)
    elif direction == 'top':
        new_position = (player_position[0] - 1, player_position[1])
    elif direction == 'bottom':
        new_position = (player_position[0] + 1, player_position[1])

    if 0 <= new_position[0] < 10 and 0 <= new_position[1] < 10:
        # Проверяем, не стоит ли на новой позиции стена
        if map[new_position[0]][new_position[1]] != 0:
            if map[new_position[0]][new_position[1]] == 3:
                amoutn_food -= 1
            map[player_position[0]][player_position[1]] = 1
            map[new_position[0]][new_position[1]] = 2

store = {}

# Выполнение
while (player_moves < 5000 and amoutn_food > 0):
    visible_zone = get_field_around_player(2, 2)

    direction, store = movePlayer(visible_zone, store)

    #print('----------')
    
    move(direction)

print('Ваше количество ходов программы: ' + str(player_moves))