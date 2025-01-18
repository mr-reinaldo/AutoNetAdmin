from base64 import b64decode, b64encode
from datetime import datetime, timedelta
from hashlib import sha256
from zoneinfo import ZoneInfo

from Crypto.Cipher import AES
from jwt import encode
from pwdlib import PasswordHash

from app.core.settings import settings

pwd_context = PasswordHash.recommended()


def create_access_token(data: dict) -> str:
    """Função para criar um token de acesso JWT.

    Args:
        data (dict): Dados a serem codificados no token.

    Returns:
        str: Token de acesso JWT.
    """

    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo(settings.TIMEZONE)) + timedelta(
        minutes=settings.JWT_EXPIRATION_TIME_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt


def get_password_hash(plain_password: str) -> str:
    """Função para gerar o hash de uma senha.

    Args:
        plain_password (str): Senha em texto plano.

    Returns:
        str: Hash da senha.
    """

    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Função para verificar se uma senha em texto plano corresponde a um hash.

    Args:
        plain_password (str): Senha em texto plano.
        hashed_password (str): Hash da senha.

    Returns:
        bool: True se a senha corresponder ao hash, False caso contrário.
    """

    return pwd_context.verify(plain_password, hashed_password)


def __get_aes_key() -> bytes:
    """Função para obter a chave AES.

    Returns:
        bytes: Chave AES.
    """

    return sha256(settings.SECRET_KEY.encode('utf-8')).digest()


def encrypt_text(text: str) -> str:
    """Função para criptografar um texto.

    Args:
        text (str): Texto a ser criptografado.

    Returns:
        str: Texto criptografado.
    """

    key: bytes = __get_aes_key()
    cipher = AES.new(key, AES.MODE_CFB)
    iv = cipher.IV
    encrypted_text = cipher.encrypt(text.encode('utf-8'))

    return b64encode(iv + encrypted_text).decode('utf-8')


def decrypt_text(encrypted_text: str) -> str:
    """Função para descriptografar um texto.

    Args:
        encrypted_text (str): Texto criptografado.

    Returns:
        str: Texto descriptografado.
    """

    key: bytes = __get_aes_key()
    encrypted_data = b64decode(encrypted_text)
    iv = encrypted_data[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted = cipher.decrypt(encrypted_data[AES.block_size :])

    return decrypted.decode('utf-8')
