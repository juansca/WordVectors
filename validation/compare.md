This is the comparition using the gensim word2vec evaluation method.

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


This is the comparition using a tagger's evaluation where our tagger has the embeddings as features.
The '@@_new' models where trained and evaluated using fasttext binary model. That means that
we use the out of vocabulary word vectors too. For the other ones we just use vector on text format
that means that we use only the vectors for word seen, and for the other ones we use a zeros vector.
  
```
model             100_1     100_1_new       100_2    100_2_new   100_3      100_3_new       Cristian
----------------------------------------------------------------------------------------------------
Known accuracy:   97.38%     97.40%       97.39%    97.39%       97.38%       97.38%         97.38%
Unknown accuracy: 89.17%     90.15%       89.46%    89.98%       89.31%       90.03%         88.22%
Total accuracy:   96.57%     96.68%       96.61%    96.65%       96.58%       96.65%         96.47%

```  
