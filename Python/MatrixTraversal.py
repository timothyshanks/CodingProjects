def column_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, cols - 1
    direction = -1  # Start going upwards
    output = []

    for i in range(rows * cols):
        output.append(matrix[row][col])
        if direction == -1:
            if row == 0:
                col -= 1
                direction *= -1
            else:
                row -= 1
        else:
            if row + 1 == rows:
                col -= 1
                direction *= -1
            else:
                row += 1

    return output

# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(column_traverse(bookshelf))
