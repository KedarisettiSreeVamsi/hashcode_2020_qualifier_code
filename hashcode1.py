file = open('a_example.txt','r')
n,l,d = list(map(int,file.readline().split()))
scores = list(map(int,file.readline().split()))
lib = []
for i in range(l):
    lib.append((i,list(map(int,file.readline().split())),list(map(int,file.readline().split()))))
lib.sort(key=lambda x:x[1][1])
days = 0
score = 0
num_libs = 0
visited = [0 for i in range(len(scores)+1)]
printer = []
for i in range(l):
    books_viewed =[x1 for x1 in range(len(visited)) if visited[x1] == 0 and x1 in lib[i][2]]
    book_visited = [0 for i in range(len(scores)+1)]
    printer1 = []
    days += lib[i][1][1]-1
    k  = 0
    count = 0
    index = 0
    for j in range(days+1,d):
        num_books = lib[i][1][2]
        x = books_viewed[k:k+num_books]
        if x == []:
            pass
        else:
            for b in x:
                visited[b] = 1
                book_visited[b] = 1
                count += 1
        k += num_books
    if count>0:
        printer1.append([lib[i][0],count])
        printer1.append([index for index in range(len(book_visited)) if book_visited[index] == 1])
        printer.append(printer1)
        days += 1
        num_libs += 1
print(num_libs)
for i in range(len(printer)):
    for j in printer[i][0]:
        print(j,end=' ')
    print()
    for j in printer[i][1]:
        print(j,end = ' ')
    print()
    
    

        
        
        
        
    
