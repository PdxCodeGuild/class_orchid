import random
ticket_counter = 0
cost = 0
prize_money = 0
match_counter = {
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
}

def pick6():
    winner = [0, 0, 0, 0, 0, 0]
    purchased = [0, 0, 0, 0, 0, 0]
    for x in range(0,6):
        winner[x] = random.randint(1,99)
        purchased[x] = random.randint(1,99)

    return winner, purchased

def num_matches(winner, purchased):
    matches = []
    for x in range(0,5):
        if winner[x] == purchased[x]:
            matches.append([winner[x], purchased[x]])
    return matches

while ticket_counter != 100000:
    tickets = pick6()
    winning_ticket = tickets[0]
    purchased_ticket = tickets[1]

    matches = len(num_matches(winning_ticket, purchased_ticket))
    see_matches = num_matches(winning_ticket, purchased_ticket)
    if matches == 1:
        match_counter['1'] += 1
        prize_money += 4
    elif matches == 2:
        match_counter['2'] += 1
        prize_money += 7
    elif matches == 3:
        match_counter['3'] += 1
        prize_money += 100
    elif matches == 4:
        print(f'winner: {winning_ticket}, purchased: {purchased_ticket}\nmatches: {matches}: {see_matches}')
        match_counter['4'] += 1
        prize_money += 50000
    elif matches == 5:
        print(f'winner: {winning_ticket}, purchased: {purchased_ticket}\,matches: {matches}: {see_matches}')
        match_counter['5'] += 1
        prize_money += 1000000
    elif matches == 6:
        print(f'winner: {winning_ticket}, purchased: {purchased_ticket}\nmatches: {matches}: {see_matches}')
        match_counter['6'] += 1
        prize_money += 25000000

    ticket_counter += 1
    cost += 2

ROI = (prize_money - cost)/cost
print(f'\ncost: ${cost}\nprize money: ${prize_money} \nmatches: {match_counter}\nROI: {ROI}')