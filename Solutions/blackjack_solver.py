import itertools


def simulate_game(deck):
  player_score = 0
  dealer_score = 0

  player_hand = [deck.pop(0), deck.pop(0)]
  dealer_hand = [deck.pop(0), deck.pop(0)]

  player_score = sum_card_values(player_hand)
  dealer_score = sum_card_values(dealer_hand)

  while player_score < 21:
    if player_score < 11:
      player_hand.append(deck.pop(0))
      player_score = sum_card_values(player_hand)
    else:
      ace_count = player_hand.count(1)
      if ace_count > 0 and player_score + 10 <= 21:
        player_score += 10
      else:
        break

  while dealer_score < 17:
    dealer_hand.append(deck.pop(0))
    dealer_score = sum_card_values(dealer_hand)

  if player_score > 21:
    return -1
  elif dealer_score > 21:
    return 1
  elif player_score > dealer_score:
    return 1
  elif player_score < dealer_score:
    return -1
  else:
    return 0


def sum_card_values(hand):
  total = sum(hand)
  return total


def blackjack_solver(deck):
  total_wins = 0
  total_losses = 0

  deck_permutations = list(itertools.permutations(deck))

  for perm in deck_permutations:
    result = simulate_game(list(perm))
    if result == 1:
      total_wins += 1
    elif result == -1:
      total_losses += 1

  return total_wins - total_losses


if __name__ == "__main__":
  deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1] * 4  # Deck of 52 cards
  max_score = blackjack_solver(deck)
  print("Maximum score:", max_score)
