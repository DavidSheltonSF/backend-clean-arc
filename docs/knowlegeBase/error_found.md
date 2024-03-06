## Erro ao comparar seleção total por feita por um repository e seleção total por feita pela engine do SqlAlchemy em
## pet_repository_test.py

**data:** 27/02/2024 00:15

Seleção completa é a seleção de todos os dados registrados em uma tabela no
banco de dados.

### Como o teste é realizado?

O teste é realizado fazendo uma seleção completa pela engine do ORM sqlalchemy
e convertento cada row instance dessa seleção em Pets instance e depois 
realizando uma seleção completa pelo repository da entidade, esta última
ocorre quando o método select do repository é chamado sem passar nenhum parâme-
tro. No final, as seleções são comparadas, verificando se cada uma das
suas instâncias são iguas a sua equivalente. Ou seja, para
verificar a igualdade de duas seleções x e y, eu quero saber se x[0] == y[0]
e daí por diante, para todos os índices de cada seleção.

### Problema

Ao comparar as seleções, as instâncias não eram iguais. Isso ocorreu porque
ao realizar a seleção completa pelo repository, o atributo specie das
instâncias era do tipo AnimalTypes e não str. Já na seleção feita pela engine,
após converter as rows instances para Pets instances, todas as instâncias
dessa seleção tinham o atributo specie do tipo str.

### Solução

Foi necessário alterar o método row_to_pet da entity Pet, para que
ao converter uma row, o atributo specie seja convertido em AnimalTypes.
Dessa forma, o atributo specie é do mesmo tipo para ambas as seleções e,
por isso, é possivel comparar as instâncias e ver que são iguais.