#conway logic
tile_data = []
tile_change=list()
for x in range(0,6):
    tile_change.append(list())
    for y in range(0,6):
        tile_change[x].append(False)

with open('setup.txt','rt') as f:
    for lines in f:
        tile_data.append(list(lines))


#find neighbours first
def conwayLogic(row,col):
    startPointX = row - 1 if row != 0 else 0
    startPointY = col - 1 if col != 0 else 0
    Neighbours = 0
    endPointX = row +2 if row+1 != 7-1 else row
    endPointY = col +2 if col+1 != 7-1 else col
    for x in range(startPointX,endPointX):
        for y in range(startPointY,endPointY):
            if tile_data[x][y]=='1':
                Neighbours+=1
    #print("the neighbours for ({},{}) is {}".format(row,col,Neighbours))
    ownState = tile_data[row][col] 
    #print(ownState)
    #main conway logic
    if ownState == '1':
        Neighbours = Neighbours - 1
        if Neighbours > 3:
            tile_change[row][col]=True
        elif Neighbours < 2:
            tile_change[row][col]=True
    elif ownState == '0':
        if Neighbours == 3:
            tile_change[row][col]=True
   






for i in range(0,6):
    for j in range(0,6):
        conwayLogic(i,j)

     
for b in range(0,6):
    for f in range(0,6):
        if tile_change[b][f] == True:
            tile_data[b][f] = '1' if tile_data[b][f] =='0' else '0'
        #print(tile_data[b][f],end=" ")
    print("\n")
