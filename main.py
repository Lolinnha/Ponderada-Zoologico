class Animal:
    def __init__(self, nome, especie, nivel_felicidade=50):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade
        self.saciado = False

    def alimentar(self):
        if self.saciado == False:
            self.saciado = True
            self.nivel_felicidade += 1
        else:
            self.nivel_felicidade -= 1

    def feliz(self):
        return self.nivel_felicidade > 70
    
    def passar_tempo(self):
        if self.saciado == False:
            self.nivel_felicidade -= 10
        self.saciado = False

class Recinto:
    def __init__(self, animais, especie, bem_cuidado=True):
        self.animais = animais
        self.especie = especie
        self.bem_cuidado = bem_cuidado

    def limpar(self):
        self.bem_cuidado = True

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
        else: 
            raise Exception(f"Animal precisa ser da espécie {self.especie} para este recinto")
    
    def remover_animal(self, animal):
        self.animais.remove(animal)
    
    def alimentar_animais(self):
        for animal in self.animais:
            animal.alimentar()

    def receber_visitas(self):
        if self.bem_cuidado:
            return sum(map(lambda a: 2 if a.feliz() else 1, self.animais)) * 10
                
        else:
            return sum(map(lambda a: 2 if a.feliz() else 1, self.animais)) * 5 
        
    def passar_tempo(self):
        self.bem_cuidado = False
        for animal in self.animais:
            animal.passar_tempo()
    
class Zoo:
    def __init__(self):
        self.recintos = []
        self.dinheiro = 500
    
    def criar_recinto(self, animais, especie):
        recinto = Recinto(animais, especie)
        self.recintos.append(recinto)
    
    def alimentar_animais(self, recinto_index):
        self.recintos[recinto_index].alimentar_animais()
    
    def receber_visitas(self):
        total_visitantes = 0
        for recinto in self.recintos:
            total_visitantes += recinto.receber_visitas()
        self.dinheiro += total_visitantes * 3 
    
    def passar_tempo(self):
        for recinto in self.recintos:
            recinto.passar_tempo()



