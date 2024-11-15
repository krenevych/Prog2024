wallet = {
    7: 3,  # 3 купюри по 7 гривень
    15: 5,  # 5 купюри по 15 гривень
    20: 3
}

max_nominal = 167

cash = 0
for nominal in range(1, max_nominal + 1):
    try:
        cash = cash + nominal * wallet[nominal]
    except KeyError:
        pass

# wallet[56]

print(cash)