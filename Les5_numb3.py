from statistics import mean

with open('salary.txt', 'r') as file:
    emp_sal = []
    for line in file:
        if line.strip():
            data = line.split()
            emp_sal.append(float(data[1]))
            if float(data[1]) < 20:
                print(data[0])
    print(f"Average salary is {round(mean(emp_sal))}k rubles")
