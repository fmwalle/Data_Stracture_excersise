def flood_fill(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    # If the new color is the same as the original color, return the image
    if original_color == new_color:
        return image

    # Helper function for DFS
    def dfs(r, c):
        # If we are out of bounds or the current pixel is not the original color, return
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        
        # Change the color
        image[r][c] = new_color
        
        # Recursively call dfs on all 4 adjacent pixels
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right

    # Start DFS from the starting pixel
    dfs(sr, sc)
    
    return image
