from mipaquete.math import sumar, restar, multiplicar


def test_sumar():
    
    assert sumar(1, 0) == 1
    assert sumar(0, 1) == 1
    assert sumar(60000, 1) == 60001
    assert sumar(4_000_000_000_000_000, 1) == 4_000_000_000_000_001
    assert sumar(4_000_000_000_000_000, 1.) == 4_000_000_000_000_001
    assert sumar(4_000_000, 4_000_000) == 8_000_000
    assert sumar(1, 0) == 1

def test_sumar_typecheck_int():
    assert type(sumar(1,1)) == int

def test_sumar_typecheck_float():
    assert  type(sumar(1,1.)) == float
    assert  type(sumar(1.,1)) == float
    assert  type(sumar(1.,1.)) == float


def test_restar():
    
    assert restar(1, 0) == 1
    assert restar(0, 1) == -1
    assert restar(60_000, 1) == 59_999
    assert restar(4_000_000_000_000_000, 1) == 3_999_999_999_999_999
    assert restar(4_000_000_000_000_000, 1.) == 3_999_999_999_999_999
    assert restar(4_000_000_000_000_000, 4_000_000_000_000_000) == 0
    assert restar(1, 0) == 1

def test_restar_typecheck_int():
    assert type(restar(1,1)) == int

def test_restar_typecheck_float():
    assert  type(restar(1,1.)) == float
    assert  type(restar(1.,1)) == float
    assert  type(restar(1.,1.)) == float



def test_multiplicar():
    
    assert multiplicar(1, 0) == 0
    assert multiplicar(0, 1) == 0
    assert multiplicar(60_000, 1) == 60_000
    assert multiplicar(4_000, 1_000) == 4_000_000
    assert multiplicar(4_000_000_000_000_000, 1.) == 4_000_000_000_000_000

def test_multiplicar_typecheck_int():
    assert type(multiplicar(1,1)) == int

def test_multiplicar_typecheck_float():
    assert  type(multiplicar(1,1.)) == float
    assert  type(multiplicar(1.,1)) == float
    assert  type(multiplicar(1.,1.)) == float
