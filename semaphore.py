from random import uniform
from time import sleep
from threading import Thread, Lock

vector = [0, 0, 0, 0, 0]  # 0 = Não comeu, 1 = Já comeu



class Semaphore(Thread):
    exec = True  # variável para realizar a execução

    def __init__(self, nome, car_esquerda, car_direita):  # Construtor da classe Filosofo
        Thread.__init__(self)
        self.nome = nome
        self.car_esquerda = car_esquerda
        self.car_direita = car_direita

    def run(self):
        """ Sobrescrita de Thread, a função run definirá o que irá acontecer após chamar o método start() na
        instância criada. """
        while self.exec:
            print(f"\n {self.nome} está parado")
            sleep(uniform(5, 15))
            self.speed()

    def speed(self):
        """
        Pega o car 1 e tenta pegar o car 2. Se o car 2 estiver livre,
         ele speeda e solta os dois cars em seguida,senão ele desiste de
        correr e continua parado.
        """
        car1, car2 = self.car_esquerda, self.car_direita

        while self.exec:  # enquanto tiver executando
            car1.acquire(True)  # tenta pegar o primeiro carro
            # verifica se o segundo carro está livre
            locked = car2.acquire(False)
            if locked:
                break
            car1.release()  # libera o carro
        else:
            return  

        print(f"\n {self.nome} começou a andar")
        sleep(uniform(5, 10))
        print(f"\n {self.nome} começou a freiar")
        # contabiliza 
        vector[nomes.index(self.nome)] += 1
        print(vector)
        car1.release()  # libera o car1
        car2.release()  # libera o car2


nomes = ['Golf', 'Skyline', 'Toyota', 'Corolla', 'Astra']  # Nomes dos carros
carss = [Lock() for _ in range(5)]
mesa = [Semaphore(nomes[i], carss[i % 5], carss[(i + 1) % 5])
        for i in range(5)]
for _ in range(50):
    Semaphore.exec = True  # Inicia a execução
    for veiculo in mesa:
        try:
            veiculo.start()  # inicia o objeto de thread criado.
            sleep(2)
        except RuntimeError:  # Se a thread já tiver sido iniciada
            pass
    sleep(uniform(5, 15))
    Semaphore.exec = False  # Para a execução
