A : int = 25
B : float = 18.9
Año : int = 2022

while B <= A:
    CrecimientoAnualA = (A * 0.02)
    CrecimientoAnualB = (B * 0.03)
    A += CrecimientoAnualA
    B += CrecimientoAnualB
    Año += 1

print(f"Para el año {Año} la población B superará a la pobción A")