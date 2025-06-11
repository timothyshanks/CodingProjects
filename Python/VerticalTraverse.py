def vertical_traverse(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    rows, cols = len(matrix), len(matrix[0])
    # We start at the bottom right for the vertical traversal.
    row, col = rows - 1, cols - 1
    result = []
    # TODO: Append each book's position to the result list by following the vertical pattern.
    for i in range(rows * cols):
        result.append(matrix[row][col])
        if row == 0:
            col -= 1
            row = rows - 1
        else:
            row -= 1
    return result

# Example matrix representing library bookshelves
bookshelves = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Output should be the vertical traverse of the bookshelves
print(vertical_traverse(bookshelves))  # [12, 8, 4, 11, 7, 3, 10, 6, 2, 9, 5, 1]
