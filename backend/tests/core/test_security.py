from datetime import datetime
from zoneinfo import ZoneInfo

from jwt import decode

from app.core.security import (
    create_access_token,
    decrypt_text,
    encrypt_text,
    get_password_hash,
    verify_password,
)
from app.core.settings import settings


def test_create_access_token(fake_user):
    """Teste para validar a função create_access_token do módulo security.

    Assertions:
        - O token gerado deve conter o payload informado.
        - O token gerado deve conter a chave "exp" no payload.

    """

    user = fake_user

    data = {'sub': f'{user.email}'}

    token = create_access_token(data)
    decoded_data = decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )

    assert decoded_data['sub'] == user.email
    assert 'exp' in decoded_data


def test_create_access_token_expiration():
    """Teste para validar a expiração do token gerado pela função create_access_token.

    Assertions:
        - O token gerado deve conter a chave "exp" no payload.
        - O valor da chave "exp" deve ser maior que o timestamp atual.

    """

    data = {'sub': 'test_user'}
    token = create_access_token(data)
    decoded_data = decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )

    assert (
        decoded_data['exp'] > datetime.now(tz=ZoneInfo(settings.TIMEZONE)).timestamp()
    )


def test_get_password_hash(plain_password):
    """Teste para validar a função get_password_hash do módulo security.

    Assertions:
        - O hash gerado deve ser diferente da senha em texto plano.
        - A função verify_password deve retornar True ao comparar a senha em texto plano com o hash gerado.
    """

    hashed_password = get_password_hash(plain_password)

    assert hashed_password != plain_password
    assert verify_password(plain_password, hashed_password)


def test_verify_password(plain_password):
    """Teste para validar a função verify_password do módulo security.

    Assertions:
        - A função verify_password deve retornar True ao comparar a senha em texto plano com o hash gerado.
        - A função verify_password deve retornar False ao comparar uma senha incorreta com o hash gerado.
    """

    hashed_password = get_password_hash(plain_password)

    assert verify_password(plain_password, hashed_password)
    assert not verify_password('wrongpassword', hashed_password)


def test_encrypt_text():
    """Teste para validar a função encrypt_text do módulo security.

    Assertions:
        - O texto criptografado deve ser diferente do texto original.
        - O texto criptografado deve ser uma string.
    """

    plain_text = 'Texto para criptografar'
    encrypted_text = encrypt_text(plain_text)

    assert encrypted_text != plain_text
    assert isinstance(encrypted_text, str)


def test_decrypt_text():
    """Teste para validar a função decrypt_text do módulo security.

    Assertions:
        - O texto descriptografado deve ser igual ao texto original.
        - A função decrypt_text deve retornar uma string.
    """

    plain_text = 'Texto para criptografar'
    encrypted_text = encrypt_text(plain_text)
    decrypted_text = decrypt_text(encrypted_text)

    assert decrypted_text == 'Texto para criptografar'
    assert isinstance(decrypted_text, str)
