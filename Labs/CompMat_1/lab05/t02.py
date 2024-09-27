
counter = 0
# for i in range(10, 100):
#     ody = i % 10
#     des = i // 10
#     if des > ody:
#         counter += 1


for des in range(1, 10):
    for ody in range(0, 10):
        if des < ody:
            counter += 1

print(counter)