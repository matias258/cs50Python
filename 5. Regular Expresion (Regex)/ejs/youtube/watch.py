import re
import sys


def main():
    print(parse(input("HTML: ")))

#1) '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
#2) '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
#3) '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
def parse(s):
    if re.search(r"<iframe src=\"https?://www\.youtube\.com/embed/(\w+)\"></iframe>", s):
        link = re.search(r"<iframe src=\"https?://www\.youtube\.com/embed/(\w+)\"></iframe>", s).group(1)
        return "https://youtu.be/" + link

    elif re.search(r'<iframe width=\"\d+\" height=\"\d+\" src=\"https?://www\.youtube\.com/embed/(\w+)\"', s):
        link = re.search(r'<iframe width=\"\d+\" height=\"\d+\" src=\"https?://www\.youtube\.com/embed/(\w+)\"', s).group(1)
        return "https://youtu.be/" + link

    else:
        return None

    

#horrible, odio regex



if __name__ == "__main__":
    main()