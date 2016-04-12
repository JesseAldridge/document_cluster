import os, codecs, re, itertools

import nltk


def load_movie_info():
  movies_dict = {}
  for name in ['titles', 'links', 'synopses_wiki', 'synopses_imdb', 'genres']:
    with codecs.open(os.path.join('data', name) + '.txt', encoding='utf8') as f:
      file_content = f.read()
      movies_dict[name] = (
        file_content.split('BREAKS HERE' if 'BREAKS HERE' in file_content else '\n'))[:100]
  movies_dict['synopses'] = [
    sw + si for sw, si in zip(movies_dict['synopses_wiki'], movies_dict['synopses_imdb'])]
  return movies_dict

def cached_stem(t, cache={}):
  if t not in cache:
    cache[t] = stemmer.stem(t)
  return cache[t]

def tokenize_and_stem(text):
    return [cached_stem(t) for t in tokenize_only(text)]

def tokenize_only(text):
  return re.findall("([\w']+)", text, re.UNICODE)

if __name__ == '__main__':
  movies_dict = load_movie_info()
  titles = movies_dict['titles']
  ranks = range(len(titles))
  stopwords = nltk.corpus.stopwords.words('english')
  stemmer = nltk.stem.snowball.SnowballStemmer('english')

  synopses = movies_dict['synopses']
  totalvocab_tokenized = list(itertools.chain(*(tokenize_only(syn) for syn in synopses)))
  totalvocab_stemmed = list(itertools.chain(*(tokenize_and_stem(syn) for syn in synopses)))
  print 'totalvocab_tokenized:', totalvocab_tokenized[:10]
  print 'totalvocab_stemmed:', totalvocab_stemmed[:10]
