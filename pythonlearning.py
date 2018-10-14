words = ["start", "middle", "end"]

#slice
print(words[0:2])  #０～１までのlistを返す

# for
for wd in words:
    print(wd)
else:  # forが終わったあとに呼ばれる。
    print("finished")

for i, wd in enumerate(words):
    if i >= 2:
        print("too much!")
        break  # for文から抜けてelseに飛ぶ
    if wd == "start":
        print("this is start")
        continue  # for文の次のループに飛ぶ
    print(wd)
else:
    print("finished")

#for文のiterableをfor文の中で編集するようなプログラムを書く際には
# コピーを撮っておかないと困ることがある。そんなとき
for i, wd in enumerate(words[:]):#sliceの[:]ですべてを含むコピーを生成する
    words.insert(2, words.pop(2))  #popで抜き出したものをinsertで挿入する
print(words)

# print関数などが返す値はNone
print(print())

# 関数の引数
def ask_ok(
    prompt: str, retries: int = 4, reminder: str = "Please Try Again!"
) -> bool:  # 型ヒントはこう書く
    """Simple console ask yes or no.
    
    Raises:
        ValueError -- raise when run out of retries
    
    Returns:
        bool -- user response
    """

    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid user respose")
        print(reminder)
#呼び出し。オプション引数は名前を指定して代入できる。
#オプションでない変数は順番を入れ替えられないので気をつける
ask_ok("Are You Human?", reminder="input again!")

#*args: tupleとして任意の数の引数を受け取る。
#**kwargs: dictionaryとして任意の数の引数を受け取る
def printstr(arg, *args, **kwargs):
    print(arg)
    (print(a) for a in args)  #printの返り値Noneのgenerator型が生成される事になってしまう
    map(print, args)  #printの返り値Noneのgenerator型が生成される事になってしまう
    for a in args:
        print(a)  #これで出力される。
    for x in kwargs:#dict型。
        print("{0}:{1}".format(x, kwargs[x]))

printstr("example", "a", "b", "c", x = "cost", y = "sint")
