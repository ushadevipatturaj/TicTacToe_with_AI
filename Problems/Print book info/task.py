def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author == year is None:
        print('"', title, '"', sep="")
    elif author is not None and year is None:
        print('"', title, '" was written by ', author, sep="")
    elif author is None and year is not None:
        print('"', title, '" was written in ', year, sep="")
    elif author is not None and year is not None:
        print('"', title, '" was written by ', author, ' in ', year, sep="")