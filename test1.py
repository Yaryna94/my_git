print("Список покупок")
x=0
zakupy_dict = {
"пекрня": ["хліб", "булочки", "пончик"],
"овочевий": ["морква", "селера", "рукола"]
}
for k,v in zakupy_dict.items():

     print (f"Я йду до {k} і купую там {v}".title())
     x+=len(v)

print(f"Разом купую {x} товарів")
print ("Like kommit")
