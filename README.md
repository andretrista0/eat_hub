# Projeto EAT HUB

#### PROBLEMA DE NEGÓCIO 

A empresa Eat Hub é uma marketplace de restaurantes, cujo objetivo é facilitar o encontro e as negociações entre clientes e estabelecimentos gastronômicos. O CEO recém-contratado, busca compreender melhor o negócio para tomar decisões estratégicas e impulsionar o crescimento da empresa.

O principal desafio é realizar uma análise nos dados da empresa e criar dashboards interativos que possam responder às perguntas-chave formuladas pelo CEO utilizando informações reais.

O foco dessa análise é fornecer insights relevantes sobre os restaurantes cadastrados, países, cidades e tipos de culinária presentes na plataforma. Com base nessas informações, o objetivo é criar um painel de visualização de dados que permita ao CEO acessar as principais informações de forma ágil e eficiente, identificando oportunidades de crescimento, pontos fortes e áreas de melhoria.


#### PREMISSAS ASSUMIDAS PARA A ANÁLISE 

Ao conduzir a análise dos dados da Eat Hub e criar os dashboards solicitados pelo CEO, foram consideradas algumas premissas importantes para garantir a qualidade e a relevância dos resultados. As principais premissas assumidas para essa análise são as seguintes:

Qualidade dos Dados: Partimos do pressuposto de que os dados disponíveis na plataforma da Eat Hub estão corretos, completos e livres de inconsistências significativas. Caso sejam identificadas questões de qualidade dos dados durante o processo de análise, serão tomadas medidas para corrigi-las ou tratá-las adequadamente.

Definição de País, Cidade e Tipo de Culinária: Pressupõe-se que os registros dos restaurantes incluam informações claras e consistentes sobre país, cidade e tipo de culinária servida. Caso existam ambiguidades ou inconsistências nessas definições, serão aplicadas medidas para padronizar-las e garantir a precisão da análise.

Avaliações de Clientes: Considera-se que as avaliações dos clientes refletem de forma fidedigna a experiência dos mesmos com os restaurantes. 

Representatividade da Amostra: A análise leva em conta que a amostra de restaurantes cadastrados na plataforma representa de forma justa a diversidade de estabelecimentos presentes no mercado. A seleção aleatória ou estratificada dos restaurantes é fundamental para obter resultados representativos.

Essas premissas fundamentam a análise dos dados e a criação dos dashboards, assegurando que as informações apresentadas sejam confiáveis, relevantes e úteis para o CEO. 


#### ESTRATÉGIA DA SOLUÇÃO 

O desenvolvimento do painel estratégico da Eat Hub se baseou na criação de quatro principais visões, cada uma enfatizando aspectos-chave do modelo de negócio da empresa. Essas visões foram cuidadosamente projetadas para fornecer uma compreensão abrangente dos dados e das métricas relevantes para a tomada de decisões estratégicas do CEO

Abaixo detalhamos cada visão com seu respectivo conjunto de métricas:

#### Visão geral dos dados
- Quantidade de restaurantes cadastrados;
- Quantidade de países cadastrados;
- Quantidade de cidades cadastradas;
- Quantidade de avaliações cadastradas; 
- Quantidade de tipos culinários cadastrados;
- Mapa com a localização geográfica dos restaurantes.

#### Visão dos países
- Quantidade de restaurantes cadastrados por país;
- Quantidade de cidades cadastrados por país;
- Média de avaliações cadastradas por país;
- Média de preço de um prato para dois por país.

#### Visão das cidades
- Top 10 cidades com mais restaurantes;
- Top 7 cidades com mais restaurantes com avaliação média acima de 4;
- Top 7 cidades com mais restaurantes com avaliação média abaixo de 2.5;
- Top 10 cidades com mais restaurantes com maior diversidade de tipos culinários..

#### Visão dos tipos culinários
- Top 5 restaurantes com maior nota na plataforma
- Melhores restaurantes por país e tipo culinário;
- Tipos culinários com maior;
- Tipos culinários com menor.


#### TOP 3 INSIGHTS DE DADOS

Ao analisar os dados da Eat Hub e examinar os dashboards, foram identificados insights cruciais que podem orientar as decisões estratégicas do CEO,para impulsionar o crescimento e o sucesso contínuo da empresa. Abaixo estão os três principais insights de dados obtidos:

#### Diversidade de Sabores ao Redor do Mundo:
Uma coisa muito interessante que percebemos é que a Eat Hub possui uma grande variedade de tipos culinários em sua plataforma, são mais de 160 tipos diferentes! Isso mostra que a empresa consegue atender a muitos gostos diferentes ao redor do mundo. Essa variedade é uma vantagem competitiva importante, que pode ser usada para atrair mais clientes e conquistar mercados diversos. Investir na promoção dessa diversidade de sabores pode ser uma estratégia eficaz para atrair mais pessoas e aumentar a participação dos usuários na plataforma.

#### Melhorias nos Restaurantes:
Embora a maioria dos restaurantes tenha avaliações positivas, percebemos que em algumas cidades a média de avaliação é baixa, abaixo de 2.5. Isso indica que alguns estabelecimentos precisam melhorar a qualidade de seus serviços e produtos para deixar os clientes mais satisfeitos. A Eat Hub pode ajudar esses restaurantes, dando dicas e orientações para os donos melhorarem o atendimento e a comida. Afinal, restaurantes com bom serviço e comida de qualidade podem melhorar a reputação da plataforma e fazer com que os clientes confiem mais na Eat Hub.

