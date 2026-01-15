class Human:
    # 属性（nameとage）を初期化するコンストラクタ
    #__init__はコンストラクタを定義するための特別なメソッド
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #大人かどうかを判定して標準出力するメソッドを追加
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは{self.age}歳なので、大人です。")
        else:
            print(f"{self.name}さんは{self.age}歳なので、大人ではありません。")

#Humanクラスのインスタンスを複数生成
person1 = Human("侍太郎", 25)
person2 = Human("侍花子", 18)
person3 = Human("侍二郎", 20)
person4 = Human("侍良子", 15)

#生成したインスタンスをリストに追加
human_list = [person1, person2, person3, person4]

#リストの要素数分だけ繰り返し、check_adultメソッドを呼び出す
for person in human_list:
    person.check_adult()