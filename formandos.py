import pandas as pd

data = [["Nome","Nota"],["Maria dos Anjos", 10],["João Paiva", 9],["Pedro Silva", 8],["Ana Oliveira", 7],["Paula Azevedo", 6]]
df = pd.DataFrame(data[1:], columns=data[0])

with pd.ExcelWriter("formandos.xlsx") as writer:
    df.to_excel(writer, sheet_name="Formandos", index=False)

print (pd.read_excel("formandos.xlsx"))