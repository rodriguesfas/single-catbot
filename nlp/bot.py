# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

BOT_NAME = "Ana"

bot = ChatBot(BOT_NAME)
bot = ChatBot(
    BOT_NAME,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
)

conversa = ListTrainer(bot)
conversa.train(
    [
        "Oi!",
        "Olá!",
        "Qual o valor da mensalidade?",
        "Informações sobre valores de mensalidade são passadas apenas através do telefone. Entre em contato com a tesouraria do Colégio Objetivo: (88) 35117050, 35117055 ou 988020095 (WhatsApp). Falar com Camila ou Solange.",
        "Mensalidade",
        "Informações sobre valores de mensalidade são passadas apenas através do telefone. Entre em contato com a tesouraria do Colégio Objetivo: (88) 35117050, 35117055 ou 988020095 (WhatsApp). Falar com Camila ou Solange.",
        "Qual preço do fardamento?",
        "Informações sobre valores são passadas apenas através do telefone. Entre em contato com o setor de Fardamento (lojinha) do Colégio Objetivo: (88) 35117050 ou 35117055. Falar com Leide.",
        "Fardamento",
        "Informações sobre valores são passadas apenas através do telefone. Entre em contato com o setor de Fardamento (lojinha) do Colégio Objetivo: (88) 35117050 ou 35117055. Falar com Leide.",
        "Qual o preço do material escolar?",
        "Informações sobre valores do material didático são passadas apenas através do telefone. Entre em contato com Lojinha do Colégio Objetivo: (88) 35117050 ou 35117055. Falar com Leide.",
        "Material escolar",
        "Informações sobre valores do material didático são passadas apenas através do telefone. Entre em contato com Lojinha do Colégio Objetivo: (88) 35117050 ou 35117055. Falar com Leide.",
        "Haverá aula?",
        "Olá! Todas as informações sobre datas e feriados estão disponíveis em nosso Calendário Letivo. Faça o download na aba Institucional. Caso haja dúvidas, entre em contato com a coordenação responsável: Educação Infantil: 988863605 Ensino Fundamental I: 988413304 Ensino Fundamental II: 988263612/988263607 Ensino Médio 1ª e 2ª série: 988080102 Ensino Médio 3ª série: 988413306",
        "Calendário letivo",
        "Olá! Todas as informações sobre datas e feriados estão disponíveis em nosso Calendário Letivo. Faça o download na aba Institucional. Caso haja dúvidas, entre em contato com a coordenação responsável: Educação Infantil: 988863605 Ensino Fundamental I: 988413304 Ensino Fundamental II: 988263612/988263607 Ensino Médio 1ª e 2ª série: 988080102 Ensino Médio 3ª série: 988413306",
        "Vocês estão contratando?",
        "No momento não temos nenhuma vaga. Mas você pode enviar seu currículo para curriculosobjetivo@gmail.com que entraremos em contato quando surgir uma.",
        "Como faço pra mandar currículo?",
        "No momento não temos nenhuma vaga. Mas você pode enviar seu currículo para curriculosobjetivo@gmail.com que entraremos em contato quando surgir uma.",
        "O Colégio oferece bolsas de estudo?",
        "Todos os anos o Colégio Objetivo Juazeiro realiza o Desafio de Português e Matemática, um concurso que garante bolsas e descontos especiais para os cinco primeiros lugares. Podem participar estudantes do Objetivo Juazeiro e de outras escolas que estejam cursando do 5º ano do Ensino Fundamental até o 2º ano do Ensino Médio. Os inscritos realizam uma prova de conhecimentos sobre as duas disciplinas e a classificação se dá em ordem decrescente (maior nota para menor nota). O concurso acontece normalmente em setembro. Fique atento às nossas redes sociais para não perder os prazos.",
        "O Colégio oferece tempo integral para crianças?",
        "O Colégio Objetivo Juazeiro oferece a modalidade Full Time para os alunos da Educação Infantil (a partir de três anos) e Ensino Fundamental (até o 5º ano). As crianças passam o dia inteiro na escola e participam de aulas de reforço, balé, judô, aula de artes, dentre outras atividades lúdicas e educativas. Eles possuem um refeitório próprio, com alimentação balanceada e cardápio que varia todos os dias, e participam do momento do descanso no dormitório. Para conhecer mais sobre o Full Time, acesse: www.objetivojuazeiro.com.br/fulltime",
        "O colégio oferece tempo integral?",
        "O Colégio Objetivo Juazeiro oferece a modalidade de Turma Integrada para o 9º ano (Ensino Fundamental II), 1º e 2º ano (Ensino Médio). Além de um material especializado, eles desfrutam de aulas extras, um horário de estudo personalizado e de um sistema de avaliação altamente rigoroso com simulados das principais instituições nacionais.",
        "Qual o endereço da escola?",
        "O Colégio Objetivo Juazeiro tem sede na Avenida Dr. Floro Bartolomeu, 776 - São Miguel, Juazeiro do Norte – Ceará.",
        "O colégio oferece atividades extraclasse?",
        "O Colégio Objetivo Juazeiro oferece diversas modalidades extracurriculares para seus alunos, como balé, judô, futsal, handebol, basquete, vôlei e turmas preparatórias. Para verificar disponibilidade, preços e turmas, entre em contato direto com a coordenação responsável. Educação Infantil: 988863605 Ensino Fundamental I: 988413304 Ensino Fundamental II: 988263612/988263607 Ensino Médio 1ª e 2ª série: 988080102 Ensino Médio 3ª série: 988413306",
        "O que é o Desafio Objetivo de Português e Matemática?",
        "Uma competição que acontece anualmente e garante bolsas de estudo e descontos especiais para estudantes novatos e veteranos. Podem participar alunos do 5º ano (Ensino Fundamental I) ao 2º ano (Ensino Médio) para concorrer a premiação referente ao ano seguinte. Os inscritos realizam uma prova de conhecimentos sobre as duas disciplinas e a classificação se dá em ordem decrescente (maior nota para menor nota). O concurso acontece normalmente em setembro. Em 2020, devido a pandemia, o Desafio foi prorrogado. Fique atento às nossas redes sociais para não perder os prazos.",
        "Quando começará a matrícula 2021?",
        "A seleção de novos alunos para 2021 já está aberta. Você pode preencher o formulário de interesse na vaga e agendar uma entrevista com uma de nossas assessoras: link do formulário.",
        "A escola oferece ensino bilíngue?",
        "O Objetivo Juazeiro oferece o ensino bilíngue a partir do Infantil II até o 6º ano do Ensino Fundamental II. Para 2021, implementaremos no 7º ano. Nossa escola trabalha com o melhor programa de educação bilíngue do Brasil, a International School, que proporciona uma imersão total na língua inglesa por meio de materiais didáticos, paradidáticos e concretos desenvolvidos especialmente para garantir um aprendizado efetivo e diferenciado do idioma. Conheça mais: https://objetivojuazeiro.com.br/programa-bilingue/.",
    ]
)

def quest(text:str):
    try:
        resposta = bot.get_response(text)

        if float(resposta.confidence) > 0.5:
            return {"bot": BOT_NAME, "res": str(resposta)}
        else:
            return {"bot": BOT_NAME, "res": "Eu não entendi :("}

    except (KeyboardInterrupt, EOFError, SystemExit):
        pass