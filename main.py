from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base , sessionmaker, relationship

Base = declarative_base()

#Criando a banco "Motorista"
class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    matricula_funcionario = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False) 

    #Relacionamento
    viagem = relationship("Viagem", back_populates="motorista")

    #Função de imprimir
    def __repr__(self):
        return f"Motorista ID = {self.id} - Nome =  {self.nome} - Matricula do motorista {self.matricula_funcionario} - status = {self.status}"

class Viagem(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destino_principal = Column(String(100), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)

    #ForeingKey
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))

    #Relacionamento
    motorista = relationship("Motorista", back_populates="viagem")

    def _repr__(self):
        return f"viagens ID = {self.id} - Destino = {self.destino_principal} - Ida = {self.data_inicio} - Volta = {self.data_fim}"
    

engine = create_engine("sqlite:///transporte.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) 

def cadastrar_motorista():
    nome_motorista = input("Digite o nome do Motorista: ").strip().capitalize()
    matricula = input("Digite sua matricula: ").capitalize()
    status = input("Digite seu status( Ativo, Inativo, Férias, Suspenso.): ").capitalize()

    with Session() as session:
        try:
            motorista = Motorista(nome = nome_motorista)
            
            session.add(motorista)
            session.commit()
            print("Motorista cadastrado com sucesso!")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

cadastrar_motorista()












def cadastrar_viagens():
    destino = input("Digite o nome da viagem: ").capitalize()
    destino_inicio = input("Digite a data do inicio da viagem: ")
    destino_fim = input("Digite a data de volta: ")
    with Session() as session:
        try:
            viagem = Viagem(destino_principal = destino,data_inicio = destino_inicio, data_fim = destino_fim)
            session.add(viagem)
            session.commit()
            print("Funcionario cadastrado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

