from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME, DECIMAL, VARCHAR
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

'''from sqlalchemy import create_engine, inspect, Column, Integer, String, delete, VARCHAR, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship'''


class Empresa:
    lista_licitacao = []
    filial = []

    def __init__(self, id, local, nome, cnpj):
        self.id = id
        self.local = local
        self.nome = nome
        self.cnpj = cnpj

    def adicionarLicitacao(self, id, id_empresa, id_local, titulo, descricao,
                           valor, data_inicio, data_fim, palavra_chave):  # >>>>>>>>>>> adiciona uma licitacao
        self.lista_licitacao.append(Licitacao(id, id_empresa, id_local, titulo,
                                              descricao, valor, data_inicio, data_fim, palavra_chave))

    def removerLicitacao(self, id):  # >>>>>> remove a licitacao através do id
        for i in range(len(self.lista_licitacao)):
            if (self.lista_licitacao[i].id == id):
                self.lista_licictacao.remove(id)

    def adicionarFilial(self, id, local, cnpj):  # ----> adiciona uma filial
        self.filial.append(Empresa(id, local, self.nome, cnpj))

    def removerFilial(self, id):
        for i in range(len(self.filial)):
            if (self.filial[i].id == id):
                self.filial.remove(id)

    # -----> editar licitacao >>>>> #incompleto#


''' def editarLicitacao(self, nome, ..):
	    id = none;
	    for i in count(self.lista_licitacao):
		    if (self.lista_licitacao[i].id == licitacaoEditar):
			    id = i
	    if(id):	
		    if(nome != none):
			    self.lista_licitacao[id].nome = nome=
'''


class ControleEmpresa:
    lista_empresas = []

    def adicionarEmpresa(self, id, local, nome, cnpj):
        self.lista_empresas.append(Empresa(id, local, nome, cnpj))

    def removerEmpresa(self, id):
        for i in range(len(self.lista_empresas)):
            if (self.lista_empresas[i].id == id):
                self.lista_empresas.remove(id)

    # ----> metodo editar empresa a fazer


'''    def editarEmpresa(self):'''


class ControleUsuario:
    lista_usuarios = []

    def adicionarUsuario(self, id, nome, email, senha):
        self.lista_usuarios.append(Usuario(id, nome, email, senha))

    def removerUsuario(self, id):
        for i in range(len(self.lista_usuarios)):
            if (self.lista_usuarios[i].id == id):
                self.lista_usuarios.remove(id)


class Usuario:
    licitacao_salva = []
    permissao = None

    def __int__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.permissao = 1
        self.controle_empresa = ControleEmpresa()

    def salvarLicitacao(self, licitacao_a_salvar):
        self.licitacao = licitacao_a_salvar
        self.licitacao_salva.append(self.licitacao)

    def removerLicitacaoSalva(self, id):
        for i in range(len(self.licitacao_salva)):
            if (self.licitacao_salva[i].id == id):
                self.licitacao_salva.remove(id)


'''    #-----> metodo editar dados de usuario >>>> a fazer
   def editarDadosUsuario(self):'
'''


class Admin(Usuario):
    controle_usuario = None

    def __init__(self):
        controle_usuario = ControleUsuario()

    def editarPermissaoUsuario(self, id):
        for i in range(len(self.controle_usuario.lista_usuarios)):
            if (self.controle_usuario.lista_usuarios[i].id == id):
                self.controle_usuario.lista_usuarios[i].permissao = 2


class Licitacao:
    palavra_chave = []  # >>>> para fazer as filtragens

    def __init__(self, id, id_empresa, id_local, titulo, descricao, valor, data_inicio, data_fim, palavra_chave):
        self.id = id
        self.id_empresa = id_empresa
        self.id_local = id_local
        self.titulo = titulo
        self.descricao = descricao
        self.valor = valor
        self.data_inicio = datetime.strptime(data_inicio)
        self.data_fim = datetime.strptime(data_fim)
        self.palavra_chave = palavra_chave


class Local:
    def __init__(self, id, pais, estado, cidade):
        self.id = id
        self.pais = pais
        self.estado = estado
        self.cidade = cidade


#### iniciando codigo sql ---incompleto--- #####

URL = "mysql+mysqlconnector://aluno:aluno123@localhost:3306/ORM"

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

    licitacao_Salva = relationship("LicitacaoSalva", backref="usuario")
    upload = relationship("Upload", backref="usuario")

class Licitacao(Base):
    __tablename__ = "Licitacao"
    id_licitacao = Column(Integer, primary_key=True)
    ''''id_empresa = Column(Integer, ForeignKey)'''
    '''id_local = Column(Integer, ForeignKey)'''
    titulo = Column(VARCHAR(50), nullable=False)
    descricao = Column(VARCHAR(300), nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data_inicio = Column(DATETIME, nullable=False)
    data_fim = Column(DATETIME, nullable=False)

    licitacao_Salva = relationship("LicitacaoSalva", backref="licitacao")
    upload = relationship("Upload", backref="id_licitacao_upload")


class LicitacaoSalva(Base):
    __tablename__ = "LicitacaoSalva"
    id = Column(Integer, primary_key=True)
    nome = Column(VARCHAR(15), nullable=False)

    id_licitacao_fk = Column(Integer, ForeignKey("Licitacao.id_licitacao"))
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"))

class Empresa(Base):
    __tablename__ = "Empresa"
    id = Column(Integer, primary_key=True)
    nome = Column(VARCHAR(50), nullable=False)
    cnpj = Column(Integer, nullable=False)

    id_local = Column(Integer, ForeignKey("Local.id_local"))

    filial = relationship("Filial", backref="empresa")

class Local(Base):
    __tablename__ = "Local"
    id_local = Column(Integer, primary_key=True)
    pais = Column(VARCHAR(30), nullable=False)
    estado = Column(VARCHAR(30), nullable=False)
    cidade = Column(VARCHAR(30), nullable=False)

    id_empresa = relationship("Empresa", backref="local")
    id_filial = relationship("Filial", backref="local")

class Filial(Base):
    __tablename__ = "Filial"
    id_filial = Column(Integer, primary_key=True)
    cnpj = Column(Integer, nullable=False)

    id_empresa_fk = Column(Integer, ForeignKey("Empresa.id_empresa"))
    id_local_fk = Column(Integer, ForeignKey("Local.id_local"))

class Upload(Base):
    __tablename__ = "Upload"
    id_upload = Column(Integer, primary_key=True)
    data_upload = Column(DATETIME, nullable=False)

    id_usuario_upload = Column(Integer, ForeignKey("Usuario.id_usuario"))
    id_licitacao_upload = Column(Integer, ForeignKey("Licitacao.id_licitacao"))

class PalavraChave(Base):
    __tablename__ = "PalavraChave"
    id_PChave = Column(Integer, primary_key=True)
    palavra = Column(VARCHAR(50), nullable=False)

def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    if __name__ == "__main__":
        main()
