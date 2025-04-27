def get_the_word(value=""):
    word = ["yoda", "best", "has"]  # -->yes
    for i in range(len(word)):
        if len(word[i]) > i:
            value += word[i][i]
    print(value)

if __name__ == "__main__":
    get_the_word()