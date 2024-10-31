def make_juice(fruit):
    return f"{fruit} + 🧃"
    print("lalalalalala")

def add_ice(juice):
    return f"{juice} + 🧊"
    print("lolololo")

def add_sugar(iced_juice):
    return f"{iced_juice} + 🍬"


juice = make_juice("🍎")
print(f"juice {juice}")
cold_juice=add_ice(juice) 
print(f"cold_juice {cold_juice}")
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)



""" 
my_name = "nico"
my_age = 12
my_color_eyes = "brown"

print(f"Hello I am {my_name}, I have {my_age} years in the earth,{my_color_eyes} is my eye color")

Return sends a vaule outside of function, Python will catch the value and it replace it in your code.
Return kills the function , any code after return is NOT going to be used

"""