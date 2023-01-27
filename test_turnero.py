import unittest
import turnero_funcional

class prueba_turnero_1(unittest.TestCase):
    
    def test_prueba_prioridad(self):

    
        turnos = [turno for _, turno in zip(range(10), turnero_funcional.funciones.p)]
    
        
        
        self.assertEqual(turnos, ['P - 1', 'P - 2', 'P - 3', 'P - 4', 'P - 5', 'P - 6', 'P - 7', 'P - 8', 'P - 9', 'P - 10'])


    
    
    def test_prueba_caja(self):

    
        turnos = [turno for _, turno in zip(range(10), turnero_funcional.funciones.c)]
    
        
        
        self.assertEqual(turnos, ['C - 1', 'C - 2', 'C - 3', 'C - 4', 'C - 5', 'C - 6', 'C - 7', 'C - 8', 'C - 9', 'C - 10'])
    

    
    
    def test_prueba_moneda_extranjera(self):

    
        turnos = [turno for _, turno in zip(range(10), turnero_funcional.funciones.m)]
    
        
        
        self.assertEqual(turnos, ['M - 1', 'M - 2', 'M - 3', 'M - 4', 'M - 5', 'M - 6', 'M - 7', 'M - 8', 'M - 9', 'M - 10'])


   
if __name__ == '__main__':
    unittest.main()




