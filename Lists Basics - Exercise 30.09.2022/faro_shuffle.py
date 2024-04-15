# # text1 = ('A', 'B', 'C', 'D', 4)     # 3, 2, 1
# # text2 = ('A', 1, 'B', 2, 'C', 3, 'D', 4)
#
# deck = input().split()
# shuffles = int(input())
#
# for shuffle in range(shuffles):
#     removed_cards = list()
#     for removed_card in range(len(deck)//2 - 1):
#         removed = deck.pop(-2)
#         removed_cards.append(removed)
#     removed_cards.reverse()
#     for added_card in range(len(removed_cards), 0, -1):
#         added = removed_cards.pop()
#         deck.insert(added_card, added)
# print(deck)

deck = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    final_deck = []
    half_cards = len(deck) // 2
    left_part = deck[:half_cards]
    right_part = deck[half_cards::]
    for card in range(len(left_part)):
        final_deck.append(left_part[card])
        final_deck.append(right_part[card])
    deck = final_deck
print(deck)