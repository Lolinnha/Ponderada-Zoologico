from main import Animal, Recinto, Zoo

#Testes Unitários

def test_alimentar_aumenta_felicidade_quando_fome():
    animal = Animal("Leão", "Felino")
    animal.alimentar()
    assert animal.nivel_felicidade == 51

def test_alimentar_diminui_felicidade_quando_saciado():
    animal = Animal("Leão", "Felino")
    animal.saciado = True
    animal.alimentar()
    assert animal.nivel_felicidade == 49

def test_receber_visitas_todos_felizes():
    animal1 = Animal("Leão", "Felino", 80)
    animal2 = Animal("Tigre", "Felino", 75)
    recinto = Recinto([animal1, animal2], "Felino")
    assert recinto.receber_visitas() == 40  

def test_receber_visitas_alguns_felizes():
    animal1 = Animal("Leão", "Felino", 80)
    animal2 = Animal("Tigre", "Felino", 60)
    recinto = Recinto([animal1, animal2], "Felino")
    assert recinto.receber_visitas() == 30  

def test_passar_tempo_afeta_felicidade_animais():
    animal1 = Animal("Leão", "Felino", 80)
    animal2 = Animal("Tigre", "Felino", 70)
    recinto = Recinto([animal1, animal2], "Felino")
    zoo = Zoo()
    zoo.recintos.append(recinto)
    zoo.passar_tempo()
    assert animal1.nivel_felicidade == 70
    assert animal2.nivel_felicidade == 60

#Testes de Sistema

def test_criar_recinto():
    zoo = Zoo()
    animal1 = Animal("Leão", "Felino")
    animal2 = Animal("Tigre", "Felino")
    zoo.criar_recinto([animal1, animal2], "Felino")
    assert len(zoo.recintos) == 1

def test_alimentar_animais():
    zoo = Zoo()
    animal1 = Animal("Leão", "Felino")
    animal2 = Animal("Tigre", "Felino")
    recinto = Recinto([animal1, animal2], "Felino")
    zoo.recintos.append(recinto)
    zoo.alimentar_animais(0)
    assert animal1.nivel_felicidade == 51
    assert animal2.nivel_felicidade == 51


def test_passar_tempo():
    zoo = Zoo()
    animal1 = Animal("Leão", "Felino", 80)
    animal2 = Animal("Tigre", "Felino", 70)
    recinto1 = Recinto([animal1], "Felino")
    recinto2 = Recinto([animal2], "Felino")
    zoo.recintos.extend([recinto1, recinto2])
    zoo.passar_tempo()
    assert animal1.nivel_felicidade == 70
    assert animal2.nivel_felicidade == 60
