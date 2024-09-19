# Visualização de Dados de Saúde Psicossocial

## Descrição do Projeto

Este projeto tem como objetivo explorar e visualizar dados referentes à saúde psicossocial. A iniciativa é de caráter acadêmico, sendo parte de um estudo em andamento. Não se trata de um projeto finalizado, portanto, não deve ser utilizado em aplicações reais ou ambientes de produção.

Através de gráficos interativos e dashboards, a aplicação permite a análise de dados relacionados à saúde mental e fatores psicossociais que afetam indivíduos e comunidades. A visualização é feita utilizando bibliotecas populares de Python, como Plotly e Pandas, com a aplicação web sendo gerenciada via Flask.

* Aviso Importante

Este projeto não tem fins comerciais ou clínicos e não deve ser usado para diagnósticos ou outras decisões relacionadas à saúde. As análises e visualizações são puramente acadêmicas, e os dados podem conter erros ou simplificações.

## Requisitos
Para rodar o projeto localmente, é necessário ter instalado:

Python (versão 3.7 ou superior)

Bibliotecas Python:

Plotly (`pip install plotly`)

Flask (`pip install flask`)

Pandas (`pip install pandas`)

## Como Executar a Aplicação

* Clone o repositório:

```
git clone https://github.com/Chris-Mathias/Projeto_Psicossocial.git
cd Projeto_Psicossocial
```

* Instale as dependências

Se você ainda não tiver o Python e as bibliotecas mencionadas acima, instale utilizando os comandos citados.

* Inicie o servidor

```
python interface.py
```

* Acesse o dashboard

Após iniciar o servidor, você poderá acessar o dashboard através do navegador, utilizando o endereço que aparecerá no terminal.

## Estrutura do Projeto
interface.py: Arquivo principal que contém a lógica para a criação da aplicação web e renderização das páginas.
graphs.py: Arquivo que contém a lógica para o tratamento dos dados e criação dos gráficos.
templates/: Pasta contendo os arquivos HTML usados para exibir a interface.
static/: Arquivos estáticos como CSS, imagens e scripts JS.
data/: Diretório onde os arquivos de dados são armazenados para análise e visualização previamente tratados.
