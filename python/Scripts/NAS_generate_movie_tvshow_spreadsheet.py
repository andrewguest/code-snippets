import os

import xlsxwriter


# Create an Excel workbook for this script
workbook = xlsxwriter.Workbook("NAS_videos.xlsx")


def get_movies():
    row = 0
    column = 0
    # List to contain the movie names
    movies_list = []

    # Get the path to the "TV Shows" folder
    movies_path = input("Enter the FULL path to the 'Movies' folder share: ")

    # Get the name of each movie
    dirs = os.listdir(movies_path)
    for movie_name in dirs:
        movies_list.append(movie_name)

    # Create a 'worksheet' (or page) inside of the workbook
    worksheet = workbook.add_worksheet("movies")
    for item in movies_list:
        worksheet.write(row, column, item)
        row += 1


def get_tvshows():
    row = 0
    column = 0
    # List to contain the TV show names
    tvshows_list = []

    # Get the path to the "TV Shows" folder
    tv_shows_path = input("Enter the FULL path to the 'TV Shows' folder share: ")

    # Get the name of each TV Show and then get every season for that show
    dirs = os.listdir(tv_shows_path)
    for tvshow_name in dirs:
        print(tvshow_name)
        for season in os.listdir(tv_shows_path + "/" + tvshow_name):
            if os.path.isdir(tv_shows_path + "/" + tvshow_name + "/" + season):
                tvshows_list.append(tvshow_name + " - " + season)

    # Create a 'worksheet' (or page) inside of the workbook
    worksheet = workbook.add_worksheet("tv_shows")
    for item in tvshows_list:
        worksheet.write(row, column, item)
        row += 1


if __name__ == "__main__":
    # get_movies()
    get_tvshows()
    workbook.close()
