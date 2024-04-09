import sys
def main():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        paragraph=file.read()
    words = paragraph.split()
    #
    word_freq={}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    print("unique word count: ",len(word_freq))
    words.sort(key=len)
    print("longest word:",words[-1])
    print("shortest word:", words[0])
if __name__ == "__main__":
    main()