from validation.tagging.corpus.ancora import AncoraCorpusReader


if __name__ == '__main__':
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = AncoraCorpusReader('scripts/corpus/ancora/', files)
    sents = list(corpus.sents())

    with open('raw_data/sbwce/ancora/ancora_without_cess.txt', 'w') as f:
        sentences = [' '.join(act_sent) + '\n' for act_sent in sents]
        f.write(' '.join(sentences))
