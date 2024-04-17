def is_winning_ticket(t):
    if len(ticket) != 20:
        return f"invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_side = ticket[:10]
    right_side = ticket[10:]
    for win_symbol in winning_symbols:
        for repeat in range(10, 5, -1):
            lucky_repeat = win_symbol * repeat
            if lucky_repeat in left_side and lucky_repeat in right_side:
                if repeat == 10:
                    return f'ticket "{ticket}" - 10{win_symbol} Jackpot!'
                return f'ticket "{ticket}" - {repeat}{win_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning_ticket(ticket))

# def length_valid(a_ticket):
#     if len(a_ticket.strip()) == 20:
#         ticket.strip()
#         return True
#     return False
#
#
# def symbol_finder(left, right):
#     if "@" in left and "@" in right:
#         return "@"
#     elif "#" in left and "#" in right:
#         return "#"
#     elif "$" in left and "$" in right:
#         return "$"
#     elif "^" in left and "^" in right:
#         return "^"
#     else:
#         return False
#
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# for ticket in tickets:
#     if not length_valid(ticket):
#         print("invalid ticket")
#         continue
#     left_side = ticket[:10]
#     right_side = ticket[10:]
#     if not symbol_finder(left_side, right_side):
#         print(f'ticket "{ticket}" - no match')
#         continue
#     else:
#         symbol = symbol_finder(left_side, right_side)
#     winner_ticket = []
#     ticket_parts = [left_side, right_side]
#     index = 0
#     for side in ticket_parts:
#         symbols_cnt = 0
#         uninterrupted = [0]
#         index_cnt = 0
#         for ch in side:
#             if ch is symbol:
#                 symbols_cnt += 1
#                 if index_cnt == len(side)-1:
#                     uninterrupted.append(symbols_cnt)
#             elif symbols_cnt > 0:
#                 uninterrupted.append(symbols_cnt)
#                 symbols_cnt = 0
#             index_cnt += 1
#         winner_ticket.append(max(uninterrupted))
#         index += 1
#     if winner_ticket[0] == winner_ticket[1] == 10:
#         print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
#     elif winner_ticket[0] >= 6 or winner_ticket[1] >= 6:
#         print(f'ticket "{ticket}" - {min(winner_ticket)}{symbol}')
#     else:
#         print(f'ticket "{ticket}" - no match')
