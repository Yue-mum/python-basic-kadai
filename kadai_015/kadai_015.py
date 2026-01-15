class Human:
    # 属性（nameとage）を初期化するメソッド
    def __init__(self, name, age):
    #selfはインスタンス自身を指す
        self.name = name
        self.age = age

    #名前と年齢を標準出力するメソッドを追加
    def printinfo(self):
        print(f"名前: {self.name}")
        print(f"年齢: {self.age}")

#Humanクラスのインスタンスを変数に代入
human_instance = Human("侍 太郎", 25)

#メソッドを実行して出力
human_instance.printinfo()