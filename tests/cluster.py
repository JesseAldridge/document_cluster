from .. import cluster

def test_load_move_info():
  info_dict = cluster.load_movie_info()
  assert info_dict['genres'][1] == "['Crime', 'Drama']"
  assert "On the day" not in info_dict['synopses_wiki'][1]
  assert "In 1947, banker Andy Dufresne" in info_dict['synopses_wiki'][1]
  assert "In 1947, Andy Dufresne (Tim Robbins)" in info_dict['synopses_imdb'][1]
  assert info_dict['titles'][1] == 'The Shawshank Redemption'
  assert info_dict['links'][1] == 'http://www.imdb.com/title/tt0111161/'
  for s in "In 1947, banker Andy Dufresne", "In 1947, Andy Dufresne (Tim Robbins)":
    assert s in info_dict['synopses'][1]
