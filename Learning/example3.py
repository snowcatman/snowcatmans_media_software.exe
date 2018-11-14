import imdb
import os

ia = imdb.IMDb()

def imdb_search(title):
    s_result = ia.search_movie(title)
    return s_result

def search_imdb_web_page(results):
#    print('page search results were found')
    for result in results:

        url = (ia.get_imdbMovieID(result.movieID))
        id_page_search = ia.get_movie(url)
#        print('================================')
#        print('Movie Title -----------> = ', id_page_search.get('title', 'No title'))
#        print('imdb.com movie ID -----> = ', 'https://www.imdb.com/title/tt' +
#              ia.get_imdbMovieID(result.movieID))
#        print('Year of movie reliece -> = ', id_page_search.get('year', 'No Year'))
#        print('Director of movie -----> = ', id_page_search.get('director', 'No Director'))
        rated1 = id_page_search.get('certificates', 'NoT Rated')
        certificates_function(rated1)
        print(certificates_function(rated1))
#        print('Rated -----------------> = ', certificates_function(rated1))
#        print('=================================')
        return results


def certificates_function(rated1):
#    print(rated1)
    country = ['United States']
    for str in rated1:
  #      print(rated1)
        rated2 = [s for s in rated1 if any(sub in s for sub in (country))]

#        print(rated2)
    return rated2

def display_results(results):
    print('The following search results were found:\n')
    for result in results:
        print('The imdbID used by the site:', ia.get_imdbMovieID(result.movieID))
        print(result.get('title', 'No Tile'))
        print(result.get('year', 'No Year'))
        print(result.get('rating', 'No Rating'))
        print(result.get('director', 'No Director'))


def write_results(filename, results):
    with open(filename, 'w+') as (file):
        for result in results:
            print('=======================================================')
            url = (ia.get_imdbMovieID(result.movieID))
            line = ""  # to keep code alive without fully commenting it out.

            title = result.get('title', 'No Title')
            year = line  # result.get('year', 'No Year')
            rating = line  # result.get('rating', 'No Rating')
            director = line  # result.get('director', 'No Director')

            id_page_search = ia.get_movie(url)
            page_title = (id_page_search.get('title', 'No title'))
            page_year = (id_page_search.get('year', 'No Year'))

            page_rated = (search_imdb_web_page(results), 'not rated')
            #  page_rated = (id_page_search.get('certificates', 'NoT Rated')[0])
            #  get the mpaa or certificates rating E.G. Rated TV-PG, RAted PG, etc.
            #  found this page https://imdbpy.readthedocs.io/en/latest/usage/movie.html?highlight=rated
            page_director = line  # (id_page_search.get('director', 'No Director'))


            file_entry = '{url} {title} {year} {rating} {director} {page_title} {page_year} ' \
                         '{page_rated} {page_director}\n'
            file_entry = file_entry.format(title=title, year=year, rating=rating, url=url, director=director, page_title=page_title, page_year=page_year, page_rated=page_rated, page_director=page_director)
            file.write(file_entry)
            print('=======================================================')

if __name__ == '__main__':
    ia = imdb.IMDb()
    movie_title = input('Enter movie title: ')
    results = imdb_search(movie_title)
#    display_results(results)
    search_imdb_web_page(results)
    path = os.getcwd() + '/results.txt'
    write_results(path, results)
    print('Results written!')