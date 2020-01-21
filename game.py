from random import choice
import sys
from cards_classes import *

# список всех классов карт
all_cards = [Card1(),
             Card2(),
             Card3(),
             Card4(),
             Card5(),
             Card6(),
             Card7(),
             Card8(),
             Card9(),
             Card10(),
             Card11(),
             Card12(),
             Card13(),
             Card14(),
             Card15(),
             Card16(),
             Card17(),
             Card18(),
             Card19(),
             Card20(),
             Card21(),
             Card22(),
             Card23(),
             Card24(),
             Card25(),
             Card26(),
             Card27(),
             Card28(),
             Card29(),
             Card30(),
             Card31(),
             Card32(),
             Card33(),
             Card34(),
             Card35(),
             Card36(),
             Card37(),
             Card38(),
             Card39(),
             Card40(),
             Card41(),
             Card42(),
             Card43(),
             Card44(),
             Card45(),
             Card46(),
             Card47(),
             Card48(),
             Card49(),
             Card50(),
             Card51(),
             Card52(),
             Card53(),
             Card54(),
             Card55(),
             Card56(),
             Card57(),
             Card58(),
             Card59(),
             Card60(),
             Card61(),
             Card62(),
             Card63(),
             Card64(),
             Card65(),
             Card66(),
             Card67(),
             Card68(),
             Card69(),
             Card70(),
             Card71(),
             Card72(),
             Card73(),
             Card74(),
             Card75(),
             Card76(),
             Card77(),
             Card78(),
             Card79(),
             Card80(),
             Card81(),
             Card82(),
             Card83(),
             Card84(),
             Card85(),
             Card86(),
             Card87(),
             Card88(),
             Card89(),
             Card90(),
             Card91(),
             Card92(),
             Card93(),
             Card94(),
             Card95(),
             Card96(),
             Card97(),
             Card98(),
             Card99(),
             Card100(),
             Card101(),
             Card102()
             ]
n_u_c = Card1()
Player1 = Player1()
Player2 = Player2()
a = int(input('введите кирпичи'))
b = int(input('магию'))
c = int(input('рекрутов'))
Player1.add_per_turn(a, b, c)
for i in range(5):
    Player1.add_card(choice(all_cards))
    Player2.add_card(choice(all_cards))


