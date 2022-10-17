import unittest

def palindromo(palabra):

    frase = palabra.replace(" ","")
    frase = frase.lower()
    frase2 = frase[: : -1]
    resultado = ""

    if frase == frase2:
        resultado = frase
        return resultado
    else:
        return resultado    

class TestWordPalindromo(unittest.TestCase):
    def test_1(self):
        palindromo_word = palindromo("reconocer")
        self.assertEqual(palindromo_word, 'reconocer')
    def test_2(self):
        palindromo_word = palindromo("oso")
        self.assertEqual(palindromo_word, 'oso')
    def test_3(self):
        palindromo_word = palindromo("anita lava la tina")
        self.assertEqual(palindromo_word, 'anitalavalatina')
    def test_4(self):
        palindromo_word = palindromo("neuquen")
        self.assertEqual(palindromo_word, 'neuquen')       
    def test_5(self):
        palindromo_word = palindromo("luz azul")
        self.assertEqual(palindromo_word, 'luzazul')
    def test_6(self):
        palindromo_word = palindromo("RECONOCER")
        self.assertEqual(palindromo_word, 'reconocer')
    def test_7(self):
        palindromo_word = palindromo("ANITA LAVA LA TINA")
        self.assertEqual(palindromo_word, 'anitalavalatina')
if __name__ == '__main__':
    unittest.main()