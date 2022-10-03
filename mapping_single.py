from sqlalchemy import create_engine, inspect, Column, Integer, String, delete, VARCHAR, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://root:sara123@localhost/ORM"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(10), nullable=False)
    permissao = Column(Integer, nullable=False)


class Licitacao(Base):
    __tablename__ = "Licitacao"
    id = Column(Integer, primary_key=True)
    ''' id_empresa = Column(Integer, ForeignKey)
    id_local = Column(Integer, ForeignKey)'''
    titulo = Column(VARCHAR(50), nullable=False)
    descricao = Column(VARCHAR(300), nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data_inicio = Column(DATETIME, nullable=False)
    data_fim = Column(DATETIME, nullable=False)


class LicitacaoSalva(Base):
    __tablename__ = "LicitacaoSalva"
    nome = Column(VARCHAR(15), nullable=False)
    '''' id_licitacao_fk = Column(Integer, ForeignKey)
    id_usuario_fk = Column(Integer, ForeignKey)'''


def main():
    engine = create_engine(url=URL)
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    '''with Session.begin() as session:
        usuario = Usuario(nome="Jhon Snow")
        id_usuario = usuario.id_usuario
        session.add(usuario)

    with Session.begin() as session:
        usuario.nome = "Jhon Snow, The King Forever"
        id_usuario = usuario.id_usuario
        session.add(usuario)


    if __name__ == "__main__":
        main()'''
