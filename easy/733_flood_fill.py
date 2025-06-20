# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the 
# pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a 
# flood fill on the image starting from the pixel image[sr][sc].


#Final Solution
def floodFill(image, sr, sc, color):
    original = image[sr][sc]

    def dfs(r, c):
        length = len(image)
        height = len(image[0])

        if length <= r or r < 0:
            return
        elif height <= c or c < 0:
            return
        elif image[r][c] != original:
            return
        else:
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


    if original == color:
        return image
    
    dfs(sr, sc)

    return image


# Using Recursion
# Keeps track of the original color, and the matrix bounds
# The recursive function takes a step every direction, starting with all the way up, then down, then right, then left
    