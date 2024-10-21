from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando usuário.
    service.criar_usuario("Marta5", "marta5@gmail.com", "123")

    # Listando todos os usuários.
    print("\nListando todos os usuários: ")
    lista_usuarios = service.listar_todos_usuario()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() # Chamada para função.