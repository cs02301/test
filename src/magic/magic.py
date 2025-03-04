import math

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """
    
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser no negativo")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        return [self.fibonacci(i) for i in range(n)]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        divisores = [i for i in range(1, n) if n % i == 0]
        return sum(divisores) == n
    
    def triangulo_pascal(self, filas):
        triangulo = []
        for i in range(filas):
            fila = [1]
            if triangulo:
                ultima = triangulo[-1]
                fila.extend([ultima[j] + ultima[j+1] for j in range(len(ultima)-1)])
                fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("n debe ser no negativo")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = [int(d) for d in str(abs(n))]
        num_digitos = len(digitos)
        return sum(d ** num_digitos for d in digitos) == n
    
    def es_cuadrado_magico(self, matriz):
        if not matriz:
            return False
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False
        suma_magica = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_magica:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_magica:
            return False
        return True
