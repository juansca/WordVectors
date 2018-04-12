# WordVectors
Este es el proyecto final de la materia de Procesamiento de Lenguaje Natural
dictada en FaMAF - UNC en el año 2017.

## Lab4

### Objetivo
En este trabajo entrenamos el modelo skipgram de FastText para generar
word embeddings y luego evaluar el desempeño de los mismos en dos tareas en
particular: tagging y la evaluación usando gensim y el corpus que es
la traducción directa del utilizado para validar el corpus de Google de Word2Vec


### Corpus
Se usaron 10GB provistos por [Cristian Cardellino](http://crscardellino.me/SBWCE/).
de texto en español. Extraído de varias fuentes:
- La porción en español de SenSem
- La porción en español de Ancora
- Wikipedia
- Manuales de usuario, etc.

Para realizar la limpieza del corpus, se ejecuta el script `clean_text.py`
implementado.
En el mismo se:
- Quitan todos los caracteres no-alfanuméricos,
- Reemplazan las fechas (días, años, meses, etc) por el token **NDATE**,
- Reemplazan los números enteros (no correspondientes con días) por el token
  **NUMBER**,
- Reemplazan todos los números flotantes por el token **NFLOAT**
- Reemplazan todos los multiples espacios en blanco por uno sólo.


El script toma los archivos con el corpus del directorio
`raw_data/sbwce` y luego guarda los archivos con el corpus limpio
en el directorio `cleaned_text/`.


Para correr el mismo se debe ejecutar
```
python scripts/clean_text.py
```

### FastText Word Embeddings
Primero, se genera un único archivo conteniendo al corpus entero
utilizando el script `concat_files.py`. Para ello corremos,
```
python scripts/concat_files.py
```

Esto es debido a que fasttext aún es incapaz de tomar varios archivos como input.

Una vez realizado esto, se debe ejecutar el script `create_vectors.py` dándole como parámetros la dimensión de los vectores y el word ngram a usar. Para
ello se debe ejecutar, por ejemplo:
```
python create_vectors.py -d 100 -w 2
```
Para generar los word vectors de dimensión 100 y con ngram 2.

Éstos se guardarán automáticamente en el directorio `vectors/100_2/`.
**NOTA:** En este caso `100_2` porque se generaron vectores de dimensión 100 y
ngram 2.

El script genera automáticamente 2 archivos: un archivo `.vec` y uno `.bin`.

- En el archivo `.vec` se guardan los word vectors literales en formato texto.
- En el archivo `.bin` se guarda el modelo de fasttext con los embeddings
asociados. Este, por ejemplo, servirá para obtener los 'word vectors for
out-of-vocabulary words'.


### Evaluación

#### **Técnica 1: Word2Vec accuracy**

Se realizaron dos técnicas de evaluación. Una utilizando
'gensim.models.KeyedVectors.accuracy' usando el corpus que es
la traducción directa del utilizado para validar el corpus de Google de
Word2Vec.
Para esta evaluación se debe correr el script:
```
python scripts/evaluate.py
```

En este caso utilizamos el corpus tal cual se encuentra en el directorio `sbcwe`.


**NOTA:** Como es un método secundario en nuestro desarrollo, ha quedado con
fallas de usabilidad. En caso de querer usarlo, se debe ir al script y
modificar la lista `word_vector_files`.


Los resultados obtenidos son comparados en la siguiente tabla:

```
model       capital-common-countries    capital-world    currency    city-in-state    family    gram1-adjective-to-adverb    gram2-opposite    gram5-present-participle    gram6-nationality-adjective    gram7-past-tense    gram8-plural    gram9-plural-verbs     total
--------  --------------------------  ---------------  ----------  ---------------  --------  ---------------------------  ----------------  --------------------------  -----------------------------  ------------------  --------------  --------------------  --------
100_1                       0.8125           0.625969   0.0576923        0.106212   0.794118                     0.283333          0.340909                    0.71                           0.834401            0.258333        0.594758              0.416667  0.555168
100_2                       0.805147         0.642442   0.0576923        0.0961924  0.797386                     0.266667          0.333333                    0.708333                       0.822507            0.263333        0.592742              0.403333  0.55244
100_3                       0.779412         0.631783   0.0384615        0.0881764  0.800654                     0.27381           0.333333                    0.706667                       0.838975            0.261667        0.573589              0.401667  0.548954
300_1                       0.878676         0.790698   0.0384615        0.236473   0.928105                     0.342857          0.378788                    0.77                           0.926807            0.315           0.694556              0.505     0.65247
300_2                       0.860294         0.796512   0.0384615        0.218437   0.921569                     0.340476          0.378788                    0.766667                       0.923147            0.308333        0.702621              0.506667  0.651864
300_3                       0.882353         0.804264   0.0192308        0.246493   0.921569                     0.338095          0.386364                    0.766667                       0.924977            0.31            0.699597              0.518333  0.656411
Cristian                    0.928105         0.882988   0.153846         0.301711   0.797794                     0.283626          0.309091                    0.784585                       0.924138            0.227273        0.523656              0.458462  0.635094
FastText                    0.871345         0.883377   0.153846         0.386691   0.885621                     0.37619           0.333333                    0.800395                       0.930782            0.23913         0.772043              0.493333  0.677529

```


#### **Técnica 2: Tagger**
Esta técnica es evaluando el accuracy de un tagger usando como feature los word
embeddings.
Para correr la evaluación en este caso se deben ejecutar los scripts
`validation/tagging/scripts/train_tagger.py` y
`validation/tagging/scripts/eval_tagger.py`
Las instrucciones de cómo utilizarlas están en cada uno ejecutando la opción
`-h`.

**NOTA:** Recordar que si se ejecuta el **tran_tagger** con la opción `-b y`
no se guardará el modelo entrenado. En vez de eso, se entrenará, se evaluará y
luego se descartará. Esto es debido a un issue de este proyecto respecto a la
capacidad de pickle de guardar el modelo de fasttext. Se debería implementar
el método `__reduce__()`.

**NOTA2:** En este caso los word embeddings fueron generados con el corpus tal
cual está en el directorio `sbcwe` exceptuando el ancora, donde sólo usamos el
correspondiente con el ancora `3LB-CAST*`. A esto lo hicimos ya que entramos
el tagger con la otra parte del corpus ancora y queríamos evitar cualquier tipo
de influencia en el resultado del accuracy.


Para este caso, la comparación del accuracy obtenido se muestra en la
siguiente tabla:
```
model             100_1     100_1_new       100_2    100_2_new   100_3      100_3_new       Cristian
----------------------------------------------------------------------------------------------------
Known accuracy:   97.38%     97.40%       97.39%    97.39%       97.38%       97.38%         97.38%
Unknown accuracy: 89.17%     90.15%       89.46%    89.98%       89.31%       90.03%         88.22%
Total accuracy:   96.57%     96.68%       96.61%    96.65%       96.58%       96.65%         96.47%

```  

Los modelos con nombre '@@_new' fueron entrenados usando el modelo de fasttext
y utilizando los 'word vectors for out-of-vocabulary words'. En el otro caso, se utilizan los word vectors literales para palabras dentro del vocabulario y, en caso de que no estén en el mismo, su vector es nulo.

En el caso del modelo 'Cristian', se corresponde con los word embeddings
generados y explicados [aquí](http://crscardellino.me/SBWCE/). Para este caso
no existe un '@@_new' debido a que fueron generados con el modelo Word2Vec y
no Fasttext.
