num = int(input())

things = list(map(int, input().split()))

things.sort(reverse=True)
boy = 0
girl = 0
for i in range(len(things)):
    if i % 2 == 0:
        girl += things[i]
    else:
        boy += things[i]

print(girl, boy)
