## Desafio Técnico Inova

  >>> Separação de contextos;

** Os contextos foram separados em - **

* __init__.py que determinou a regra da atividade das rotas e da validação do método HTTP;

* jsonarray.py para a criação de um banco de dados a partir do json com um C.R.U.D. básico, desisti da ideia;

* schema.py que determinou a regra única, pequena e específica para o banco de dados com só um tarefa de POST.

  >>> Error handing;

* Utilizei Asserts utilizei de BDD e TDD para especificar a forma tentei determinar a maneira de reduzir o escopo e delimitar os erros;

 >>> Manutenabilidade;

* Mantive o que é preconizado pela comunidade no que tange ao Framework Flask para sua arquitetura.

>>> Baixo acoplamento;

* Baseado em Orientação a Objeto.

- Código pythonico;

- README com todas as instruções de como executar o projeto e como usar os endpoints existentes.
+++ Sem definição, 5 testes falharam, como já havia pedido tempo extra, não poderia ultrapasssar o tempo estipulado de hoje

+++ A ideia se baseava em colocar em ordem numérica os id's (que é uma forma de ordenação) e extrair a quantidade exigida

** o desenvolvimento da minha solução foi aquém do que era esperado e exigido no desafio técnico.
Necessito estudar ainda mais. A notícia boa do processo seletivo, é que começo entendi como funciona a framework Flask.

>>> Utilização:
>>> Clone a repo utilizando a sua forma predileta;
>>> Acesse o terminal do computador
>>> Entre na pasta onde você armazenou este projeto
>>> Ative a virtualenv com .api/bin/activate  em sistema unix
>>> Teste de integração com: behave/'pasta_armazenada'/fetures
>>> Teste unitário com unittest: unittest discovery -m test/ -v
>>> Rode a aplicação com: flask run
