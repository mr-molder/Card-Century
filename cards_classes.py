from random import choice


class Player1:
    def __init__(self):
        self.bricks = 0
        self.magic = 0
        self.recruits = 0
        self.tower = 10
        self.wall = 0
        self.bricks_per_turn = 1
        self.magic_per_turn = 1
        self.recruits_per_turn = 1
        self.cards = []

    def add_per_turn(self, b, m, r):
        self.bricks += b
        self.magic += m
        self.recruits += r
        if self.bricks < 0:
            self.bricks = 0
        if self.magic < 0:
            self.magic = 0
        if self.recruits < 0:
            self.recruits = 0

    def add_production(self, br, ma, re):
        self.bricks_per_turn += br
        self.magic_per_turn += ma
        self.recruits_per_turn += re
        if self.bricks_per_turn < 1:
            self.bricks_per_turn = 1
        if self.magic_per_turn < 1:
            self.magic_per_turn = 1
        if self.recruits_per_turn < 1:
            self.recruits_per_turn = 1

    def add_defence(self, t, w):
        self.tower += t
        self.wall += w
        if self.wall < 0:
            self.wall = 0

    def add_card(self, card):
        self.cards.append(card)

    def del_card(self, card):
        del self.cards[card]


class Player2:
    def __init__(self):
        self.bricks = 5
        self.magic = 5
        self.recruits = 5
        self.tower = 10
        self.wall = 0
        self.bricks_per_turn = 1
        self.magic_per_turn = 1
        self.recruits_per_turn = 1
        self.cards = []

    def add_per_turn(self, b, m, r):
        self.bricks += b
        self.magic += m
        self.recruits += r
        if self.bricks < 0:
            self.bricks = 0
        if self.magic < 0:
            self.magic = 0
        if self.recruits < 0:
            self.recruits = 0

    def add_production(self, br, ma, re):
        self.bricks_per_turn += br
        self.magic_per_turn += ma
        self.recruits_per_turn += re
        if self.bricks_per_turn < 1:
            self.bricks_per_turn = 1
        if self.magic_per_turn < 1:
            self.magic_per_turn = 1
        if self.recruits_per_turn < 1:
            self.recruits_per_turn = 1

    def add_defence(self, t, w):
        self.tower += t
        self.wall += w
        if self.wall < 0:
            self.wall = 0

    def add_card(self, card):
        self.cards.append(card)

    def del_card(self, card):
        del self.cards[card]


class AI:
    def __init__(self):
        self.ai_cards = []
        self.bricks = 1
        self.magic = 1
        self.recruits = 1
        self.bricks_per_turn = 1
        self.magic_per_turn = 1
        self.recruits_per_turn = 1
        self.tower = 1
        self.wall = 1
        self.ability = 0
        self.a = 1
        self.b = 2

    def find_inf(self, player):
        self.ai_cards = player.cards
        self.bricks = player.bricks
        self.magic = player.magic
        self.recruits = player.recruits
        self.bricks_per_turn = player.bricks_per_turn
        self.magic_per_turn = player.magic_per_turn
        self.recruits_per_turn = player.recruits_per_turn
        self.tower = player.tower
        self.wall = player.wall

    def check_capability(self, card):
        if card.need_resource == 'brick':
            if card.cost <= self.bricks:
                self.ability = 1
        elif card.need_resource == 'magic':
            if card.cost <= self.magic:
                self.ability = 1
        elif card.need_resource == 'recruits':
            if card.cost <= self.recruits:
                self.ability = 1

    def variants_of_turns(self):
        for i in range(len(self.ai_cards)):
            self.check_capability(self.ai_cards[i])
            if self.ability == 1:
                self.a = i + 1
                self.b = 1


class Card1:
    def __init__(self):
        self.need_resource = 'brick'
        self.cost = 5
        self.bricks = 2
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 0
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 0
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -3


class Card2:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card3:
    def __init__(self):
        self.need_resource = 'recruits'
        self.cost = 6
        self.bricks = 2
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 5
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 0
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 0
        self.tower = 0
        self.enemy_tower = 1
        self.wall = 0
        self.enemy_wall = -2


class Card4:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card5:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card6:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card7:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card8:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card9:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card10:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card11:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card12:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card13:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card14:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card15:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card16:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card17:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card18:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card19:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card20:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card21:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card22:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card23:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card24:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card25:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card26:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card27:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card28:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card29:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card30:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card31:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card32:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card33:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card34:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card35:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card36:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card37:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card38:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card39:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card40:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card41:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card42:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card43:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card44:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card45:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card46:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card47:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card48:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card49:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card50:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card51:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card52:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card53:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card54:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card55:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card56:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card57:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card58:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card59:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card60:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card61:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card62:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card63:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card64:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card65:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card66:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card67:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card68:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card69:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card70:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card71:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card72:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card73:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card74:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card75:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card76:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card77:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card78:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card79:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card80:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card81:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card82:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card83:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card84:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card85:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card86:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card87:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card88:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card89:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card90:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card91:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card92:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card93:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card94:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card95:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card96:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card97:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card98:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card99:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card100:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card101:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4


class Card102:
    def __init__(self):
        self.need_resource = 'magic'
        self.cost = 5
        self.bricks = 1
        self.enemy_bricks = 0
        self.magic = 1
        self.enemy_magic = 0
        self.recruits = 0
        self.enemy_recruits = 0
        self.b_p_t = 0
        self.enemy_b_p_t = 0
        self.m_p_t = 5
        self.enemy_m_p_t = 0
        self.r_p_t = 0
        self.enemy_r_p_t = 1
        self.tower = 0
        self.enemy_tower = 0
        self.wall = 0
        self.enemy_wall = -4
