tile_data = []
tile_change =[[False,False,False,False,False,False],
            [False,False,False,False,False,False],
            [False,False,False,False,False,False],
            [False,False,False,False,False,False],
            [False,False,False,False,False,False],
            [False,False,False,False,False,False]]
with open('setup.txt','rt') as f:
    for lines in f:
        a=list(lines)
        a.remove("\n")
        tile_data.append(a)

def logicConway(row,column):
    startPointX = 0 if row==0 else row-1
    startPointY = 0 if column==0 else column-1

    endPointX = row+1 if row+1 == 6 else row+2
    endPointY = column+1 if column+1 == 6 else column+2

    Neighbours = 0
    
    for x in range(startPointX,endPointX):
        for y in range(startPointY,endPointY):
            if tile_data[x][y]=='1':
                Neighbours +=1
    
    #main conway logic
    if tile_data[row][column] == '1':
        Neighbours-=1
        if Neighbours > 3:
            tile_change[row][column] = True
        elif Neighbours < 2:
            tile_change[row][column] = True
    elif tile_data[row][column]== '0':
        if Neighbours == 3:
            tile_change[row][column] = True



for a in range(0,6):
    for b in range(0,6):
        logicConway(a,b)


for i in range(0,6):
    for j in range(0,6):
        print(tile_change[i][j],end=" ")
    print("\n")
