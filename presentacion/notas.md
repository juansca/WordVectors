podrías intentar entrenarlo para el castellano. 
Aunque parece que ya está hecho, se puede tratar de hacer un poco mejor,
jugando un poco con los parámetros y quizás agarrando un corpus más grande (como el que compiló Cristian).

Limpieza de corpus:
- NUMBER (1,2,3,49045)
- NFLOAT (1.2, 5.222)
- NDATE (fechas y años)

  las stop-words, mi hipótesis es que dejarlas resulta en embeddings más
  orientados a lo sintáctico, y sacarlas en embeddings más orientados a lo semántico.

  Estuve leyendo un poco (1, 2, y algunos más)  y, como bien expresas, hay como
  varias opiniones al respecto... capaz podríamos dejarlas y ver cómo anda.
  Porque también me parece por lo que dicen que, para este caso, es mejor dejarlas. Te parece??


  la idea es hacer lo minimo y esperar q el gran volumen de datos se encargue
  de q ande bien. Ni siquiera se toca el uso de mayúsculas.

  no se usan php, ubuntu, openoffice3 y kde de sbcwe



- Param tunning:

  Para dim se pueden hacer dos corridas, una con 100 y una con 300.
  word_ngrams me suena que es un parámetro muy sensible. Probaría 1, 2 y capaz 3.


- Evaluación:

  - Word2Vec format
  - Tagger:
    - sin palabras desconocidas (vector nulo)
    - con cálculo de vector para palabras desconocidas
