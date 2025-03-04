import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    """
    
    def es_palindromo(self, texto):
        clean = "".join(texto.split()).lower()
        return clean == clean[::-1]

    def invertir_cadena(self, texto):
        result = ""
        for i in range(len(texto) - 1, -1, -1):
            result += texto[i]
        return result

    def contar_vocales(self, texto):
        count = 0
        vowels = "aeiouAEIOU"
        for char in texto:
            if char in vowels:
                count += 1
        return count

    def contar_consonantes(self, texto):
        count = 0
        for char in texto:
            if char.isalpha() and char.lower() not in "aeiou":
                count += 1
        return count

    def es_anagrama(self, texto1, texto2):
        t1 = sorted(texto1.replace(" ", "").lower())
        t2 = sorted(texto2.replace(" ", "").lower())
        return t1 == t2

    def contar_palabras(self, texto):
        words = texto.split()
        return len(words)

    def palabras_mayus(self, texto):
        def cap(match):
            return match.group(0).capitalize()
        return re.sub(r'\b\w+', cap, texto)

    def eliminar_espacios_duplicados(self, texto):
        return re.sub(r' {2,}', ' ', texto)

    # Se cambia el nombre a es_numero_ent para coincidir con el test
    def es_numero_ent(self, texto):
        try:
            int(texto)
            return True
        except ValueError:
            return False

    def cifrar_cesar(self, texto, desplazamiento):
        result = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                result += char
        return result

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        positions = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            if texto[i:i+m] == subcadena:
                positions.append(i)
        return positions
