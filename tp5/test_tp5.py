import pytest 
from funciones_tp5 import *

#ejercicio_1

@pytest.mark.parametrize("input_dni, res",
    [("1234567",True),("123456",False),("12345678",True),])

def test_dni(input_dni, res):
    assert dni(input_dni) == res

#ejercicio_2
@pytest.mark.parametrize("phrase, res",
    [("Buenas tardes", 6),("hola como estas", 5),("chau loco", 4),])
def test_last_word_len(phrase, res):
    assert last_word_len(phrase) == res

#ejercicio_3
@pytest.mark.parametrize("name, dni, res",
    [("Jorge agustin Garcia", "44662355", "Jorge6446"),("Santiago Bazan", "34223456", "Santiago5342"),("Agustin Lottero","44662090", "Agustin7446")])

def test_identifier(name, dni, res):
    assert identifier(name, dni) == res

#ejercicio_4

@pytest.mark.parametrize("a, b, res",
    [(10, 5, True), (20, 2, True), (40, 4, True)])

def test_multiplos(a,b,res):
    assert multiplos(a,b) == res

#ejercicio_5

@pytest.mark.parametrize("min, max, avg, res",
    [(12,30,21,21),(21,31,26,26),(2,16,9,9)])

def test_temperature(min,max,avg, res):
    assert temperature(min,max,avg) == res

#ejercicio_6

@pytest.mark.parametrize("phrase, res",
    [("buenas", "b u e n a s"),("hola", "h o l a"),("adios", "a d i o s")])

def test_split(phrase,res):
    assert split(phrase) == res

#ejercicio_7

@pytest.mark.parametrize("number_list, res",
    [([1,2,4,5,3],(5,1)),([40,45,3,26,200],(200,3))])

def test_max_min(number_list, res):
    assert max_min(number_list) == res

#ejercicio_8

@pytest.mark.parametrize("radius, res",
    [ (2, (12.56, 12.56)) ])
def test_circle(radius, res):
    assert circle(radius) == res

#ejercicio_9

@pytest.mark.parametrize("u,p,res",
    [("usuario1", "asdasd", True), ("hola", "quetal", False)])

def test_login(u,p,res):
    assert login(u,p) == res

#ejercicio_10

@pytest.mark.parametrize("prize, in_discount, res",
    [(500,50,250), (4500,48,2340)])

def test_discount(prize, in_discount, res):
    assert discount(prize,in_discount) == res

#ejercicio_11

@pytest.mark.parametrize("num_listt, res",
    [([1,2,3,4,5],[2,3,4,5,6]),([30,12,34,65,62],[31,13,35,66,63])])

def test_list_new(num_listt,res):
    assert list_new(num_listt) == res

#ejercicio_12

@pytest.mark.parametrize("phrase,res",
    [("hola que tal", {"hola":4, "que":3, "tal":3}),("buenos dias", {"buenos":6, "dias":4})])

def test_lenght_dictionarie(phrase,res):
    assert lenght_dictionarie(phrase) == res

#ejercicio_13

@pytest.mark.parametrize("vector, res",
    [({1,2,3,4,5},5),({"buenas","tardes"},2)])

def test_vector_length(vector,res):
    assert vector_length(vector) == res

#ejercicio_14

@pytest.mark.parametrize("num, res",
[(11,True),(12,False),(7,True)])

def test_prime_number(num,res):
    assert prime_number(num) == res

#ejercicio_15

@pytest.mark.parametrize("num, res",
[(3,6),(4,24),(2,2)])

def test_factorial(num,res):
    assert factorial(num) == res

#ejercicio_16

@pytest.mark.parametrize("num,num_to_find,c,res",
[(3312,3,2,2),(456784434,4,4,4),(321411231,1,4,4)])

def test_appareances(num,num_to_find,c,res):
    assert appareances(num,num_to_find,c) == res

