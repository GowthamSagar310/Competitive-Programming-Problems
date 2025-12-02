for _ in range(int(input())):
    n = int(input())
    game = []
    for _ in range(n):
        game.append(input().find("#")+1)
    print(*reversed(game))
    
