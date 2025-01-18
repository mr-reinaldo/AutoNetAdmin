import factory
import pytest
from faker import Factory as FakerFactory

from app.models.user_model import User

faker = FakerFactory.create()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyFunction(lambda: faker.password)


@pytest.fixture
def fake_user():
    new_user = UserFactory()

    return new_user


@pytest.fixture
def plain_password():
    return faker.password()
