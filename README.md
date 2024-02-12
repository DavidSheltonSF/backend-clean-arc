# Sobre:

Este é um projeto backend que estou desenvolvendo a partir da playlist de Clean Architecture com Python do canal Programador Lhama.


## Arquitetura

Estou condando esse projeto para aprender **Clean Architecture**.

Aprendi que esse tipo de arquitetura possui alguns benefícios:

- Testabilidade: Eu posso testar partes da aplicação separadamente, como repositories, use cases e controllers. Isso facilita para encontrar erros e garantir que cada uma das partes funciona.

- Flexibilidade e Adaptabilidade: Um sistema feito pela Clean Architecture, não está preso a um banco de dados, uma API, ou um framework específico.


## Testes

A ferramenta que uso para testar os componentes do projeto é o **pytest**

*Testando so repositórios:*
```
pytest src/infra/repo
```
<img src="./readmeImgs/testingRepo.png">

## Outras ferramentas

Também estou utilizando o repositório **black** para formatar os meus códigos e o repositório **flake8** para me apontar algumas. Ambos visam alinhar o código de acordo com a pep8

Para aplicar os duas ferramentas anteriores eu utilizo o **pre-commit**, que realiza algumas tarefinhas antes de cada commit, como verificar se os requisitos do black, flake8 e pytest foram atendidos, e adicionar as dependências no requirements.txt

Além disso também estou utilizando o **pylint** que me passa algumas dicas de acordo com a pep8.
<img src="./readmeImgs/pylintError.png">
