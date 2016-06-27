# book_sorter_with_unittest

Dependencies:<br />
<br />
Python3.4+ - sudo apt-get install python3 <br />
<br />
<br />
Introdução:<br />
O sorter é completamente implementado com bibliotecas nativas do python3.<br />
A configuração é totalmente feita por arquivos.<br />
A execução é feita via linha de comando.<br />
O resultado é retornado via arquivo.<br />
Os testes unitários do Sorter e do carregamento de configurações estão inclusos na entrega.<br />
<br />
Para este projeto ainda, foi cogitada a ideia de implementar client/server separados:<br />
O serviço rodaria via TCP, comunicando via protocolo jsonRPC.<br />
Mas dados os requisitos solicitados e meu tempo dinsponível, essas ideias foram descartadas.<br />
<br />
Ainda assim, creio estar entregando um trabalho satisfatório.<br />
<br />
Considerações:<br />
Sobre os testes unitários:<br />
Nunca havia trabalhado com isso, inclusive é a primeira vez que uso a biblioteca de testes do python.<br />
Não tenho certeza se foram implementados da melhor forma possível.<br />
Os testes foram feitos para apenas acusar o primeiro erro de cada TestCase, os demais são ignorados constando como se apresentassem sucesso.<br />
No entanto, corrigindo o erro apresentado e havendo erros posteriores na linha de execução do código, será acusado na próxima execução dos testes.<br />
<br />
Arquivos de configuração:<br />
São necessários dois arquivos de configuração para o serviço rodar, ambos em formato INI. Seus nomes e diretórios podem ser configurados.<br />
O primeiro arquivo tem por default o nome config.ini. Opcionalmente um outro nome/path pode ser passado via argumento na execução do serviço.<br />
Seguindo o formato INI, este arquivo possui duas seções obrigatórias:<br />
SorterConfig e Rules (case sensitive)<br />
-<br />
Na seção SorterConfig, duas chaves são obrigatórias:<br />
BooksINI e SaveINI (case sensitive)<br />
BooksINI -> o valor deve ser o nome/path do arquivo INI contendo os livros a serem ordenados pelo serviço.<br />
SaveINI -> o valor deve ser o nome/path do arquivo INI a ser salvo com os livros ordenados.<br />
-<br />
Na seção Rules, as chaves são opcionais:<br />
Podem ser três:<br />
title, author, edition_year (case sensitive)
Seus valores podem ser 2:<br />
ascending ou descending (case sensitive)<br />
A ordem de prioridade no ordenamento é: A chave acima no arquivo terá maior prioridade que a chave abaixo.<br />
-<br />
<br />
Exemplo de config.ini:<br />
[SorterConfig]<br />
BooksINI = meuslivros<br />
SaveINI = meuslivrosordenados<br />
[Rules]<br />
edition_year = ascending<br />
title = descending<br />
<br />
<br />
<br />
O arquivo de livros a serem ordenados possuem o seguinte formato:<br />
[um titulo qualquer]<br />
author = meu autor predileto<br />
edition_year = 1800<br />
-<br />
Neste caso podem existir N livros cadastrados, ou nenhum. Mas para cada seção existente (livro cadastrado), as duas chaves são obrigatórias, embora sua ordem seja irrelevante.
<br />
<br />
O arquivo gerado pelo serviço tem o mesmo formato descrito acima.<br />
<br />
Observação: Todos os valores de chaves devem ser não nulos.<br />
<br />
<br />
Execução:<br />
Todos os paths configurados devem apontar para diretórios válidos com permissão de leitura. O path do arquivo gerado deve ter permissão de escrita.<br />
python3 -B sort_app.py (Usando por default o arquivo padrão config.ini)<br />
python3 -B sort_app.py minha_configuracao.ini<br />
<br />
<br />
Dúvidas e sugestões:<br />
davi.abreu.w@gmail.com<br />
<br />