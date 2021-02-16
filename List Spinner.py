def counterClockwise(List_awal):
    list_baru=[]
    for i in range(len(List_awal)-1,-1,-1):
        sementara=[]
        for j in range(len(List_awal)):
            sementara.append(List_awal[j][i])
        list_baru.append(sementara)
    return list_baru

List_awal=[[1, 2, 3, 4],      
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

print(counterClockwise(List_awal))

