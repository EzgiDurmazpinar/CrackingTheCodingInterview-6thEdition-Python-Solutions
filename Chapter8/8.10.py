#8.10
#Implement the 'paint fill' function that one might see on many image editing programs.
#That is, given a screen (represented by a two-dimensional array of colors),
#a point, and a new color, fill in the surrounding area until the color changes from the original color.
def paint(screen,r,c,newcolor):
    if screen[r][c] == newcolor:
        return False
    else:
        paint_fill(screen,r,c,screen[r][c],newcolor)
def paint_fill(screen, r, c,oldcolor,newcolor):
    if r<0 or r >= len(screen) or c<0 or c>= len(screen[0]):
        return False
    if (screen[r][c] == oldcolor):
        screen[r][c] = newcolor
        paint_fill(screen, r-1, c, oldcolor, newcolor) #up
        paint_fill(screen, r+1, c, oldcolor, newcolor) #down
        paint_fill(screen, r, c-1, oldcolor, newcolor) #left
        paint_fill(screen, r, c+1, oldcolor, newcolor) #right

    return True
def main():
    image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]

    image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]


    #print(paint(image1, 3, 1, 30) == image2)
if __name__ == '__main__':
    main()
