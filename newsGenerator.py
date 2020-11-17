import markovify
import os, random, time, random
import csv, sys
path = os.getcwd() + "/files/"
def getDataFromFile(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        header = f.read()
    data = None
    model = markovify.NewlineText(header)
    while data == None:
        data = model.make_short_sentence(min_chars=20, max_chars=120)
    return data

def getRandomImage():
    rand_file = getRandomFileFromFolder(path + "images/")
    with open(rand_file, 'r', encoding="utf-8") as f1:
        images = f1.read()
        images = images.split("\n")
    return random.choice(images)

def getArticle():
    now = time.time()
    rand_file = getRandomFileFromFolder(path + "articles/")
    with open(rand_file, 'r', encoding="utf-8") as f1:
        content = f1.read().split("\n")
        maxlen = 1000 if len(content) < 1000 else len(content)
        index = random.randint(0, len(content) - maxlen)
        content = content[index:index+200]
    data = None
    while data == None:
        model = markovify.NewlineText(content, retain_original=False)
        data = model.make_short_sentence(min_chars=1000, max_chars=2500)
    return model.sentence_split(data)[0].split(". ")


def getRandomFileFromFolder(folder):
    files = os.listdir(folder)
    return folder + random.choice(files)

def getRandomNews():
    now = time.time()
    data = {
        "title": getDataFromFile(getRandomFileFromFolder(path + "titles/")), 
        "article": getArticle(), 
        "caption": getDataFromFile(getRandomFileFromFolder(path + "captions/")), 
        "image": getRandomImage(),
    }
    # done = (int)(time.time() - now)
    # data["time"] = done
    return data



def splitData():
    csv.field_size_limit(int(sys.maxsize/1000000000000))
    files = os.listdir(path + "csvnews/")
    counter = 1
    titles = []
    images = []
    captions = []
    articles = []
    for fil in files:
        print("Reading from...",fil)
        with open(path + "csvnews/" + fil, "r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=',')
                for data in reader:
                        headers = ['Title', 'Link', 'Author', 'Date', 'DateScraped', 'Image', 'ImageCaption', 'Page', 'Article']
                        if "mbl" in fil:
                            headers = ['Title','Link','Author','Date','Image','ImageCaption','Page','Article']
                            if data != headers:
                                if data[0]:
                                    titles.append(data[0])
                                if data[4]:
                                    images.append(data[4])
                                if data[5]:
                                    captions.append(data[5])
                                if data[7]:
                                    articles.append(data[7])
                        else: 
                            if data != headers:
                                if data[0]:
                                    titles.append(data[0])
                                if data[4]:
                                    images.append(data[5])
                                if data[5]:
                                    captions.append(data[6])
                                if data[7]:
                                    articles.append(data[8])
        f.close()
    random.shuffle(titles)
    random.shuffle(images)
    random.shuffle(captions)
    random.shuffle(articles)
    createTextFiles(titles, "titles/news_titles")
    createTextFiles(images, "images/news_images")
    createTextFiles(captions, "captions/news_captions")
    createTextFiles(articles, "articles/news_articles")

def createTextFiles(arr, folder):
    counter = 1
    f2 = open(path + folder + str(counter) + ".txt" , "w", encoding="utf-8")
    n = 0
    for t in arr:
        if t: 
            f2.write(t.replace("\n", "").replace("\r", "") + "\n")
            n += 1
            if n == 25000:
                counter += 1
                f2.close()
                f2 = open(path + folder + str(counter) + ".txt" , "w", encoding="utf-8")
                n = 0
    f2.close()
# splitData()
