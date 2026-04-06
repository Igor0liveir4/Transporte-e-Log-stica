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
    motorista = relationship("Motorista", back_populates="viagens")

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
    motorista = relationship("Motorista", back_populates="viagens")

    def _repr__(self):
        return f"viagens ID = {self.id} - Destino = {self.destino_principal} - Ida = {self.data_inicio} - Volta = {self.data_fim}"
    

engine = create_engine("sqlite:///transporte.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) 