#### Oportunidades em Cidades com Muitos Restaurantes:
Outro ponto importante é que identificamos cidades com um grande número de restaurantes cadastrados. Essas cidades podem ser ótimas oportunidades para a Eat Hub expandir seus negócios, porque já existe uma demanda consolidada por serviços gastronômicos. Investir em ações de marketing específicas para essas cidades, como campanhas promocionais e parcerias locais, pode ajudar a atrair novos clientes para a plataforma. Isso significa que a empresa pode crescer ainda mais se focar nesses lugares com muitos restaurantes cadastrados.

Esses insights são fundamentais para orientar as decisões estratégicas do CEO, fornecendo uma visão holística do negócio e apontando direcionamentos para maximizar o crescimento e o sucesso da Eat Hub. As análises realizadas com base nos dados do painel estratégico são ferramentas poderosas que capacitam a empresa a aprimorar seus serviços, identificar oportunidades de expansão e continuar a fornecer uma experiência gastronômica diversificada e satisfatória para seus clientes em todo o mundo.


#### PRODUTO FINAL DO PROJETO 

É um painel online, hospedado em uma plataforma de nuvem (Cloud), que está disponível para acesso em qualquer dispositivo conectado à internet.

Para acessar o painel, basta utilizar o seguinte link: https://eath-b.streamlit.app/


#### CONCLUSÃO

O projeto foi desenvolvido com o objetivo de criar dashboards estratégicos e responder às perguntas do CEO Kleiton Guerra utilizando dados. Através desse painel online hospedado na nuvem, o CEO agora tem acesso fácil e interativo a informações valiosas sobre o negócio, permitindo que ele tome decisões mais embasadas para alavancar o crescimento da empresa.

Ao analisar os dados, podemos destacar algumas conclusões importantes. A Eat Hub possui uma ampla diversidade de tipos culinários cadastrados, o que é uma vantagem competitiva significativa. Essa variedade permite atender a diferentes preferências gastronômicas em várias partes do mundo, e pode ser explorada para atrair novos clientes e expandir a empresa em mercados diversos.

Além disso, identificamos oportunidades de melhoria em avaliações de restaurantes. Algumas cidades apresentam médias de avaliação abaixo de 2.5, indicando a necessidade de aprimoramento nos serviços e produtos de alguns estabelecimentos. A Eat Hub pode oferecer orientações e apoio aos proprietários para elevar a qualidade dos restaurantes cadastrados e fortalecer sua reputação.

Outro insight relevante é o potencial de expansão em cidades com maior concentração de restaurantes. Investir em ações de marketing nessas regiões pode atrair novos clientes e consolidar ainda mais a presença da Eat Hub no mercado.

Com base nos dados e insights obtidos, podemos concluir que a Eat Hub está bem posicionada para enfrentar os desafios do mercado de restaurantes online. Através do uso inteligente dos dados e análises constantes, a empresa pode tomar decisões informadas e estratégicas para impulsionar o sucesso e a satisfação dos clientes em todo o mundo.

Em resumo, o projeto proporcionou à Eat Hub uma visão abrangente do negócio e uma ferramenta valiosa para acompanhar o desempenho e tomar decisões mais fundamentadas. 


#### PRÓXIMOS PASSOS

Após a conclusão do projeto e a implementação do painel online, identificamos diversas oportunidades para aprimorar ainda mais a ferramenta e obter insights adicionais que podem impulsionar o sucesso contínuo da Eat Hub. 

#### Aumentar a Granularidade dos Dados: 
Para obter insights mais detalhados, é recomendado coletar e analisar dados em níveis mais granulares. Por exemplo, segmentar os dados por região ou bairro pode fornecer informações específicas sobre o desempenho dos restaurantes em áreas geográficas específicas.

#### Integração de Dados em Tempo Real: 
Considerar a integração de dados em tempo real permitirá que o painel seja atualizado constantemente, fornecendo informações em tempo real sobre o desempenho dos restaurantes, avaliações e outras métricas-chave.

#### Análise de Sentimento: 
Implementar técnicas de análise de sentimento nas avaliações dos clientes pode fornecer uma compreensão mais profunda do feedback dos usuários, ajudando a identificar aspectos específicos que precisam ser aprimorados nos restaurantes cadastrados.

#### Personalização do Dashboard: 
Oferecer a opção de personalização do dashboard para cada usuário pode proporcionar uma experiência mais personalizada, permitindo que cada stakeholder visualize as métricas de maior relevância para suas necessidades.

#### Engajamento com os Proprietários dos Restaurantes: 
Promover um maior engajamento com os proprietários dos restaurantes cadastrados, através de pesquisas de satisfação, pode fornecer valiosos feedbacks para aprimorar ainda mais a experiência do cliente na plataforma.

#### Expansão para Novos Mercados: 
Utilizar os insights gerados para identificar novos mercados com alta demanda por serviços gastronômicos pode ser uma estratégia para expandir a presença da Eat Hub globalmente.

Ao implementar esses próximos passos, a Eat Hub poderá aprimorar significativamente a eficácia do painel estratégico, adquirir uma compreensão mais profunda dos dados e alinhar suas decisões estratégicas com as necessidades dos clientes e do mercado. 
