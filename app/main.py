from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connention import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um usuário
    service.criar_usuario("Marta", "marta@gmail.com", "123")

    # Listano todos os usuários
    print("\nListando todos os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