# начало основного цикла игры
running = True
while running:
    print('Игрок 1:')
    print()
    print('кирпичей:', Player1.bricks, '  производится за ход:', Player1.bricks_per_turn)
    print('магии:', Player1.magic, '     производится за ход:', Player1.magic_per_turn)
    print('рекрутов:', Player1.recruits, '  поступает за ход:', Player1.recruits_per_turn)
    print()
    print('Высота башни:', Player1.tower)
    print('Высота стены:', Player2.wall)
    print()
    print(Player1.cards)
    print()
    cont = 0

    # цикл ожидания допустимого хода игрока
    while cont == 0:
        print('Выберете карту, или напишите выйти, чтобы закончить')
        c = input()
        if c == 'выйти':
            break
        n_u_c = Player1.cards[int(c) - 1]

        print('Вы хотите использовать карту(1) или скинуть её(2)?')
        ans = input()
        if ans == '2':
            Player1.del_card(int(c) - 1)
            Player1.add_card(choice(all_cards))
            cont = 1
        elif ans == '1':
            kr = 0
            if n_u_c.need_resource == 'brick':
                if Player1.bricks >= n_u_c.cost:
                    kr = 1
                    Player1.add_per_turn(-n_u_c.cost, 0, 0)
            elif n_u_c.need_resource == 'magic':
                if Player1.magic >= n_u_c.cost:
                    kr = 1
                    Player1.add_per_turn(0, -n_u_c.cost, 0)
            elif n_u_c.need_resource == 'recruits':
                if Player1.recruits >= n_u_c.cost:
                    kr = 1
                    Player1.add_per_turn(0, 0, -n_u_c.cost)
            if kr == 1:
                Player1.del_card(int(c) - 1)
                Player1.cards.append(choice(all_cards))

                # подсчет ресурсов игроков после хода
                Player1.add_per_turn(n_u_c.bricks, n_u_c.magic, n_u_c.recruits)
                Player1.add_production(n_u_c.b_p_t, n_u_c.m_p_t, n_u_c.r_p_t)
                Player1.add_defence(n_u_c.tower, n_u_c.wall)

                Player2.add_per_turn(n_u_c.enemy_bricks, n_u_c.enemy_magic, n_u_c.enemy_recruits)
                Player2.add_production(n_u_c.enemy_b_p_t, n_u_c.enemy_m_p_t, n_u_c.enemy_r_p_t)
                Player2.add_defence(n_u_c.enemy_tower, n_u_c.enemy_wall)
                cont = 1
            else:
                print('Недостаточно ресурсов')
                print()
            if Player2.tower <= 0:
                print('Игрок 1 Выйграл!!!')
                c = 'выйти'
            elif Player1.tower <= 0:
                print('Игрок 2 выйграл!!!')
                c = 'выйти'

    if c == 'выйти':
        break

    print('Игрок 2:')
    print()
    print('кирпичей:', Player2.bricks, '  производится за ход:', Player2.bricks_per_turn)
    print('магии:', Player2.magic, '     производится за ход:', Player2.magic_per_turn)
    print('рекрутов:', Player2.recruits, '  поступает за ход:', Player2.recruits_per_turn)
    print()
    print('Высота башни:', Player2.tower)
    print('Высота стены:', Player2.wall)
    print()
    print(Player2.cards)
    print()
    cont = 0

    # цикл ожидания допустимого хода игрока
    while cont == 0:
        print('Выберете карту, или напишите выйти, чтобы закончить')
        AI().find_inf(Player2)
        AI().variants_of_turns()
        c = AI().a
        if c == 'выйти':
            break
        use_card = Player2.cards[int(c) - 1]
        print('Вы хотите использовать карту(1) или скинуть её(2)?')
        ans = AI().b
        if ans == 2:
            Player2.del_card(int(c) - 1)
            Player2.add_card(choice(all_cards))
            cont = 1
        elif ans == 1:
            kr = 0
            if n_u_c.need_resource == 'brick':
                if Player2.bricks >= n_u_c.cost:
                    kr = 1
                    Player2.add_per_turn(-n_u_c.cost, 0, 0)
            elif n_u_c.need_resource == 'magic':
                if Player2.magic >= n_u_c.cost:
                    kr = 1
                    Player2.add_per_turn(0, -n_u_c.cost, 0)
            elif n_u_c.need_resource == 'recruits':
                if Player2.recruits >= n_u_c.cost:
                    kr = 1
                    Player2.add_per_turn(0, 0, -n_u_c.cost)
            if kr == 1:
                Player2.del_card(int(c) - 1)
                Player2.cards.append(choice(all_cards))

                # подсчет ресурсов игроков после хода
                Player2.add_per_turn(n_u_c.bricks, n_u_c.magic, n_u_c.recruits)
                Player2.add_production(n_u_c.b_p_t, n_u_c.m_p_t, n_u_c.r_p_t)
                Player2.add_defence(n_u_c.tower, n_u_c.wall)

                Player1.add_per_turn(n_u_c.enemy_bricks, n_u_c.enemy_magic, n_u_c.enemy_recruits)
                Player1.add_production(n_u_c.enemy_b_p_t, n_u_c.enemy_m_p_t, n_u_c.enemy_r_p_t)
                Player1.add_defence(n_u_c.enemy_tower, n_u_c.enemy_wall)
                cont = 1
            else:
                print('Недостаточно ресурсов')
                print()
            if Player1.tower <= 0:
                print('Игрок 2 выйграл!!!')
                c = 'выйти'
            elif Player2.tower <= 0:
                print('Игрок 1 Выйграл!!!')
                c = 'выйти'

    if c == 'выйти':
        break





