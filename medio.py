import unittest

def medio(x, y, z):

    if(x == "Hola" or y == "Hola" or z == "Hola"):
        return None

    lista = [x, y, z]
    ordenado = sorted(lista)
    return ordenado[1]

class TestMedio(unittest.TestCase):

    def test164(self):
        self.assertEqual(medio(1, 6, 4), 4)

    def test9106(self):
        self.assertEqual(medio(9, 10, 6), 9)

    def testestarmedio(self):
        resultado = medio(4, 8, 2) #2  4  8
        self.assertTrue(resultado >= 4 or resultado >= 8 or resultado >= 2)

    def testlista(self):
        resultado = medio(10, 100, 70) 
        lista_test = [10, 100, 70]
        self.assertIn(resultado, lista_test)
        # elemento
        # lista
        # true / false = el elemento está en la lista?

    def testnone(self):
        resultado = medio(3, "Hola", 6)
        self.assertIsNone(resultado)
        #es "resultado" igual a None?

    def test000(self):
        self.assertEqual(medio(0, 0, 0), 0)

    def testfalse(self):
        resultado = medio(9, 10, 6)
        self.assertFalse(resultado > 9 and resultado > 10 and resultado > 6)

    #assertIn solo para listas, probando que string sea una lista :)
    def teststring(self):
        lista_test = "Hola"
        self.assertIn('H', lista_test)
      
if __name__ == '__main__':
    unittest.main()