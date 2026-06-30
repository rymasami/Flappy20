# Flappy Demo

Demo de jogo 2D feito em Python com Pygame, para a disciplina de Linguagem de
Programação Aplicada (UNINTER).

Inspirado na mecânica do Flappy Bird, mas com código próprio. Reaproveita a
estrutura de classes ensinada em aula (Game, Background, Menu, Score), porém
com mecânica de física (gravidade + pulo) e obstáculos (canos) totalmente
diferentes do projeto de referência da disciplina, que era baseado em tiros.

## Como jogar

- Espaço: pular
- Objetivo: desviar dos canos e alcançar 20 pontos para vencer
- Perde ao colidir com um cano, com o chão ou com o teto

## Estrutura do projeto

```
FlappyClone/
├── main.py              <- ponto de entrada (rode com: python main.py)
├── requirements.txt
├── asset/
│   └── player.png       <- sprite do personagem (placeholder, troque pela sua foto)
└── code/
    ├── Game.py           <- orquestra o fluxo geral (menu -> partida -> restart)
    ├── Menu.py           <- tela inicial com instruções de controle
    ├── Level.py           <- lógica de uma partida (spawns, colisão, vitória/derrota)
    ├── Player.py          <- física do personagem (gravidade, pulo)
    ├── Pipe.py            <- obstáculo (par de canos com gap)
    ├── PipeFactory.py     <- cria novos canos
    ├── Background.py      <- céu (gradiente) e chão
    └── Score.py           <- controla e desenha a pontuação
```

## Rodando localmente

```
pip install -r requirements.txt
python main.py
```

## Compilando para Windows (.exe)

Veja o guia "Como compilar o projeto Python" fornecido pela disciplina.
Resumo:

```
pyinstaller --onefile main.py
```

Depois copie a pasta `asset/` para dentro de `dist/`, ao lado do `main.exe`
gerado.
