# AutoNetAdmin

## Descrição do Projeto

O **AutoNetAdmin** é uma aplicação web destinada ao gerenciamento e automação de dispositivos de rede. Este projeto é uma evolução do [NPLMW (NAPALM Web)](https://github.com/mr-reinaldo/NPLMW), originalmente desenvolvido como Trabalho de Conclusão de Curso no Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB) - Campus João Pessoa. Nesta nova versão, pretendemos criar novas funcionalidades que o projeto original não tinha sido implementadas incorporando diversas bibliotecas de automação de rede, proporcionando maior flexibilidade.

## Funcionalidades

- Interface web intuitiva para gerenciamento de dispositivos de rede.
- Automação de tarefas de rede utilizando múltiplas bibliotecas especializadas.
- Suporte a uma ampla gama de dispositivos e sistemas operacionais de rede.

## Tecnologias Utilizadas

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: [Vuetify](https://vuetifyjs.com/) com [Vue.js](https://vuejs.org/)
- **Automação de Rede**:
  - [NAPALM](https://napalm.readthedocs.io/): Biblioteca Python que implementa um conjunto de funções para interagir com diferentes sistemas operacionais de dispositivos de rede usando uma API unificada.
  - [Netmiko](https://github.com/ktbyers/netmiko): Biblioteca Python que simplifica conexões SSH com dispositivos de rede, facilitando a automação de tarefas através da linha de comando.
  - [Paramiko](https://www.paramiko.org/): Implementação em Python do protocolo SSHv2, permitindo a execução de comandos remotos e transferência de arquivos de forma segura.
  - [AsyncSSH](https://asyncssh.readthedocs.io/): Biblioteca Python que fornece suporte para conexões SSH e SFTP assíncronas, permitindo operações de rede de alta performance.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
