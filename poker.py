from card import Card
from player import Player
from random import choice

QUIT = False

# Define as pontuaçoes de acordo com o indice da carta na lista
valueRanking = [str(v) for v in range(11)]
valueRanking.append('J')
valueRanking.append('Q')
valueRanking.append('K')
valueRanking[1] = 'A'

suitRanking = ('ouro', 'copas', 'espada', 'paus' )


def shuffle(suits: list, values: list)-> list:
    """Cria o baralho
    Parameters:
    suits (list[str]): lista dos naipes do baralho
    values (list[str]): lista dos valores do baralho

    Returns:
    list[Card]: Baralho

   """
    Deck = []
    for suit in suits:
        for value in values:
            Deck.append(Card(value, suit))
    
    return Deck

def get_points(*cards: Card) -> int:
    """Cria o baralho
    Parameters:
    suits (list[Card]): lista de cartas

    Returns:
    ind: A soma dos pontos correspontentes

   """

    score = 0
    for card in cards:
        if card.suit == 'ESPADA':
            score+= valueRanking.index(card.value)
    
    return score

def get_winner(*players:list)->tuple:
    """Cria o Define o vencedor
    Parameters:
    players (list[Player]): lista de jogadores

    Returns:
    tuple(Player.name, dict{player:score}): Tupla com o vencedor e a lista dos jogadores e
    os respectivos pontos

   """

    player_score ={}
    _max = 0
    winner = None
    for player in players:
        points = get_points(*player.hand)
        player_score[player.name] = points
        if points >_max:
            winner = player.name
            _max = points
    return winner, player_score

def make_hand(lenght: int, Deck:list, player:Player)->list:
    """Cria o Define o vencedor
    Parameters:
    length (int): numero de cartas
    Deck  (list[Card]): Baralho
    player (Player): Jogador

    Returns:
    tuple(Player.name, dict{player:score}): Tupla com o vencedor e a lista dos jogadores e
    os respectivos pontos

   """

    hand = []
    while len(hand)<lenght:
        current_card = choice(Deck).set_card(player)
        if current_card:
            hand.append(current_card)

    return hand   


MAX_PLAYERS = 4
MIN_PLAYERS = 2
HAND_LENGTH = 5

while QUIT!=True:
    print('Preciona [Q] para sair')
    Op = input('Quantos jogadores?')
    if Op.upper() == 'Q':
        #Verifica se O jogador quer sair
        QUIT = True
        break

    try:
        player_number = int(Op)
    except ValueError:
        player_number = 0

    if MIN_PLAYERS <= player_number <= MAX_PLAYERS:

        deck = shuffle(suitRanking, valueRanking[1:])
        players = []

        try:
            for player in range(player_number):
                
                players.append(Player(f'Player {player}'))            
                players[-1].get_cards(*make_hand(HAND_LENGTH,deck,players[-1]))


            score = get_winner(*players)

            print('Vencedor:', score[0])
            print('\n'.join([f'{p.name}: {score[1][p.name]:0>2}pts {p.hand}' for p in players]))

            Out = input('Sair [S]/[N]').upper()
            if Out=='S':
                break
        except:
            print('Desculpe! Deixei o Baralho cair. Vamos tentar de novo')


    else:
        
        print(f'Por favor digite um numero entre {MIN_PLAYERS} e {MAX_PLAYERS}')
        

