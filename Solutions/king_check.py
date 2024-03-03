def is_king_in_check(board):

  def find_piece(piece):
    for i in range(8):
      for j in range(8):
        if board[i][j] == piece:
          return (i, j)
    return None

  def is_diagonal_attack(king_pos, opponent_pos):
    king_row, king_col = king_pos
    opponent_row, opponent_col = opponent_pos
    return abs(king_row - opponent_row) == abs(king_col - opponent_col)

  king_pos = find_piece('K')
  if king_pos is None:
    return False  # King not found

  # Check for Bishop or Queen
  for piece in ['B', 'Q']:
    opponent_pos = find_piece(piece)
    if opponent_pos is not None and is_diagonal_attack(king_pos, opponent_pos):
      return True

  # Check for Rook or Queen
  for piece in ['R', 'Q']:
    opponent_pos = find_piece(piece)
    if opponent_pos is not None and (king_pos[0] == opponent_pos[0]
                                     or king_pos[1] == opponent_pos[1]):
      return True

  # Check for Knight
  for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),
                 (2, -1), (2, 1)]:
    if 0 <= king_pos[0] + dr < 8 and 0 <= king_pos[1] + dc < 8 and board[
        king_pos[0] + dr][king_pos[1] + dc] == 'N':
      return True

  # Check for Pawn
  if king_pos[0] > 0:
    if king_pos[1] > 0 and board[king_pos[0] - 1][king_pos[1] - 1] == 'P':
      return True
    if king_pos[1] < 7 and board[king_pos[0] - 1][king_pos[1] + 1] == 'P':
      return True

  return False


# Example usage
board = [['.', '.', '.', 'K', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', 'N', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', 'P', '.'],
         ['.', 'B', '.', '.', '.', '.', 'R', '.'],
         ['.', '.', 'N', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'K', '.', 'Q', '.', '.']]

print(is_king_in_check(board))  # Output: True
